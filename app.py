from pathlib import Path
from pypdf import PdfWriter
from flask import Flask, render_template, request, flash, url_for, redirect, send_file

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="dev")

UPLOAD = Path("uploads")
RESULT = "result.pdf"
UPLOAD.mkdir(exist_ok=True)

list_of_pdf = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("file")
        if file.filename.endswith(".pdf"):
            print(file)
            path = UPLOAD / file.filename
            file.save(path)
            print(path)
            list_of_pdf.append(path)
            flash(f"{file.filename} added to list", "success")
            print(list_of_pdf)
        else:
            flash("Invalid file", "error")

    return render_template("index.html", files=list_of_pdf)


@app.route("/merge", methods=["POST"])
def merge():
    if not list_of_pdf:
        flash("No files for merging", "error")
        return redirect(url_for("home"))

    merger = PdfWriter()
    for pdf in list_of_pdf:
        merger.append(pdf)

    merger.write(RESULT)

    return send_file(RESULT, as_attachment=True)


@app.route("/clear", methods=["POST"])
def clear_pdf_list():
    if list_of_pdf:
        list_of_pdf.clear()
        flash("List of files cleared", "success")
    else:
        flash("List is empty", "error")
    return redirect(url_for("home"))


@app.route("/pop", methods=["POST"])
def delete_last_item():
    if list_of_pdf:
        last_item = list_of_pdf.pop()
        flash(f"{last_item} deleted from list", "success")
    else:
        flash("List is empty", "error")

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
