<template>
    <div class="home">
        <img alt="Pulsar logo" src="../assets/pulsar.png"/>
        <Heatmap msg="The pulsar monitor"/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import Heatmap from "@/components/Heatmap";

    export default {
        name: "Home",
        components: {
            Heatmap
        }


    };
</script>
