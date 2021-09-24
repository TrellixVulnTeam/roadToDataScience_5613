<template>
    <div class="container">

    <div class="row align-items-center">
        <div class="col">
            <div class="col title">
                <h1>How can i help you learning data science</h1>
                <hr>
            </div>
            <p id="introduction-text">
                Data Science is a vast field with many application in almost every sector and it's easy to get lost. I started my journey during my bachelor degree in Physics. At the time i used what i found on the internet to improve my skills but i was often overwelmed by the amount of the material available online. In this blog i'll try to guide you throught main 
                topics, giving you the best tips and a solid mathematical background. 
            </p>
            <p id="introduction-text">Welcome in the amazing world of data science!</p>
            <router-link to="/blog" style="text-decoration:none">
                <button class="btn btn-outline-primary">Start Learning Now</button>
            </router-link>
        </div>
    </div>

    </div>
</template>

<script>
export default {
    name: "SecondSection"
}
</script>


<style scoped>

.container{
    margin-top: 5vh;
    min-height: 100%;
    margin-bottom:  20vh;
}

.title{
    width: 100%;
    text-align: center;
    margin-bottom: 5vh;

}

h1 {
    margin-bottom: 20px;
    font-size: 6vh;
    font-weight: lighter;
}
#introduction-text{
    text-align: center;
    font-size: 3vh;
    margin-bottom: 1vh;
    color: rgba(41, 41, 41, 1);
    line-height: 4vh;
    letter-spacing: -0.1vh;
    text-rendering: optimizeLegibility;

}


hr{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 7vw;
    height: 0.5vh;
    color: rgb(14, 99, 173);
}
.btn{
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 4vh;
    margin-bottom: 4vh;
}

</style>