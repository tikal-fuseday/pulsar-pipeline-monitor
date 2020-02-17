const BaseUrl = 'http://192.168.100.37:5000/pipeline'

export class TopicsService {

    async getTopics(pipelineName) {
        if (!pipelineName) {
            return [];
        }
        const response = await fetch(`${BaseUrl}/${pipelineName}`);
        const topics = await response.json();
        return Object.entries(topics).map(item => ({name: item[0], value: item[1]}));
    }

    async getTopicData(pipeline, topic) {
        const response = await fetch(`${BaseUrl}/${pipeline}/${topic.name}`);
        return await response.json();
    }

    async queryTopics(pipeline, topicNames) {
        const response = await  fetch(`${BaseUrl}/${pipeline}`, {
            method: 'post',
            body: JSON.stringify(topicNames)
        });

        return response;
    }

    getColor(value) {

        const [min, max] = [0, 10];

        const middle = (min + max) / 2;
        const scale = 255 / (max - min);

        if (value <= min) {
            return '#FF0000';
        }
        if (value >= max) {
            return '#00FF00';
        }
        return `#FF${((value - min) * scale).toString(16)}00`;


    }

}
