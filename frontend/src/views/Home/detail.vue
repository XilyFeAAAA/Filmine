<template>
    <div class="detail">
        <div
            class="box"
            :class="{ 'animated-loading': loading }"
            @wheel.prevent="boxScroll"
            :style="{
                backgroundImage: loading
                    ? ''
                    : `url(https://image.tmdb.org/t/p/original${data.detail.backdrop_path})`,
            }"
        >
            <div class="info" v-if="!loading" :class="{ scrolled: scrolled }">
                <div class="top">
                    <div class="left">
                        <div class="name">
                            <span>{{ data.detail.title || data.detail.name }}</span>
                        </div>
                        <div class="minor_info">
                            <span style="margin-right: 25px">
                                <font-awesome-icon
                                    icon="fa-solid fa-star"
                                    style="color: #fabc29; margin-right: 5px"
                                />
                                <span style="font-size: 1.1rem"
                                    >{{ data.detail.vote_average }}
                                </span>
                                / {{ data.detail.vote_count }}</span
                            >
                            <span
                                >{{ data.detail.runtime }} mins · {{ genre }} ·
                                {{ data.detail.release_date }}</span
                            >
                        </div>
                        <div class="summary">
                            {{ data.detail.overview }}
                        </div>
                        <div class="btns" style="margin-top: 50px">
                            <button style="background-color: #1f58ff">
                                <font-awesome-icon
                                    icon="fa-solid fa-play"
                                    style="margin-right: 15px"
                                />PLAY NOW
                            </button>
                            <button style="background-color: #3b424d">TRAILER</button>
                        </div>
                    </div>
                </div>
                <div class="bottom">
                    <div class="left">
                        <div class="panel">
                            <h3>Actors</h3>
                            <div class="cast-scroller">
                                <ul class="scroller">
                                    <li v-for="(cast, idx) in data.casts" :key="idx">
                                        <a
                                            ><img
                                                :src="
                                                    'https://image.tmdb.org/t/p/original' +
                                                    cast.profile_path
                                                "
                                        /></a>

                                        <p>
                                            <a>{{ cast.name }}</a>
                                        </p>
                                        <p>{{ cast.character.replace('(voice)', '') }}</p>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import Swiper from 'swiper'
export default {
    data() {
        return {
            genre: '',
            id: '',
            loading: true,
            scrolled: false,
            data: {
                detail: null,
                casts: null,
                videos: null,
            },
            urls: {
                detail: 'https://api.themoviedb.org/3/{genre}/{movie_id}?api_key=6c2c417273397900965840db9bc1ed55',
                credits:
                    'https://api.themoviedb.org/3/{genre}/{movie_id}/credits?api_key=6c2c417273397900965840db9bc1ed55',
                videos: 'https://api.themoviedb.org/3/{genre}/{movie_id}/videos?api_key=6c2c417273397900965840db9bc1ed55',
            },
        }
    },
    mounted() {
        this.genre = this.$route.params.genre
        this.id = this.$route.params.id
        this.getDetail()
        new Swiper('.poster-swiper', {
            slidesPerView: 5,
        })
    },
    beforeRouteUpdate(to, from, next) {
        this.genre = to.params.genre
        this.id = to.params.id
        this.getDetail().then(() => {
            next()
        })
    },
    methods: {
        // 阻止页面滚动的函数
        boxScroll(e) {
            e.preventDefault()
            this.scrolled = e.deltaY > 0
        },
        getAvatarUrl(path) {
            if (path === null) return ''
            if (path.indexOf('/https://secure.gravatar.com/avatar/') === 0) {
                // 如果是 Gravatar URL，直接返回
                return path.slice(1)
            } else {
                // 否则，拼接成 Gravatar URL 并返回
                return 'https://secure.gravatar.com/avatar/' + path.slice(1)
            }
        },
        async getDetail() {
            this.loading = true
            try {
                const [detailResp, creditsResp] = await Promise.all([
                    axios.get(
                        this.urls.detail
                            .replace('{genre}', this.genre)
                            .replace('{movie_id}', this.id),
                    ),
                    axios.get(
                        this.urls.credits
                            .replace('{genre}', this.genre)
                            .replace('{movie_id}', this.id),
                    ),
                ])
                this.data.detail = detailResp.data
                this.data.casts = creditsResp.data.cast.slice(0, 5)

                // 在这里处理返回的数据
            } catch (error) {
                console.error('请求数据失败：', error)
                // 在这里处理请求错误
            }
            this.loading = false
        },
    },
}
</script>
<style scoped>
::-webkit-scrollbar {
    width: 10px;
}
* {
    font-family: 'Roboto Condensed', 'Helvetica Neue', helvetica, arial, sans-serif;
}

.detail {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
.box {
    position: relative;
    height: 90%;
    width: 92%;
    letter-spacing: 1px;
    color: #fff;
    background-position: center center;
    border-radius: 1.5rem;
    overflow: hidden;
    box-shadow: 20px 20px 60px 0 rgba(0, 0, 0, 0.4);
}

.box:not(.animated-loading) {
    background-size: cover;
}

.info {
    position: absolute;
    width: 100%;
    height: 85%;
    bottom: -45%;
    transition: all 0.5s;
    background: linear-gradient(to top, #1b2331 0%, rgb(27, 35, 49) 20%, transparent 100%);
}

.info.scrolled {
    bottom: 0%;
}

.top {
    display: flex;
    width: 100%;
    height: 270px;
}

.top .left {
    width: 70%;
    height: 100%;
    padding-left: 5%;
}

.top .right .title {
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.top .right > div {
    height: 50%;
    width: 100%;
}

.top .left .name {
    letter-spacing: 0.5px;
    font-size: 4rem;
}

.minor_info {
    display: flex;
    align-items: center;
    font-size: 0.9rem;
    margin: 0.5rem auto 1rem;
}

.btns button {
    width: 10vw;
    height: 3rem;
    color: #fff;
    font-weight: bold;
    border-radius: 0.5rem;
    margin-right: 2rem;
    box-shadow: 0 8px 24px rgba(17, 17, 26, 0.1), 0 16px 56px rgba(17, 17, 26, 0.1),
        0 24px 140px 10px rgba(0, 0, 0, 0.1);
}

.bottom {
    display: flex;
    opacity: 0;
    margin-top: 50vh;
    padding-top: 5ch;
    transition: opacity 1s ease-in-out, margin-top 0.8s ease-in-out; /* 添加底部向上滑动的过渡动画 */
}

.bottom .left {
    width: 100%;
    padding-left: 5%;
}

.scrolled .bottom {
    opacity: 1;
    margin-top: 0;
}

.panel {
    width: 100%;
    display: block;
    padding-top: 30px;
    /* border-top: 1px solid #d7d7d7; */
}

.left .panel h3 {
    font-weight: 600;
    font-size: 1.4em;
    margin-bottom: 20px;
}

.cast-scroller {
    position: relative;
    top: 0;
    left: 0;
}

.scroller::-webkit-scrollbar {
    height: 8px;
    width: 8px;
}

.scroller::-webkit-scrollbar-track {
    background: transparent;
}

.scroller::-webkit-scrollbar-thumb {
    background-color: grey;
    border-radius: 20px;
}

.cast-scroller .scroller {
    position: relative;
    display: flex;
    top: 0;
    left: 0;
    list-style-type: none;
    list-style-position: inside;
    overflow-y: hidden;
    overflow-x: scroll;
    margin-left: -10px;
    margin-top: -10px;
    padding-bottom: 10px;
}

.scroller li {
    margin: 10px 4px 10px 10px;
    border: 1px solid grey;
    padding-bottom: 10px;
    border-radius: 8px;
    overflow: hidden;
    min-width: 140px;
    width: 140px;
    background-color: #fff;
    color: #000;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.3);
}

.scroller li > a {
    min-width: 138px;
    width: 138px;
    height: 175px;
    display: block;
}

.scroller li img {
    width: 100%;
    height: 100%;
}
img,
a img {
    outline: none;
}

.scroller li > p {
    text-align: center;
    padding-top: 10px;
    font-size: 1em;
    overflow: hidden;
    text-overflow: ellipsis;
}

.scroller li > p a {
    font-weight: bold;
    color: #000;
}
</style>
