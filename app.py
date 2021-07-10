#!/usr/bin/python3
import os

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
##postgress
engine = create_engine("mysql+pymysql://root:free@localhost:3306/malik")


db = scoped_session(sessionmaker(bind=engine))



@app.route("/Form", methods=['GET'])
def insert():
    return render_template("Form.html")

@app.route("/view", methods=['POST', 'GET'])
def view():
    if request.method == "POST":

        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        semester = request.form.get("semester")
        program = request.form.get("program")
        session = request.form.get("session")
        totalfee = request.form.get("totalfee")
        submittedfee = request.form.get("submittedfee")

        db.execute("INSERT into fee(firstname, lastname, semester, program, session, totalfee, submittedfee,) VALUES (:firstname, :lastname, :semester, :program, :session, :totalfee, :submittedfee,)",
                {"firstname": firstname, "lastname": lastname,"semester":semester, "program": program, "session": session, "totalfee":totalfee, "submittedfee":submittedfee})
        db.commit()

        # Get all records again
        students = db.execute("SELECT * FROM fee").fetchall()
        return render_template("view.html", students=students)
    else:
        students = db.execute("SELECT * FROM fee").fetchall()
        return render_template("view.html", students=students)


# @app.route("/update/<int:id>/", methods=['POST','GET'])
# def update(id):
#     if request.method=="POST":
#         fname = request.form.get("fname")
#         lname = request.form.get("lname")
#         session = request.form.get("session")
#         subfee = request.form.get("subfee")
#         duefee = request.form.get("duefee")
#         totfee = request.form.get("totfee")
#         db.execute("Update fee SET firstname=:fname, lastname=:lname, Session=:session, submitted_fee=: subfee, due_fee=: duefee, total_fee=:totfee where id = :id",)
#                 {"firstname": fname, "lastname": lname, "Session":session, "submitted_fee": subfee, "due_fee": duefee, "total_fee":totfee})
#         db.commit()
#         return redirect(url_for('intro'))
#     else:
#         stud = db.execute("SELECT * FROM fee WHERE id = :id", {"id": id}).fetchone()
#         return render_template("update.html", stud=stud, id=id)
#
#
# @app.route("/update_now/<int:id>/", methods=['POST', 'GET'])
# def update_now(id):
#     stud = db.execute("SELECT * FROM fee WHERE id = :id", {"id": id}).fetchone()
#     if stud is None:
#         return "No record found by ID = " + str(id) +". Kindly go back to <a href='/intro'> Intro </a>"
#     else:
#         stud = db.execute("delete FROM students WHERE id = " + str(id))
#         db.commit()
#         return redirect(url_for('intro'))
# # @app.route("/delete/<int:id>/")
# # def delete(id):
# #     stud = db.execute("SELECT * FROM students WHERE id = :id", {"id": id}).fetchone()
# #     if stud is None:
# #         return "No record found by ID = " + str(id) +". Kindly go back to <a href='/intro'> Intro </a>"
# #     else:
# #         stud = db.execute("delete FROM students WHERE id = " + str(id))
# #         db.commit()
# #         return redirect(url_for('intro'))
#

if __name__ == "__main__":
    app.run(debug=True)
