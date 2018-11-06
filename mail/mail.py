import smtplib
from email.mime.text import MIMEText


class MailCfg:
    SMTP_SERVER_DOMAIN = 'smtp.163.com'
    SMTP_SERVER_PORT = 25  # smtp服务器默认端口为25
    SMTP_SERVER_USER = 'yixius@163.com'  # 设置账户
    SMTP_SERVER_PWD = '***'


def send_email(receivers, title, content):
    """
    发送邮件的方法
    :param receivers: 收件人，逗号分隔的字符串；'hmyixiu@qq.com,yixius@163.com'
    :param title: 邮件标题
    :param content: 邮件内容
    :return:
    """
    try:
        smtp = smtplib.SMTP()
        # 连接SMTP 服务器，并进行账户验证
        smtp.connect(MailCfg.SMTP_SERVER_DOMAIN, MailCfg.SMTP_SERVER_PORT)
        smtp.login(MailCfg.SMTP_SERVER_USER, MailCfg.SMTP_SERVER_PWD)

        # 初始化邮件内容
        message = MIMEText(content, 'html', 'utf-8')
        # From就是邮件中显示的收件人
        message['From'] = MailCfg.SMTP_SERVER_USER
        message['To'] = receivers
        message['Subject'] = title

        # 进行发送，收件人需要是个数组，表示接受邮件的账户
        smtp.sendmail(message['From'], receivers.split(','),
                      message.as_string())
    except Exception as e:
        print(e)


send_email('hmyixiu@qq.com,yixius@163.com', 'youjian test', '66666')
