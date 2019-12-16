from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    up_ime=request.cookies.get("uporabnisko_ime")
    return  f"<h1>Spletna stran, ime ti je: {up_ime} </h1>"

@app.route("/about", methods=["GET"])
def on_about():
    return  render_template("about.html")

@app.route("/about", methods=["POST"])
def on_about_post ():
    ime = request.form.get("vnos-imena")
    response = make_response(render_template("success.html", ime=ime))
    response.set_cookie("uporabnisko_ime", ime)
    return response

@app.route("/logout")
def logout():
    response = make_response("logout")
    response.set_cookie("uporabnisko_ime","", expires=0)
    return response

if __name__=="__main__":
    app.run()