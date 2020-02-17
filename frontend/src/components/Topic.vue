<template>
    <div v-bind:style="this.getStyle(topic.value)" v-on:click="onClick()">
        {{topic.name}} ({{topic.value}})
    </div>

</template>
<style scoped>

    div {
        border-style: solid;
        border-width: 1px;
        border-radius: 5px;
        cursor: pointer;
        transition: font-weight 0.5s;
        min-height: 2em;
        padding: 3px;
        padding-top: 10px;
    }

    div:hover {
        opacity: 0.8;
        font-weight: bolder;
    }
</style>
<script>
    import {Vue} from "vue-property-decorator";

    import Component from "vue-class-component";
    import {TopicsService} from "@/services/topics-service";

    const topicsService = new TopicsService();

    @Component({
        props: {
            topic: {
                default: {name: 'test', value: 10}
            }
        }
    })
    export default class Topic extends Vue {

        getStyle(value) {
            return {
                color: 'black',
                'background-color': `${topicsService.getColor(10 - value)}FE`
            };
        }

        onClick() {
            this.$emit('topicSelected', this.topic);
        }




    }
</script>

<style scoped>

</style>
