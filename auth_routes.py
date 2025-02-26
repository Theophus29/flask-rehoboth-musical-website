from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from app import mysql  # Import MySQL directly
import re

auth_bp = Blueprint('auth', __name__)

# Regular Expressions
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9_]{3,20}$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9@#*!$%^&+=]{5,20}$')

@auth_bp.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not USERNAME_REGEX.match(username):
            flash("Invalid username format.", "error")
            return render_template("admin_login.html")

        if not PASSWORD_REGEX.match(password):
            flash("Invalid password format.", "error")
            return render_template("admin_login.html")

        # Access MySQL directly from the global variable
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM admin_login WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            session['admin_logged_in'] = True
            session['admin_username'] = username
            return redirect(url_for('admin.dashboard'))
        else:
            flash("Invalid username or password", "error")

    return render_template("admin_login.html")

@auth_bp.route('/student_login')
def stud_login():
    return render_template('student_login.html')