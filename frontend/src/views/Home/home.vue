<template>
    <div class="home">
        <div class="middle">
            <!-- <navHeader :navItems="navHeaderItems" style="margin-bottom: 1rem" /> -->
            <div class="swiper-container banner-swiper">
                <div class="swiper-wrapper">
                    <div v-for="(info, index) in banner_info" :key="index" class="swiper-slide">
                        <banner :info="info" class="banner" />
                    </div>
                </div>
                <!-- 如果需要分页器 -->
                <div class="swiper-pagination"></div>
            </div>
            <div class="row-block">
                <row v-for="(val, key) in rows" :key="key" :row_data="val" :title="key" />
            </div>
        </div>
        <div class="right-slider">
            <div class="search-input">
                <input type="text" placeholder="Type to Search..." />
                <span><font-awesome-icon :icon="['fas', 'magnifying-glass']" /> </span>
            </div>
            <div class="more">
                <moreVideo v-for="(info, index) in more_info" :key="index" :info="info" />
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import navSlider from '@/components/navSlider.vue'
import banner from '@/components/banner.vue'
import moreVideo from '@/components/moreVideo.vue'
import row from '@/components/row.vue'
import Swiper from 'swiper'
export default {
    components: {
        navSlider,
        banner,
        moreVideo,
        row,
    },
    data() {
        return {
            banner_info: [],
            rows: {
                trending: [],
                rated: [],
                netflix: [],
                upcoming: [],
            },
            more_info: [
                {
                    title: 'Popular Series',
                    videos: [
                        {
                            url: 'https://picx.zhimg.com/80/v2-32163c331f2ff31771c67ab232171e52_720w.webp?source=1940ef5c',
                            name: 'Wayne',
                            episode: 'Season1/Season Series 13',
                            score: '8.8',
                        },
                        {
                            url: 'https://pic.monidai.com/img/upload/vod/2021-05-13/202105131620900645.jpg',
                            name: 'The end of the fucking world',
                            episode: 'Season1/Season Series 13',
                            score: '8.7',
                        },
                    ],
                },
                {
                    title: 'Watchlists',
                    videos: [
                        {
                            url: 'https://picx.zhimg.com/80/v2-32163c331f2ff31771c67ab232171e52_720w.webp?source=1940ef5c',
                            name: 'Wayne',
                            episode: 'Season1/Season Series 13',
                            score: '8.8',
                        },
                        {
                            url: 'https://pic.monidai.com/img/upload/vod/2021-05-13/202105131620900645.jpg',
                            name: 'The end of the fucking world',
                            episode: 'Season1/Season Series 13',
                            score: '8.7',
                        },
                    ],
                },
            ],
        }
    },
    methods: {
        initSwiper() {
            var mySwiper = new Swiper('.banner-swiper', {
                loop: true, // 循环模式选项
                slidesPerView: 1,
                // 如果需要分页器
                pagination: {
                    el: '.swiper-pagination',
                },
                autoplay: true,
            })
        },
        getTrending() {
            Promise.all([
                axios.get(
                    'https://api.themoviedb.org/3/movie/popular?api_key=6c2c417273397900965840db9bc1ed55',
                ),
                axios.get(
                    'https://api.themoviedb.org/3/trending/movie/week?api_key=6c2c417273397900965840db9bc1ed55&sort_by=popularity.desc&language=en-US',
                ),
                axios.get(
                    'https://api.themoviedb.org/3/movie/top_rated?api_key=6c2c417273397900965840db9bc1ed55&sort_by=popularity.desc&region=US',
                ),
                axios.get(
                    'https://api.themoviedb.org/3/discover/tv?api_key=6c2c417273397900965840db9bc1ed55&with_networks=213&sort_by=popularity.desc&language=en-US',
                ),
                axios.get(
                    'https://api.themoviedb.org/3/movie/upcoming?api_key=6c2c417273397900965840db9bc1ed55&language=en-US',
                ),
            ]).then(([res1, res2, res3, res4, res5]) => {
                this.banner_info = res1.data.results.slice(0, 4)
                // this.initSwiper()
                setTimeout(() => {
                    this.initSwiper()
                }, 0)
                this.rows.trending = res2.data.results
                this.rows.rated = res3.data.results
                this.rows.netflix = res4.data.results
                this.rows.upcoming = res5.data.results
            })
        },
    },
    mounted() {
        console.log('over')
        this.getTrending()
    },
}
</script>
<style>
.home {
    display: flex;
    width: 100%;
    height: 100%;
    overflow-x: hidden;
    /* font-family: 'Inter', sans-serif !important; */
}

@media screen and (max-width: 1350px) {
    .home .middle {
        width: 100%; /* 宽度为100% */
    }

    .home .right-slider {
        display: none; /* 隐藏 */
    }
}

/* 中间推荐板块 */
.middle {
    position: relative;
    padding: 3rem 2rem 0;
    width: 80%;
    /* min-width: 705px; */
    height: 100%;
    border-right: 1px solid var(--border-color);
    overflow: auto;
}
.banner-swiper {
    border-radius: 1rem;
}
.middle::-webkit-scrollbar {
    display: none; /* 初始状态下隐藏滚动条 */
}

.middle:hover::-webkit-scrollbar {
    display: block; /* 鼠标悬停时显示滚动条 */
}

.swiper-slide:hover .poster-info {
    opacity: 1;
    transform: translateY(0);
}

.swiper-slide:hover > .poster::after {
    opacity: 1;
}

/* 中间区域banner */
.banner {
    width: 100%;
    height: 100%;
}

.banner-swiper {
    height: 52%;
}
/* 中间区域rows */
.row-block {
    overflow-y: auto;
}

/* 右侧css */
.right-slider {
    padding: 3rem 2rem;
    width: 20%;
}

.search-input {
    position: relative;

    margin-bottom: 5px;
}

.search-input span {
    position: absolute;
    top: 50%;
    left: 10px;
    transform: translateY(-50%);
}

.search-input input {
    border: 1px solid var(--input-border-color);
    border-radius: 1rem;
    line-height: 2rem;
    width: 100%;
    padding-left: 2rem;
    font-size: 0.6rem;
    background-color: var(--bg2-color);
}
.more {
    height: 100%;
    width: 100%;
    overflow: auto;
}
</style>
