<template>
    <div class="discovery">
        <div class="discovery-title">{{ this.genre }} / {{ this.t }}</div>
        <div class="discovery-wrap">
            <poster
                class="Poster"
                v-for="(poster, idx) in posters"
                :key="idx"
                :genre="genre"
                :poster="poster"
            />
        </div>
        <div v-if="loading">Loading...</div>
    </div>
</template>
<script>
import { throttle } from 'lodash'
import axios from 'axios'
import row from '@/components/row.vue'
import poster from '@/components/poster.vue'
export default {
    components: {
        row,
        poster,
    },
    data() {
        return {
            genre: '',
            t: '',
            page: 1,
            loading: false, // 控制是否展示 loading
            posters: [], // 用于存放已加载的 item
            threshold: 100, // 距离底部多少像素时触发加载
            urls: {
                'movie/trending': 'https://api.themoviedb.org/3/trending/movie/week',
                'tv/trending': 'https://api.themoviedb.org/3/trending/tv/week',
            },
        }
    },
    mounted() {
        this.genre = this.$route.params.genre
        this.t = this.$route.params.t
        this.loadPosters()
        document
            .querySelector('.discovery')
            .addEventListener('scroll', throttle(this.handleScroll, 3000)) // 绑定滚动事件
    },
    beforeRouteUpdate(to, from, next) {
        this.genre = to.params.genre
        this.t = to.params.t
        this.loadPosters().then(() => {
            next()
        })
    },
    methods: {
        async loadPosters() {
            this.page = 1
            this.posters = await this.getMovies()
            await this.addPosters()
        },
        async addPosters() {
            this.posters.push(...(await this.getMovies()))
        },
        async getMovies() {
            this.loading = true
            const key = '6c2c417273397900965840db9bc1ed55' // API key
            const sort = 'popularity.desc'
            const lang = 'en-US'
            const { data } = await axios.get(this.urls[`${this.genre}/${this.t}`], {
                params: {
                    api_key: key,
                    sort_by: sort,
                    language: lang,
                    page: this.page,
                },
            })
            this.page++
            this.loading = false
            return data.results
        },
        handleScroll() {
            const scrollTop = document.querySelector('.discovery').scrollTop
            const windowHeight = window.innerHeight // 获取视口高度
            const scrollHeight = document.querySelector('.discovery').scrollHeight
            if (scrollHeight - (scrollTop + windowHeight) < this.threshold) {
                // 判断是否已滚动到底部
                this.addPosters()
            }
        },
    },
    beforeDestroy() {
        document
            .querySelector('.discovery')
            .removeEventListener('scroll', throttle(this.handleScroll, 3000)) // 解绑滚动事件
    },
}
</script>
<style>
.discovery {
    position: relative;
    padding: 2rem 2rem 0;
    width: 100%;
    height: 100%;
    overflow-x: hidden;
}

.discovery-title {
    font-size: 1.2vw;
    color: var(--text1-color);
}

.discovery-wrap {
    display: flex;
    flex-wrap: wrap; /* 每行超出范围自动到下一行 */
    justify-content: start; /* 元素之间的间距自动 */
    align-items: center; /* 元素垂直居中对齐 */
    margin-top: 2rem;
    width: 100%;
    /* overflow-y: auto; */
}

.discovery .Poster {
    margin: 0 10px 50px 0;
    transition: transform 0.5s 0.2s;
}

@media (min-width: 330px) {
    .Poster {
        width: calc(50% - 10px);
    }
    .Poster:nth-child(1n) {
        transform-origin: initial;
    }
    .Poster:nth-child(2n + 1) {
        transform-origin: left;
    }
    .Poster:nth-child(2n + 2) {
        transform-origin: right;
    }
}

@media (min-width: 625px) {
    .Poster {
        width: calc(33.3% - 10px);
    }
    .Poster:nth-child(1n) {
        transform-origin: initial;
    }
    .Poster:nth-child(3n + 1) {
        transform-origin: left;
    }
    .Poster:nth-child(3n + 3) {
        transform-origin: right;
    }
}

@media (min-width: 998px) {
    .Poster {
        width: calc(25% - 10px);
    }
    .Poster:nth-child(1n) {
        transform-origin: initial;
    }
    .Poster:nth-child(4n + 1) {
        transform-origin: left;
    }
    .Poster:nth-child(4n + 4) {
        transform-origin: right;
    }
}

@media (min-width: 1378px) {
    .Poster {
        width: calc(16.6% - 10px);
    }
    .Poster:nth-child(1n) {
        transform-origin: initial;
    }
    .Poster:nth-child(6n + 1) {
        transform-origin: left;
    }
    .Poster:nth-child(6n + 6) {
        transform-origin: right;
    }
}

.discovery .poster:hover {
    z-index: 999;
    transform: scale(1.3);
}

.discovery .poster:hover .poster-info {
    opacity: 1;
    transform: translateY(0);
}
.discovery .poster:hover::after {
    opacity: 1;
}
</style>
