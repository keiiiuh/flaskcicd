from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("templates/index.html")

@application.route("/cicd")
def helppage():
    return render_template("cicd.html")

@application.route("/hello")
def index():
    return "Hello World from Flask Hello Page.<b> v1.0"

#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------
