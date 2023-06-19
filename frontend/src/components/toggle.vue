<template>
    <div class="toggle-switch">
        <p class="content">{{ text }}</p>
        <div class="toggle-container" :class="{ 'toggle-on': on }" @click="on = !on">
            <p class="toggle-circle"></p>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        val: Boolean,
        text: String,
    },
    watch: {
        val(val) {
            this.on = val
        },
        on(val) {
            this.$emit('update:val', val)
        },
    },
    data() {
        return {
            on: this.val,
        }
    },
}
</script>
<style scoped>
* {
    font-family: MyFont, sans-serif;
}
.toggle-switch {
    position: relative;
    display: flex;
    align-items: center;
}

.toggle-container {
    display: flex;
    align-items: center;
    position: relative;
    width: 45px;
    height: 24px;
    padding: 5px;
    background-color: #eaeaea;
    opacity: 0.8;
    transition: all 0.8s;
    border-radius: 20px;
    cursor: pointer;
}

.toggle-container:hover {
    opacity: 1;
}

p.toggle-circle {
    margin-left: -2px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background-color: #fff;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.2), 0 1px 3px 0 rgba(0, 0, 0, 0.1);
    transition: all 0.2s;
}

.toggle-container.toggle-on {
    background-color: rgba(0, 120, 215, 0.8);
}

.toggle-container.toggle-on p.toggle-circle {
    margin-left: calc(100% - 22px);
    border-color: transparent;
}
p.content {
    margin-right: 10px;
    color: #666;
    font-size: 12px;
    font-weight: 500;
    transition: all 0.2s;
    user-select: none;
}
</style>
