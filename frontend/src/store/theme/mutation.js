export default {
    setTheme(state, theme) {
        state.theme = theme
        console.log(theme)
        localStorage.setItem('filmine-theme', theme)
        document.head
            .querySelector('#theme-link')
            .setAttribute('href', `<%= BASE_URL %>${theme}-theme.css`)
    },
    //获取缓存主题
    getTheme(state) {
        state.theme = localStorage.getItem('filmine-theme') || 'light'
        document.head
            .querySelector('#theme-link')
            .setAttribute('href', `./${state.theme}-theme.css`)
    },
}
