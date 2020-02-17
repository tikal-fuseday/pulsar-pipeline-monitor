<template>
    <div>
        <div>
            Message rate In: {{Math.floor(topicData.msgRateIn)}}
        </div>
        <div>
            Message Rate Out: {{Math.floor( topicData.msgRateOut)}}
        </div>
        <div>
            Average message size: {{Math.floor( topicData.averageMsgSize)}}
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
