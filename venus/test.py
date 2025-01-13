## Flask application factory:

from flask import Flask 
from flask_mail import Message
from flask_mail import Mail

mail = Mail()

app = Flask(__name__)  
app.config["TESTING"] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "prawinrahul1411@gmail.com"
app.config['MAIL_PASSWORD'] = "prawinrahul1998"	
app.config['MAIL_DEBUG'] = True
mail = Mail(app)

@app.route("/")
def index():
	return "hi"

@app.route("/send_mail/<email>",methods=["GET"])
def send_email(email):
    print(email)
    msg_title = "THis is test Email"
    sender = "prawinrahul1411@gmail.com"
    msg = Message(msg_title,sender=sender,recipients=[email])
    msg_body = "This is a mail body"
    msg.body = msg_body
    # data = {
	# "app_name " : "TaskHive",
	# "title" : msg_title,
	# "body" : msg_body,      
	# }
	# msg.html = render_template("email.html",data=data)

    try:
        print(msg)
        mail.send(msg)
        return "email sent .."
    except  Exception as e :
            print(e)    
            return ("the email was not sent")
        
if __name__ == "__main__":
    app.run(debug=True)      
    