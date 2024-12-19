<template>
  <div>
    <!-- 卡片化的标签页 -->
    <el-tabs type="card" @tab-click="handleTabClick">
      <!-- 主体风险 -->
      <el-tab-pane label="主体风险">
        <el-card style="height:508px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">主体风险</div>
          <div class="form">
            <component :is="compName" :zoom="datazoom" @datazoom="changeComp" ></component>
          </div>
        </el-card>
      </el-tab-pane>
      <!-- 利率风险 -->
      <el-tab-pane label="利率风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">利率风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch1"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario1" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit1" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 汇率风险 -->
      <el-tab-pane label="汇率风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">汇率风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch2"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario2" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit2" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 股票价格风险 -->
      <el-tab-pane label="股票价格风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">股票价格风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch3"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario3" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit3" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 智能利率风险 -->
      <el-tab-pane label="智能利率风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">智能利率风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch1"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario4" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit1" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 智能汇率风险 -->
      <el-tab-pane label="智能汇率风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">智能汇率风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch2"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario4" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit2" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 智能股票价格风险 -->
      <el-tab-pane label="智能股票价格风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">智能股票价格风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch3"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario4" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit3" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
    </el-tabs>
      <div v-if="activeTab === '利率风险' || activeTab === '智能利率风险'" class="table">
        <el-table 
          v-if="interestRateResults.length > 0"
          :data="interestRateResults" 
          :header-cell-style="{background: 'rgba(242, 242, 242)'}"
          :span-method="arraySpanMethod"
          :row-class-name="tableRowClassName"
          border
          :row-style="{height:'28px'}"
          :cell-style="{padding:'3px'}"
          header-row-class-name="active_header"
          header-cell-class-name="active_header"
          cell-class-name="content_center"
          style="width: 100%; border: 1px solid #7f7f7f;">
          <el-table-column prop="year" label="年份"></el-table-column>
          <el-table-column prop="type" label=""></el-table-column>
          <el-table-column prop="gap1" label="3个月内"></el-table-column>
          <el-table-column prop="gap2" label="3个月到1年"></el-table-column>
          <el-table-column prop="gap3" label="1年到5年"></el-table-column>
          <el-table-column prop="gap4" label="5年以上"></el-table-column>
          <el-table-column prop="total" label="总计"></el-table-column>
        </el-table>
        <div v-if="interestRateResults.length > 0" class="tip-text">
          <i class="header-icon el-icon-info"></i>净利息收入波动越大，表示承受的利率风险越大
        </div>
      </div>

      <div v-if="activeTab === '汇率风险' || activeTab === '智能汇率风险'" class="table">
        <el-table 
          v-if="currencyResults.length > 0"
          :data="currencyResults" 
          :header-cell-style="{background: 'rgba(242, 242, 242)'}"
          :span-method="arraySpanMethod"
          :row-class-name="tableRowClassName"
          border
          :row-style="{height:'28px'}"
          :cell-style="{padding:'3px'}"
          header-row-class-name="active_header"
          header-cell-class-name="active_header"
          cell-class-name="content_center"
          style="width: 100%; border: 1px solid #7f7f7f;">
          <el-table-column prop="year" label="年份"></el-table-column>
          <el-table-column prop="type" label=""></el-table-column>
          <el-table-column prop="USD" label="美元"></el-table-column>
          <el-table-column prop="HKD" label="港币"></el-table-column>
          <el-table-column prop="other" label="其他币种"></el-table-column>
          <el-table-column prop="total" label="总计"></el-table-column>
        </el-table>
        <div v-if="currencyResults.length > 0" class="tip-text">
    <i class="header-icon el-icon-info"></i>外币损益波动越大，表示承受的汇率风险越大
  </div>
      </div>

      <div v-if="activeTab === '股票价格风险' || activeTab === '智能股票价格风险'" class="table">
        <el-table 
          v-if="stockPriceResults.length > 0"
          :data="stockPriceResults" 
          :header-cell-style="{background: 'rgba(242, 242, 242)'}"
          :span-method="arraySpanMethod"
          :row-class-name="tableRowClassName"
          border
          :row-style="{height:'28px'}"
          :cell-style="{padding:'3px'}"
          header-row-class-name="active_header"
          header-cell-class-name="active_header"
          cell-class-name="content_center"
          style="width: 100%; border: 1px solid #7f7f7f;">
          <el-table-column prop="year" label="年份"></el-table-column>
          <el-table-column prop="type" label=""></el-table-column>
          <el-table-column prop="invest1" label="长期股权投资"></el-table-column>
          <el-table-column prop="invest2" label="金融投资：交易性金融资产"></el-table-column>
          <el-table-column prop="invest3" label="金融投资：其他权益工具投资"></el-table-column>
          <el-table-column prop="total" label="总计"></el-table-column>
        </el-table>
        <div v-if="stockPriceResults.length > 0" class="tip-text">
          <i class="header-icon el-icon-info"></i>经济资本越大，表示承受的股票价格风险越大
        </div>
      </div>
  </div>
</template>

<script>
import http from '@/utils/request'; // 引入封装的http实例
import mainRiskComponent from '@/components/mainRiskComponent';

export default {
  name: 'StressTesting',
  components:{
    mainRiskComponent,
  },
  data() {
    return {
      datazoom:[],
      compName:'mainRiskComponent',
      formInline: {
        company: '',
        scenario: ''
      },
      companyValid: true, // 用于存储公司名称是否有效的标志
      weightedResults: [], // 用于存储返回的加权结果
      options_scenario1: [
        {value: 0.05},
        {value: 0.10},
        {value: -0.05},
        {value: -0.10},
      ].map(item => ({
        label: `${item.value > 0 ? '上升' : '下降'}${(Math.abs(item.value) * 100) % 1 === 0 ? Math.abs(item.value) * 100 : (Math.abs(item.value) * 100).toFixed(2)}%`,
        value: item.value
      })),
      options_scenario2: [
        {value: 0.05},
        {value: 0.10},
        {value: -0.05},
        {value: -0.10},
      ].map(item => ({
        label: `${item.value > 0 ? '外币升值' : '外币贬值'}${(Math.abs(item.value) * 100) % 1 === 0 ? Math.abs(item.value) * 100 : (Math.abs(item.value) * 100).toFixed(2)}%`,
        value: item.value
      })),
      // 股票价格风险压力情景，经济资本是为了覆盖可能的损失而预留的资金，只考虑不利变动（下跌）情况
      options_scenario3: [
        {value: -0.10},
        {value: -0.20},
        {value: -0.30},
      ].map(item => ({
        label: `${item.value > 0 ? '上升' : '下降'}${(Math.abs(item.value) * 100) % 1 === 0 ? Math.abs(item.value) * 100 : (Math.abs(item.value) * 100).toFixed(2)}%`,
        value: item.value
      })),
      options_scenario4: [],
      interestRateResults: [], // 利率风险结果
      currencyResults: [], // 汇率风险结果
      stockPriceResults: [], // 股票价格风险结果
      activeTab: '利率风险', // 当前激活的标签页
    };
  },
  methods: {
    changeComp(mesg){
      this.datazoom=mesg
      console.log(mesg)
    },
    querySearch1(queryString, cb) {
      http.get('/interest_rate_risk/search', { params: { company: queryString } })
        .then(response => {
          const re = response.data.map(item => ({ value: item }));
          cb(re);
          this.companyValid = true; // 设置标志
        })
        .catch(error => {
          if (error.response && error.response.status === 404) {
            this.$message.error('公司名称不存在');
            this.companyValid = false; // 设置标志
          }
        });
    },
    querySearch2(queryString, cb) {
      http.get('/currency_risk/search', { params: { company: queryString } })
        .then(response => {
          const re = response.data.map(item => ({ value: item }));
          cb(re);
          this.companyValid = true; // 设置标志
        })
        .catch(error => {
          if (error.response && error.response.status === 404) {
            this.$message.error('公司名称不存在');
            this.companyValid = false; // 设置标志
          }
        });
    },
    querySearch3(queryString, cb) {
      http.get('/stock_price_risk/search', { params: { company: queryString } })
        .then(response => {
          const re = response.data.map(item => ({ value: item }));
          cb(re);
          this.companyValid = true; // 设置标志
        })
        .catch(error => {
          if (error.response && error.response.status === 404) {
            this.$message.error('公司名称不存在');
            this.companyValid = false; // 设置标志
          }
        });
    },
    onSubmit1() {
      if (!this.formInline.company || !this.companyValid) {
        this.$message.error('请选择正确的公司名称');
        return;
      }
      if(!this.formInline.scenario){
        this.$message.error('请选择压力情景');
        return;
      }
      http.post('/interest_rate_risk/test', this.formInline)
        .then(response => {
          this.interestRateResults = response.data;
        })
        .catch(error => {
          console.error("利率风险测试失败", error);
        });
    },
    onSubmit2() {
      if (!this.formInline.company || !this.companyValid) {
        this.$message.error('请选择正确的公司名称');
        return;
      }else if(!this.formInline.scenario){
        this.$message.error('请选择压力情景');
        return;
      }
      http.post('/currency_risk/test', this.formInline)
        .then(response => {
          this.currencyResults = response.data;
        })
        .catch(error => {
          console.error("汇率风险测试失败", error);
        });
    },
    onSubmit3() {
      if (!this.formInline.company || !this.companyValid) {
        this.$message.error('请选择正确的公司名称');
        return;
      }else if(!this.formInline.scenario){
        this.$message.error('请选择压力情景');
        return;
      }
      http.post('/stock_price_risk/test', this.formInline)
        .then(response => {
          this.stockPriceResults = response.data;
        })
        .catch(error => {
          console.error("股票价格风险测试失败", error);
        });
    },
    handleTabClick(tab) {
      this.activeTab = tab.label;
      // 重置表单数据
      this.formInline.company = '';
      this.formInline.scenario = '';
      // 清空所有结果
      this.interestRateResults = [];
      this.currencyResults = [];
      this.stockPriceResults = [];
      if (tab.label === '智能利率风险') {
        this.calculateScenario1();
      }else if (tab.label === '智能汇率风险') {
        this.calculateScenario2();
      }else if (tab.label === '智能股票价格风险') {
        this.calculateScenario3();
      }
    },
    calculateScenario1() {
      http.post('/smart_interest_rate_risk', {scenarios: this.options_scenario1})
        .then(response => {
          this.options_scenario4 = response.data.scenarios;
        })
        .catch(error => {
          console.error("智能利率风险压力测试失败", error);
        });
    },
    calculateScenario2() {
      http.post('/smart_currency_risk', {scenarios: this.options_scenario2})
        .then(response => {
          this.options_scenario4 = response.data.scenarios;
        })
        .catch(error => {
          console.error("智能汇率风险压力测试失败", error);
        });
    },
    calculateScenario3() {
      http.get('/smart_stock_price_risk')
        .then(response => {
          this.options_scenario4 = response.data.scenarios;
        })
        .catch(error => {
          console.error("智能股票价格风险压力测试失败", error);
        });
    },
    arraySpanMethod({ rowIndex, columnIndex }) {
      if (columnIndex === 0) {  // 年份列
        if (rowIndex % 2 === 0) {
          return {
            rowspan: 2,
            colspan: 1
          };
        } else {
          return {
            rowspan: 0,
            colspan: 0
          };
        }
      }
    },
    tableRowClassName({ rowIndex }) {
      if (rowIndex % 2 === 1) {
        return 'success-row';
      }
      return '';
    }
  }
};
</script>

<style lang="less" scoped>
.grayish_btn{//浅灰色按钮
  color: #fff;//文字颜色
  background-color: #aaaaaa;//背景颜色
}
.card_label{
  font-size: 13px;
  // padding:10px; 
  color:#fff;
  background-color: #7f7f7f;
}
.form{//产品搜索栏
    display:flex;
    justify-content:space-between;//左右贴边
    margin-top:5px; 
    // height: 40px;
    padding-left: 40px;
    // padding: 30px;

}

.table {
  margin-top: 10px;
  font-size: 12px;

  // 调整表头间隔、设置表头下方边框颜色
  /deep/ .el-table td.el-table__cell, .el-table th.el-table__cell.is-leaf {
    border-bottom: 1px solid #333333 !important;
    padding: 1px 0; 
    min-width: 0;
  }
  
  // 去除表格cell间隔
  .el-table .el-table__cell {
    padding: 0px 0; 
    min-width: 0;
    border-color: #333333;
  }
  
  /deep/ .active_header {  //表头
    color: #333333;
    font-size: 13px;
    text-align: center !important;
    border-color: #333333;
  }
  
  /deep/ .content_center {  //表的内容
    text-align: center !important;
    font-size: 13px;
    border-color: #333333;
  }
  /deep/ .el-table .success-row {
    background-color: #ECF5FF;  // 你可以改成你想要的颜色
    color: #333;
  }
}
.tip-text {
  font-size: 13px;  /* 调整字体大小 */
  color: #333333;   /* 调深颜色使文字更清晰 */
  margin-top: 8px;  /* 适当增加上边距 */
  padding-left: 5px;
}

.header-icon {
  margin-right: 5px;
  font-size: 14px;  /* 图标也相应调大 */
}
</style>




