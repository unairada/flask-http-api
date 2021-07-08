from flask import Flask
import os

# set up environment variables
context_path=os.getenv('CONTEXT_PATH','/myapp')
port=int(os.getenv('PORT', '8080'))
doc_path=os.getenv('DOC_PATH', './resources/')


app = Flask(__name__)


@app.route(context_path + '/')
def hello_world():
    return 'Welcome to my app!'

# Read the content of the doc.txt file if CONTEXT_PATH is accessed
@app.route(context_path + '/doc/')
def file_read():
    doc=open(os.path.join(doc_path,'doc.txt'),"r") #open the document
    lines = doc.readlines() #read the content of the document 
    content=''
    for line in lines:
        content += (line + '\n')
    doc.close() #close the document
    return content

app.run(host='0.0.0.0',port=port)