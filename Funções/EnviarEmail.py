import smtplib
import email.message
from GerarLog.Log import log
from decouple import config

def envia_email(html) -> None:
    """
    Enviar e-mail
    :param html: html a ser enviado no e-mail
    :return: None
    """
    msg = email.message.Message()
    msg['Subject'] = "Relatorio dos Clientes - Automação"
    msg['From'] = config('MAIL_FROM')
    msg['To'] = config('MAIL_TO')
    password = config('PASSWORD')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(html)

    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(msg['From'], password)
    smtp.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    log.mensagem('Email enviado')