<template>
    <div>
        {{msg}}
        <div class="topics-container">
            <div v-for="item in this.topics" v-bind:key="item.name" style="display: flex">
                <Topic v-bind:topic="item" v-on:topicSelected="topicSelected($event)">
                </Topic>
                <div v-if="item !== topics[topics.length - 1]">
                    <svg height="5px">
                        <line x1="0" y1="0" x2="300" y2="0" style="stroke:rgb(0,0,0);stroke-width:5"/>
                    </svg>
                </div>
            </div>

        </div>
        <TopicData v-if="selectedTopicData" v-bind:topic-data="this.selectedTopicData"></TopicData>
    </div>
</template>

<style scoped>
    div.topics-container {
        display: flex;
        justify-content: center;
    }

</style>

<script>


    import {Vue} from "vue-property-decorator";
    import Component from "vue-class-component";
    import Topic from "@/components/Topic";
    import TopicData from "@/components/TopicData";

    @Component({
        components: {TopicData, Topic},
        props: {
            msg: {
                default: ''
            },

        }

    })
    export default class HeatMap extends Vue {
        topics = [{name: 'test', value: 10}];
        selectedTopicData = null;
        constructor() {
            super();

            this.getTopics();
        }

        async getTopics() {
            const response = await fetch('http://192.168.100.37:5000/pipeline/a');
            const topics = await response.json();
            this.topics = Object.entries(topics).map(item => ({name: item[0], value: item[1]}));
        }

        async topicSelected(topic) {
            const response = await fetch(`http://192.168.100.37:5000/pipeline/a/${topic.name}`);
            const topicData = await response.json();
            this.selectedTopicData = topicData;
        }

    }
</script>

<style scoped>

</style>
