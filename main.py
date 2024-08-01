from flask import Flask, request, jsonify
# GET - Reuqest data from a specified resource
# POST - Create a resource
# PUT - Update a resource
# DELETE - Remove a reource

app = Flask(__name__)

# GET

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name" : "Rittique Alam",
        "email" : "md.rittique.alam@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# POST

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)