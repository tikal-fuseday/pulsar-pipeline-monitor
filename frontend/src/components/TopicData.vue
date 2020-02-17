<template>
    <div>
        <h3>{{topicData.name}}</h3>
        <div>
            Message rate In: {{Math.floor(topicData.msgRateIn * 100) / 100}}
        </div>
        <div>
            Message Rate Out: {{Math.floor( topicData.msgRateOut * 100) / 100}}
        </div>
        <div>
            Average message size: {{Math.floor( topicData.averageMsgSize)}}
        </div>
        <div>
            Storage size: {{Math.floor( topicData.storageSize)}}
        </div>
        <div>
            Backlog size: {{Math.floor( topicData.backlogSize)}}
        </div>
    </div>
</template>

<script>
    import {Vue} from "vue-property-decorator";
    import Component from "vue-class-component";

    @Component({
    props: {
        topicData: {
            default : () => ({})
        }
    }
    })
    export default class TopicData extends Vue{

    }
</script>

<style scoped>

</style>
