from flask import Flask
 
app = Flask(__name__)
 
@app.route('/pipeline/<string:pipeline_name>', methods = ['POST'])
def create_pipeline(pipeline_name):
    return f"Creating new pipeline: {pipeline_name}"


@app.route('/pipeline/<string:pipeline_name>', methods = ['DELETE'])
def delete_pipeline(pipeline_name):
    return f"Deleting Pipeline: {pipeline_name}" 

@app.route('/pipeline/<string:pipeline_name>', methods = ['GET'])
def get_pipeline_status(pipeline_name):
    return f"Getting Pipeline status: {pipeline_name}"

@app.route('/pipeline/<string:pipeline_name>/<string:topic_name>', methods = ['GET'])
def get_topic_status(pipeline_name, topic_name):
    return f"Getting {pipeline_name} Topic status: {topic_name}"