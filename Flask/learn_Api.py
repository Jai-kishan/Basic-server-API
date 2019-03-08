from flask import Flask, jsonify, make_response,abort,request,url_for
import json,os.path
app=Flask(__name__)


saral_api=[
	{
		"Id":1,
		"Name":"Python",
		"Description":"This course design for python programmers 'Basic Level'",
	},

	{
		"Id":2,
		"Name":"Navgurukul's Constitution-English",
		"Description":"In this Course you can read about Navgurukul Constitutionsuch as Navgurukul rules and regulation for servive in Navgurukul"
	}
]

exercise=[
	{
	"Id":1,
	"Exercise_id":1,
	"Exercise_Name":"Varibles in python",
	"Exercise_content":"Jo badal sakta hai usse VARIABLE kehte hai. VARIABLE ka aap kuch bhi naam rakh sakte hai, and usmei kuch bhi store kar sakte hai.",
	"Hint":"Sorry here is not available any hints"

	},
	{
	"Id":1,
	"Exercise_id":2,
	"Exercise_Name":"Constant in python",
	"Exercise_content":"Jaise numbers, letters, strings ko hum constants bolte hai.",
	"Hint":"Sorry here is not available any hints"
	},
	{
	"Id":2,
	"Exercise_id":1,
	"Exercise_Name":"counsel members",
	"Exercise_content":"navgurukul in many types of counsel members lke that tresure etc.",
	"Hint":"Sorry here is not available any hints"
	},
	{
	"Id":2,
	"Exercise_id":2,
	"Exercise_Name":"Disco",
	"Exercise_content":"Disco mantains on the rules and regulation of the campus.",
	"Hint":"Sorry here is not available any hints"
	}]

# def read_file(r_file):
# 	with open(r_file+".json","r") as file:
# 			read_file = file.read()
# 			file_store=json.loads(read_file)
# 	return jsonify(file_store)


# def write_file(w_file):
# 	with open(w_file+".json","w") as file:
# 			json.dump(saral_api,file)
# 	return jsonify({"details":saral_api})



@app.route("/todo/jai/v.01/saral_api",methods=["get"])

def get_data():
	if os.path.exists("create_api"):
		with open("saral_api.json","r") as file:
			read_file = file.read()
			file_store=json.loads(read_file)
		return jsonify(file_store)

	with open("create_api.json","w") as file:
			json.dump(saral_api,file)
	return jsonify({"details":saral_api})



@app.route("/todo/jai/v.01/saral_api/<int:task_id>", methods=["get"])

def get_id(task_id):
	api_id =[]
	for i in saral_api:
		if i["Id"]==task_id:
			api_id.append(i)

	if len(api_id)==0:
		abort(403)
	return jsonify({"api_get":api_id[0]})



@app.route("/todo/jai/v.01/saral_api",methods=["post"])

def post_data():
	if not request.json or not "Name" in request.json:
		abort(404)
	api_create={
		"Id":saral_api[-1]["Id"]+1,
		"Name":request.json["Name"],
		"Description":request.json["Description"]
	}
	saral_api.append(api_create)
	return jsonify({"new_key":saral_api}),201




@app.route("/todo/jai/v.01/saral_api/<int:task_id>/exercise", methods=["get"])
def get_sub_content(task_id):
	sub_data=[]
	for i in exercise:
		if i["Id"]==task_id:
			sub_data.append(i)
	if len(sub_data)==0:
		abort(403)
	return jsonify({"sub_exercise":sub_data})



@app.route("/todo/jai/v.01/saral_api/<int:task_id>/exercise/<int:sub_id>", methods=['get'])

def get_sub_exercise(task_id,sub_id):
	sub_exercise_id=[]
	for i in exercise:
		if i["Exercise_id"]==sub_id and i["Id"]==task_id:
			sub_exercise_id.append(i)
	if len(sub_exercise_id)==0:
		abort(405)
	return jsonify({"sub_exercise":sub_exercise_id})


# @app.route("/todo/jai/v.01/saral_api/<int:task_id>/exercise",methods=["post"])

# def post_exercise(task_id):
# 	if not request.json or not "Name" in request.json:
# 		abort(404)
# 	api_create={
# 		"Id":saral_api[-1]["Id"]+1,
# 		"Name":request.json["Name"],
# 		"Description":request.json["Description"]
# 	}
# 	saral_api.append(api_create)
# 	return jsonify({"new_key":saral_api}),201


@app.route("/todo/jai/v.01/saral_api/<int:task_id>",methods=["put"])

def update_data(task_id):

	api_update=[]
	for i in saral_api:
		if i["Id"]==task_id:
			api_update.append(i)
	# api_update=[data for data in saral_api if data["Id"]==task_id]

	if len(api_update)==0:
		abort(400)
	if not request.json:
		abort(400)
	# if 'Name'in request.json and type(request.json['Name'] !=str):
	# 	abort(400)
	# if 'Description' in request.json and type(request.json['Description'] is not str):
	# 	abort(400)

	api_update[0]['Name']=request.json['Name']
	api_update[0]['Description']=request.json['Description']
	return jsonify({'tasks':api_update[0]})


if __name__ == "__main__":
	app.run(debug=True,port=8000)