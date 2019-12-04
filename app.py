import os, datetime
from flask import Flask, render_template, jsonify, send_from_directory, redirect, url_for, request, session, Response, make_response
from flask_socketio import SocketIO, emit
from threading import Lock
##from gevent import monkey
##monkey.patch_all()
async_mode = None
from collections import OrderedDict
app = Flask(__name__)
app.config["SECRET_KEY"] = "something super secret"
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

newListOfTextsInChats = {}
listOfChats = []

listOfNames = []



@app.route("/")
def index():
	return render_template('index.html',async_mode=socketio.async_mode)



@app.route("/channels", methods=["POST"])
def channels():
	print("inside channels")
	name = request.form.get("name")
	return render_template("createChatRoom.html", name=name, listOfChats=listOfChats)


@app.route("/createChat/<name>", methods=["POST"])
def createChat(name):
	
	
	##Get the name of the chat that was attempted to be created
	chatName = request.form.get("chatName")
	
	##check and see if that chat has already been created
	tof=False
	for chat in listOfChats:
	
		if(chat == chatName):
		
			##If it has pull up error page
			tof = True
	
	if(tof==True):
		return render_template("error.html", message="You Cannot Create A Chat With An Already Existing Name. Go Back To Try Again")
		
		
	else:
		##If it hasn't add it to the list of chats
		listOfChats.append(chatName)
		##create a chat list and add it and the chat name to newListOfTextsInChats
		list = []

		newListOfTextsInChats.update({chatName: list})
		##Load Render Template for the chat Room
		return render_template("chatRoom.html", chatName=chatName, name=name, listOfTextsInChats=list)

@app.route("/joinExistingChat/<name>/<chatID>", methods = ["POST"])
def joinExistingChat(name, chatID):
	print("in join existing chat " + name)
	if name == "placeholder":
		print("in if")
		altName = request.form.get("userName")
		altChatID = request.form.get("chat")
		listOfTextsInChats=newListOfTextsInChats.get(altChatID)
		print(altName)
		return render_template('chatRoom.html', name=altName, chatName=altChatID, listOfTextsInChats=listOfTextsInChats)
	else:
		print("in else")
		listOfTextsInChats=newListOfTextsInChats.get(chatID)
		return render_template('chatRoom.html', name=name, chatName=chatID, listOfTextsInChats=listOfTextsInChats)

@app.route("/logout")
def logout():
	return render_template('index.html')



@socketio.on('announce', namespace='/test')
def text(message):
	print("we have made it to announce")
	
	
	now = datetime.datetime.now()
	
	theList = newListOfTextsInChats.get(message['chat'])
	theList.append(message['text'] + " " + now.strftime("%Y-%m-%d %H:%M:%S"))
	
	newListOfTextsInChats[message['chat']] = theList
	
	print(newListOfTextsInChats)
	emit("announce text", {"text": message['text'] + " " + now.strftime("%Y-%m-%d %H:%M:%S")}, broadcast=True)

@socketio.on('toCreateChatRoom', namespace='/test2')
def toCreateChatRoom(message):
	listOfNames.append(message['name'])
	print("inside toCreateChatRoom" + message['name'])
	return redirect(url_for('channels'))
	




if __name__ == '__main__':
	app.run(debug=True)
	socketio.run(app)

	##index()

	"""
	
	flask run --no-reload 
	
	run with this command"""