<template>
    <div class="poster">
        <img :src="'https://image.tmdb.org/t/p/original/' + poster.backdrop_path" />
        <div class="poster-info" @click="setLayer(layer_payload)">
            <div class="poster-info-iconswrp">
                <button class="btn-play" @click.stop="play(genre, poster.id)">
                    <font-awesome-icon icon="fa-solid fa-play" />
                </button>
                <button class="btn-add" @click.stop>
                    <font-awesome-icon icon="fa-solid fa-plus" />
                </button>
                <button class="btn-more" @click.stop="setLayer(layer_payload)">
                    <font-awesome-icon :icon="['fas', 'chevron-down']" />
                </button>
            </div>
            <div class="poster-info-title">
                <h3>{{ poster.title || poster.name }}</h3>
            </div>
            <div class="poster-info-genres">
                <span v-for="(id, idx) in poster.genre_ids.slice(0, 3)" :key="idx">
                    {{ genres[id] }}
                </span>
            </div>
        </div>
    </div>
</template>
<script>
import { mapMutations } from 'vuex'
export default {
    props: {
        genre: String,
        poster: Object,
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
    computed: {
        layer_payload() {
            return {
                data: this.poster,
                genre: this.genre,
            }
        },
    },
    methods: {
        ...mapMutations('layer', ['setLayer']),
        play(genre, id) {
            this.$router.push({ path: `/detail/${genre}/${id}` })
        },
    },
}
</script>
<style scoped>
.poster {
    position: relative;
    overflow: hidden;
    /* margin-right: 0.1rem; */
    /* cursor: pointer; */
}

.poster::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 5px;
    background: linear-gradient(1turn, rgba(0, 0, 0, 0.6), transparent 65%);
    z-index: 0;
    opacity: 0;
    transition: opacity 0.2s ease-out;
}

.poster img {
    display: inline-block;
    height: 100%;
    width: 100%;
    border-radius: 5px;
}

.poster-info {
    position: absolute;
    left: 0;
    bottom: 0;
    transform: translateY(15%);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    height: 100%;
    padding: 0.6em;
    opacity: 0;
    z-index: 2;
    border-radius: 5px;
    transition: all 0.4s ease 0.15s;
}

.poster-info-iconswrp {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-bottom: 15px;
}

.poster-info-title h3 {
    color: #fff;
    font-size: 15px;
    font-weight: 600;
    text-transform: none;
}

.poster-info-genres {
    display: block;
    width: 100%;
}

.poster-info-genres span {
    display: inline-block;
    width: auto;
    color: #fff;
    font-size: 5px;
    margin-right: 0.3vw;
}

.poster-info-genres span:not(:last-of-type)::after {
    content: '●';
    display: inline-block;
    margin: 0 0 0 0.3vw;
    font-size: 6px;
    text-shadow: 0 1px 1px transparent;
    color: hsla(0, 0%, 94.9%, 0.4);
}

button {
    height: 32px;
    width: 32px;
    border-radius: 50%;
    margin-right: 5px;
    transition: all 0.3s;
}

.btn-add,
.btn-more {
    color: #fff;
    border: 1px solid #fff;
    background-color: transparent;
}

.btn-add:hover,
.btn-more:hover {
    color: #000;
    background-color: #fff;
}

.btn-play:hover {
    background-color: rgba(255, 255, 255, 0.6);
}

@media (min-width: 1080px) {
    /* Styles for screens wider than 1875px */
    .poster-info-title h3 {
        font-size: 12px;
    }
    .poster-info-genres span {
        font-size: 3px;
    }
}
</style>
