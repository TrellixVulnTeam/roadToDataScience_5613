<template>
    <div id='content'>
        <div class="page-section" :style="style">
            <div v-if="content=='topics'">
                <Topics />
            </div>
        <div v-if="content=='popular'">
                <PopularPosts v-if="allPosts" :posts="allPosts" />
            </div>
        <div v-if="content=='about'">
                <HomepageAbout />
            </div>
        </div>
    </div>
</template>

<script>
import Topics from './Topics.vue'
import PopularPosts from './PopularPosts.vue'
import HomepageAbout from './HomepageAbout.vue'

import gql from 'graphql-tag'


export default {
    name: "HomePageSection",

    components: {
        Topics,
        PopularPosts,
        HomepageAbout
    },

    props: {
        color: String,
        content: String
    },
    apollo: {
    allPosts: gql`query {
      allPosts {
        title
        subtitle
        publishDate
        published
        metaDescription
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
    computed: {
    style () {
    return 'background-color: ' + this.color;
        }
    },
}
</script>


<style scoped>
.page-section{
    width: 100%;
    padding-top: 70px;
    min-height: 500px;
    padding-bottom: 30px;
}
#content{
    min-height: 100%;
}
</style>