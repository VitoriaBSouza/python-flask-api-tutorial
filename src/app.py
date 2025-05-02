# Import flask to py file
# add jsonify and post request
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# create a fetch GET to request data from server
@app.route('/todos', methods=['GET'])
def hello_world():
    # Convert variable into a json string
    json_text = jsonify(todos)
    # returns the json string
    return json_text

# create a fetch POST add data on server database
@app.route('/todos', methods=['POST'])
def add_new_todo():
    # The request body is already JSON decoded, and it comes in the request.json variable
    request_body = request.json
    todos.append(request_body);
    print("Incoming request with the following body", request_body);
    return jsonify(todos);

# create a fetch DELETE to remove data from server database
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position);
    print("This is the position to delete:", position);
    return jsonify(todos);



# This has to be at the end of the file
# Add all new code above this line
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)