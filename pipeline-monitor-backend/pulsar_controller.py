import requests
import json

url = 'http://localhost:8080/admin/v2/non-persistent/public/default/%s/stats'


def pipeline_health(topic_list):
    print("Get the Health of all topics {topic_list}")
    json_data = {}
    for topic in topic_list:
        topic_data = topic_stats(topic)
#        json_data[topic] = (topic_data['msgRateIn']/topic_data['msgRateOut'])%10
        json_data[topic] = topic_data['msgRateIn']
    return json_data

def topic_stats(topic_name):
    print("Get the stats on {topic_name}")
    return requests.get(url.format(topic_name)).json()
    
