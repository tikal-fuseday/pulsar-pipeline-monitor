from flask import abort, request, Flask, jsonify
from flask_cors import CORS
import json
import random
from posix import abort
import pulsar_controller as pc


app = Flask(__name__)
app.run(host= '0.0.0.0')
CORS(app)

pipelines = {}

@app.route('/pipeline/<string:pipeline_name>', methods = ['POST'])
def create_pipeline(pipeline_name):
    pipelines[pipeline_name] = json.loads(request.data)
    return f"Created pipeline: {pipeline_name}", 201


@app.route('/pipeline/<string:pipeline_name>', methods = ['DELETE'])
def delete_pipeline(pipeline_name):
    print(pipelines[pipeline_name])
    del pipelines[pipeline_name]
    return f"Deleted Pipeline: {pipeline_name}", 200    

@app.route('/pipeline/<string:pipeline_name>', methods = ['GET'])
def get_pipeline_status(pipeline_name):
    if pipeline_name in pipelines.keys():
        return pc.pipeline_health(pipelines[pipeline_name]), 200
    else:
        return f"can't find pipe", 404

@app.route('/pipeline/<string:pipeline_name>/<string:topic_name>', methods = ['GET'])
def get_topic_status(pipeline_name, topic_name):
    return pc.topic_stats(topic_name), 200