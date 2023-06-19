export default {
    setLayer(state, payload) {
        console.log(payload)
        state.data = payload.data
        state.data.genre = payload.genre
        state.isShow = true
    },
    closeLayer(state) {
        state.isShow = false
    },
}
