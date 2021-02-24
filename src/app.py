
from flask import Flask
from flask import jsonify
app = Flask(__name__)
from flask import request
import json


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
   
    ]


@app.route('/todos', methods=['GET'])
def hello_world():
    
    json_text=jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data  #llamo la info
    decoded_object = json.loads(request_body)   #convertimos la info en python
    

    todos.append(decoded_object)  #se inserta el objeto en la lista
    new_list=jsonify(todos)
    
    return  new_list



@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)  #Se elimina el objeto en position
    new_list=jsonify(todos)  #se le da formato json
    return new_list



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)