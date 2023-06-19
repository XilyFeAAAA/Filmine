<template>
    <div class="row">
        <h2 class="row-title" @click="jumpRouter">
            <span>{{ title }}</span>
            <span class="row-showmore"
                >Show all <font-awesome-icon :icon="['fas', 'chevron-right']" size="2xs" />
            </span>
        </h2>
        <div class="row-poster">
            <div class="swiper-container">
                <div
                    class="swiper-wrapper"
                    :class="{ 'is-left': isLeft, 'is-right': isRight }"
                    @mouseover="handleMouseOver"
                >
                    <div v-for="(poster, index) in row_data" :key="index" class="swiper-slide">
                        <poster :poster="poster" :genre="genre" />
                    </div>
                </div>
                <!-- 如果需要导航按钮 -->
                <div class="swiper-button-prev"></div>
                <div class="swiper-button-next"></div>
            </div>
        </div>
    </div>
</template>
<script>
import poster from '@/components/poster.vue'
import Swiper from 'swiper'
export default {
    props: {
        title: String,
        row_data: Array,
    },
    components: {
        poster,
    },
    data() {
        return {
            genre: 'movie',
            hoveredIndex: null,
        }
    },
    computed: {
        isLeft() {
            return this.hoveredIndex === 0
        },
        isRight() {
            return this.hoveredIndex === this.row_data.length - 1
        },
    },
    methods: {
        handleMouseOver(e) {
            const hoveredSlide = e.target.closest('.swiper-slide')
            if (!hoveredSlide) return

            this.hoveredIndex = Array.from(hoveredSlide.parentNode.children).indexOf(hoveredSlide)
        },
        jumpRouter() {
            if (this.title == 'trending') this.$router.push('/index/discovery/movie/trending')
            else if (this.title == 'rated') this.$router.push('/index/discovery/movie/rated')
        },
    },
    mounted() {
        new Swiper('.swiper-container', {
            autoplay: false,
            slidesPerView: 'auto',
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        })
    },
}
</script>
<style scoped>
.row {
    padding: 3vh 0 0.5vh;
    font-family: 'Montserrat', sans-serif;
}

.row-title {
    display: inline-block;
    font-size: 1.2vw;
    margin-bottom: 1rem;
    line-height: 1.25vw;
    text-align: left;
    cursor: pointer;
}
.row-title span {
    color: var(--text1-color);
}

.row-title .row-showmore {
    font-size: 0.6vw;
    line-height: 1vw;
    display: inline-flex;
    align-items: center;
    color: #000;
    white-space: nowrap;
    opacity: 0;
    max-width: 0;
    transform: translateZ(0);
    transition: max-width 0.45s, opacity 0.45s, transform 0.75s, -webkit-transform 0.75s;
}

.row-title:hover .row-showmore {
    opacity: 1;
    max-width: 200px;
    -webkit-transform: translate(1vw);
    transform: translate(1vw);
}

.row-poster {
    position: relative;
}

.row .swiper-container {
    overflow: initial;
    width: 100%;
    height: auto;
    /* padding: 0 4%; */
}

@media only screen and (min-width: 768px) {
    .swiper-wrapper:hover .swiper-slide {
        transform: translateX(-15%);
        opacity: 0.3;
    }

    .swiper-wrapper:hover .swiper-slide:hover {
        transform: scale(1.3) !important;
        z-index: 1;
        opacity: 1;
    }

    .swiper-wrapper:hover .swiper-slide:hover ~ .swiper-slide {
        transform: translateX(15%);
    }

    .swiper-wrapper.is-left:hover .swiper-slide:hover ~ .swiper-slide {
        transform: translateX(28%);
    }

    .swiper-wrapper.is-right:hover .swiper-slide {
        transform: translateX(-20%);
        opacity: 0.3;
    }

    .swiper-wrapper.is-right:hover .swiper-slide:hover {
        transform: scale(1.3) !important;
        z-index: 1;
        opacity: 1;
    }

    .swiper-wrapper.is-right:hover .swiper-slide:hover ~ .swiper-slide {
        transform: translateX(0%);
    }
}

.swiper-slide {
    margin-right: 30px;
    display: inline-flex;
    width: 10vw;
    min-width: 200px;
    transform: scale(1);
    transition: transform 0.3s ease-out, opacity 0.3s ease-out;
}

@media (min-width: 330px) {
    .swiper-slide:nth-child(1n) {
        transform-origin: initial;
    }
    .swiper-slide:nth-child(2n + 1) {
        transform-origin: left;
    }
    .swiper-slide:nth-child(2n + 2) {
        transform-origin: right;
    }
}

@media (min-width: 625px) {
    .swiper-slide:nth-child(1n) {
        transform-origin: initial;
    }
    .swiper-slide:nth-child(3n + 1) {
        transform-origin: left;
    }
    .swiper-slide:nth-child(3n + 3) {
        transform-origin: right;
    }
}

@media (min-width: 998px) {
    .swiper-slide:nth-child(1n) {
        transform-origin: initial;
    }
    .swiper-slide:nth-child(4n + 1) {
        transform-origin: left;
    }
    .swiper-slide:nth-child(4n + 4) {
        transform-origin: right;
    }
}

@media (min-width: 1378px) {
    .swiper-slide:nth-child(1n) {
        transform-origin: initial;
    }
    .swiper-slide:nth-child(6n + 1) {
        transform-origin: left;
    }
    .swiper-slide:nth-child(6n + 6) {
        transform-origin: right;
    }
}
</style>
