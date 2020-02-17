<template>
    <div>
        <label>Pipeline name
        <input type="text" v-on:change="queryPipeline($event)"></label>

        <label>
            Topics
            <input type="text" placeholder="topics" ref="topicNames">

        </label>
        <button v-on:click="addTopic()" >Create topics</button>


        <div class="topics-container">
            <div v-for="item in this.topics" v-bind:key="item.name" style="display: flex">
                <Topic v-bind:topic="item" v-on:topicSelected="topicSelected($event)">
                </Topic>
                <div v-if="item !== topics[topics.length - 1]">
                    <svg height="5px" width="100px">
                        <line x1="0" y1="0" x2="100" y2="0" style="stroke:rgb(0,0,0);stroke-width:5"/>
                    </svg>
                </div>
            </div>

        </div>
        <TopicData v-if="selectedTopicData" v-bind:topic-data="this.selectedTopicData"></TopicData>

        <div v-bind:style="getStyle(getMaxValue())">
            Pipeline value {{getMaxValue()}}
        </div>
    </div>
</template>

<style scoped>
    div.topics-container {
        display: flex;
        justify-content: center;
        max-width: 70em;
        overflow-x: scroll;
    }
    div.topics-container div {
        align-self: center;
    }

</style>

<script>


    import {Vue} from "vue-property-decorator";
    import Component from "vue-class-component";
    import Topic from "@/components/Topic";
    import TopicData from "@/components/TopicData";
    import {TopicsService} from "@/services/topics-service.js";

    const topicsService = new TopicsService();
    @Component({
        components: {TopicData, Topic},
        props: {
            msg: {
                default: ''
            },

        }

    })
    export default class HeatMap extends Vue {
        topics = [];
        selectedTopicData = null;

        queryPipeline(changeEvent) {
            const pipelineName = changeEvent.target.value;
            this.pipelineName = pipelineName;
            this.getTopics(pipelineName);
        }

        getMaxValue() {
            if (!this.topics || !this.topics.length) {
                return null;
            }
            return this.topics.map( t=> t.value ).reduce((accumolator, value) =>  value > accumolator ? value : accumolator);
        }

        getStyle(maxValue) {
            return {'background-color':  topicsService.getColor(10 - maxValue)};
        }

        async getTopics(pipelineName) {

            try {
                this.topics = await topicsService.getTopics(pipelineName);
            } catch(err) {
                this.topics = [];
            }

        }

        async topicSelected(topic) {
            this.selectedTopicData = await topicsService.getTopicData(this.pipelineName, topic);

        }
        addTopic() {
            topicsService.queryTopics(this.pipelineName, this.$refs.topicNames.value);
        }

    }
</script>


