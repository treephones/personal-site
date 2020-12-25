from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)
form_out = [["Sent!", "Your message has been sent. I'll get back to you shortly!"], ["Uh Oh!", "Something went wrong, L."]]

def submit_form(name, email, message):
    form_email = "moezbpersonalsite@gmail.com"
    sfjd = "personalsite"
    me = "moezbajwa@hotmail.com"
    header = "New Contact Form Submission From MOEZB.COM!"
    msg = f"{header}\n\nName: {name}\nEmail: {email}\nMessage:\n{message}"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(form_email, sfjd)
    s.sendmail(form_email, me, msg)
    s.close()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
     return render_template("projects.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["msg"]
        if "@" not in email or "." not in email:
            return render_template("contact.html", invalid_message="Invalid Email Address!")
        elif len(message) < 5:
            return render_template("contact.html", invalid_message="Message not long enough!")
        else:
            try:
                submit_form(name, email, message)
                t = form_out[0][0]
                d = form_out[0][1]
            except:
                t = form_out[1][0]
                d = form_out[1][1]
            return render_template("sent.html", t=t, d=d)
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run()