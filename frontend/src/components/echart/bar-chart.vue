<template>
    <div ref="bar_chart" style="position: relative; flex: 1; height: 500px"></div>
</template>

<script>
import * as echarts from 'echarts'

export default {
    props: {
        data: Array,
    },
    mounted() {
        this.this.checkWidthAndInit()
    },
    watch: {
        data(newVal) {
            this.checkWidthAndInit()
        },
    },
    methods: {
        checkWidthAndInit() {
            const chartDom = this.$refs.bar_chart
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
            const myChart = echarts.init(this.$refs.bar_chart)
            const option = {
                xAxis: {
                    type: 'category',
                    data: this.data.map((item) => item.name),
                },
                yAxis: {
                    type: 'value',
                },
                series: [
                    {
                        type: 'bar',
                        data: this.data.map((item) => item.value),
                    },
                ],
            }

            myChart.setOption(option)
        },
    },
}
</script>
