# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

htmlLinkPy='/stub/'
htmlFile="stub.html"

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/stub/', methods=['GET', 'POST'])
def stub(htmlLinkPy='/stub/', htmlFile="stub.html"):
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template(htmlFile, greetInput=name, htmlLinkHtml=htmlLinkPy)
    return render_template(htmlFile, greetInput="World", htmlLinkHtml=htmlLinkPy)

@app.route('/avinh/', methods=['GET', 'POST'])
def avinh():
    stub('/avinh/', "avinh.html")

@app.route('/akhil/')
def akhil():
    return render_template("akhil.html")

@app.route('/calissa/')
def calissa():
    return render_template("calissa.html")

@app.route('/valen/')
def valen():
    return render_template("valen.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
