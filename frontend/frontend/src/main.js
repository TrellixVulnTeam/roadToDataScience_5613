import Vue from 'vue'
import App from './App.vue'

import { createProvider } from './vue-apollo'

import router from '@/router'

import VuePrism from 'vue-prism'

import 'prismjs/themes/prism-okaidia.css'
import 'prismjs/components/prism-python.js'

Vue.use(VuePrism)

Vue.config.productionTip = false



new Vue({
  router,

  apolloProvider: createProvider({
    httpEndpoint: 'http://localhost:8000/graphql',
    wsEndpoint: null,
  }),

  render: h => h(App),
}).$mount('#app')
