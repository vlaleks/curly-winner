from flask import Flask, render_template, redirect, request, url_for, send_from_directory,session,flash, make_response
from datetime import datetime
import sqlite3
import os
from flask.helpers import flash
from db.database import Database
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
import smtplib
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText                
from email.mime.base import MIMEBase
from email import encoders

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

DATABASE = 'db/sota.db'

app = Flask(__name__)
app.secret_key = 'gfahasdhjfgjsaghfgasgfgahgsdfgahdgfasdgg'
MAX_CONTENT_LENGHT = 1024 * 1024
db = Database(DATABASE)
db.init_db() 
accounts = db.get_accounts_count() #Кол-во всех аккаунтов 

flag_enter = False
id_account = -1

session = {}



@app.route('/', methods = ['GET'])  # ГЛАВНАЯ ВХОД
def title():
    global flag_enter
    global id_account
    flag_enter = False
    id_account = -1
    username_id = request.cookies.get('username_id')
    if username_id:
        flag_enter = True
        id_account = int(username_id)
        return redirect(url_for('user_page', id = id_account ))
    return render_template('/title_frame/title_frame.html')

