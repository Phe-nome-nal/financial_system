<template>
<div>
  <div v-if="loading" class="loading-overlay">
    <div class="loading-spinner"></div>
    <p class="loading-text">Loading...</p>
  </div>
  <div style="display: flex;">
    <div  ref="whole risk"  style=" float: left;width: 1200px; height: 350px;margin-left: 15px;margin-top: 0px;margin-right: 0px"></div>
    <div  ref="future"  style=" float: left; width: 50px; height: 350px;margin-left: -127px;margin-top: 0px;"></div>

  </div>
  <div class="warning-component">
    <div class="warning-dates">
      <div class="date-item">前日：<span>{{ prevDayRisk }}</span></div>
      <div class="date-item">昨日：<span>{{ yesterdayRisk }}</span></div>
      <div class="date-item">今日：<span>{{ todayRisk }}</span></div>
      <div class="date-item">明日：<span>{{ tomorrowRisk }}</span></div>
      <div class="warning-recent">
        最近预警：<span>{{ warningRisk }}</span>

      </div>
    </div>
  </div>
</div>
</template>

<script>
import * as echarts from "echarts";
import { Message } from "element-ui";

export default {

  data(){
    return {
      yMax:2,
      yMin:0,
      prevDayRisk:'',
      yesterdayRisk:'',
      todayRisk:'',
      tomorrowRisk:'',
      warningRisk:'',
      riskData:[],
      markLine: [],
      markPoint: [],
      markArea:[],
      future:[],
      datazoom:[],
      loading: true,
    }
  },
props:{
    zoom:{
      type:Array,
      default: function () {
        return []
      }
    }
},
  watch:{
    zoom(newVal){
      this.datazoom=newVal
    },
    yMax(newVal){
      console.log(newVal)
    }

  },
  mounted() {
    this.loading = true;
    fetch('http://152.89.211.77:5000/api/v1/risk')
    .then(res => res.json())
    .then((data) => {
      this.loading = false;
      this.riskData=data.wholerisk
      this.markPoint=data.markpoint
      this.markLine=data.markline
      this.markArea=data.markarea
      this.prevDayRisk=data.detail[0]
      this.yesterdayRisk=data.detail[1]
      this.todayRisk=data.detail[2]
      this.tomorrowRisk=data.detail[3]
      this.warningRisk=data.detail[4]
      this.future=data.future
      // console.log(this.riskData,this.markLine,this.markPoint[0])
      this.initChart()
    })
    .catch((error) => {
      Message.error('网络连接失败，请稍后再试');
      console.error('Error:', error);
    });

    // this.initChart(this.dat)

  },

  methods:{
    initChart(){
      /*
      示例参考如下
      * https://echarts.apache.org/v4/examples/zh/editor.html?c=line-aqi
      *
      * https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples/data/asset/data/aqi-beijing.json
      *
      * */
      let data=this.riskData
      const future=this.future
      var myChart = echarts.init(this.$refs["whole risk"])
      var myChartFuture= echarts.init(this.$refs["future"])
      let option = {
        title: {
          text: '系统性金融风险指数',
          left:'center'
        },
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          axisLabel:{
            fontSize:5
          },
          data: data.map(function (item) {
            return item[0];
          })
        },
        yAxis: {
          scale:true,
          splitLine: {
            show: false
          }
        },

        toolbox: {
          right: 120,
          feature: {
            // dataZoom: {
            //   yAxisIndex: 'none'
            // },
            dataView:{
              show:true,
              title: '查看数据',
            },
            restore: {},
            saveAsImage: {}
          }
        },
        //以下是时间轴
        dataZoom: [{
          //也应该是动态的
          startValue: '2022-07-01'
        }, {
          type: 'inside'
        }],
        //以上是时间轴
        visualMap: {
          top: 10,
          right: 0,
          precision:2,
          pieces: [
            {
              gt: 0,
              lte: parseFloat(this.markLine[0]),
              color: '#096'
            },
            {
              gt: parseFloat(this.markLine[0]),
              lte: parseFloat(this.markLine[1]),
              color: '#ffde33'
            },
            //   {
            //   gt: 100,
            //   lte: 150,
            //   color: '#ff9933'
            // },
            //   {
            //   gt: 150,
            //   lte: 200,
            //   color: '#cc0033'
            // },
            //   {
            //   gt: 200,
            //   lte: 300,
            //   color: '#660099'
            // },
            //   {
            //   gt: 300,
            //   color: '#7e0023'
            // }
          ],
          outOfRange: {
            color: '#fa0744'
          }
        },
        series: {
          name: '系统性金融风险指数',
          type: 'line',
          data: data.map(function (item) {
            return item[1];
          }),

          //标记极端值
          markPoint:{
            symbol:'circle',
            symbolSize:10,
            data: [{
              itemStyle:{
                //标注的颜色
                color: {
                  type: 'radial',
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [{
                    offset: 0, color: 'purple' // 0% 处的颜色
                  }, {
                    offset: 1, color: '#258ddc' // 100% 处的颜色
                  }],
                  global: false // 缺省为 false
                }
              },
              //x轴的index和y值
              coord: this.markPoint[0] // 其中 5 表示 xAxis.data[5]，即 '33' 这个元素。
              // coord: ['5', 33.4] // 其中 '5' 表示 xAxis.data中的 '5' 这个元素。
              // 注意，使用这种方式时，xAxis.data 不能写成 [number, number, ...]
              // 而只能写成 [string, string, ...]
            }]

          },
          markLine: {
            //阈值标记线  这里应该是动态的
            silent: true,
            symbol:'none',
            label:{ position:'middle',},

            lineStyle:{
              color:'black'

            },
            data: [{
              yAxis: this.markLine[0]
            }, {
              yAxis:this.markLine[1]
            },

              //   {
              //   yAxis: 200
              // }, {
              //   yAxis: 300
              // }
            ]
          },
          markArea:{
            label: { // 分界线上的文字标签
              // position: 'end',
              formatter: '预测值'
            },
            data:[[{
              xAxis:this.markArea[0]},
              {
                xAxis:this.markArea[1]
                // x:'100%'
              },
            ]]

          }
        }
      }
      let opt2={
        tooltip: {
          trigger: 'item',
        },
        grid:

          {backgroundColor: '#eeb0ae',
            left:'0%',
            show:true,
            zlevel:0,
          }
        ,
        xAxis:
          {
            data:[{value:'未来一个月'}],
            axisLabel:{
              fontSize:5
            }
            // gridIndex: 0,
          },
        yAxis: {
          min:0.3,
          max:2,
          type: 'value',
          show:false,
          // boundaryGap: false,
          // gridIndex: 1
        },
        series: {
          type: 'boxplot',
          boxWidth : [2, 10],
          itemStyle: {
            clip: true
          },
          data:[{value: this.future,} ],
          // 确保箱型图显示在折线图之后
          // zlevel: 3,
          // 箱型图的x轴数据应对应未来一个月的日期，由于这些日期没有具体值，我们使用null，ECharts会自动处
          // ... 箱型图其他配置，如颜色、样式等
          markArea:{
            label: { // 分界线上的文字标签
              // position: 'start',
              formatter: '预测值'
            },
            itemStyle:{
              color:'yellow'
            }
            // data: [[  {
            //   name: '平均值到最大值',
            //   type: 'average'
            // },
            //   {
            //     type: 'max'
            //   }]]
          },
          tooltip: {
            formatter: function () {
              return [
                // 'Experiment ' + param.name + ': ',
                '最大值: ' + future[4],
                '均值+标准差: ' + future[3],
                '中位数: ' +future[2],
                '均值-标准差: ' + future[1],
                '最小值: ' + future[0]
              ].join('<br/>');
            }
          }
        }
      }
      myChart.setOption(option);
      myChartFuture.setOption(opt2)
      const that=this
      myChart.on('datazoom', function () {
        // Y轴最大值
        this.yMax = myChart.getModel().getComponent('yAxis').axis.scale._extent[1];
        // Y轴最小值
        this.yMin = myChart.getModel().getComponent('yAxis').axis.scale._extent[0];

        that.$nextTick(() => {
          // 设置 myChartFuture 的 y 轴值
          myChartFuture.setOption({
            yAxis: {
              min: this.yMin,
              max: this.yMax
            }
          });
        });

        // that.$emit("datazoom",[params.start,params.end])

      });

      // myChart.dispatchAction({
      //   type: 'dataZoom',
      //   batch: [{
      //     // 第一个 dataZoom 组件
      //     start: this.datazoom[0],
      //     end: this.datazoom[1]
      //   }]
      // })

    }

  },

}
</script>

<style scoped>
.warning-component {
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 100%;
  text-align: center;

  margin: auto;
}

.warning-dates {
  display: flex;
  justify-content: space-between;
}

.date-item {
  margin: 0 10px;
  font-weight: bold;
}

.warning-recent {
  color: #ff4d4f;
  font-weight: bold;
  margin-bottom: 10px;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  background: rgba(0 0 0 / 0.5);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 5px solid rgba(255, 255, 255, 0.2);
  border-top-color: #fff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.loading-text {
  margin-top: 10px;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
}

/* 动画效果 */
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

</style>