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
}

    div:hover {
        opacity: 0.8;
        font-weight: bolder;
    }
</style>
<script>
import {Vue} from "vue-property-decorator";

  import Component from "vue-class-component";

const colors = ['#00FF00','#7FFF00', '#FDFF03', '#FFFF00', '#FF0000' ];

@Component({
        props: {
            topic: {
                    default: {name: 'test', value: 10}
            }
        }
    })
    export default class Topic extends Vue {

        getStyle(value) {
            return  {color: 'black',
            'background-color': `${this.getColor(value)}FE` };
        }

        onClick() {
            this.$emit('topicSelected', this.topic);
        }


        getColor(value) {

            const [min, max] = [0, 10];

            const middle = ( min + max ) / 2;
            const scale = 255 / ( middle - min );

            if (value <= min) {
                return '#FF0000';
            }
            if (value >= max) {
                return '#00FF00';
            }
            if (value < middle) {
                return `#FF${ ((value - min) * scale).toString(16)}00`;
            }

            return `#FF${((value - middle) * scale).toString(16)}00`;

          //  const colorValue = Math.round(value / 2);

          //  return  colors[colorValue - 1];

        }

    }
</script>

<style scoped>

</style>
