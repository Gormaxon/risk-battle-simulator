from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def risk_battle():
    red = []
    blue = []
    counter_red = 0
    counter_blue = 0

    if request.method == "POST":
        # Get user input
        red1 = int(request.form["red_dice"])
        blue1 = int(request.form["blue_dice"])

        # Roll dice
        for i in range(red1):
            red.append(random.randint(1, 6))
        for i in range(blue1):
            blue.append(random.randint(1, 6))

        # Sort in descending order
        red.sort(reverse=True)
        blue.sort(reverse=True)

        # Compare dice results
        for i in range(min(len(red), len(blue))):
            if red[i] > blue[i]:
                counter_blue += 1
            else:
                counter_red += 1

    return render_template("index.html", red=red, blue=blue, counter_red=counter_red, counter_blue=counter_blue)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
