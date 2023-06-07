from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask
from models import User
from flask_login import login_required, current_user
from main import db
from flask_mail import Mail, Message


emails = Blueprint('emails', __name__)
app = Flask(__name__)
#configuration for mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'logan.dube9@gmail.com'
app.config['MAIL_PASSWORD'] = 'vtjfpsgcteoogvta'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)
mail.init_app(app)

#forgot password email
@emails.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    link = redirect(url_for('auth.reset_password'))
    if request.method == "POST":
        email = request.form.get('email-address')
        #email to be sent
        msg = Message('Forgot Password', sender='Login_Website@gmail.com', recipients=[email])
        msg.html = render_template('reset_password_email.html', link=link)
        mail.send(msg)
        flash('Change password email has been sent!')

    return render_template('forgot_password.html', user=current_user)
