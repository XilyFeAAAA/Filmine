import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './routers'

// 引入全局样式
import '@/assets/css/base.css'
import '@/assets/css/xilyfe.css'
import 'swiper/css/swiper.min.css'
// 引入全局URL
import api from '@/assets/js/api'
Vue.prototype.$api = api
//挂载genre
Vue.prototype.$genres = {
    28: 'Action',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    80: 'Crime',
    99: 'Documentary',
    18: 'Drama',
    10: 'Family',
    14: 'Fantasy',
    36: 'History',
    27: 'Horror',
    10402: 'Music',
    9648: 'Mystery',
    10749: 'Romance',
    878: 'Science Fiction',
    10770: 'TV Movie',
    53: 'Thriller',
    10752: 'War',
    37: 'Western',
    10751: 'Family',
}
// 引入icon
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
Vue.component('font-awesome-icon', FontAwesomeIcon)
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
library.add(fas)

Vue.config.productionTip = false

new Vue({
    store,
    router,
    render: (h) => h(App),
}).$mount('#app')
