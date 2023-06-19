import Vue from 'vue'
import Vuex from 'vuex'

// 导入store
import theme from './theme'
import layer from './layer'
// 应用Vuex插件
Vue.use(Vuex)
export default new Vuex.Store({
    modules: {
        theme,
        layer,
    },
})
