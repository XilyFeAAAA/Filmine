<template>
    <div class="score">
        <span>{{ score }}</span>
        <font-awesome-icon icon="fa-solid fa-star" size="2xs" style="color: #fff" />
    </div>
</template>
<script>
export default {
    props: {
        score: String,
    },
}
</script>
<style scoped>
* {
    user-select: none;
}
.score {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 60px;
    height: 23px;
    background-color: #c00000;
    border-radius: 15px;
}

.score span {
    color: #fff;
    font-size: 0.8rem;
    margin-right: 3px;
}
</style>
