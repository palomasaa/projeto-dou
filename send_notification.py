import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_email_notification(recipient_email, subject, message_body):
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("❌ Erro: Credenciais de e-mail não configuradas nas variáveis de ambiente.")
        print("Por favor, defina EMAIL_USER e EMAIL_PASSWORD no seu arquivo .env")
        return

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message_body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print(f"📧 E-mail enviado para {recipient_email}")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail para {recipient_email}: {e}")

if __name__ == "__main__":
    # Exemplo de uso (para testes locais)
    # Certifique-se de ter um arquivo .env com EMAIL_USER e EMAIL_PASSWORD
    # e de ter habilitado o acesso de aplicativos menos seguros ou gerado uma senha de app no Gmail
    test_email = "palomasaaa@gmail.com" # Substitua pelo seu e-mail de teste
    test_subject = "Alerta de Teste DOU"
    test_message = "Esta é uma mensagem de teste do sistema de notificação do DOU."
    send_email_notification(test_email, test_subject, test_message)


