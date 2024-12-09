<template>
    <div>
       <!-- 搜索栏 -->

       <div class="form">
                                                        <!-- inline="true"表单域在一行 -->
          <el-form :inline="true"  :model="formInline" class="demo-form-inline">
            <el-form-item label="市场">
              <el-select   v-model="formInline.market" placeholder="选择市场" size="mini">
                <el-option v-for="item in options_market" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="行业">
              <el-select   v-model="formInline.industry" placeholder="选择行业" size="mini">
                <el-option v-for="item in options_industry" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-form-item>
          
            <el-form-item label="压力模型">
              <el-select   v-model="formInline.pressure" placeholder="选择压力模型" size="mini">
                <el-option v-for="item in options_pressure" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-form-item>

            <el-form-item>
              <el-button class="grayish_btn" @click="onSubmit1" icon="el-icon-search" size="mini">测试</el-button>
            </el-form-item>
          </el-form>
        </div>

    </div>
  </template>
  
  <script>
  import * as echarts from "echarts"
  export default {
    name:'pressure',
    data() {
      return {

         // 搜索栏——1市场选项
         options_market: [{
          value: '市场1',
          label: '市场1'
        }, {
          value: '市场2',
          label: '市场2'
        }, {
          value: '市场3',
          label: '市场3'
        }],

        // 搜索栏——2行业选项
        options_industry: [{
          value: '行业1',
          label: '行业1'
        }, {
          value: '行业2',
          label: '行业2'
        }, {
          value: '行业3',
          label: '行业3'
        }],
        
        // 搜索栏——3压力选项
        options_pressure: [{
          value: '压力1',
          label: '压力1'
        }, 
      ],
        // 搜索栏——整合收据进行接收
        formInline: {
            market: '',
            industry: '',
            pressure:'',
            // start_date:'',
            // end_date:'',
        },
          }          
  },
    computed:{
      isLogin(){
        return this.$store.state.isLogin
      }
    },
    mounted(){
          
  },
    methods:{
      
      onSubmit1(){
          console.log()

  }


  
  }


}

  </script>
  
<style lang="less" scoped>

.grayish_btn{//浅灰色按钮
  color: #fff;//文字颜色
  background-color: #aaaaaa;//背景颜色
}
</style>




