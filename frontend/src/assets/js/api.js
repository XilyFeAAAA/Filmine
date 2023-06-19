const baseURL = 'http://localhost:7070'
const apiLIST = {
    loginAPI: '/user/login',
    registerAPI: '/user/register',
    verifyAPI: '/user/verify',
    addProjectAPI: '/store/add',
    deployProjectAPI: '/store/deploy',
    qrcodeAPI: '/store/qrcode',
    getStoretAPI: '/store/get',
    stateAPI: '/store/state',
    getProjectAPI: '/store/project',
    getMovieStatsAPI: '/store/getMovieStats',
}

const base = function () {
    let api = {}
    for (let k in apiLIST) {
        api[k] = baseURL + apiLIST[k]
    }
    return api
}

export default {
    INTERFACES: base(),
}
