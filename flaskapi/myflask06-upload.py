import pandas as pd
from flask import Flask, redirect, url_for, render_template, request, send_file
from werkzeug import secure_filename
app = Flask(__name__)
app.debug = True


@app.route("/upload")
def upload():
  return render_template("upload.html")

@app.route("/uploader", methods = ["GET", "POST"])
def upload_file():
  if request.method == "GET":  # if method is a get (same as "/upload")
     return render_template("upload.html")
  if request.method == "POST":
     f = request.files["file"]
     f.save("uploads/" + secure_filename(f.filename))
     return redirect(url_for("jsonToExcel", fn = f.filename))    # <- lifted from RZFeeser on github.com
     # now that a file has been uploaded... redirect to /json2excel

@app.route("/json2excel/<fn>")
def jsonToExcel(fn):   # expect input of the file that was uploaded
    # use panadas to open the file fn and created a dataframe
    pdf = pd.read_json("uploads/" + fn)
    # convert the incoming json data to excel
    pdf.to_excel("itworked.xls")
    # return the new xls file to the user
    return send_file("itworked.xls", attachment_filename="itworked.xls")

if __name__ == "__main__":
   app.run(port = 5006)
