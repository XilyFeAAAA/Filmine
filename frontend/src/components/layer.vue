<template>
    <div class="layer">
        <div class="layer-mask" v-show="isShow" @click="closeLayer()"></div>
        <div class="layer-content" :class="{ 'layer-show': isShow, 'layer-hide': !isShow }">
            <slot></slot>
            <button class="close-btn">
                <font-awesome-icon :icon="['fas', 'xmark']" size="2xl" @click="closeLayer()" />
            </button>
        </div>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
    methods: {
        ...mapMutations('layer', ['closeLayer']),
    },
    computed: {
        ...mapState('layer', ['isShow']),
    },
}
</script>

<style>
.layer-mask {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7); /* 使用半透明黑色遮罩 */
    z-index: 9999;
}

.layer-content {
    position: fixed;
    bottom: -100%; /* 初始位置在底部 */
    left: 50%;
    width: 40%;
    max-width: 750px;
    height: 85%;
    opacity: 0.3;
    background-color: #fff;
    z-index: 10000;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
    overflow: auto;
    transform: translateX(-50%);
    transition: opacity 0.8s ease-in-out, bottom 0.5s ease-in-out; /* 添加底部向上滑动的过渡动画 */
    border-radius: 0.5rem;
}

.layer-show {
    bottom: 8%;
    opacity: 1;
}

.layer-hide {
    bottom: -100%;
}

.layer-close {
    border: none;
    background-color: transparent;
    font-size: 20px;
    cursor: pointer;
}

.close-btn {
    position: absolute;
    top: 20px;
    right: 20px;
    border: 1px solid #fff;
    border-radius: 50%;
    height: 45px;
    width: 45px;
    color: #fff;
    background-color: #000;
    cursor: pointer;
}
</style>
