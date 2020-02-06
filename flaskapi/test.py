from flask import Flask, render_template, request
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
     f.save(secure_filename("uploads/"+f.filename))
     return "file uploaded successfully"

if __name__ == "__main__":
   app.run(port = 5006)