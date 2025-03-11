from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

VEREADORES = [
    {"nome": "Antonio Carlos Pereira (Pereira da Saúde)", "email": "pereira.da.saude@camaracabreuva.sp.gov.br"},
    {"nome": "Armando Erik Domingues de Castro (Armando Castro)", "email": "armando.castro@camaracabreuva.sp.gov.br"},
    {"nome": "Devani Cristina de Araújo Debone (Devani Debone)", "email": "devani.debone@camaracabreuva.sp.gov.br"},
    {"nome": "Inivaldo dos Santos (Mirandinha)", "email": "mirandinha@camaracabreuva.sp.gov.br"},
    {"nome": "Luciano Carlos Barboza (Luciano Barboza)", "email": "luciano.barboza@camaracabreuva.sp.gov.br"},
    {"nome": "Luis Henrique Berti Barcelos (Barcelos)", "email": "barcelos@camaracabreuva.sp.gov.br"},
    {"nome": "Marlúcia de Fátima Valente (Marlúcia Valente)", "email": "marlucia.valente@camaracabreuva.sp.gov.br"},
    {"nome": "Rodrigo José Santi (Rodrigo Santi)", "email": "rodrigo.santi@camaracabreuva.sp.gov.br"},
    {"nome": "Vitor Davi Ricci Camargo (Vitor Camargo)", "email": "vitor.camargo@camaracabreuva.sp.gov.br"}
]

def get_db_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vereadores', methods=['GET', 'POST'])
def vereadores():
    if request.method == 'POST':
        vereador_id = request.form['vereador']
        return redirect(url_for('formulario', vereador_id=vereador_id))
    return render_template('vereadores.html', vereadores=VEREADORES)

@app.route('/formulario/<vereador_id>', methods=['GET', 'POST'])
def formulario(vereador_id):
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        descricao = request.form['descricao']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO solicitacoes (vereador_id, nome, telefone, descricao) VALUES (%s, %s, %s, %s)',
            (vereador_id, nome, telefone, descricao)
        )
        conn.commit()
        solicitacao_id = cursor.lastrowid
        cursor.close()
        conn.close()
        
        return redirect(url_for('foto', solicitacao_id=solicitacao_id))
    return render_template('formulario.html', vereador_id=vereador_id)

@app.route('/foto/<solicitacao_id>', methods=['GET', 'POST'])
def foto(solicitacao_id):
    if request.method == 'POST':
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto.filename != '':
                foto_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{solicitacao_id}.jpg")
                foto.save(foto_path)
                
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute('UPDATE solicitacoes SET foto_path = %s WHERE id = %s', (foto_path, solicitacao_id))
                conn.commit()
                cursor.close()
                conn.close()
        return redirect(url_for('confirmacao', solicitacao_id=solicitacao_id))
    return render_template('foto.html', solicitacao_id=solicitacao_id)

@app.route('/confirmacao/<solicitacao_id>', methods=['GET', 'POST'])
def confirmacao(solicitacao_id):
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM solicitacoes WHERE id = %s', (solicitacao_id,))
        solicitacao = cursor.fetchone()
        cursor.close()
        conn.close()

        vereador = VEREADORES[int(solicitacao[1])]
        msg = MIMEMultipart()
        msg['From'] = app.config['EMAIL_USER']
        msg['To'] = vereador['email']
        msg['Subject'] = 'Nova Solicitação - Sou Cidadão'
        body = f"Nome: {solicitacao[2]}\nTelefone: {solicitacao[3]}\nDescrição: {solicitacao[4]}"
        if solicitacao[5]:
            body += f"\nFoto: {solicitacao[5]}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(app.config['EMAIL_SERVER'], app.config['EMAIL_PORT'])
            server.starttls()
            server.login(app.config['EMAIL_USER'], app.config['EMAIL_PASSWORD'])
            server.send_message(msg)
            server.quit()
            flash('Sua solicitação foi enviada com sucesso!')
        except Exception as e:
            flash('Erro ao enviar a solicitação. Tente novamente.')
        
        return redirect(url_for('index'))
    return render_template('confirmacao.html', solicitacao_id=solicitacao_id)

if __name__ == '__main__':
    app.run(debug=True)