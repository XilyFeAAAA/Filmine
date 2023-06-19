<template>
    <div ref="wordcloud" style="width: 50%; height: 400px"></div>
</template>
<script>
import * as echarts from 'echarts'
import 'echarts-wordcloud'
export default {
    props: { data: Array },
    mounted() {
        this.init()
    },
    watch: {
        data(newVal) {
            this.init()
        },
    },
    methods: {
        init() {
            if (!this.data) return
            console.log(1)
            const wordcloud = echarts.init(this.$refs.wordcloud)
            const option = {
                series: [
                    {
                        type: 'wordCloud',
                        shape: 'circle',
                        sizeRange: [12, 50],
                        rotationRange: [-90, 90],
                        rotationStep: 45,
                        gridSize: 10,
                        textStyle: {
                            normal: {
                                fontFamily: 'sans-serif',
                                color: function () {
                                    return (
                                        'rgb(' +
                                        [
                                            Math.round(Math.random() * 255),
                                            Math.round(Math.random() * 255),
                                            Math.round(Math.random() * 255),
                                        ].join(',') +
                                        ')'
                                    )
                                },
                            },
                        },
                        data: this.data,
                    },
                ],
            }
            wordcloud.setOption(option)
        },
    },
}
</script>
