from flask import Flask, Blueprint,render_template

staff_bp = Blueprint("staff", __name__)

@staff_bp.route('/staff_management')
def staff():
    return render_template('staff_manager.html')