from flask import Flask, redirect, render_template_string, session
app = Flask(__name__)
app.secret_key = "counter_secret"

HTML = """
<!DOCTYPE html><html><body style="font-family:Arial;text-align:center;margin-top:80px">
<h2>Counter App</h2>
<h1 style="font-size:72px;color:#1565c0">{{ count }}</h1>
<form method="POST" action="/increment" style="display:inline">
  <button style="padding:12px 24px;font-size:18px;background:#4caf50;color:white;border:none;border-radius:6px;cursor:pointer">+ Increment</button>
</form>
<form method="POST" action="/decrement" style="display:inline;margin:0 10px">
  <button style="padding:12px 24px;font-size:18px;background:#f44336;color:white;border:none;border-radius:6px;cursor:pointer">- Decrement</button>
</form>
<form method="POST" action="/reset" style="display:inline">
  <button style="padding:12px 24px;font-size:18px;background:#9e9e9e;color:white;border:none;border-radius:6px;cursor:pointer">Reset</button>
</form>
</body></html>
"""

@app.route("/")
def index():
    return render_template_string(HTML, count=session.get("count", 0))

@app.route("/increment", methods=["POST"])
def increment():
    session["count"] = session.get("count", 0) + 1
    return redirect("/")

@app.route("/decrement", methods=["POST"])
def decrement():
    session["count"] = session.get("count", 0) - 1
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session["count"] = 0
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
