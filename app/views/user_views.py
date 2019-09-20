from app import app


@app.route("/user/")
def user_dashboard():
    return "Hello world!!"


@app.route("/user/profile")
def user_profile():
    return "Hello world!!"
