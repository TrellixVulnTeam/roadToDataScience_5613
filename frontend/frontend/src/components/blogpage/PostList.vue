<template>
    <div class="container">
        <div>
            <div v-if="postsToRender">
              <Posts  v-if="allPosts" :posts=allPosts.slice(0,postsToRender) />
            </div>
            <div v-else>
              <Posts  v-if="allPosts" :posts=allPosts />
            </div>
        </div>

    </div>
</template>

<script>

import Posts from '../blogpage/Posts.vue'
import gql from 'graphql-tag'

export default {
    name: 'PostList',

    components: {
        Posts
    },

    props:{
      postsToRender: String,
    },

    apollo: {
    allPosts: gql`query {
      allPosts {
        title
        subtitle
        publishDate
        published
        metaDescription
        truncatedBody
        postImage
        readingTime
        body
        slug
        popular
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
    }`
    },
    
}
</script>



<style scoped>

</style>