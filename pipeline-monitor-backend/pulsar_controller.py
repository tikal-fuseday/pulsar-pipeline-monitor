import requests
import json
import random


def pipeline_health(topic_list):
    print(f"Get the Health of all topics {topic_list}")
    json_data = {}
    for topic in topic_list:
        topic_data = topic_stats(topic)
        json_data[topic] = random.randint(1,10)
    return json_data

def topic_stats(topic_name):
    print(f"Get the stats on {topic_name}")
    str = f'http://localhost:8080/admin/v2/persistent/public/default/{topic_name}/stats'
    print(str)
    return requests.get(str).json()
    
