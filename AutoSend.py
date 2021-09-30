
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import Recommender as reco
import creds

def sendMail_Recommendation():
    instnifty = reco.Recommender('Nifty50')
    instBovespa = reco.Recommender('Bovespa')
    instRtsi = reco.Recommender('RTSI')
    instTW = reco.Recommender('TW')

    # instnifty.updateDB()
    # instBovespa.updateDB()
    # instRtsi.updateDB()
    # instTW.updateDB()

    sender = creds.sender
    receiver = creds.receiver
    emailserver = creds.emailserver
    password = creds.password
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Recommendation"
    msg['From'] = sender
    msg['To'] = receiver

    # Create the body of the message (a plain-text and an HTML version).
    text = f""""

    TW
    {instTW.recommender()} ,   

    Nifty 
    {instnifty.recommender()},

    Bovespa
    {instBovespa.recommender()},

    RTSI
    {instRtsi.recommender()}

    Good Luck !!!"""

    html = f"""\
    <html>
    <head>
    <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
        <title>Recommendation</title>
    </head>
    <body>
    <div class="container">
            <div class="row"><h2 style="align:center;">股市分析(Stock Recommendation System by SK.,)</h2></div>
            <hr>
            <div class="row"><h3>TW 台灣股市(TWSE)</h3></div>
            <p>{instTW.recommender()}<p>
            <hr>
            <div class="row"><h3>印度 India (Nifty 50)</h3></div>
            <p>{instnifty.recommender()}<p>
            <hr>
            <div class="row"><h3>巴西 Brazil (Bovespa)</h3></div>
            <p>{instBovespa.recommender()}<p>
            <hr>
            <div class="row"><h3>俄羅斯 Russia (RTSI)</h3></div>
            <p>{instRtsi.recommender()}<p>
        

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>        
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" integrity="sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/" crossorigin="anonymous"></script>
        
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP(emailserver,587)
    s.login(sender,password)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(sender, receiver , msg.as_string())
    s.quit()

if __name__=="__main__":
    sendMail_Recommendation()