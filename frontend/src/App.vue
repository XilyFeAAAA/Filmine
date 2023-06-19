<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'App',
    created() {
        this.$store.commit('theme/getTheme') /*加载上次退出是选择的主题*/
    },
}
</script>

<style>
#app {
    position: relative;
    width: 100%;
    height: 100%;
}
</style>
