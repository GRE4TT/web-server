from flask import Flask, render_template,url_for, request, redirect
import csv
app = Flask(__name__)


@app.route("/<string:name_page>")
def html_page(name_page):
	return render_template(name_page)

def store_to_file(data):
	with open("database.txt", mode="a") as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file=database.write(f"\n {email}, {subject}, {message}")

def store_to_csv(data):
	with open("database.csv",newline="", mode="a") as database2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_writer=csv.writer(database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])


@app.route('/submit', methods=['POST', 'GET'])
def submit():
	if request.method=="POST":
		data=request.form.to_dict()
		store_to_csv(data)
		return redirect("submitted.html")
	else:
		return "an error occured, please try again"

