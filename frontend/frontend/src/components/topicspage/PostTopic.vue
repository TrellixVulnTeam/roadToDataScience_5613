<template>
<div>

    <div v-if="noPosts">
        <div class="post">
            <h3 class="post-title">No posts yet...</h3>
        </div>
    </div>

    <div v-else>
        <div class="post" v-for="post in getTopicPosts" :key="post.title">
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

</div>
</template>

<script>
export default {
    name:'PostsTopic',
    props:{
        posts: Array
    },
    
    
    computed:{
        postPublished(){
            return this.posts.filter(post => post.published)
        },
        
        getTopicPosts(){
            return this.posts.filter(post => (post.tags[0].name === this.$route.params.topic & post.published))
        },

        noPosts(){
            return this.getTopicPosts.length === 0
        }
    }
    }

</script>

<style scoped>

.post{
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 80vh;
    min-height: 100vh;

}

.post-image{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 100%;

}

.author-tag{
    margin-top: 30px;
    margin-bottom: 5px;
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
    border-width: 1px;
    padding: 1vh;
    border-radius: 50px;
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
    margin-top: 50px;
    margin-bottom: 50px;
}
.read{
    color: rgb(94, 94, 94);
    font-weight: bolder;
}


</style>