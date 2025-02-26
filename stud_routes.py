from flask import Flask, Blueprint,render_template

stud_bp = Blueprint("student", __name__)

@stud_bp.route('/student')
def student():
    return render_template('student.html')

@stud_bp.route('/registration')
def registration():
    return render_template('registrationform.html')

@stud_bp.route('/all_students')
def all_students():
    return render_template('all_students.html')

@stud_bp.route('/inactive_students')
def inactive_student():
    return render_template('inactive_students.html')