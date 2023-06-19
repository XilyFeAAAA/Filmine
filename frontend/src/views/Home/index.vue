<template>
    <div class="index">
        <!-- <div class="container"> -->
        <navSlider
            :title="title"
            :navItems="navItems"
            style="width: 12%; border-right: 1px solid var(--border-color)"
        />
        <div class="router" style="width: 88%">
            <transition name="fade">
                <router-view></router-view>
            </transition>
        </div>

        <layer>
            <summaryLayer />
        </layer>
    </div>
</template>
<script>
import navSlider from '@/components/navSlider.vue'
import layer from '@/components/layer.vue'
import summaryLayer from '@/components/summary-layer.vue'
export default {
    components: {
        navSlider,
        layer,
        summaryLayer,
    },
    data() {
        return {
            title: 'Filmine',
            layerShow: false,

            navItems: [
                {
                    text: 'Menu',
                    branch: [
                        {
                            text: 'Home',
                            active: false,
                            path: '/home',
                            icon: 'fa-solid fa-home',
                        },
                        {
                            text: 'Discovery',
                            active: false,
                            show: false,
                            icon: 'fa-solid fa-compass',
                            son: [
                                {
                                    text: 'Movie',
                                    active: false,
                                    path: '/discovery/movie/trending',
                                },
                                {
                                    text: 'TV Series',
                                    active: false,
                                    path: '/discovery/tv/trending',
                                },
                            ],
                        },
                        {
                            text: 'Coming soon',
                            active: false,
                            icon: 'fa-solid fa-sack-dollar',
                        },
                    ],
                },
                {
                    text: 'Social',
                    branch: [
                        {
                            text: 'Store',
                            active: false,
                            path: '/store',
                            icon: 'fa-solid fa-building',
                        },
                        {
                            text: 'Friends',
                            active: this.$router.currentRoute.path === '/friends',
                            icon: 'fa-solid fa-user-plus',
                        },
                        {
                            text: 'Parties',
                            active: this.$router.currentRoute.path === '/party',
                            icon: 'fa-solid fa-user-group',
                        },
                        {
                            text: 'Media',
                            active: this.$router.currentRoute.path === '/media',
                            icon: 'fa-solid fa-compact-disc',
                        },
                    ],
                },
                {
                    text: 'General',
                    branch: [
                        {
                            text: 'Setting',
                            active: this.$router.currentRoute.path === '/setting',
                            icon: 'fa-solid fa-gear',
                        },
                        {
                            text: 'Log Out',
                            icon: 'fa-solid fa-right-from-bracket',
                            path: '/login',
                        },
                    ],
                },
            ],
        }
    },
}
</script>
<style scoped>
.index {
    position: relative;
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    background-color: var(--bg-color);
}
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
