from flask import Flask, render_template, request
import elo_calculation

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=['POST'])
def calculate():
    first_rating = int(request.form.get("firstRating"))
    second_rating = int(request.form.get("secondRating"))
    k = int(request.form.get("k"))
    result = float(request.form.get("result"))
    new_first_rating, new_second_rating = elo_calculation.calculate_new_elo(first_rating, second_rating, result, k)
    return render_template("calculate.html", first_rating=first_rating, second_rating=second_rating, k=k, result=result, new_first_rating = new_first_rating, new_second_rating = new_second_rating)
