# from flask import *
from flask import Flask ,jsonify ,make_response,abort,request,url_for
import json,os.path
app=Flask(__name__)


# task 1 : return a dictionary through get methods

tasks=[
  {
  "id":1,
  "title":"buy grocerices",
  "description":"milk , cheese ,pizza ,fruit",
  "done":False
  },
  {
   "id":2,
  "title":"learning Backend",
  "description":" you need to study REST so that you get a clear idea about how  it works",
  "done":False
  }
]



@app.route("/todo/api/v1.0/tasks",methods=["GET"])


def get_task():
	with open('offline.json','w') as file1:
		json.dump([make_public_task(task) for task in tasks], file1)
	return jsonify({"tasks":[make_public_task(task) for task in tasks]})




@app.route("/todo/api/v1.0/tasks/<int:task_id>",methods=["GET"])
def get_tasks(task_id):

	task=[task for task in tasks if task["id"]==task_id]
	if len(task)==0 :
		abort(404)

	return jsonify({"task":task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route("/todo/api/v1.0/tasks",methods=["POST"])
def create_task():
	if not request.json or not "title" in request.json:
		abort(404)
	task={
	"id":tasks[-1]["id"]+1,
	"title":request.json["title"],
	"description":request.json["description"],
	"done":request.json["done"]
	}
	tasks.append(task)
	return jsonify({"task":task}),201

@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=["PUT"])
def update_task(task_id):
	task=[task for task in tasks if task["id"]==task_id]
	if len(task)==0:
		abort(404)
	if not request.json:
		abort(400)
	if 'title' in request.json and type(request.json['title']) != str:
		abort(400)
	if 'description' in request.json and type(request.json['description']) is not str:
		abort(400)
	if 'done' in request.json and type(request.json['done']) is not bool:
		abort(400)
	task[0]["title"]=request.json["title"]
	task[0]["description"]=request.json["description"]
	task[0]["done"]=request.json["done"]
	return jsonify({"tasks":task[0]})	



@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
	task=[task for task in tasks if task['id']==task_id]
	if len(task)==0:
		abort (404)
	tasks.remove(task[0])			
	return jsonify({'result':task})

def make_public_task(task):
    new_task = {}
    for key in task:
        if key == 'id':
            new_task['uri'] = url_for('get_tasks', task_id=task['id'], _external=True)
        else:
            new_task[key] = task[key]
    return new_task



if __name__ == "__main__":
	app.run(debug=True,port=8000)





# def read_file(r_file):
# 	with open(r_file+".json","r") as file:
# 			read_file = file.read()
# 			file_store=json.loads(read_file)
# 	return jsonify(file_store)


# def write_file(w_file):
# 	with open(w_file+".json","w") as file:
# 			json.dump(saral_api,file)
# 	return jsonify({"details":saral_api})