<template>
<div style="width: 100%;">
  <div class="wrapper">
    <div class="hidden-title">预警日期</div>
    <el-date-picker
      v-model="predictDate"
      type="date"
      placeholder="选择日期"
      format="yyyy-MM-dd"
      value-format="yyyy-MM-dd"
    >
    </el-date-picker>
    <div class="hidden-title">压力场景</div>
    <el-form ref="form" :model="form" label-width="80px">
      <el-collapse v-model="activePanels">
        <el-collapse-item name="0">
          <template slot="title">
            <span class="prefix"></span>预设场景
          </template>
          <el-row type="flex" class="row">
            <el-col :span="24">
              <el-popover
                title="全球贸易战"
                width="600"
                trigger="hover"
                content="描述: 主要经济体之间爆发全面贸易战，关税壁垒大幅提高，出口导向型经济遭受重创，外汇储备快速消耗，通胀压力上升。
经济原因: 根据比较优势理论，贸易壁垒破坏全球资源配置效率，导致生产成本上升和经济增长放缓。汇率波动进一步放大经济不确定性。"
              >
                <el-button @click="sceneChange($event, 'taxWar')" style="margin-right:5px;" slot="reference">全球贸易战</el-button>
              </el-popover>
              <el-popover
                title="经济大萧条"
                width="600"
                trigger="hover"
                content="描述: 全球需求急剧萎缩，贸易保护主义抬头，国内消费和投资大幅下降，导致经济陷入严重衰退。金融机构流动性枯竭，股市暴跌，房地产市场崩溃。
经济原因: 根据凯恩斯经济学，当总需求（AD = C + I + G + NX）急剧下降时，经济产出会大幅萎缩，导致失业率上升和通货紧缩压力。流动性陷阱可能出现，货币政策失效。"
              >
                <el-button @click="sceneChange($event, 'greatDepression')" style="margin-right:5px;" slot="reference">经济大萧条</el-button>
              </el-popover>
              <el-popover
                title="全球性疫情"
                width="600"
                trigger="hover"
                content="描述: 突发全球性疫情，封锁措施导致供应链中断，消费和投资锐减，经济陷入停滞。
经济原因: 根据需求冲击理论，隔离和不确定性降低消费与生产活动，供应链瓶颈加剧经济衰退。"
              >
                <el-button @click="sceneChange($event, 'globalPandemic')" style="margin-right:5px;" slot="reference">全球性疫情</el-button>
              </el-popover>
              <el-popover
                title="局部战争"
                width="600"
                trigger="hover"
                content="描述: 中东地区爆发局部战争，导致全球能源供应链中断，原油价格飙升，通胀压力加剧。国内企业成本上升，股市震荡，外汇市场承压。
经济原因: 根据供给冲击理论，关键资源（如石油）供应中断会推高生产成本，引发滞胀（高通胀+低增长）。资本流动性和地缘政治风险加剧市场波动。"
              >
                <el-button @click="sceneChange($event, 'localWars')" style="margin-right:5px;" slot="reference">局部战争</el-button>
              </el-popover>
              <el-popover
                title="房地产泡沫破裂"
                width="600"
                trigger="hover"
                content="描述: 房地产市场因过度投机和高杠杆融资而崩溃，房价暴跌，开发商破产，银行不良贷款激增，拖累整体经济。
经济原因: 根据资产泡沫理论，房地产价格的非理性上涨最终会因供需失衡或外部冲击（如加息）而破裂，导致财富效应逆转，消费和投资减少。"
              >
                <el-button @click="sceneChange($event, 'housingBubbleBurst')" style="margin-right:5px;" slot="reference">房地产泡沫破裂</el-button>
              </el-popover>
            </el-col>
          </el-row>
        </el-collapse-item>
        <el-collapse-item name="1">
          <template slot="title">
            <span class="prefix"></span>金融机构维度
          </template>
          <el-row type="flex" class="row">
            <el-col :span="8">
              <el-form-item label="存贷比" prop="finance-deposit-loan">
                <el-slider
                  v-model="form['finance-deposit-loan']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="M2/GDP" prop="finance-m2-gdp">
                <el-slider
                  v-model="form['finance-m2-gdp']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="M2/M1" prop="finance-m2-m1">
                <el-slider
                  v-model="form['finance-m2-m1']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row type="flex" class="row">
            <el-col :span="8">
              <el-form-item label="贷款/GDP" prop="finance-loan-gdp">
                <el-slider
                  v-model="form['finance-loan-gdp']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="中长期贷款" prop="finance-long-term-loans-loans" label-width="84px">
                <el-slider
                  v-model="form['finance-long-term-loans-loans']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="短期贷款" prop="finance-short-term-loans-gdp">
                <el-slider
                  v-model="form['finance-short-term-loans-gdp']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
          </el-row>
        </el-collapse-item>
        <el-collapse-item name="2">
          <template slot="title">
            <span class="prefix"></span>股票市场维度
          </template>
          <el-row type="flex" class="row">
            <el-col :span="8">
              <el-form-item label="上证指数" prop="stock-shanghai-index">
                <el-slider
                  v-model="form['stock-shanghai-index']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="平均市盈率" prop="stock-average-pe" label-width="84px">
                <el-slider
                  v-model="form['stock-average-pe']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="平均市净率" prop="stock-average-pb" label-width="84px">
                <el-slider
                  v-model="form['stock-average-pb']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
          </el-row>
        </el-collapse-item>
        <el-collapse-item name="3">
          <template slot="title">
            <span class="prefix"></span>外汇市场维度
          </template>
          <el-row type="flex" class="row">
            <el-col :span="8">
              <el-form-item label="外汇储备" prop="fx-reserves">
                <el-slider
                  v-model="form['fx-reserves']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="进出口总额" prop="fx-total-import-export" label-width="84px">
                <el-slider
                  v-model="form['fx-total-import-export']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="出口额" prop="fx-export-yoy">
                <el-slider
                  v-model="form['fx-export-yoy']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row type="flex" class="row">
            <el-col :span="8">
              <el-form-item label="进口额" prop="fx-import-yoy">
                <el-slider
                  v-model="form['fx-import-yoy']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
          </el-row>
        </el-collapse-item>
        <el-collapse-item name="4">
          <template slot="title">
            <span class="prefix"></span>房地产市场维度
          </template>
          <el-row type="flex" class="row">
            <el-col :span="8">
              <el-form-item label="投资完成额" prop="real-estate-investment" label-width="84px">
                <el-slider
                  v-model="form['real-estate-investment']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="销售额" prop="real-estate-housing-sales">
                <el-slider
                  v-model="form['real-estate-housing-sales']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
          </el-row>
        </el-collapse-item>
        <el-collapse-item name="5">
          <template slot="title">
            <span class="prefix"></span>政府部门维度
          </template>
          <el-row type="flex" class="row">
            <el-col :span="8">
              <el-form-item label="GDP" prop="macro-gdp">
                <el-slider
                  v-model="form['macro-gdp']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="CPI" prop="macro-cpi">
                <el-slider
                  v-model="form['macro-cpi']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="PPI" prop="macro-ppi">
                <el-slider
                  v-model="form['macro-ppi']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
          </el-row>
        </el-collapse-item>
        <el-collapse-item name="6">
          <template slot="title">
            <span class="prefix"></span>债券市场维度
          </template>
          <el-row type="flex" class="row">
            <el-col :span="9">
              <el-form-item label="综合指数同比" prop="bond-index-yoy" label-width="96px">
                <el-slider
                  v-model="form['bond-index-yoy']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
            <el-col :span="10">
              <el-form-item label="长短期国债收益" prop="bond-5y-3m" label-width="110px">
                <el-slider
                  v-model="form['bond-5y-3m']"
                  :min="-1.0"
                  :max="1.0"
                  :step="0.1"
                ></el-slider>
              </el-form-item>
            </el-col>
          </el-row>
        </el-collapse-item>
      </el-collapse>
      <div class="form-actions">
        <el-button type="primary" size="small" @click="submitForm">确定</el-button>
        <el-button size="small" @click="resetForm">重置</el-button>
      </div>
    </el-form>
  </div>
  <div class="wrapper">
    <div class="hidden-title">结果预测</div>
    <div v-if="loading" class="loading-overlay">
      <div class="loading-spinner"></div>
      <p class="loading-text">Loading...</p>
    </div>
    <div style="display: flex;">
      <div  ref="whole risk"  style=" float: left;width: 1200px; height: 350px;margin-left: 15px;margin-top: 0px;margin-right: 0px"></div>
      <div  ref="future"  style=" float: left; width: 50px; height: 350px;margin-left: -64px;margin-top: 0px;"></div>
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
      form: {},
      activePanels: ['0', '1', '2', '3'],
      stressTestData: {
        predicted_stress_index: 0.2,
        base_stress_index: 0.2
      },
      myChart: null,
      predictDate: '2025-02-04'
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
    fetch(`http://127.0.0.1:5000/api/v1/predict?predict=${this.predictDate}`)
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
          startValue: '2024-10-01'
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
        series: [{
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
            data:[[{xAxis:this.markArea[0]},
              {xAxis:this.markArea[1]},
            ]]

          }
        }]
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
          min:0.0,
          max:1,
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
      this.myChart = myChart;
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

    },

    submitForm() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          const stressedData = this.formatStressData();
          console.log('表单提交:', stressedData)
          this.loading = true;
          fetch(`http://127.0.0.1:5000/api/v1/stress_test?predict=${this.predictDate}`, {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ...stressedData }),
          })
          .then(res => res.json())
          .then(data => {
            this.$message.success('提交成功')
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
            // const opt = this.myChart.getOption();
            // const dates = opt.xAxis[0].data;
            // this.myChart.setOption({
            //   xAxis: {
            //     axisLabel:{
            //       fontSize:5
            //     },
            //     data: [...dates, ...this.markArea]
            //   },
            //   series: this.updateSeries(res)
            // })
          })
          .catch(e => console.error(e))

          
        }
      })
    },
    resetForm() {
      this.$refs.form.resetFields()
      this.form = {};
    },
    updateSeries(res) {
      console.log(res);
      const opt = this.myChart.getOption()
      const fsiSeries = opt.series[0]
      const predicted_stress_index = res.change <= 0 ? res.base_stress_index - res.change : res.predicted_stress_index;
      return [{...fsiSeries}, {
          name: 'Stress Test',
          type: 'scatter', // 用散点图表示压力测试值
          data: [[this.markArea[1], predicted_stress_index]], // 对应 markarea 结束日期
          itemStyle: { color: '#ff0000' }, // 红色表示压力测试数据
          symbolSize: 10,
          markLine: {
              silent: true,
              data: [
                  { yAxis: res.base_stress_index, name: 'Base Stress Index', lineStyle: { color: '#ff0000', type: 'dashed' } }
              ]
          }
        }]
    },
    sceneChange(event, sceneType) {
      if (sceneType === 'taxWar') { // 全球贸易战
        this.form['finance-deposit-loan'] = +0.05
        this.form['finance-m2-gdp'] = +0.05
        this.form['finance-m2-m1'] = +0.10
        this.form['finance-loan-gdp'] = +0.10
        this.form['finance-long-term-loans-loans'] = +0.10
        this.form['finance-short-term-loans-gdp'] = -0.10

        this.form['stock-shanghai-index'] = -0.25
        this.form['stock-average-pe'] = -0.25
        this.form['stock-average-pb'] = -0.15

        this.form['fx-total-import-export'] = -0.30
        this.form['fx-reserves'] = -0.25
        this.form['fx-export-yoy'] = -0.45
        this.form['fx-import-yoy'] = -0.20

        this.form['real-estate-investment'] = -0.20
        this.form['real-estate-housing-sales'] = -0.25
        
        this.form['macro-gdp'] = -0.12
        this.form['macro-cpi'] = +0.12
        this.form['macro-ppi'] = +0.15

        this.form['bond-index-yoy'] = +0.15
        this.form['bond-5y-3m'] = -0.1
      } else if (sceneType === 'greatDepression') { // 经济大萧条
        this.form['finance-deposit-loan'] = +0.15
        this.form['finance-m2-gdp'] = -0.10
        this.form['finance-m2-m1'] = -0.05
        this.form['finance-loan-gdp'] = -0.25
        this.form['finance-long-term-loans-loans'] = -0.30
        this.form['finance-short-term-loans-gdp'] = -0.20

        this.form['stock-shanghai-index'] = -0.40
        this.form['stock-average-pe'] = -0.50
        this.form['stock-average-pb'] = -0.30

        this.form['fx-total-import-export'] = -0.20
        this.form['fx-reserves'] = -0.35
        this.form['fx-export-yoy'] = -0.40
        this.form['fx-import-yoy'] = -0.30

        this.form['real-estate-investment'] = -0.50
        this.form['real-estate-housing-sales'] = -0.60
        
        this.form['macro-gdp'] = -0.20
        this.form['macro-cpi'] = -0.10
        this.form['macro-ppi'] = -0.15

        this.form['bond-index-yoy'] = +0.30
        this.form['bond-5y-3m'] = -0.20
      } else if (sceneType === 'globalPandemic') { // 全球性疫情
        this.form['finance-deposit-loan'] = +0.10
        this.form['finance-m2-gdp'] = -0.05
        this.form['finance-m2-m1'] = -0.08
        this.form['finance-loan-gdp'] = -0.20
        this.form['finance-long-term-loans-loans'] = -0.30
        this.form['finance-short-term-loans-gdp'] = -0.15

        this.form['stock-shanghai-index'] = -0.30
        this.form['stock-average-pe'] = -0.35
        this.form['stock-average-pb'] = -0.20

        this.form['fx-total-import-export'] = -0.15
        this.form['fx-reserves'] = -0.30
        this.form['fx-export-yoy'] = -0.25
        this.form['fx-import-yoy'] = -0.35

        this.form['real-estate-investment'] = -0.40
        this.form['real-estate-housing-sales'] = -0.50
        
        this.form['macro-gdp'] = -0.50
        this.form['macro-cpi'] = -0.02
        this.form['macro-ppi'] = -0.05

        this.form['bond-index-yoy'] = +0.10
        this.form['bond-5y-3m'] = +0.05
      } else if (sceneType === 'localWars') { // 局部战争
        this.form['finance-deposit-loan'] = +0.10
        this.form['finance-m2-gdp'] = +0.08
        this.form['finance-m2-m1'] = +0.05
        this.form['finance-loan-gdp'] = +0.20
        this.form['finance-long-term-loans-loans'] = -0.10
        this.form['finance-short-term-loans-gdp'] = +0.25

        this.form['stock-shanghai-index'] = -0.15
        this.form['stock-average-pe'] = -0.20
        this.form['stock-average-pb'] = -0.10

        this.form['fx-total-import-export'] = -0.10
        this.form['fx-reserves'] = -0.15
        this.form['fx-export-yoy'] = -0.10
        this.form['fx-import-yoy'] = -0.05

        this.form['real-estate-investment'] = -0.15
        this.form['real-estate-housing-sales'] = -0.10
        
        this.form['macro-gdp'] = -0.05
        this.form['macro-cpi'] = +0.15
        this.form['macro-ppi'] = +0.20

        this.form['bond-index-yoy'] = +0.10
        this.form['bond-5y-3m'] = +0.10
      } else if (sceneType === 'housingBubbleBurst') { // 房地产泡沫破灭
        this.form['finance-deposit-loan'] = +0.10
        this.form['finance-m2-gdp'] = -0.05
        this.form['finance-m2-m1'] = -0.10
        this.form['finance-loan-gdp'] = -0.20
        this.form['finance-long-term-loans-loans'] = -0.40
        this.form['finance-short-term-loans-gdp'] = -0.15

        this.form['stock-shanghai-index'] = -0.25
        this.form['stock-average-pe'] = -0.30
        this.form['stock-average-pb'] = -0.20

        this.form['fx-total-import-export'] = -0.10
        this.form['fx-reserves'] = -0.05
        this.form['fx-export-yoy'] = 0.00
        this.form['fx-import-yoy'] = -0.10

        this.form['real-estate-investment'] = -0.60
        this.form['real-estate-housing-sales'] = -0.70
        
        this.form['macro-gdp'] = -0.15
        this.form['macro-cpi'] = -0.05
        this.form['macro-ppi'] = -0.10

        this.form['bond-index-yoy'] = +0.25
        this.form['bond-5y-3m'] = +0.05
      }
    },
    formatStressData() {
      const indicators = {
        "finance": [
          "finance-deposit-loan",
          "finance-m2-gdp",
          "finance-m2-m1",
          "finance-loan-gdp",
          "finance-long-term-loans-loans",
          "finance-short-term-loans-gdp",
          "finance-leverage-ratio",
        ],
        "stock": [
          "stock-shanghai-index",
          "stock-average-pe",
          "stock-average-pb",
        ],
        "foreign_exchange": [
          "fx-reserves",
          "fx-total-import-export",
          "fx-export-yoy",
          "fx-import-yoy",
        ],
        "macro": [
          "macro-gdp",
          "macro-cpi",
          "macro-ppi",
        ],
        "bond": [
          "bond-index-yoy",
          "bond-5y-3m",
        ]
      }

      const result = {};
      Object.keys(indicators).map(market => {
        const market_indicators = indicators[market];
        const hasKey = market_indicators.some(key => Object.keys(this.form).includes(key))
        if (hasKey) {
          result[market] = {};
          market_indicators.forEach(indicator => {
            if (this.form[indicator]) {
              result[market][indicator] = this.form[indicator];
            }
          })
        }
      });
      return result;
    }

  },

}
</script>

<style scoped>
.wrapper {
  border: 1px solid #f9f9f9;
  padding: 16px;
}
.hidden-title {
  font-size: 12px;
  color: #D7D7D7;
  margin: 6px 0;
}
.prefix {
  width: 8px;
  display: inline-block;
  background-color: #409EFF;
  height: 30px;
  margin-right: 12px;
}
.row {
  margin-right: 24px;
}
.form-actions {
  margin-top: 20px;
  text-align: left;
}
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
  z-index: 1002;
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