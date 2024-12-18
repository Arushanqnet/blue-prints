from flask import Flask ,render_template
from views.blueprint import sampleBlueprint


app=Flask(__name__)
app.register_blueprint(sampleBlueprint,url_prefix="/views")
@app.route("/")
def test():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)