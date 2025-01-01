# app.py
from flask import Flask, render_template, send_from_directory
from routes.product_router import router as product_router

app = Flask(__name__, static_folder='/static', static_url_path='/')

app.static_folder = 'static'

app.register_blueprint(product_router)
@app.route("/")
def hello():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)