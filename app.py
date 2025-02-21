from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solicitacoes.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
db = SQLAlchemy(app)

# Configurações de e-mail
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = "seu_email@gmail.com"
EMAIL_PASSWORD = "sua_senha"

# Vereadores pré-definidos
VEREADORES = [
    {"nome": "João Silva", "email": "joao.silva@cabreuva.sp.gov.br"},
    {"nome": "Maria Oliveira", "email": "maria.oliveira@cabreuva.sp.gov.br"}
]

# Modelo do banco de dados
class Solicitacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    foto_path = db.Column(db.String(200), nullable=True)
    vereador_email = db.Column(db.String(100), nullable=False)

# Cria o banco de dados
with app.app_context():
    db.create_all()

@app.route('/')
def apresentacao():
    return render_template('apresentacao.html')

@app.route('/selecao_vereador', methods=['GET', 'POST'])
def selecao_vereador():
    if request.method == 'POST':
        vereador_email = request.form['vereador']
        return redirect(url_for('preencher_dados', vereador_email=vereador_email))
    return render_template('selecao_vereador.html', vereadores=VEREADORES)

@app.route('/preencher_dados/<vereador_email>', methods=['GET', 'POST'])
def preencher_dados(vereador_email):
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        descricao = request.form['descricao']
        if not nome or not telefone or not descricao:
            flash('Preencha todos os campos obrigatórios!')
            return redirect(url_for('preencher_dados', vereador_email=vereador_email))
        solicitacao = Solicitacao(nome=nome, telefone=telefone, descricao=descricao, 
                                vereador_email=vereador_email)
        db.session.add(solicitacao)
        db.session.commit()
        return redirect(url_for('adicionar_foto', solicitacao_id=solicitacao.id))
    return render_template('preencher_dados.html', vereador_email=vereador_email)

@app.route('/adicionar_foto/<int:solicitacao_id>', methods=['GET', 'POST'])
def adicionar_foto(solicitacao_id):
    solicitacao = Solicitacao.query.get_or_404(solicitacao_id)
    if request.method == 'POST':
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto.filename:
                foto_path = os.path.join(app.config['UPLOAD_FOLDER'], foto.filename)
                foto.save(foto_path)
                solicitacao.foto_path = foto_path
                db.session.commit()
        return redirect(url_for('confirmacao', solicitacao_id=solicitacao_id))
    return render_template('adicionar_foto.html', solicitacao_id=solicitacao_id)

@app.route('/confirmacao/<int:solicitacao_id>', methods=['GET', 'POST'])
def confirmacao(solicitacao_id):
    solicitacao = Solicitacao.query.get_or_404(solicitacao_id)
    if request.method == 'POST':
        try:
            msg = MIMEMultipart()
            msg["From"] = EMAIL_USER
            msg["To"] = solicitacao.vereador_email
            msg["Subject"] = "Solicitação do Cidadão - Sou Cidadão"
            corpo = f"Nome: {solicitacao.nome}\nTelefone: {solicitacao.telefone}\nDescrição: {solicitacao.descricao}"
            msg.attach(MIMEText(corpo, "plain"))
            if solicitacao.foto_path:
                with open(solicitacao.foto_path, "rb") as f:
                    img = MIMEImage(f.read())
                    msg.attach(img)
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASSWORD)
                server.send_message(msg)
            flash("Solicitação enviada com sucesso!")
            return redirect(url_for('apresentacao'))
        except Exception as e:
            flash(f"Erro ao enviar solicitação: {str(e)}")
    return render_template('confirmacao.html', solicitacao=solicitacao)

if __name__ == '__main__':
    app.run(debug=True)