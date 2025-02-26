from flask import Flask, render_template, request, redirect, url_for, session, jsonify,Blueprint

admin_bp = Blueprint("admin", __name__)


@admin_bp.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')

        print(f"New Enquiry: {name}, {phone}, {email}, {message}")  # Debugging

        return redirect(url_for('admin.index'))  # Redirect after submission

    return render_template("index.html")

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('Dashboard.html')

@admin_bp.route('/batches')
def batch():
    return render_template('batches.html')

@admin_bp.route('/add_batch')
def add_batch():
    return render_template('add_batches.html')

@admin_bp.route('/fee')
def fee():
    return render_template('fee_management.html')

@admin_bp.route('/terms_and_conditions')
def terms():
    return render_template('terms_condotions.html')

@admin_bp.route('/enquiry')
def enquiry():
    return render_template('enquiry_manager.html')

@admin_bp.route('/settings')
def settings():
    return render_template('settings.html')

@admin_bp.route('/course')
def course():
    return render_template('course_details.html')

@admin_bp.route('/fee_change')
def fee_change():
    return render_template('fee_change.html')

@admin_bp.route('/add_course')
def add_course():
    return render_template('add_course.html')