from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def liyu():
    return render_template("index.html")
@app.route("/kemis")
def those():
    return render_template("a.html", ቀሚስ="ቀሚስ", about=" 650 ብር", image="KEMIS.jpg")
@app.route("/suri")
def this():
    return render_template("a.html", ቀሚስ="ሱሪ", about=" 700 ብር", image="suri.jpg")
@app.route("/kidcloth")
def these():
    return render_template("a.html", ቀሚስ="የህጻን ቀሚስ", about=" 675 ብር", image="kids cloth.jpg")
@app.route("/gurdkemis")
def that():
    return render_template("a.html", ቀሚስ="ጉርድ ቀሚስ" , about=" 600 ብር", image="miniskirt.jpg")
@app.route("/order_here")
def order():
    return render_template("order.htm")
@app.route("/enter")
def enter():
    return render_template("enter.html")
if __name__ == "__main__":
    app.run()
