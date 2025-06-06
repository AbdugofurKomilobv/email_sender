import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Email sozlamalari
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Xabar matni
    msg.attach(MIMEText(body, 'plain'))

    # Gmail SMTP serveriga ulanamiz
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # TLS dan foydalanamiz
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email muvaffaqiyatli yuborildi!")
    except Exception as e:
        print("Xatolik yuz berdi:", e)

# Foydalanish
if __name__ == "__main__":
    sender_email = "sizning_email@gmail.com"
    sender_password = "sizning_email_parolingiz"
    receiver_email = "qabul qiluvchi_email@example.com"
    subject = "Salom!"
    body = "Bu test xabari Python dasturi orqali yuborildi."

    send_email(sender_email, sender_password, receiver_email, subject, body)
