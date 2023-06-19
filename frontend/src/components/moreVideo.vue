<template>
    <div class="moreVideo">
        <header>
            <span>{{ info.title }}</span>
            <font-awesome-icon :icon="['fas', 'ellipsis-vertical']" style="cursor: pointer" />
        </header>
        <div class="container">
            <div v-for="(video, index) in info.videos" :key="index" class="video-info-container">
                <div class="video-cover">
                    <img :src="video.url" />
                </div>
                <div class="video-info">
                    <h3>{{ video.name }}</h3>
                    <p>{{ video.episode }}</p>
                    <div class="score">
                        <span>{{ video.score }}</span>
                        <font-awesome-icon icon="fa-solid fa-star" size="xs" />
                    </div>
                </div>
            </div>

            <button>See More</button>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        info: Object,
    },
}
</script>
<style scoped>
.moreVideo {
    margin-top: 20px;
    width: 100%;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header {
    color: var(--text1-color);
    font-weight: bold;
    font-size: 1.1rem;
}
.container {
    display: flex;
    flex-direction: column;
}

.video-info-container {
    display: flex;
    align-items: center;
    margin-top: 25px;
    height: calc((17.6vw - 4rem) * 0.5);
    width: 100%;
    color: var(--text1-color);
}

.video-cover {
    width: 40%;
    padding-right: 1rem;
    cursor: pointer;
}

.video-cover img {
    border-radius: 1rem;
    height: 100%;
    width: 100%;
    object-fit: cover;
}

.video-info {
    width: 50%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding-left: 1rem;
}

.video-info h3 {
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
}

.video-info p {
    margin: 0;
    font-size: 0.9rem;
}
button {
    margin-top: 1.5rem;
    width: 100%;
    height: 2.5rem;
    border-radius: 1rem;
    border: 0;
    font-weight: bold;
    cursor: pointer;
    color: var(--text2-color);
    background-color: var(--bg1-color);
}

.fonticon {
    cursor: pointer;
}

.score {
    display: flex;
    color: var(--text4-color);
    align-items: center;
    /* border: 1px solid var(--text4-color); */
}

.score span {
    margin-right: 5px;
    font-size: 0.8rem;
}
</style>
