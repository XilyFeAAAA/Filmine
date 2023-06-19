<template>
    <div class="navBar">
        <nav>
            <div class="navTitle">
                <font-awesome-icon
                    :icon="['fas', 'clapperboard']"
                    size="xl"
                    style="color: #cb3628"
                />
                <span>{{ title }}</span>
            </div>
            <div class="navArea">
                <div v-for="(menu, index) in menus" :key="index" class="navBlock">
                    <h3>{{ menu.text }}</h3>
                    <ul>
                        <li v-for="(item, index) in menu.branch" :key="index">
                            <div
                                class="navItem"
                                :class="{ active: item.active }"
                                @click="handleClick(item)"
                            >
                                <font-awesome-icon :icon="item.icon" class="nav_icon" />
                                <span>{{ item.text }}</span>
                            </div>
                            <div v-show="item.son && item.show" class="sonItem">
                                <div
                                    v-for="(son, idx) in item.son"
                                    :class="{ active: son.active }"
                                    :key="idx"
                                    @click="handleClick(son)"
                                >
                                    <span>{{ son.text }}</span>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="web-tools">
            <font-awesome-icon
                :icon="['fas', 'language']"
                size="xl"
                style="color: var(--text1-color); cursor: pointer"
            />
            <font-awesome-icon
                :icon="['fas', 'moon']"
                @click="switchTheme"
                style="color: var(--text1-color); cursor: pointer"
            />
        </div>
    </div>
</template>
<script>
export default {
    props: {
        title: {
            type: String,
            require: true,
        },
        navItems: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            menus: this.navItems,
            theme: localStorage.getItem('filmine-theme') || 'light',
        }
    },
    mounted() {
        const currentPath = this.$router.currentRoute.path
        this.menus.forEach((menu) => {
            menu.branch.forEach((menuItem) => {
                if (menuItem.son) {
                    menuItem.son.forEach((submenuItem) => {
                        if (submenuItem.path === currentPath) submenuItem.active = false
                    })
                } else {
                    if (menuItem.path === currentPath) menuItem.active = true
                }
            })
        })
    },
    methods: {
        switchTheme() {
            this.theme = this.theme === 'light' ? 'dark' : 'light'
            this.$store.commit('theme/setTheme', this.theme)
        },
        handleClick(item) {
            if (item.son) item.show = !item.show
            else {
                this.menus.forEach((menu) => {
                    menu.branch.forEach((menuItem) => {
                        if (menuItem.son) {
                            menuItem.son.forEach((submenuItem) => {
                                submenuItem.active = false
                            })
                        } else {
                            menuItem.active = false
                        }
                    })
                })
                item.active = true
                if (item.path === '/login') {
                    localStorage.removeItem('token')
                }
                this.$router.push({ path: item.path })
            }
        },
    },
}
</script>
<style scoped>
.navBar {
    position: relative;
    padding-left: 2%;
    min-width: 200px;
}

.navTitle {
    display: flex;
    align-items: center;
    padding: 60px 0;
}

.navTitle span {
    color: var(--text1-color);
    font-size: 1.2rem;
    font-weight: bold;
    margin-left: 10px;
}

.navArea {
    margin-top: 2vh;
    overflow: auto;
    max-height: calc(85vh - 145px); /* 设置一个固定的高度 */
}

.navArea::-webkit-scrollbar {
    display: none; /* 初始状态下隐藏滚动条 */
}

.navArea:hover::-webkit-scrollbar {
    display: block; /* 鼠标悬停时显示滚动条 */
}

.navBlock {
    margin-bottom: 2rem;
}

.navBlock h3 {
    color: var(--text2-color);
    font-size: 0.7rem;
    /* letter-spacing: 0.1em; */
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}
.navBlock li .navItem {
    user-select: none;
    position: relative;
    display: flex;
    align-items: center;
    line-height: 2rem;
    margin-top: 1rem;
    color: var(--text3-color);
    cursor: pointer;
    transition: all 0.1s;
}

.nav_icon {
    min-width: 2rem;
    margin-right: 1rem;
}

.navBlock .active {
    border-right: 6px solid var(--text4-color);
}

.navBlock .active span {
    font-weight: 700;
    color: var(--text1-color);
}

.navBlock .active .nav_icon {
    color: var(--text4-color);
}

.navBlock .sonItem > div:not(.active):hover,
.navBlock .navItem:not(.active):hover {
    border-right: 6px solid var(--text5-color);
}
.web-tools {
    position: absolute;
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 100%;
    left: 50%;
    bottom: 20px;
    transform: translateX(-50%);
}

.sonItem {
    display: flex;
    flex-direction: column;
    color: var(--text3-color);
    cursor: pointer;
}

.sonItem > div {
    text-align: center;
    width: 100%;
    margin-top: 10px;
}
</style>
