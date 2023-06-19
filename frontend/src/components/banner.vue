<template>
    <div
        class="banner"
        :style="{
            backgroundImage: 'url(https://image.tmdb.org/t/p/original' + info.backdrop_path + ')',
        }"
    >
        <div class="mask">
            <span class="title">{{ info.title }}</span>
            <div class="btns">
                <button class="btn-play" @click="play('movie', info.id)">
                    <font-awesome-icon style="margin-right: 8px" icon="fa-solid fa-play" />Play
                </button>
                <button class="btn-more" @click="setLayer(layer_payload)">
                    <font-awesome-icon
                        style="margin-right: 8px"
                        :icon="['fas', 'circle-info']"
                    />More Info
                </button>
            </div>
            <div class="genres">
                <span v-for="(id, index) in info.genre_ids" :key="index"
                    >{{ $genres[id] }}
                    <span class="slash" v-if="index < info.genre_ids.length - 1">/</span>
                </span>
            </div>
            <p>{{ info.overview }}</p>
        </div>
        <score :score="String(info.vote_average)" class="score" />
    </div>
</template>
<script>
import { mapMutations } from 'vuex'
import score from '@/components/score.vue'
export default {
    props: {
        info: Object,
    },
    computed: {
        layer_payload() {
            return {
                data: this.info,
                genre: 'movie',
            }
        },
    },
    components: {
        score,
    },
    methods: {
        ...mapMutations('layer', ['setLayer']),
        play(genre, id) {
            this.$router.push({ path: `/detail/${genre}/${id}` })
        },
    },
    watch: {
        info: function (newVal, oldVal) {
            console.log(oldVal)
        },
    },
}
</script>
<style scoped>
* {
    user-select: none;
}
.banner {
    position: relative;
    background-position: center center;
    background-size: cover;
    border-radius: 1rem;
    overflow: hidden;
}

.mask {
    position: relative;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    padding: 5% 0 0 2rem;
    background-image: linear-gradient(
        to right,
        rgba(0, 0, 0, 0.8) 0%,
        rgba(0, 0, 0, 0.8) 30%,
        rgba(0, 0, 0, 0) 60%,
        rgba(0, 0, 0, 0) 100%
    );
}
.mask p {
    text-indent: 2em;
    font-size: 0.9rem;
    margin-top: 1rem;
    width: 30%;
    overflow: hidden;
    color: var(--text7-color);
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    line-height: 1.5rem;
}

.mask .title {
    color: var(--text-color);
    font-size: 3rem;
    font-weight: bold;
}

.genres {
    display: flex;
    align-items: center;
    margin-top: 1rem;
    color: var(--text9-color);
}

.genres span:not(.slash) {
    font-size: 0.6rem;
    padding: 4px 6px;
    color: #d1d1d1;
}

.genres span:last-of-type {
    margin-right: 0;
}

.score {
    position: absolute;
    top: 10px;
    right: 10px;
}

.btns {
    margin: 5vh 0 0;
}

.btns button {
    color: #fff;
    width: 150px;
    height: 50px;
    font-size: 15px;
    border-radius: 5px;
    margin-right: 10px;
    transition: all 0.3s;
}

.btn-play {
    background-color: #e50914;
}

.btn-more {
    background-color: rgba(109, 109, 110, 0.7);
}

.btn-play:hover {
    background-color: #cc0812;
}
</style>
