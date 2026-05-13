from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        principal = float(request.form["principal"])
        years = int(request.form["years"])
        cibil = int(request.form["cibil"])

        months = years * 12

        # Interest rate using CIBIL score
        if cibil > 800:
            annual_rate = 7.5
        else:
            annual_rate = 8.3

        monthly_rate = annual_rate / (12 * 100)

        # EMI Formula
        emi = (
            principal * monthly_rate * (1 + monthly_rate) ** months
        ) / (
            (1 + monthly_rate) ** months - 1
        )

        balance = principal

        schedule = []

        # EMI breakdown table
        for month in range(1, months + 1):

            interest = balance * monthly_rate

            principal_paid = emi - interest

            balance -= principal_paid

            if balance < 0:
                balance = 0

            schedule.append({
                "month": month,
                "emi": round(emi, 2),
                "interest": round(interest, 2),
                "principal": round(principal_paid, 2),
                "balance": round(balance, 2)
            })

        return render_template(
            "index.html",
            emi=round(emi, 2),
            rate=annual_rate,
            schedule=schedule
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
