<!-- 预警服务主页面 -->
<template>
  <div>
    <div class="one">
      <el-card style='height: 360px;' :body-style={padding:0}> 
       <!-- height:400px -->
       <!-- 1、上标 -->
        <span class="superscript" style="width: 20px; height: 40px;">整体风险概括</span>
        <!-- 2、卡片x3 -->
        <div class="tirCard">
          <!-- 股票市场 -->
          <div class="my-element" style="width: 380px; height: 250px;">
            <h4 style="padding-left: 50px;">股票市场</h4>
            <div class="tirCircle">
              <div class="circle_low">
                <div style="display: flex;justify-content:center;margin-top: 25px;">{{ stockLow }}</div>
              </div>
              <div class="circle_mid">
                <div style="display: flex;justify-content:center;margin-top: 25px;">{{ stockMid }}</div>
              </div>
              <div class="circle_high">
                <div style="display: flex;justify-content:center;margin-top: 25px;">{{ stockHigh }}</div>
              </div>
            </div>
            <div class="tirText"> 
              <span>低风险</span>
              <span>中风险</span>
              <span>高风险</span>
            </div>

            <div>
              <h5 style="display: flex;justify-content:center">综合风险水平       95</h5>
            </div>


          </div>

          <!-- 债券市场 -->
          <div class="my-element" style="width: 380px; height: 250px;">
            <h4 style="padding-left: 50px;">债券市场</h4>
            <div class="tirCircle">
              <div class="circle_low">
                <div style="display: flex;justify-content:center;margin-top: 25px;">1862</div>
              </div>
              <div class="circle_mid">
                <div style="display: flex;justify-content:center;margin-top: 25px;">441</div>          
              </div>
              <div class="circle_high">
                <div style="display: flex;justify-content:center;margin-top: 25px;">87</div>
              </div>
            </div>
            <div class="tirText"> 
              <span>低风险</span>
              <span>中风险</span>
              <span>高风险</span>
            </div>
            <div>
              <h5 style="display: flex;justify-content:center">综合风险水平       95</h5>
            </div>
          </div>
          <!-- 期货市场 -->
          <div class="my-element" style="width: 380px; height: 250px;">
            <h4 style="padding-left: 50px;">期货市场</h4>
            <div class="tirCircle">
              <div class="circle_low">
                <div style="display: flex;justify-content:center;margin-top: 25px;">1862</div>
              </div>
              <div class="circle_mid">
                <div style="display: flex;justify-content:center;margin-top: 25px;">441</div>          
              </div>
              <div class="circle_high">
                <div style="display: flex;justify-content:center;margin-top: 25px;">87</div>
              </div>
            </div>
            <div class="tirText"> 
              <span>低风险</span>
              <span>中风险</span>
              <span>高风险</span>
            </div>
            <div>
              <h5 style="display: flex;justify-content:center">综合风险水平       95</h5>
            </div>
          </div>

        </div>
        <!-- 3、总结语句 -->
<!--        <span style="margin: 10px;padding-left:20px;padding-right:20px;display: inline-block;">-->
<!--          &#8194 &#8194中国资本市场主要由股票市场、债券市场和期货市场组成，-->
<!--          其中股票市场份额占比为 50%，-->
<!--          债券市场份额占比为 30%、-->
<!--          期货市场份额占比为20%，-->
<!--          整体市场风险水平评估为 89，属于 低风险</span>-->

          <!--  &#32; == 普通的英文半角空格
                &#160; == &nbsp; == &#xA0; == no-break space （普通的英文半角空格但不换行）
                &#12288; == 中文全角空格 （一个中文宽度）
                &#8194; == &ensp; == en空格 （半个中文宽度）
                &#8195; == &emsp; == em空格 （一个中文宽度）
                &#8197; == 四分之一em空格 （四分之一中文宽度） -->
      </el-card>
    </div>

  <div class="two">
      <el-card style='height: 800px;margin-top:5px' :body-style={padding:0} > 
       <!-- height:400px -->
       <!-- 1、上标 -->
        <span class="superscript" style="width: 20px; height: 40px;">预警服务</span>
       <!-- 2、搜索栏 -->
        <div class="form">
          <el-form :inline="true"  class="demo-form-inline" :model="formInline1" ref="formInline">
            <el-form-item label="预警市场">
              <el-select  v-model="formInline1.market" size="mini">
                <el-option label="股票" value="stock"></el-option>
                <el-option label="债券" value="bond"></el-option>
                <el-option label="期货" value="future"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item>
              <el-button class="grayish_btn" @click="onSubmit1" size="mini">查询</el-button>
            </el-form-item>
          </el-form>
        </div>
        <!-- 3、内容 -->
        <div class="one_twins_card">
          <!-- 一左 -->
          <el-card style=" height:600px;width: 68%;" :body-style={padding:0}>         <!--:body-style={padding:0}取消卡片边距，btn就能在左上角 -->
            <!--(1)风险预警  -->
            <div style="display:flex;justify-content:space-between;">
              <div style="display:flex;padding-bottom: 10px;">
                <el-divider direction="vertical" class="sublabel"></el-divider>
                <span class='title' >风险预警</span>
              </div>
              <div style="display:flex;">
<!--                <span class="text"  v-on:click="statistics1()">查看风险统计</span>-->
                <span class="text"  v-on:click="detail2()">查看全部详情</span>
              </div>
            </div>
            <el-table class='table' :data="tableData_main_1" :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}" 
                  border  
                  
                  :row-style="{height:'28px'}"
                  :cell-style="{padding:'0px'}"
                  header-row-class-name="active_header"
                  header-cell-class-name="active_header"
                  cell-class-name="content_center"
                  height="215"
                    >
                <el-table-column v-for='(val,key) in tableLabel_main_1' :prop="key" :label="val"  show-overflow-tooltip :min-width="calculateColumnWidth(key,tableData_main_1)">
              
              </el-table-column><!--插槽里面没有东西就可以用单标签  -->
                                                                              <!-- show-overflow-tooltip可以省略展示较多的文字内容 -->
            </el-table>
            <!--(2)异常预警 -->
            <div style="display:flex;justify-content:space-between;">
              <div style="display:flex;padding-bottom: 10px;">
                <el-divider direction="vertical" class="sublabel"></el-divider>
                <span class='title' >异常预警</span>
              </div>
              <div style="display:flex;">
<!--                <span class="text"  v-on:click="statistics3()">查看异常统计</span>-->
<!--                <span class="text"  v-on:click="detail3()">查看全部详情</span>-->
              </div>
            </div>
<!--            v-if动态选择表类型-->
            <el-table class='table' :data="tableData_main_2" :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}" 
                  border  
                  
                  :row-style="{height:'28px'}"
                  :cell-style="{padding:'0px'}"
                  header-row-class-name="active_header"
                  header-cell-class-name="active_header"
                  cell-class-name="content_center"
                      v-if="formInline1.market==='stock'"
                  height="215"   >
                <el-table-column  v-for='(val,key) in tableLabel1' :prop="key" :label="val"  show-overflow-tooltip :min-width="calculateColumnWidth(key,tableData_main_2)">
              
              </el-table-column><!--插槽里面没有东西就可以用单标签  -->
                                                                              <!-- show-overflow-tooltip可以省略展示较多的文字内容 -->
            </el-table>
            <el-table class='table' :data="tableData_main_2" :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}"
                      border

                      :row-style="{height:'28px'}"
                      :cell-style="{padding:'0px'}"
                      header-row-class-name="active_header"
                      header-cell-class-name="active_header"
                      cell-class-name="content_center"
                      v-if="formInline1.market==='bond'"
                      height="215"   >
              <el-table-column  v-for='(val,key) in tableLabel2' :prop="key" :label="val"  show-overflow-tooltip :min-width="calculateColumnWidth(key,tableData_main_2)">

              </el-table-column><!--插槽里面没有东西就可以用单标签  -->
              <!-- show-overflow-tooltip可以省略展示较多的文字内容 -->
            </el-table>
            <el-table class='table' :data="tableData_main_2" :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}"
                      border

                      :row-style="{height:'28px'}"
                      :cell-style="{padding:'0px'}"
                      header-row-class-name="active_header"
                      header-cell-class-name="active_header"
                      cell-class-name="content_center"
                      v-if="formInline1.market==='future'"
                      height="215"   >
              <el-table-column  v-for='(val,key) in tableLabel3' :prop="key" :label="val"  show-overflow-tooltip :min-width="calculateColumnWidth(key,tableData_main_2)">

              </el-table-column><!--插槽里面没有东西就可以用单标签  -->
              <!-- show-overflow-tooltip可以省略展示较多的文字内容 -->
            </el-table>


          </el-card>
          
          <!-- 一右 -->
          <el-card style=" height:600px;width: 31%;" :body-style={padding:0} overflow:hidden >
            <div style="display:flex;margin-bottom: 10px;">
              <el-divider direction="vertical" class="sublabel"></el-divider>
              <span class='title'>预警提示</span>
            </div>
            


<!--            <div style="padding: 5px;">【{{warning_type1}}】2023/6/29 16:00股票1监测到风险流动风险<span class="text_detail"  v-on:click="detail1(warning_type1)">[查看详情]</span></div>-->
<!--            <div style="padding: 5px;">【{{warning_type1}}】2023/6/2916:00股票1检测到风险流动风险<span class="text_detail"  v-on:click="detail1(warning_type1)">[查看详情]</span></div>-->
<!--            <div style="padding: 5px;">【{{warning_type1}}】2023/6/29 16:00股票1检测到风险流动风险<span class="text_detail"  v-on:click="detail1(warning_type1)">[查看详情]</span></div>-->
<!--            <div style="padding: 5px;">【{{warning_type1}}】2023/6/29 16:00股票1检测到风险流动风险<span class="text_detail"  v-on:click="detail1(warning_type1)">[查看详情]</span></div>-->
<!--            <div style="padding: 5px;">【{{warning_type2}}】2023/6/29 16:00股票1检测到异常股价波动异常<span class="text_detail"  v-on:click="detail1(warning_type2)">[查看详情]</span></div>-->
<!--            <div style="padding: 5px;">【{{warning_type2}}】2023/6/2916:00股票1检测到异常股价波动异常<span class="text_detail"  v-on:click="detail1(warning_type2)">[查看详情]</span></div>-->
<!--            <div style="padding: 5px;">【{{warning_type2}}】2023/6/2916:00股票1检测到异常股价波动异常<span class="text_detail"  v-on:click="detail1(warning_type2)">[查看详情]</span></div>-->
<!--            <div style="padding: 5px;">【{{warning_type2}}】2023/6/29 16:00股票1检测到异常股价波动异常<span class="text_detail"  v-on:click="detail1(warning_type2)">[查看详情]</span></div>-->

            <vue-seamless-scroll v-if="contentList.length>0" :data="contentList" class="wrap"  >
<!--            <div v-for="(val,key) in contentList" :key="key" style="padding: 5px;">【{{warning_type2}}】{{val.time}},{{val.entity}}检测到{{val.type}}<span class="text_detail"  v-on:click="detail1(warning_type2)">[查看详情]</span></div>-->
              <ul class="item">
                <li v-for="(item, index) in contentList" :key="index">
                  <span class="time" v-text="item.time"></span>
                  <span class="entity" v-text="item.entity"></span>
                  <span class="type" v-text="item.type"></span>
<!--                 <span class="text_detail"  v-on:click="detail1(item.type)">[详情]</span>-->
                </li>
              </ul>
            </vue-seamless-scroll>
<!--            <vue-seamless-scroll :data="listData" class="warp">-->
<!--              <ul class="item">-->
<!--                <li v-for="(item, index) in listData" :key="index">-->
<!--                  <span class="title" v-text="item.title"></span>-->
<!--                  <span class="date" v-text="item.date">检测大</span>-->
<!--                  <span class="t" v-text="item.t"></span>-->
<!--                </li>-->
<!--              </ul>-->
<!--            </vue-seamless-scroll>-->
          </el-card>
        </div>
      </el-card>

      <!-- #1跳转-风险预警-查看风险统计 -->
      <!-- 待完成 -->
      <!-- #3跳转-异常预警-查看异常统计 -->
      <!-- 待完成 -->

      <!-- #1弹窗-风险预警-查看单条信息详情 -->
      <el-dialog  :visible.sync="detailsdialog1" width="100%" @open="open()" >
        <!-- 详细信息 -->
        <el-card style=" height:100% ;margin-bottom:10px ; " :body-style={padding:0} >    
          <span class="superscript" style="width: 20px; height: 40px;">预警详情-风险个体</span>
          <el-table class='detail_table' :data="tableData_detail_1_1" :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}" 
                  border  
                  
                  :row-style="{height:'28px'}"
                  :cell-style="{padding:'0px'}"
                  header-row-class-name="active_header"
                  header-cell-class-name="active_header"
                  cell-class-name="content_center"
                  height="215"   >
                <el-table-column v-for='(val,key) in tableLabel_detail_1' :prop="key" :label="val"  show-overflow-tooltip :min-width="calculateColumnWidth(key,tableData_detail_1_1)">
              
              </el-table-column><!--插槽里面没有东西就可以用单标签  -->
                                                                              <!-- show-overflow-tooltip可以省略展示较多的文字内容 -->
          </el-table>
            <div>
                <el-table class='detail_table'
                    :data="tableData_detail_1_2"
                    style="width: 100%"
                    :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}"
                    border


                    :row-style="{height:'28px'}"
                    :cell-style="{padding:'0px'}"
                    header-row-class-name="active_header"
                    header-cell-class-name="active_header"
                    cell-class-name="content_center">

                    <el-table-column
                    prop="name"
                    label="公司名称"
                    width="100">
                  </el-table-column>
                  <el-table-column label="风险水平">
                    <el-table-column
                      prop="财务杠杆"
                      label="财务杠杆"
                      sortable
                      width="70">
                    </el-table-column>
                    <el-table-column
                      prop="经营杠杆"
                      label="经营杠杆"
                      sortable
                      width="70">
                    </el-table-column>
                    <el-table-column
                      prop="综合杠杆"
                      label="综合杠杆"
                      sortable
                      width="70">
                    </el-table-column>
                    <el-table-column
                      prop="流动比率"
                      label="流动比率"
                      sortable
                      width="70">
                    </el-table-column>
                  </el-table-column>
                    <el-table-column label="（一）流动风险">
                      <el-table-column
                        prop="速动比率"
                        label="速动比率"
                        sortable
                        width="70">
                      </el-table-column>
                      <el-table-column
                        prop="应收账款周转天数(天)"
                        label="应收账款周转天数（天）"
                        width="100">
                      </el-table-column>
                      <el-table-column
                        prop="流动风险综合指数"
                        label="流动风险综合指数"
                        width="120"
                        sortable>
                      </el-table-column>
                    </el-table-column>

                    <el-table-column label="（二）市场风险">
                      <el-table-column
                        prop="在险价值"
                        label="在险价值"
                        sortable
                        width="120">
                      </el-table-column>
                    </el-table-column>

                      <el-table-column label="（三）经营风险">
                        <el-table-column
                          prop="资产收益率标准差"
                          label="资产收益率标准差"
                          sortable
                          width="120">
                        </el-table-column>
                    </el-table-column>

                    <el-table-column label="（四）信用风险">
                        <el-table-column
                          prop="资产负债率"
                          label="资产负债率"
                          sortable
                          width="100">
                        </el-table-column>

                        <el-table-column
                          prop="投资盈利率"
                          label="投资盈利率"
                          sortable
                          width="100">
                        </el-table-column>

                    </el-table-column>
                  <el-table-column
                      prop="声誉风险综合指数"
                      label="声誉风险"
                      width="100">
                  </el-table-column>
                  <el-table-column
                      prop="政策风险综合指数"
                      label="政策风险"
                      width="100">
                  </el-table-column>
                  <el-table-column
                      prop="法律风险综合指数"
                      label="法律风险"
                      width="100">
                  </el-table-column>
                  <el-table-column
                      prop="操作风险综合指数"
                      label="操作风险"
                      width="100">
                  </el-table-column>
                    <el-table-column
                    prop="综合风险等级"
                    label="综合风险等级"
                    width="100">
                  </el-table-column>
                </el-table>
            </div>
        </el-card>
      </el-dialog>      
      <!-- #2弹窗-异常预警-查看单条信息详情 -->
      <el-dialog  :visible.sync="detailsdialog2" width="100%" @open="open()" >
        <!-- 详细信息 -->
        <el-card style=" height:100%;margin-bottom:10px ; " :body-style={padding:0} >    
          <span class="superscript" style="width: 20px; height: 40px;">预警详情-风险个体</span>
          <el-table class='detail_table' :data="tableData_detail_2_1" :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}" 
                  border  
                  
                  :row-style="{height:'28px'}"
                  :cell-style="{padding:'0px'}"
                  header-row-class-name="active_header"
                  header-cell-class-name="active_header"
                  cell-class-name="content_center"
                  height="215"   >
                <el-table-column v-for='(val,key) in tableLabel_detail_2_1' :prop="key" :label="val"  show-overflow-tooltip :min-width="calculateColumnWidth(key,tableData_detail_1_1)">
              
              </el-table-column><!--插槽里面没有东西就可以用单标签  -->
                                                                              <!-- show-overflow-tooltip可以省略展示较多的文字内容 -->
          </el-table>
          <div style="display:flex;">
              <el-divider direction="vertical" class="sublabel"></el-divider>
              <span class='title'>异常关联分析</span>
          </div>
          <div style="height:300px;margin-left: 20px;">图谱</div>
          <el-table class='detail_table'
                    :data="tableData_detail_2_2"
                    style="width: 100%"
                    :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}"
                    border


                    :row-style="{height:'28px'}"
                    :cell-style="{padding:'0px'}"
                    header-row-class-name="active_header"
                    header-cell-class-name="active_header"
                    cell-class-name="content_center"
                    height="215" >
                    <el-table-column v-for='(val,key) in tableLabel_detail_2_2' :prop="key" :label="val"  show-overflow-tooltip :min-width="calculateColumnWidth(key,tableData_detail_1_1)">
              
                    </el-table-column><!--插槽里面没有东西就可以用单标签  -->
                 
                  
                </el-table>
                <Histogram/>
              <span style="display:block;text-indent:2em;line-height: 25px;margin: 10px;">
                股票1在2021-01-01至2021-02-01时间段内，在2021-1-8内达到股价峰值，为26元/每股，比该公司该段时间内平均股价（9元/每股），上涨15元，涨幅188.8%。在股价过高的情况下可能会导致风险增加、股票泡沫、不良收购等多种导致经济不稳定的风险因素的增加，在2021-01-09达到交易量峰值，为231支，比该公司该段时间内平均交易量（121股），上涨110股，涨幅为90.9%。在交易量过高的情况下可能会在一定程度上可能对市场稳定性、公平竞争和投资者信心造成负面影响。
                
              </span>



        </el-card>
      </el-dialog>
      <!-- #3弹窗-风险预警-查看全部详情 -->
      <el-dialog  :visible.sync="detailsdialog_all_1"    width="100%" @open="open()" >
        <!-- 详细信息 -->
        <el-card style=" margin-bottom:10px ; " :body-style={padding:0} >    
          <span class="superscript" style="width: 20px; height: 40px;">预警详情</span>
          <el-table class='detail_table' :data="tableData_detail_all_risk_1" :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}" 
                  border  
                  
                  :row-style="{height:'28px'}"
                  :cell-style="{padding:'0px'}"
                  header-row-class-name="active_header"
                  header-cell-class-name="active_header"
                  cell-class-name="content_center"
                  height="300"   >
                <el-table-column v-for='(val,key) in tableLabel_detail_all_1' :prop="key" :label="val"  show-overflow-tooltip :min-width="calculateColumnWidth(key,tableData_detail_1_1)">
              
              </el-table-column><!--插槽里面没有东西就可以用单标签  -->
                                                                              <!-- show-overflow-tooltip可以省略展示较多的文字内容 -->
          </el-table>
        </el-card>

<!--        暂不需要-->
<!--          <div style="display:flex;padding-bottom: 10px;">-->
<!--            <el-divider direction="vertical" class="sublabel"></el-divider>-->
<!--            <span class='title' >个体风险指数分析</span>-->
<!--          </div>-->
<!--          <el-table class='detail_table'-->
<!--                    :data="tableData_detail_1_2"-->
<!--                    style="width: 100%"-->
<!--                    :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}"-->
<!--                    border-->


<!--                    :row-style="{height:'28px'}"-->
<!--                    :cell-style="{padding:'0px'}"-->
<!--                    header-row-class-name="active_header"-->
<!--                    header-cell-class-name="active_header"-->
<!--                    cell-class-name="content_center">-->

<!--                    <el-table-column-->
<!--                    prop="name"-->
<!--                    label="公司名称"-->
<!--                    width="100">-->
<!--                  </el-table-column>-->
<!--                  <el-table-column label="风险水平">-->
<!--                    <el-table-column-->
<!--                      prop="财务杠杆"-->
<!--                      label="财务杠杆"-->
<!--                      sortable-->
<!--                      width="70">-->
<!--                    </el-table-column>-->
<!--                    <el-table-column-->
<!--                      prop="经营杠杆"-->
<!--                      label="经营杠杆"-->
<!--                      sortable-->
<!--                      width="70">-->
<!--                    </el-table-column>-->
<!--                    <el-table-column-->
<!--                      prop="综合杠杆"-->
<!--                      label="综合杠杆"-->
<!--                      sortable-->
<!--                      width="70">-->
<!--                    </el-table-column>-->
<!--                    <el-table-column-->
<!--                      prop="流动比率"-->
<!--                      label="流动比率"-->
<!--                      sortable-->
<!--                      width="70">-->
<!--                    </el-table-column>-->
<!--                  </el-table-column>-->
<!--                    <el-table-column label="（一）流动风险">-->
<!--                      <el-table-column-->
<!--                        prop="速动比率"-->
<!--                        label="速动比率"-->
<!--                        sortable-->
<!--                        width="70">-->
<!--                      </el-table-column>-->
<!--                      <el-table-column-->
<!--                        prop="应收账款周转天数(天)"-->
<!--                        label="应收账款周转天数（天）"-->
<!--                        width="100">-->
<!--                      </el-table-column>-->
<!--                      <el-table-column-->
<!--                        prop="流动风险综合指数"-->
<!--                        label="流动风险综合指数"-->
<!--                        width="120"-->
<!--                        sortable>-->
<!--                      </el-table-column>-->
<!--                    </el-table-column>-->

<!--                    <el-table-column label="（二）市场风险">-->
<!--                      <el-table-column-->
<!--                        prop="在险价值"-->
<!--                        label="在险价值"-->
<!--                        sortable-->
<!--                        width="120">-->
<!--                      </el-table-column>-->
<!--                    </el-table-column>-->

<!--                      <el-table-column label="（三）经营风险">-->
<!--                        <el-table-column-->
<!--                          prop="资产收益率标准差"-->
<!--                          label="资产收益率标准差"-->
<!--                          sortable-->
<!--                          width="120">-->
<!--                        </el-table-column>-->
<!--                    </el-table-column>-->

<!--                    <el-table-column label="（四）信用风险">-->
<!--                        <el-table-column-->
<!--                          prop="资产负债率"-->
<!--                          label="资产负债率"-->
<!--                          sortable-->
<!--                          width="100">-->
<!--                        </el-table-column>-->

<!--                        <el-table-column-->
<!--                          prop="投资盈利率"-->
<!--                          label="投资盈利率"-->
<!--                          sortable-->
<!--                          width="100">-->
<!--                        </el-table-column>-->

<!--                    </el-table-column>-->
<!--                  <el-table-column-->
<!--                      prop="声誉风险综合指数"-->
<!--                      label="声誉风险"-->
<!--                      width="100">-->
<!--                  </el-table-column>-->
<!--                  <el-table-column-->
<!--                      prop="政策风险综合指数"-->
<!--                      label="政策风险"-->
<!--                      width="100">-->
<!--                  </el-table-column>-->
<!--                  <el-table-column-->
<!--                      prop="法律风险综合指数"-->
<!--                      label="法律风险"-->
<!--                      width="100">-->
<!--                  </el-table-column>-->
<!--                  <el-table-column-->
<!--                      prop="操作风险综合指数"-->
<!--                      label="操作风险"-->
<!--                      width="100">-->
<!--                  </el-table-column>-->
<!--                    <el-table-column-->
<!--                    prop="综合风险等级"-->
<!--                    label="综合风险等级"-->
<!--                    width="100">-->
<!--                  </el-table-column>-->
<!--                </el-table>-->


      </el-dialog>
      <!-- #4弹窗-异常预警-查看异常统计 -->
      <el-dialog  :visible.sync="detailsdialog_all_2" width="100%" @open="open()" >
        <!-- 详细信息 -->
        <el-card style="margin-bottom:10px ; " :body-style={padding:0} >    
          <span class="superscript" style="width: 20px; height: 40px;">预警详情</span>
          <el-table class='detail_table' :data="tableData_detail_all_risk_1" :header-cell-style="{background: 'rgba(242, 242, 242, 0.654901960784314)'}" 
                  border  
                  
                  :row-style="{height:'28px'}"
                  :cell-style="{padding:'0px'}"
                  header-row-class-name="active_header"
                  header-cell-class-name="active_header"
                  cell-class-name="content_center"
                  height="500"   >
                <el-table-column v-for='(val,key) in tableLabel_detail_all_1' :prop="key" :label="val"  show-overflow-tooltip :min-width="calculateColumnWidth(key,tableData_detail_1_1)">
              
              </el-table-column><!--插槽里面没有东西就可以用单标签  -->
                                                                              <!-- show-overflow-tooltip可以省略展示较多的文字内容 -->
          </el-table>
        </el-card>
      </el-dialog>
  </div>
</div>
</template>

<script>
import Histogram from "@/components/echarts/Histogram.vue";
import http from "@/utils/request";
import vueSeamlessScroll from 'vue-seamless-scroll'
import {Loading} from "element-ui";
export default {
  name:'warning',
  components:{
    Histogram,
    vueSeamlessScroll,
  },
  data () {
    return {
      stockLow:1862,
      stockMid:442,
      stockHigh:87,
      // 滚动窗数据
      listData: [{
        'title': '无缝滚动第一行无缝滚动第一行',
        'date': '2017-12-16',
        't':'ss'
      }, {
        'title': '无缝滚动第二行无缝滚动第二行',
        'date': '2017-12-16',
        't':'qq'
      }, {
        'title': '无缝滚动第三行无缝滚动第三行',
        'date': '2017-12-16'
      }, {
        'title': '无缝滚动第四行无缝滚动第四行',
        'date': '2017-12-16'
      }, {
        'title': '无缝滚动第五行无缝滚动第五行',
        'date': '2017-12-16'
      }, {
        'title': '无缝滚动第六行无缝滚动第六行',
        'date': '2017-12-16'
      }, {
        'title': '无缝滚动第七行无缝滚动第七行',
        'date': '2017-12-16'
      }, {
        'title': '无缝滚动第八行无缝滚动第八行',
        'date': '2017-12-16'
      }, {
        'title': '无缝滚动第九行无缝滚动第九行',
        'date': '2017-12-16'
      }],
      defaultOption:{
        step: 0.1, // 数值越大速度滚动越快
        limitMoveNum: 10, // 开始无缝滚动的数据量 this.dataList.length
        hoverStop: true, // 是否开启鼠标悬停stop
        direction: 0, // 0向下 1向上 2向左 3向右
        openWatch: true, // 开启数据实时监控刷新dom
        singleHeight: 0, // 单步运动停止的高度(默认值0是无缝不停止的滚动) direction => 0/1
        singleWidth: 0, // 单步运动停止的宽度(默认值0是无缝不停止的滚动) direction => 2/3
        waitTime: 1000 // 单步运动停止的时间(默认值1000ms)
      },
      contentList:[],
      // 整合收据进行接收
      formInline1:{
        market:'stock'
      },
      // 表格数据
      tableData_main_1:[
        {
          序号:1,
          主体名称:'股票1',
          主体代码:'688001.SH',
          主体类型:'股票',
          行业:'计算机',
          当前预警时刻:'2023/6/29 16:00',
          预警类型:'严重',
          风险类型:'流动风险',
        },
        {
          序号:2,
          主体名称:'股票3',
          主体代码:'688002.SH',
          主体类型:'股票',
          行业:'计算机',
          当前预警时刻:'2023/6/29 16:00',
          预警类型:'严重',
          风险类型:'市场风险',
        },
      ],
      tableLabel_main_1: {
        // 序号: '序号',
        // 主体名称: '主体名称',
        code: '主体代码',
        // 主体类型: '主体类型',
        industry:'行业',
        early_warning_time:'预警时刻',
        warning_type:'风险水平',
        risk_type:'风险类型',

      },
        
      tableData_main_2:[
        {
          序号:1,
          主体名称:'股票1',
          主体代码:'688001.SH',
          主体类型:'股票',
          行业:'计算机',
          当前预警时刻:'2023/6/29 16:00',
          预警类型:'严重',
          风险类型:'流动风险',
        },
        {
          序号:2,
          主体名称:'股票2',
          主体代码:'688002.SH',
          主体类型:'股票',
          行业:'计算机',
          当前预警时刻:'2023/6/29 16:00',
          预警类型:'严重',
          风险类型:'市场风险',
        },
      ],
      tableLabel_main_2: {
        编码: '序号',
        // 名称: '主体名称',
        名称: '主体代码',
        // 主体类型: '主体类型',
        // 行业:'行业',
        监测时间:'预警时刻',
        异常水平:'异常水平',
        异常关联类型:'风险类型',
      },

      //三个表
      tableLabel1: {
        编码: '编号',
        异常关联类型: '异常关联类型',
        名称: '涉及股票',
        监测时间: '监测时间',
        股票价格: '股票价格',
        交易数量: '交易数量',
        风险等级: '风险等级',
      },
      tableLabel2: {
        编码: '编号',
        异常关联类型: '异常关联类型',
        名称: '涉及主体',
        监测时间: '监测时间',
        股票价格: '债券价格',
        交易数量: '交易数量',
        风险等级: '风险等级',
      },
      tableLabel3: {
        编码: '编号',
        异常关联类型: '异常关联类型',
        涉及商品: '涉及商品',
        合约名称: '合约名称',
        监测时间: '监测时间',
        股票价格: '股票价格',
        交易数量: '交易数量',
        风险等级: '风险等级',

      },
      // 弹窗-表格全部数据
      tableData_detail_all_risk_1:[
      {
        序号: 1,
        主体名称: '股票1',
        主体代码: '680001.SH',
        主体类型: '股票',
        省份:'北京',
        行业:'计算机',
        当前预警时刻:'2023/6/29 10:00',
        历史预警时刻:'2023/6/21 16:00',
        预警值:80,
        预警值同比:'+1',
        预警类型:'严重',
        风险类型:'流动风险',
        风险等级:8,
        影响力等级:'高',
        健康等级:'危险',

      },

      ],
      tableLabel_detail_all_1: 
      {
        // 序号: '序号',
        name: '主体名称',
        code: '主体代码',
        // 主体类型: '主体类型',
        province:'省份',
        industry:'行业',
        early_warning_time:'预警时刻',
        last_time:'历史预警时刻',
        warning_score:'预警值',
        increase:'预警值同比',
        // warning_type:'预警类型',
        risk_type:'风险类型',
        warning_type:'风险水平',
        index:'影响力等级',
        健康等级:'健康等级',

      },
      tableData_detail_all_risk_2: [
      {
      name:'秦农商行',
      },
      {  
      name:'华夏商行',
      },
      ],

      // 弹窗-滑动窗数据
      tableData_detail_1_1:[
      {
        序号: 1,
        主体名称: '股票1',
        主体类型: '股票',
        省份:'北京',
        行业:'计算机',
        历史预警时刻:'2023/6/21 16:00',
        当前预警时刻:'2023/6/29 10:00',
        预警值:80,
        预警值同比:'+1',
        预警类型:'严重',
        风险类型:'流动风险',
        风险等级:8,
        影响力等级:'高',
        健康等级:'危险',

      },

      ],
      tableLabel_detail_1: 
      {
        序号: '序号',
        主体名称: '主体名称',
        主体类型: '主体类型',
        省份:'省份',
        行业:'行业',
        历史预警时刻:'历史预警时刻',
        当前预警时刻:'当前预警时刻',
        预警值:'预警值',
        预警值同比:'预警值同比',
        预警类型:'预警类型',
        风险类型:'风险类型',
        风险等级:'风险等级',
        影响力等级:'影响力等级',
        健康等级:'健康等级',

      },
      tableData_detail_1_2: [
      {
      name:'秦农商行',
      },
      {  
      name:'华夏商行',
      },
      ],
      
      tableData_detail_2_1:[
      {
        序号: 1,
        主体名称: '股票1',
        主体类型: '股票',
        省份:'北京',
        行业:'计算机',
        历史预警时刻:'2023/6/21 16:00',
        当前预警时刻:'2023/6/29 10:00',
        预警值:80,
        预警值同比:'+1',
        预警类型:'严重',
        风险类型:'流动风险',
        风险等级:8,
        影响力等级:'高',
        健康等级:'危险',

      },

      ],
      tableLabel_detail_2_1: 
      {
        序号: '序号',
        主体名称: '主体名称',
        主体类型: '主体类型',
        省份:'省份',
        行业:'行业',
        历史预警时刻:'历史预警时刻',
        当前预警时刻:'当前预警时刻',
        预警值:'预警值',
        预警值同比:'预警值同比',
        预警类型:'预警类型',
        风险类型:'风险类型',
        风险等级:'风险等级',
        影响力等级:'影响力等级',
        健康等级:'健康等级',

      },
      tableLabel_detail_2_2: 
      {
        编号: '编号',
        异常主体:'异常主体',
        关联对象:'关联对象',
        异常关联类型:'异常关联类型',
        关联相似度:'关联相似度',
        涉及事件详情:'涉及事件详情',
        高影响力主体分析:'高影响力主体分析',
        风险等级:'风险等级',
      },
      tableData_detail_2_2:[
      {
        编号: '',
        异常主体:'股票1',
        关联对象:'股票2',
        异常关联类型:'高频交易',
        关联相似度:'关联相似度',
        涉及事件详情:'事件分析',
        高影响力主体分析:'高影响力主体分析',
        风险等级:'',
      },

      ],


      // 判断是否弹窗打开
      detailsdialog1:false,
      detailsdialog2:false,
      detailsdialog_all_1:false,
      detailsdialog_all_2:false,

      //预警类型
      warning_type1:'风险预警',
      warning_type2:'异常预警',


    }
 
  },
  mounted(){
    let that=this
    http.get('/warning/get_warning_count/').then((res)=> {
        this.stockLow=res.data["低风险"]
      this.stockMid=res.data["中风险"]
      this.stockHigh=res.data["高风险"]
    })
          this.contentList.length=0
    http.get('/anomaly/item_anomaly/',{params:{
        sc:this.formInline1.market,
      }}).then((res)=>{

      for (let i in res.data.data){
        let tmp={}
        if (that.formInline1.market!=='future')
        {tmp['time']=res.data.data[i].监测时间
        tmp['entity']=res.data.data[i].名称
        tmp['type']=res.data.data[i].异常关联类型}
        else {
          tmp['time']=res.data.data[i].监测时间
          tmp['entity']=res.data.data[i].涉及商品
          tmp['type']=res.data.data[i].异常关联类型
        }
        this.contentList.push(tmp)
      }
      // console.log(this.contentList)
      // console.log(this.listData)
    })
    this.onSubmit1()
  },
  methods:{
// 调整表格列宽
  calculateColumnWidth(prop,data) {
      const text = String(data[0][prop]); // 使用第一行的数据作为示例
      const calculatedWidth = text.length;
      // console.log('console.log(calculatedWidth):',calculatedWidth)
      if(calculatedWidth>10 && calculatedWidth<=50){
        const baseWidth= 20 + calculatedWidth * 0.5
        return `${baseWidth}px`;
      }
      if(calculatedWidth<=10){
        const baseWidth= 15
        return `${baseWidth}px`;
      }
      else{
        const baseWidth= 20 + calculatedWidth * 0.5
        return `${baseWidth}px`;
      }
 },


    onSubmit1(){
      http.get('/anomaly/item_anomaly/',{params:{
          sc:this.formInline1.market,
        }}).then((res)=>{
        this.tableData_main_2=res.data.data
      })
      http.get('/warning/risk_warning/',{params:{
          market: this.formInline1.market,
        }}).then((res)=>{
        this.tableData_main_1=res.data
      })
    },
    // 1、风险/异常单条数据查看详情
    detail1(warning_type){
      if(warning_type==='价格波动异常'){
          this.detailsdialog1 = true//打开弹窗
      }
      if (warning_type==='高频交易异常') {
        this.detailsdialog2 = true//打开弹窗
        
      }
         
    },
     // 2、风险预警-查看全部详情
     detail2(){
       this.$message({
         showClose: true,
         message: '请稍候',
         type: 'info'
       });
       let options={
         text:'请稍等'
       }
       let loadingInstance = Loading.service(options);
       http.get('/warning/risk_warning_detail/',{params:{
           market: this.formInline1.market,
         }}).then((res)=>{
           // unicode?
         this.tableData_detail_all_risk_1=eval(unescape(res.data.replace(/\\u/g, '%u')))

         // this.tableData_detail_all_risk_1=res.data
         loadingInstance.close()
         this.detailsdialog_all_1 = true//打开弹窗
       }).finally(()=>loadingInstance.close())

    },
     // 4、异常预警-查看全部详情
     detail3(){  
      this.detailsdialog_all_2 = true//打开弹窗
    },

    // 1、风险预警-查看风险统计
    statistics1(){
      // 页面跳转
    },
    // 2、异常预警-查看异常统计
    statistics3(){
      // this.detailsdialog3 = true//打开弹窗
    },
   
    // 打开弹窗图像
    open(){
              // this.$nextTick(() => {
              // //  执行echarts方法
              //   this.initEcharts()
              // })
            },
    
  },
  watch:{
    'formInline1.market': {
      handler() {
        this.contentList.length = 0
          http.get('/anomaly/item_anomaly/', {
            params: {
              sc: this.formInline1.market,
            }
          }).then((res) => {
            for (let i in res.data.data) {
              let tmp = {}
              tmp.time = res.data.data[i].监测时间
              tmp.entity = res.data.data[i].名称
              tmp.type = res.data.data[i].异常关联类型
              this.contentList.push(tmp)
      }
    })
    }
  }
  }
}
</script>

<style lang='scss' scoped>
.wrap {
  
  // height: 270px;
  width: 100%;
  margin: 0 auto;
  overflow: hidden;
  ul {
    list-style: none;
    padding: 10px;
    // padding: 0;
    margin: 0 auto;
    li,
    //span {
    //  display: block;
    //  height: 30px;
    //  line-height: 30px;
    //  display: flex;
    //  justify-content: space-between;
    //  font-size: 15px;
    //}
    span {
      display: inline-block;
      height: 30px;
      line-height: 30px;
      display: flex;
      // width: 550px;
      white-space: normal;
      word-break: break-all;
      justify-content: space-between;
      font-size: 15px;
    }
  }
}
.form{//产品搜索栏
    display:flex;
    justify-content:space-between;//左右贴边
    margin-top:5px; 
    margin-bottom:0px; 
    // height: 40px;
    margin-left: 50px;
    padding: 0px;
    .el-form-item {
    margin-bottom: 5px;
    }
  }

.my-element {
  background-image: url('~@/assets/card.png');
  // width:100%;			//大小设置为100%
  // height:100%;			//大小设置为100%
  // position:fixed;
  background-size:100% 100%;
  margin-left: 20px;
  margin-right: 20px;
  margin-top: 20px;



}
.tirCard {
  display:flex;
  justify-content:space-between;
}
.tirCircle{
  display:flex;
  justify-content:space-between;
  margin-left: 20px;
  margin-right: 30px;
  .circle_low {
    background: #dffbee;
    border: 0.7em solid #4dca8e;
    border-radius: 50%;
    // box-shadow: 0.375em 0.375em 0 0 rgba(15, 28, 63, 0.125);
    height: 5em;
    width: 5em;
    // margin-left: 20px;
  }
  .circle_mid {
    background: #fdf6e5;
    border: 0.7em solid #f1c049; 
    border-radius: 50%;
    // box-shadow: 0.375em 0.375em 0 0 rgba(15, 28, 63, 0.125);
    height: 5em;
    width: 5em;

  }
  .circle_high {
    background: #fce0ee;
    border: 0.7em solid #c43434cc;
    border-radius: 50%;
    // box-shadow: 0.375em 0.375em 0 0 rgba(15, 28, 63, 0.125);
    height: 5em;
    width: 5em;
    // margin-right: 20px;
  }
}
.tirText{
  display:flex;
  justify-content:space-between;
  margin-left: 45px;
  margin-right: 60px;
}


.one_twins_card{
    margin-top:0px;
    margin-bottom:10px;
    margin-left: 10px;
    margin-right: 10px;
    display:flex;
    justify-content:space-between;//左右贴边
    .el-card {
      width:49.5%;
    } 
    .el-col-2 {
     width: 2%;

  }
}
.sublabel{ // 小标签标识
    // font-size: 13px;
    // padding:2px;
    margin-top:10px;
    background-color: rgba(2, 167, 240, 0.5);
    width: 5px; 
    height: 35px;

    
  }
.title{
    padding-left: 4px;
    margin-top:15px;
    font-weight: bold;//字体加粗
    display:flex;
    justify-content:flex-start
}
  ::v-deep(.text){
      color:rgba(2, 167, 240, 0.729411764705882);
      margin-top:15px;
      padding: 10px;
      padding-bottom: 5px;
      display:flex;
    // justify-content:right;
    }
  ::v-deep(.text_detail){
      color:rgba(2, 167, 240, 0.729411764705882);
      cursor: pointer;
    // justify-content:right;
    }

  





.table{
  font-size: 12px;
  margin: 2px 10px 2px 10px;//返回表格添加间隙 上 右
  // padding-right:10px;
}
.detail_table{
  margin-top: 15px;
  margin-left: 10px;
  margin-right: 0px;
  ::v-deep(.el-table) {
  width: 98.5% !important;
}
}
  // 右侧空只能这样调整，左侧必须用margin
  ::v-deep(.el-table) {
    width: 97.5% !important;
    // margin-right: 10px;
  }

  // 调整表头间隔、设置表头下方边框颜色
  ::v-deep(.el-table td.el-table__cell, .el-table th.el-table__cell.is-leaf) {
  // border-bottom: 1px solid #333333 !important;
  padding: 1px 1px 1px 1px; 
  min-width: 0;
  }
  // 去除表格cell间隔
  .el-table .el-table__cell {
    padding: 0px 0; 
    min-width: 0;
    // border-color:#333333;

  }
  ::v-deep(.active_header) {//表头
    color: #333333;
    font-size: 13px;
    text-align: center !important;
    // border-color:#333333;

    // height: 1px;
  }
  ::v-deep(.content_center) {//表的内容
    text-align: center !important;
    font-size: 13px;
    // border-color:#333333;
  }



    .grayish_btn{//浅灰色按钮
    color: #fff;//文字颜色
    background-color: #aaaaaa;//背景颜色
  }
</style>
