from flask import Flask, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

app = Flask(__name__)

# Configurações de e-mail (no servidor)
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = "seu_email@gmail.com"  # Substitua por um e-mail válido
EMAIL_PASSWORD = "sua_senha"        # Substitua por uma senha válida (ex.: senha de app do Gmail)

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        nome = request.form['nome']
        telefone = request.form['telefone']
        descricao = request.form['descricao']
        to_email = request.form['to_email']
        
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = to_email
        msg["Subject"] = "Solicitação do Cidadão - Sou Cidadão"
        corpo = f"Nome: {nome}\nTelefone: {telefone}\nDescrição: {descricao}"
        msg.attach(MIMEText(corpo, "plain"))

        if 'foto' in request.files:
            foto = request.files['foto']
            if foto.filename:
                img = MIMEImage(foto.read())
                msg.attach(img)

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        
        return {"status": "success"}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)