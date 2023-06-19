<template>
    <div class="login">
        <div class="container log-panel" v-show="!reg">
            <div class="title">
                <img src="/logo.svg" />
                <h2>登录到Filmine</h2>
            </div>
            <input type="text" name="username" v-model="username" placeholder="输入你的用户名" />
            <input
                type="password"
                name="password"
                v-model="password"
                placeholder="输入你的密码"
                @keydown.enter="handleLogin"
            />
            <div class="login-tools">
                <div class="remember"><input type="checkbox" :value="remember" />记住账号</div>
                <span @click="reg = true" style="cursor: pointer">还未注册？</span>
            </div>

            <div class="btns">
                <button class="btn-clear" @click="handleClear">清除</button>
                <button class="btn-login" @click="handleLogin">登陆</button>
            </div>
            <button class="btn-tourist">以游客身份登陆</button>
            <div class="web-tools">
                <font-awesome-icon
                    :icon="['fas', 'language']"
                    size="2xl"
                    style="color: rgb(120, 127, 133); cursor: pointer"
                />
                <font-awesome-icon
                    :icon="['fas', 'moon']"
                    size="xl"
                    style="color: rgb(120, 127, 133); cursor: pointer"
                    @click="switchTheme"
                />
            </div>
        </div>
        <div class="container reg-panel" v-show="reg">
            <div class="title">
                <img src="/logo.svg" />
                <h2>注册Filmine</h2>
            </div>
            <input type="text" v-model="username" placeholder="输入你的用户名" />
            <input type="email" v-model="email" placeholder="输入你的邮箱" />
            <input
                type="password"
                v-model="password"
                placeholder="输入你的密码"
                @keydown.enter="handleLogin"
            />
            <div class="tips" :class="{ active: send }">
                <p>
                    <span><font-awesome-icon :icon="['fas', 'exclamation']" /></span>
                    注册邮件已发送，请在邮箱确认
                </p>
            </div>
            <div class="btns">
                <button class="btn-clear" @click="handleClear">清除</button>
                <button class="btn-login" @click="handleRegister">注册</button>
            </div>
            <div class="web-tools">
                <font-awesome-icon
                    :icon="['fas', 'language']"
                    size="2xl"
                    style="color: rgb(120, 127, 133); cursor: pointer"
                />
                <font-awesome-icon
                    :icon="['fas', 'moon']"
                    size="xl"
                    style="color: rgb(120, 127, 133); cursor: pointer"
                    @click="switchTheme"
                />
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            reg: false,
            username: '',
            password: '',
            email: '',
            send: false,
            remember: false,
            theme: localStorage.getItem('filmine-theme') || 'light',
        }
    },
    methods: {
        handleClear() {
            this.username = ''
            this.password = ''
            this.email = ''
        },
        handleRegister() {
            this.send = true
            axios
                .post(
                    this.$api.INTERFACES.registerAPI,
                    {
                        username: this.username,
                        password: this.password,
                        email: this.email,
                    },
                    {
                        headers: {
                            'Content-Type': 'application/json',
                        },
                    },
                )
                .then((response) => {
                    if (response.data.code === 200) {
                        this.send = false
                    } else {
                        alert('注册失败,用户名或邮箱重复')
                    }
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        handleLogin() {
            axios
                .post(
                    this.$api.INTERFACES.loginAPI,
                    {
                        grant_type: 'password',
                        username: this.username,
                        password: this.password,
                    },
                    {
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                        },
                    },
                )
                .then((response) => {
                    if (response.data.code === 200) {
                        localStorage.setItem('token', response.data.data.token)
                        console.log('resolve')
                        this.$router.push({ path: '/home' })
                    } else {
                        // 登录失败，提示错误信息
                        alert(' 登录失败')
                    }
                })
                .catch((error) => {
                    console.error(error)
                    // 处理请求错误
                })
        },
        switchTheme() {
            this.theme = this.theme === 'light' ? 'dark' : 'light'
            this.$store.commit('theme/setTheme', this.theme)
        },
    },
}
</script>
<style scoped>
.login {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    background-size: 400%;
    background-image: var(--bg-image);
    animation: bgmove 20s infinite;
}

.container.reg-panel {
    /* display: none; */
}

.reg .reg-panel {
    display: block;
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 1rem;
    width: 364px;
    border-radius: 0.75rem;
    padding: 24px;
    background: var(--login-bg-color);
    transition: 0.5s;
}

.container > input {
    border: 1px solid transparent;
    background-color: #f1f3f5;
    min-height: 2.5rem;
    font-size: 0.8rem;
    line-height: 1rem;
    color: #11181c;
    width: 100%;
    padding-inline-start: 0.75rem;
    padding-inline-end: 0.75rem;
    border-radius: 0.5rem;
    transition: border-color 0.3s ease-in-out;
}
.container input:focus {
    border: 1px solid #5eb0ef;
}

.title {
    display: flex;
    align-items: center;
    justify-content: space-around;
}

.title img {
    width: 3rem;
    height: 3rem;
    margin-right: 0.5rem;
}

.title h2 {
    color: #0091ff;
    font-size: 1.7rem;
}

.login-tools {
    display: flex;
    padding-inline-start: 0.25rem;
    padding-inline-end: 0.25rem;
    width: 100%;
    font-size: 0.8rem;
    color: #7e868c;
    justify-content: space-between;
    align-items: center;
}

.login-tools .remember {
    position: relative;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    cursor: pointer;
    user-select: none;
    color: #7e868c;
}

.login-tools .remember input {
    margin-top: 0.2rem;
    width: 1rem;
    height: 1rem;
    cursor: pointer;
}

.btns {
    display: flex;
    flex-direction: row;
    align-items: center;
    column-gap: 0.5rem;
    width: 100%;
}

button {
    width: 100%;
    height: 2.5rem;
    font-size: 1rem;
    padding-top: 0px;
    padding-bottom: 0px;
    padding-inline-start: 1rem;
    padding-inline-end: 1rem;
    border-radius: 0.5rem;
    border: 1px solid transparent;
    cursor: pointer;
    transition: transform 0.1s ease-in;
}

button:active {
    transform: scale(0.95);
}

.btn-clear {
    color: #0c7792;
    background-color: #d8f3f6;
}

.btn-clear:hover {
    background-color: #c4eaef;
}

.btn-login {
    color: #006adc;
    background-color: #e1f0ff;
}

.btn-login:hover {
    background-color: #cee7fe;
}

.btn-tourist {
    color: #5746af;
    background-color: #ede9fe;
}

.btn-tourist:hover {
    background-color: #e4defc;
}

.web-tools {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;
}

@keyframes bgmove {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.tips {
    display: none;
    padding: 0.375rem 0;
    font-size: 0.675rem;
    width: 100%;
    color: #444;
    text-align: center;
    background-color: #d8f3f6;
    border-radius: 5px;
}
.tips p {
    display: flex;
    justify-content: center;
    align-items: center;
}

.tips span {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 15px;
    width: 15px;
    border: 1px solid #666;
    border-radius: 50%;

    margin-right: 5px;
}

.tips.active {
    display: block;
}
</style>
