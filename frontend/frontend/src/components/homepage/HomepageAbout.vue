<template>
    <div class="container">

    <div class="row align-items-center">
        <div class="col">
            <div class="col title">
                <h1>Who am I?</h1>
                <hr>
            </div>
            <p id="introduction-text">
               Hi everyone, i'm Alberto and i'm here to guide you in the word of data science. Okay that's interesting, but who am i? I'm a student at the University of Milano Bicocca where i am attending the master's degree course in data science. I also have a bachelor degree in Physics. My aim is to show you all the major data science topics, exactly like if you were attending a university course.
            </p>
            <router-link to="/blog" style="text-decoration:none">
                <button class="btn btn-outline-primary">Start Learning Now</button>
            </router-link>
        </div>
        <div class="col ">
            <img class="profile-img" src="https://cdn.pixabay.com/photo/2018/03/30/15/12/dog-3275593_960_720.jpg" alt="">
        </div>
    </div>

    </div>
</template>

<script>
export default {
    name: "HomepageAbout"
}
</script>

<style scoped>

.container{
    min-height: 70vh;
    margin-bottom: 30px;
    width: 100%;
}

.title{
    width: 100%;
    text-align: center;
    margin-bottom: 5vh;
}

.row{
    margin-top: 10vh;
    margin-left: auto;
    margin-right: auto;
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

h1 {
    margin-bottom: 1vh;
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


.profile-img{
    height:40vh;
    width:40vh;
    border-radius:50%;
    display: block;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 3px 6px #888888;
}

</style>