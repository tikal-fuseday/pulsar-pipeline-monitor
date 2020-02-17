from flask import Flask, jsonify
 
app = Flask(__name__)
 
@app.route('/pipeline/<string:pipeline_name>', methods = ['POST'])
def create_pipeline(pipeline_name):
    return f"Creating new pipeline: {pipeline_name}", 201


@app.route('/pipeline/<string:pipeline_name>', methods = ['DELETE'])
def delete_pipeline(pipeline_name):
    return f"Deleting Pipeline: {pipeline_name}", 200

@app.route('/pipeline/<string:pipeline_name>', methods = ['GET'])
def get_pipeline_status(pipeline_name):
    return {
        "topic_1": 1,
        "topic_2": 2,
        "topic_3": 6,
        "topic_4": 9,
        "topic_5": 2,
    }, 200

@app.route('/pipeline/<string:pipeline_name>/<string:topic_name>', methods = ['GET'])
def get_topic_status(pipeline_name, topic_name):
    return {
        "msgRateIn": 4641.528542257553,
        "msgThroughputIn": 44663039.74947473,
        "msgRateOut": 0,
        "msgThroughputOut": 0,
        "averageMsgSize": 1232439.816728665,
        "storageSize": 135532389160,
        "publishers": [
            {
            "msgRateIn": 57.855383881403576,
            "msgThroughputIn": 558994.7078932219,
            "averageMsgSize": 613135,
            "producerId": 0,
            "producerName": None,
            "address": None,
            "connectedSince": None
            }
        ],
        "subscriptions": {
            "my-topic_subscription": {
            "msgRateOut": 0,
            "msgThroughputOut": 0,
            "msgBacklog": 116632,
            "type": None,
            "msgRateExpired": 36.98245516804671,
            "consumers": []
            }
        },
        "replication": {}
        }, 200