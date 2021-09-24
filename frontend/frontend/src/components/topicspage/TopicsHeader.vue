<template>
    <div class="container">
        <h1>Blog</h1>
        <h3>{{topic}}</h3>
    </div>
</template>

<script>
export default {
    name: 'TopicsHeader',
    props:{
        topic: String
    }
}
</script>

<style scoped>
.container{
    height: 100px;
}
h1{
    font-size:8vh;
    font-weight: lighter;
}
h3{
    font-size: 3vh;
    font-weight: lighter;
}
</style>