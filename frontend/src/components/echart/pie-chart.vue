<template>
    <div ref="pie_chart" style="position: relative; flex: 1; height: 500px"></div>
</template>

<script>
import * as echarts from 'echarts'

export default {
    props: {
        data: Array,
    },
    mounted() {
        this.checkWidthAndInit()
    },
    watch: {
        data(newVal) {
            this.checkWidthAndInit()
        },
    },
    methods: {
        checkWidthAndInit() {
            const chartDom = this.$refs.pie_chart
            const width = chartDom.clientWidth
            if (width === 0) {
                setTimeout(() => {
                    this.checkWidthAndInit()
                }, 100)
                return
            }
            this.init()
        },
        init() {
            const myChart = echarts.init(this.$refs.pie_chart)
            const option = {
                series: [
                    {
                        type: 'pie',
                        radius: '50%',
                        data: this.data,
                    },
                ],
            }

            myChart.setOption(option)
        },
    },
}
</script>
