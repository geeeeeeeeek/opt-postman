import requests
from bs4 import BeautifulSoup

import smtplib

# Credit: https://stackoverflow.com/a/24364538 (Ricky Wilson, Jun 23 '14)
class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        msg = headers + "\r\n\r\n" + body
        self.session.sendmail(
            self.email,
            self.email,
            msg.encode("utf-8"))


def check_my_status(case_id):
    r = requests.post("https://egov.uscis.gov/casestatus/mycasestatus.do", data = {
        "completedActionsCurrentPage": 0,
        "upcomingActionsCurrentPage": 0,
        "appReceiptNum": case_id,
        "caseStatusSearchBtn": "CHECK STATUS"
    })

    soup = BeautifulSoup(r.text, features="html.parser")
    status = soup.select(".rows.text-center p")
    header = soup.select(".rows.text-center h1")

    if len(status) and len(header):
        return str(status[0]), header[0].string
    else:
        return "<h1>Script Needs Update</h1>", "Script Needs Update"


def check_statistics():
    r = requests.get("http://www.checkuscis.com/")

    soup = BeautifulSoup(str(r.content, "utf-8"), features="html.parser")
    status = soup.select(".markdown-body  p:nth-of-type(3)")

    if len(status):
        return str(status[0]) + "<a href='http://www.checkuscis.com/'>View Graph</a>"
    else:
        return "<h1>Script Needs Update</h1><a href='http://www.checkuscis.com/'>View Graph</a>"

def compose_email():
    status, title = check_my_status("YSC1990042321")
    statistics = check_statistics()

    return "[OPT Update] " + title, status + statistics

def send_email(username, password):
    title, content = compose_email()
    gm = Gmail(username, password)
    gm.send_message(title, content)

send_email("{REPLACE_WITH_YOUR_GMAIL}", "{REPLACE_WITH_YOUR_PASSWORD}")
