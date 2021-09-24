<template>
    <div>
        <div class="post" v-for="post in postPublished" :key="post.title">
            <div class="author-tag">
                <span class="post-author">{{post.author.user.firstName}} {{post.author.user.lastName}}</span>
                <router-link style="text-decoration:none" :to="`/topic/${post.tags[0].name}`">
                    <span class="post-tag">{{post.tags[0].name}}</span>
                </router-link>
            </div>
            <router-link style="text-decoration:none" :to="`/post/${post.slug}`">
                <h3 class="post-title">{{post.title}}</h3>
            </router-link>
            <p class="post-subtitle">{{post.subtitle}}</p>
            <p class="post-date">{{ displayableDate(post.publishDate) }}</p>
            <router-link style="text-decoration:none" :to="`/post/${post.slug}`">
                <img class="post-image" :src="`${post.postImage}`" alt="">
            </router-link>
            <article class="post-truncated-body" v-html="post.truncatedBody"></article>
            <router-link style="text-decoration:none" :to="`/post/${post.slug}`">
                <div class="read">
                    <span class="post-reading-time">Reading time</span>
                    <span class="time">{{post.readingTime}} Min</span>
                </div>
            </router-link>

            <hr>
        </div>
        
    </div>
</template>

<script>
export default {
    name:'Posts',
    props:{
        posts: Array
    },
    
    computed:{
        postPublished(){
            return this.posts.filter(post => post.published)
        }
    },
    methods: {
    displayableDate (date) {
      return new Intl.DateTimeFormat('en-US', { dateStyle: 'full' }).format(new Date(date))
    }
  },
    watch: {
      '$route': function () {
        location.reload()
      }
    },
}
</script>

<style scoped>

.post{
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 80vh;

}

.post-image{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 100%;

}

.author-tag{
    margin-top: 4vh;
    margin-bottom: 0.7vh;
}
.horizontal-margin{
    width: 5vw;
    font-size: 1.5vh;
}

.post-author{
    font-size: 1.5vh;
    color: rgb(0, 74, 134);
    font-weight: bolder;
    white-space:normal;
}
.post-author::after{
    content: " \00B7";
    color: black;
}

.post-title{
    margin-top: 2vh;
    font-size: 4.5vh;
    color: black;
    font-weight: bolder;
}
.post-date{
    font-size: 1.8vh;
    margin-bottom: 3vh;
}

.post-subtitle{
    margin-bottom: 2vh;
    font-size: 2.5vh;
    color: rgb(117, 117, 117);
}

.post-truncated-body{
    font-size: 2.7vh;
    font-weight: 400;
    margin-top: 3vh;
    margin-bottom: 3vh;
    line-height: 4.5vh;
    letter-spacing: 0.03vw;
    text-rendering: optimizeLegibility;
}
.post-tag{
    font-size: 1.5vh;
    font-weight: bolder;
    margin-left: 0.5vh;
    color: rgb(94, 94, 94);
    border-style: solid;
    border-width: 0.01vh;
    padding: 1vh;
    border-radius: 7vh;
    text-align: center;
}
.time{
    margin-left: 0.5vh;
}

.post-reading-time{
    font-weight: bolder;
}
.post-reading-time:after{
    content: " \00B7"
}


hr{
    margin-top: 7vh;
    margin-bottom: 7vh;
}
.read{
    color: rgb(94, 94, 94);
    font-weight: bolder;
    font-size: 2vh;
}


</style>