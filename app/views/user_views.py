from app import app, mongo


@app.route("/user/")
def user_dashboard():
    return "Hello world!!"


@app.route("/user/profile")
def user_profile():
    online_users = mongo.db.users.find({"online": True})
    print(online_users)
    return "Hello world!!"
