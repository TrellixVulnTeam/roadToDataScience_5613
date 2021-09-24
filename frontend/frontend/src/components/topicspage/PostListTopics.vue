<template>
    <div class="container">
        <div>
            <PostsTopic  v-if="allPosts" :posts=allPosts />
        </div>

    </div>
</template>

<script>

import PostsTopic from './PostTopic.vue'

import gql from 'graphql-tag'

export default {
    name: 'PostList',

    props:{
        topic: String
    },

    components: {
        PostsTopic
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