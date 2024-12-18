from flask import Flask ,render_template,Blueprint
sampleBlueprint=Blueprint("sample",__name__,template_folder="templates",static_folder="static")

@sampleBlueprint.route("/")
def home():
    return render_template("views/index.html")


@sampleBlueprint.route("/admin")
def blank():
    return "<h1>This is blue print route</h1>"