<template>
    <div class="summary-layer">
        <header
            :style="{
                backgroundImage: data
                    ? `url(https://image.tmdb.org/t/p/original${data.backdrop_path})`
                    : 'none',
            }"
            style="background-position: center center; background-size: cover"
        >
            <div class="btns">
                <button class="play-btn" @click="play(data.genre, data.id)">
                    <font-awesome-icon :icon="['fas', 'play']" style="margin-right: 15px" />Play
                </button>
                <button class="add-btn">
                    <font-awesome-icon :icon="['fas', 'plus']" size="xl" />
                </button>
            </div>
        </header>
        <div class="content">
            <div class="upper">
                <h1 class="glow-animation">{{ data.title || data.name }}</h1>
                <p>{{ data.overview || '' }}</p>
            </div>
            <div class="lower">
                <h2>
                    Info on <span class="glow">{{ data.title || data.name }}</span>
                </h2>
                <h3>
                    <span class="label">Genres:</span>
                    <span v-for="(id, idx) in data.genre_ids" :key="idx">
                        {{ genres[id] }}
                    </span>
                </h3>
                <h3><span class="label">Release date:</span> {{ data.release_date }}</h3>
                <h3><span class="label">Average vote:</span> {{ data.vote_average }}</h3>
                <h3><span class="label">Original language:</span> {{ data.original_language }}</h3>
                <h3>
                    <span class="label">Age classification:</span>
                    {{ data.adult === false ? 'Suitable for all ages' : 'Suitable for adults' }}
                </h3>
            </div>
        </div>
    </div>
</template>
<script>
import { mapState, mapMutations } from 'vuex'
export default {
    computed: {
        ...mapState('layer', ['data']),
    },
    data() {
        return {
            genres: {
                28: 'Action',
                12: 'Adventure',
                16: 'Animation',
                35: 'Comedy',
                80: 'Crime',
                99: 'Documentary',
                18: 'Drama',
                10: 'Family',
                14: 'Fantasy',
                36: 'History',
                27: 'Horror',
                10402: 'Music',
                9648: 'Mystery',
                10749: 'Romance',
                878: 'Science Fiction',
                10770: 'TV Movie',
                53: 'Thriller',
                10752: 'War',
                37: 'Western',
                10751: 'Family',
            },
        }
    },
    methods: {
        ...mapMutations('layer', ['closeLayer']),
        play(genre, id) {
            this.$router.push({ path: `/detail/${genre}/${id}` })
            this.closeLayer()
        },
    },
}
</script>
<style scoped>
.summary-layer {
    position: relative;
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
}

header {
    position: relative;
    width: 100%;
    height: 50%;
    min-height: 300px;
}

header img {
    width: 100%;
    height: 100%;
}

header:before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 20%;
    background: linear-gradient(to top, rgb(24, 24, 24) 0%, transparent 100%);
}

.content {
    flex: 1;
    width: 100%;
    /* height: 55%; */
    background-color: #181818;
    color: #fff;
    padding: 2rem;
}
.content p {
    color: #fff;
}

.upper {
    border-bottom: 2px solid #666;
}
.upper h1 {
    font-size: 2.3rem;
}

.upper p {
    font-size: 1rem;
    margin: 1rem 0;
}

.lower {
    margin-top: 1.5rem;
}

.lower h2,
.lower h3 {
    opacity: 0;
    margin-top: 50px;
    transition: opacity 0.8s ease-in-out, margin-top 1s 0.2s ease-in-out; /* 添加底部向上滑动的过渡动画 */
}

.layer-show .lower h2,
.layer-show .lower h3 {
    opacity: 1;
    margin-top: 0;
}

.lower h2 {
    font-size: 1.2rem;
    margin-bottom: 0.4rem;
}

.lower h3 {
    font-size: 0.8rem;
    line-height: 2rem;
}
.btns {
    position: absolute;
    display: flex;
    align-items: center;
    left: 2rem;
    bottom: 3rem;
}

.play-btn {
    width: 13rem;
    height: 3.5rem;
    border: 0;
    border-radius: 7px;
    font-size: 1.2rem;
    color: #fff;
    background-color: #f81d0f;
    margin-right: 2rem;
}
.add-btn {
    height: 3rem;
    width: 3rem;
    color: #fff;
    border: 1px solid #fff;
    border-radius: 50%;
    background-color: transparent;
}

.label {
    color: #747171;
}

.glow {
    text-shadow: 0 0 20px #fff;
}

.glow-animation {
    animation: glowing 2s ease-in-out infinite;
}
@keyframes glowing {
    0% {
        text-shadow: 0 0 10px #fff;
    }
    50% {
        text-shadow: 0 0 20px #fff;
    }
    100% {
        text-shadow: 0 0 10px #fff;
    }
}
</style>
