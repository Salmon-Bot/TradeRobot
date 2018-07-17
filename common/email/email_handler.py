import datetime
from config import settings
from common.email import mail_agent
from config import settings


# 记录上一次邮件发送的时间
last_mail_datetime = None

def send_mail(title, content):
    if not mail_agent:
        return
    global last_mail_datetime
    now = datetime.datetime.now()
    # if last_mail_datetime and now - last_mail_datetime < datetime.timedelta(
    #         minutes=settings.N_MINUTES_STATE):
    #     return
    last_mail_datetime = now

    if settings.MAIL_ACCOUNT and settings.MAIL_AUTH_CODE:
        agent = mail_agent.MailAgent(settings.MAIL_ACCOUNT, settings.MAIL_AUTH_CODE)

    with agent.SMTP() as s:
        s.send(settings.MAIL_RECEIPIENTS, content, title)