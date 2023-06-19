import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/Login/index.vue'
import Index from '@/views/Home/index.vue'
import Home from '@/views/Home/home.vue'
import Discovery from '@/views/Home/discovery.vue'
import Detail from '@/views/Home/detail.vue'
import NotFound from '@/views/notFound.vue'
import Store from '@/views/Home/store.vue'

// import utils function
import { verify } from '@/utils/account'
Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '*',
            component: NotFound,
        },
        {
            path: '/',
            component: Index,
            meta: {
                requireAuth: true, // 需要鉴权
            },
            children: [
                {
                    path: '/',
                    redirect: '/home',
                },
                {
                    path: '/home',
                    name: 'Home',
                    component: Home,
                },
                {
                    path: '/discovery',
                    redirect: '/discovery/movie/trending',
                },
                {
                    path: '/discovery/:genre/:t',
                    name: 'Discovery',
                    component: Discovery,
                },
                {
                    path: '/detail/:genre/:id',
                    name: 'Detail',
                    component: Detail,
                },
                {
                    path: '/store/:method?/:token?',
                    name: 'Store',
                    component: Store,
                    props: true,
                },
            ],
        },
        {
            path: '/login',
            name: 'Login',
            component: Login,
        },
    ],
})

// router.beforeEach((to, from, next) => {
//     const requireAuth = to.matched.some((record) => record.meta.requireAuth)
//     if (requireAuth) {
//         // 验证token
//         verify().then((response) => {
//             if (response) {
//                 console.log('verify')
//                 next()
//                 console.log('in')
//             } else {
//                 console.log('not')
//                 next('/login')
//             }
//         })
//     } else next()
// })

export default router
