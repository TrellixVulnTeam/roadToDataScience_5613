<template>
  <div>
  <header>
        <!-- This div is  intentionally blank. It creates the transparent black overlay over the video which you can modify in the CSS -->
    <div class="overlay"></div>

    <!-- The HTML5 video element that will create the background video on the header -->
    <video playsinline="playsinline" autoplay="autoplay" muted="muted" loop="loop">
        <source src="../assets/videoTitle.mp4" type="video/mp4">
    </video>

    <!-- The header content -->
    <div class="container h-100">
        <div class="d-flex h-100 text-right align-items-center">
        <div class="w-150 text-white">
        
        <h1>Road to Data Science</h1>
        
        </div>
        </div>
    </div>
    </header>
  <div class="container">
  <div class="post" v-if="post">



    <div class="author-tag">
        <span class="post-author">{{post.author.user.firstName}} {{post.author.user.lastName}}</span>
        <router-link style="text-decoration:none" :to="`/topic/${post.tags[0].name}`">
          <span class="post-tag">{{post.tags[0].name}}</span>  
        </router-link>
    </div>

    <h3 class="post-title">{{ post.title }}</h3>
    <p class="post-subtitle">{{ post.subtitle }}</p>
    <p class="post-date">{{ displayableDate(post.publishDate) }}</p>

    <img class="post-image" :src="`${post.postImage}`" alt="">

    <article class="post-body" v-html="post.body">
    </article>
  </div>

  <div class="newsletter">
    <p class="sign-up">Sign up to the newsletter</p>
    <p class="desc">Stay tuned for more great articles!</p>

    <form action="POST" @submit.prevent="subscribe">
    <input type="email" id="inlineFormInput" placeholder="Email" v-model="email">
    <button type="submit" class="btn-primary mb-2">Learn More</button>

    </form>
    <div v-if="subscribed"><p class="desc">Congratulations, you joined the newsletter</p></div>
  </div>



  </div>

  <div class="end-page">

  <div class="container more">
    
    <p class="more-title" style="font-weight:bolder">Read more from Road to Data Science</p>

    <PostList postsToRender = 3 />

  <div class="redirect">
    <router-link style="text-decoration:none" to="/blog">
      <p class="redirect-to-blog">Read more from Road to Data Science</p>
    </router-link>

  </div>
  </div>
  
  </div>


  </div>
</template>

<script>
import gql from 'graphql-tag'
import PostList from './blogpage/PostList.vue'
import { CreateEmail, EmailQuery } from '../graphqlQueries/graphql'



export default {
  name: 'Post',

  components:{
    PostList
  },

  data () {
    return {
      post: null,
      email: '',
      subscribed: false,
    }
  },
  async created () {
    const post = await this.$apollo.query({
        query: gql`query ($slug: String!) {
          postBySlug(slug: $slug) {
            title
            subtitle
            publishDate
            metaDescription
            slug
            body
            postImage
            author {
              user {
                username
                firstName
                lastName
              }
            }
            tags {
              name
            }
          }
        }`,
        variables: {
          slug: this.$route.params.slug,
        },
    })
    this.post = post.data.postBySlug

  },
  methods: {
    displayableDate (date) {
      return new Intl.DateTimeFormat('en-US', { dateStyle: 'full' }).format(new Date(date))
    },
    async subscribe() {
    const email = this.email

    if (email !== ''){
      this.subscribed = true
  
      // Call to the graphql mutation
      let data = await this.$apollo.mutate({
        // Query
        mutation: CreateEmail,
        // Parameters
        variables: {
          email: email,
        },
        update: (store, { data: { createEmail } }) => {
          // Add to All tasks list
          const data = store.readQuery({ query: EmailQuery })
          data.emails.push(createEmail.email)
          store.writeQuery({ query: EmailQuery, data })
        },
        })
        console.log( data)
    }

    }


  },
    
}
</script>

<style scoped>

h1{

  font-size:5vh;
  font-weight: lighter;
  width:100%;
  margin-top:7vh;
  margin-left: 10%;

}

header {
  position: relative;
  background-color: black;
  height: 25vh;
  min-height: 100%;
  width: 100%;
  overflow: hidden;
  margin-bottom: 10vh;
}

video {
  opacity: 0.3;
}

header video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: 0;
  -ms-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -webkit-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}

header .container {
  position: relative;
  z-index: 2;
}

header .overlay {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: black;
  opacity: 0.5;
  z-index: 1;
}


.post{
    
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 100%;
    max-width: 90vh;

}

.post-image{
    max-width: 100%;
    min-width: 100%;

}

.author-tag{
    margin-top: 4.1vh;
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
    margin-top: 3vh;
    font-size: 4.5vh;
    color: black;
    font-weight: bolder;
}

.post-subtitle{
    margin-bottom: 1vh;
    font-size: 2.5vh;
    color: rgb(117, 117, 117);
}

.post-date{
  margin-bottom: 4vh;
}

.post-body{
    color: rgba(41, 41, 41, 1);
    justify-content: center;
    font-size: 2.7vh;
    margin-top: 10vh;
    margin-bottom: 10vh;
    line-height: 4.5vh;
    letter-spacing: 0.02vw;

}

.post-tag{
    font-size: 1.5vh;
    font-weight: bolder;
    margin-left: 0.5vh;
    color: rgb(94, 94, 94);
    border-style: solid;
    border-width: 0.13vh;
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
    margin-top: 50px;
    margin-bottom: 50px;
}
.read{
    color: rgb(94, 94, 94);
    font-weight: bolder;
}

.newsletter{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  max-width: 90vh;

  background-color: #ffffff;
  background-image: linear-gradient(0deg, #ffffff 0%, #f7f7f7 74%);
  min-height: 33vh;
  padding: 5vh;

  border-top-style: solid;
  border-top-color: rgba(102, 138, 170, 1);
  border-top-width: 3px;

  margin-bottom: 10vh;
}

input {
    width: 40vh;
    height: 7vh;
    margin-top: 60px;
    font-size: 2vh;
    padding-left: 30px;
    outline: none;

}

button {
    width: 14vh;
    height: 7vh;
    font-size: 2vh;
    background-color: rgba(102, 138, 170, 1);
    border-style: none;
    border-color: rgba(102, 138, 170, 1);
    outline: none;
}


.sign-up{
  font-size:4vh;
  font-weight:700;
}

.desc{
  font-size:2.2vh;
}

.more{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  max-width: 90vh;

}

.more-title{
  font-size: 5vh;
  margin-bottom: 5vh;

}

.end-page{
  
  padding-top: 2vh;
  background-color: #ffffff;
  background-image: linear-gradient(0deg, #ffffff 0%, #f7f7f7 74%);

}

.redirect{


  width: 100%;
  width: 100%;
}

.redirect-to-blog{
  
  display: block;
  margin-left: auto;
  margin-right: auto;

  max-width: 45vw;
  font-size: 2vh;
  font-family: sohne, "Helvetica Neue", Helvetica, Arial, sans-serif;
  text-align: center;
  padding: 2vh;
  color:white;
  font-weight: bolder;
  border-radius: 5vh;
  background-color: rgba(102, 138, 170, 1);

  margin-bottom: 5vh;
}

.redirect :hover{
  background-color: rgb(116, 145, 170);
}


</style>