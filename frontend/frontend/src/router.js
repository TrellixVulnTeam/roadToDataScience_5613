import Vue from 'vue'
import VueRouter from 'vue-router'

import Post from '@/components/Post'
import Author from '@/components/Author'
import Topics from '@/views/Topics'
import AllPosts from '@/components/AllPosts'
import Home from '@/views/Home'
import Blog from '@/views/Blog'
import About from '@/views/About'
import Contact from '@/views/Contact'



Vue.use(VueRouter)

const routes = [
    { path: "/author/:username",component: Author},
    { path: '/post/:slug', component: Post },
    { path: '/topic/:topic', component: Topics, props:true},
    { path: '/', component: Home }, 
    { path: '/posts', component: AllPosts },
    { path: '/blog', component: Blog, props:true},
    { path: '/about', component: About},
    { path: '/contact', component: Contact}
]

const router = new VueRouter({
    routes: routes,
    mode: 'history',
    scrollBehavior() {
        document.getElementById('app').scrollIntoView();
    }
})

export default router