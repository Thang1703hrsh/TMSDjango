<template >
  <div id="app" class="container-fluid">
    <div class="col-md-2">
      <div class="panel panel-default">
        <div class="panel-body">
          <div>
            <div @node-click="selectNode(material)">
              <app-tabs class="w-11/12 lg:w-11/12 mx-auto mb-16" :tabList="tabList">
                <template v-slot:tabPanel-1> 
                  <div  v-if = "selectedNode" class = "options1 custom-scrollbar">
                    <ul>
                      <li>
                        <b>Mã nguyên phụ liệu</b> <div class = "form-control">{{ selectedNode.name}}</div>  
                        <b>Tên nguyên phụ liệu</b> <div class = "form-control">{{selectedNode.title}} </div>
                        <div class="col-lg-6 col-12" style = "padding-left: 1px">
                          <b>Quy cách</b>  <div class = "form-control">{{selectedNode.specification}} </div>
                        </div> 
                        <div class="col-lg-6 col-12" style = "padding: 0px">
                          <b>Cơ số dự trữ</b>  <div class = "form-control">{{selectedNode.reserve_quantity}} </div>
                        </div>
                        
                        <div class="col-lg-6 col-12" style = "padding-left: 1px">
                          <b>Tồn kho</b>  <div class = "form-control">{{selectedNode.quantity}} </div>
                        </div> 
                        <div class="col-lg-6 col-12" style = "padding: 0px">
                          <b>Đã đặt</b>  <div class = "form-control"> {{selectedNode.ordered_quantity}} </div>
                        </div> 
                        <div class="col-lg-6 col-12" style = "padding-left: 1px">
                          <b>SL cần</b>  <div class = "form-control">{{selectedNode.need_quantity}} </div>
                        </div> 
                        <div class="col-lg-6 col-12" style = "padding: 0px">
                          <b>SL cần theo TC</b>  <div class = "form-control">{{selectedNode.need_for_outsourcing}} </div>
                        </div> 

                        <b>Đã xuất kho GCN</b>  <div class = "form-control">{{selectedNode.outsourcing_stock_out}} </div>

                        <b>Trừ tạm:</b> <div class = "form-control"> {{selectedNode.temporary_quantity}} </div>
                      </li>
                    
                    </ul>
                  </div>
                  <div v-else> 
                    <br><br><br>
                    <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
                    </vue-loading>
                  </div>
                </template>
                <template v-slot:tabPanel-2> 
                  <div v-if = "searchQueryParent" class = "options1 custom-scrollbar">
                    <span v-if = "filteredParent.length == 0"><br> 
                      <svg id = "svgelem" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="52"><path fill="none" d="M0 0h24v24H0z"/>
                        <path d="M3.515 2.1l19.092 19.092-1.415 1.415-2.014-2.015A5.985 5.985 0 0 1 17 21H7A6 6 0 0 1 5.008 9.339a6.992 6.992 0 0 1 .353-2.563L2.1 3.514 
                        3.515 2.1zM7 9c0 .081.002.163.006.243l.07 1.488-1.404.494A4.002 4.002 0 0 0 7 19h10c.186 0 .369-.013.548-.037L7.03 8.445C7.01 
                        8.627 7 8.812 7 9zm5-7a7 7 0 0 1 6.992 7.339 6.003 6.003 0 0 1 3.212 8.65l-1.493-1.493a3.999 3.999 0 0 0-5.207-5.206L14.01 
                        9.795C14.891 9.29 15.911 9 17 9a5 5 0 0 0-7.876-4.09l-1.43-1.43A6.97 6.97 0 0 1 12 2z"/></svg>
                      Không tồn tại NPL<br>
                    </span>
                    <ul>
                      <div 
                        v-for="materialParent in filteredParent" 
                        :key="materialParent.name">
                        <li v-for="(materialParent , index) in materialParent.children" :key = "index">
                          <div class = "dotted"><b><font-awesome-icon icon="fas fa-cogs" /> </b> <b style = "color: #4a90e2;"> {{materialParent.name}} </b></div>
                        </li> 
                      </div>
                    </ul>
                  </div>
                  <div v-else> 
                    <br><br><br>
                    <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
                    </vue-loading>
                  </div>
                </template>
              </app-tabs>
            </div>
          </div>
        </div>
      </div>
      <div class="panel panel-default">
        <div class="panel-body-cons">
          <div>
            <div @node-click="selectNode(material)">
              <app-tabs class="w-11/12 lg:w-11/12 mx-auto mb-16" :tabList="tabListConstitutive">
                <template v-slot:tabPanel-1> 
                  <div  v-if = "selectedNode" class = "options1 custom-scrollbar">
                    <ul>
                      <li>
                        <b>Số nguyên phụ liệu gia công</b> 
                        <div class = "form-control">
                          <div v-if = "allData.length == 0"> 
                            <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
                            </vue-loading>
                          </div>
                          <div v-else @node-click="selectNode(material)">
                            <div v-if = "searchQueryParent">
                                <div style = "text-align: center;" v-if = "filteredParent.length == 0" >
                                  0
                                </div>
                                <div 
                                  v-for="materialParent in filteredParent" 
                                  :key="materialParent.name">
                                  <div style = "text-align: center;">
                                    {{materialParent.children.length}}
                                  </div> 
                                </div>
                              </div>
                          </div>                             
                        </div>  
                        <b>Số nguyên phụ liệu cấu thành</b> 
                        <div class = "form-control">
                          <div v-if = "allData.length == 0"> 
                            <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
                            </vue-loading>
                          </div>
                          <div v-else @node-click="selectNode(material)">
                            <div v-if = "searchQueryChild">
                                <div style = "text-align: center;" v-if = "filteredChild.length == 0" >
                                  0
                                </div>
                                <div 
                                  v-for="material in filteredChild" 
                                  :key="material.name">
                                  <div style = "text-align: center;">
                                    {{material.children.length}}
                                  </div> 
                                </div>
                              </div>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                  <div v-else> 
                    <br><br><br>
                    <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
                    </vue-loading>
                  </div>
                </template>
              </app-tabs>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-md-10">
        <!-- <section class = "dropdown-wrapper"> -->
          <!-- <div @click="isVisible = !isVisible" class="selected-item">
            <svg :fill="'#5386e4'" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
              <path fill="none" d="M0 0h24v24H0z"/><path d="M18.031 16.617l4.283 4.282-1.415 1.415-4.282-4.283A8.96 
              8.96 0 0 1 11 20c-4.968 0-9-4.032-9-9s4.032-9 9-9 9 4.032 9 9a8.96 8.96 0 0 1-1.969 5.617zm-2.006-.742A6.977 
              6.977 0 0 0 18 11c0-3.868-3.133-7-7-7-3.868 0-7 3.132-7 7 0 3.867 3.132 7 7 7a6.977 6.977 0 0 0 4.875-1.975l.15-.15z"/>
            </svg>
            <span v-if = "selectedItem" >{{ selectedItem.name }}</span>
            <span v-else>Tìm nguyên phụ liệu</span>
            
            <svg 
            :class = "isVisible ? 'dropdown' : ''"
            class = "drop-down-icon"
            xmlns="http://www.w3.org/2000/svg" 
            viewBox="0 0 24 24" 
            width="24" 
            height="24">
              <path fill="none" d="M0 0h24v24H0z"/>
              <path d="M12 10.828l-4.95 4.95-1.414-1.414L12 8l6.364 6.364-1.414 1.414z"/>
            </svg>

          </div> -->
          <div class="row search">
            <div class="col-sm-4">
              <div class="pagetitle">
                <h1 align="left">Traceback</h1>
                <nav>
                  <ol class="breadcrumb">
                    <li class="breadcrumb-item active">Traceback</li>
                    <li class="breadcrumb-item"><a href="http://localhost:8080/#/dashboard">Dashboard</a></li>
                  </ol>
                </nav>
              </div>
            </div>
            <div class="col-sm-4"></div>
            <div class="col-sm-4">
              <div class="search-bar">
                <form class="search-form d-flex align-items-center">
                    <input v-if = "filteredChild.length == 0" type="text" placeholder="Nhập mã NPL" title="Enter search keyword">
                    <input v-else type="text" placeholder="Nhập mã NPL" title="Enter search keyword" @keydown.enter="selectItem(material)" v-for="material in filteredChild" 
                  :key="material.name">
                  <button title="Search"><b-icon icon="search"></b-icon></button>
                </form>
              </div>
            </div>
          </div>
            <!-- <div class = "options">
              <ul>
                <li 
                  v-for="material in filteredMat" 
                  :key="material.name">
                </li>
              </ul>
            </div> -->
        <!-- </section> -->

      <div class="row">  
        <div class="col-sm-2 panel panel-row">
            <div class = "b"></div>
          <div style = " padding:5px; "> Tổng số nguyên phụ liệu </div>
          <div v-if = "allData.length == 0"> 
            <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
            </vue-loading>
          </div>
          <div id = "info" v-else> {{allData["total product"]}} </div>
        </div>
        <div class="col-sm-2 panel panel-row ">
          <div class = "b"></div>
          <div style = " padding:5px; "> Số nguyên phụ liệu sơ cấp </div>
          
          <div v-if = "allData.length == 0"> 
            <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
            </vue-loading>
          </div>
          <div id = "info"> {{allData["total product isn't outsouring"]}} </div>
        </div>
        <div class="col-sm-2 panel panel-row">
          <div class = "b"></div>
          <div style = " padding:5px; "> Số nguyên phụ liệu thứ cấp </div>
          
          <div v-if = "allData.length == 0"> 
            <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
            </vue-loading>
          </div>
          <div id = "info"> {{allData["total product is outsouring"]}} </div>
        </div>
        <div class="col-sm-2 panel panel-row">
            <div class = "b"></div>
          <div style = " padding:5px; "> Nguyên phụ liệu đang chọn</div>
          <div v-if = "allData.length == 0"> 
            <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
            </vue-loading>
          </div>
          <div id = "info" v-else> {{selectedNode.name}} </div>
        </div>
        <!-- <div class="col-sm-2 panel panel-row">
            <div class = "b"></div>
          <div style = " padding:5px; "> Nguyên phụ liệu cấu thành </div>
          <div v-if = "allData.length == 0"> 
            <vue-loading type="spiningDubbles" color="black" :size="{ width: '30px', height: '30px' }">
            </vue-loading>
          </div>
          <div id = "info" v-else> a </div>
        </div> -->
      </div>
      <div class="panel panel-default">
        <org-chart 
          :datasource="ds" 
          @node-click="selectNode"
          :pan = "true"
          :activity= "active"
          >
        </org-chart>
      </div>
        <!-- <button @node-click="selectNode"></button> -->
    </div>
  </div>
</template>

<script>
import OrgChart from '../components/OrganizationChartContainer.vue'
import axios from 'axios'
import AppTabs from "../components/Tabs";
import { VueLoading } from 'vue-loading-template'

export default {
  components: {
    OrgChart,
    AppTabs,
    VueLoading,
  },
  data () {
    return {
      active: false,
      tabList: ["Chi tiết NPL", "NPL gia công"],
      tabListConstitutive: ["Cấu thành NPL"],
      treeData: [],
      ds: {
            "name": "4-MICRIN-WHI-D7-30",
            "title": "Đai Microfiber 4 đường 3.0cm White in sub ép lưới màn 80G White úp mí lót gòn - lót giấy 80G White",
            "quantity": 0.0,
            "ordered_quantity": 0.0,
            "need_quantity": 0.0,
            "need_for_outsourcing": 0.0,
            "outsourcing_stock_out": 0.0,
            "temporary_quantity": 0.0,
            "reserve_quantity": 0.0,
            "specification": "3.0cm",
            "children": [
                {
                    "name": "9-MICRIN-WHI-L2-78",
                    "title": "BTP 7.8cm vải Microfiber White in sub ép lưới màn 80G Black",
                    "quantity": 0.0,
                    "ordered_quantity": 0.0,
                    "need_quantity": 0.0,
                    "need_for_outsourcing": 0.0,
                    "outsourcing_stock_out": 0.0,
                    "temporary_quantity": 0.0,
                    "reserve_quantity": 0.0,
                    "specification": "7.8cm",
                    "children": [
                        {
                            "name": "1-MICRIN-WHI-L1-HV",
                            "title": "Vải Microfiber White in sub ép lưới màn 80G White",
                            "quantity": 8.29,
                            "ordered_quantity": 6.5,
                            "need_quantity": 0.0,
                            "need_for_outsourcing": 0.0,
                            "outsourcing_stock_out": 0.0,
                            "temporary_quantity": 14.79,
                            "reserve_quantity": 0.0,
                            "specification": "1.45m",
                            "children": [
                                {
                                    "name": "1-MICRIN-WHI-00-HV",
                                    "title": "Vải Microfiber White in sub",
                                    "quantity": 269.0305,
                                    "ordered_quantity": 1.5,
                                    "need_quantity": 0.0,
                                    "need_for_outsourcing": 74.1266,
                                    "outsourcing_stock_out": 0.0,
                                    "temporary_quantity": 196.4039,
                                    "reserve_quantity": 0.0,
                                    "specification": "1.45m",
                                    "children": [
                                        {
                                            "name": "1-MICRO0-WHI-00-HV",
                                            "title": "Vải Microfiber White",
                                            "quantity": 768.84,
                                            "ordered_quantity": 0.0,
                                            "need_quantity": 0.0,
                                            "need_for_outsourcing": 1.5,
                                            "outsourcing_stock_out": 1.5,
                                            "temporary_quantity": 768.84,
                                            "reserve_quantity": 0.0,
                                            "specification": "1.45m"
                                        }
                                    ]
                                },
                                {
                                    "name": "1-LUOIMA-WHI-80-CM",
                                    "title": "Lưới màn 80G White",
                                    "quantity": 13742.73,
                                    "ordered_quantity": 0.0,
                                    "need_quantity": 4299.46,
                                    "need_for_outsourcing": 15664.290621,
                                    "outsourcing_stock_out": 0.0,
                                    "temporary_quantity": -6221.020621,
                                    "reserve_quantity": 0.0,
                                    "specification": "1.45m"
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "9-GIA80G-WHI-30-TA",
                    "title": "BTP 3.0cm Giấy 80g White",
                    "quantity": 0.0,
                    "ordered_quantity": 0.0,
                    "need_quantity": 0.0,
                    "need_for_outsourcing": 4981.13,
                    "outsourcing_stock_out": 0.0,
                    "temporary_quantity": -4981.13,
                    "reserve_quantity": 0.0,
                    "specification": "3.0cm",
                    "children": [
                        {
                            "name": "9-GIA80G-WHI-00-TQ",
                            "title": "Giấy 80g White",
                            "quantity": 1004.0046,
                            "ordered_quantity": 14.4,
                            "need_quantity": 113.8,
                            "need_for_outsourcing": 1285.706756,
                            "outsourcing_stock_out": 0.0,
                            "temporary_quantity": -381.102156,
                            "reserve_quantity": 0.0,
                            "specification": " "
                        }
                    ]
                },
                {
                    "name": "9-GOLDAI-WHI-30-TA",
                    "title": "BTP 3.0cm Goong lót đai",
                    "quantity": 0.0,
                    "ordered_quantity": 0.0,
                    "need_quantity": 0.0,
                    "need_for_outsourcing": 4498.32,
                    "outsourcing_stock_out": 0.0,
                    "temporary_quantity": -4498.32,
                    "reserve_quantity": 0.0,
                    "specification": "3.0cm",
                    "children": [
                        {
                            "name": "1-GOLDAI-WHI-00-EP",
                            "title": "Goong lót đai (Gòng 2SRVHNP màu trắng 100g/m2 khổ 60\")",
                            "quantity": 695.3951,
                            "ordered_quantity": 0.0,
                            "need_quantity": 91.51,
                            "need_for_outsourcing": 169.614934,
                            "outsourcing_stock_out": 25.0,
                            "temporary_quantity": 459.270166,
                            "reserve_quantity": 0.0,
                            "specification": "1.45M"
                        }
                    ]
                }
            ]
        },
      searchQuery: "",
      searchQueryParent: "",
      searchQueryChild: "",
      selectedItem: null ,
      selectedNode: null,
      parentNode: [],
      isVisible: true,
      parentData: [],
      allData: [],
      allTraceback: [],
    }
  },
  mounted() {
    this.getOutsourcingProductMaterials()
    this.getParent()
  },
  methods: {
    getOutsourcingProductMaterials() {
      axios
        .get('/api/v1/outsourcing_product/')
        .then(response => {
          this.treeData = response.data["children"];
          this.allData = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    getParent() {
      axios
        .get('/api/v1/outsourcing_product_materials/')
        .then(response => {
          this.parentData = response.data["children"];
          this.allTraceback = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    reRender(){
        this.$forceUpdate()
    },

    selectItem(material){
      console.log(1)
      this.active = false; 
      this.selectedItem = material;
      this.ds = material;
      console.log(material)
      this.isVisible = false;
      
      // this.$forceUpdate();
      
    },
    selectNode (material){
      this.selectedNode = material;
      this.active = true; 
      this.searchQueryParent = material.name;
      this.searchQueryChild = material.name;
      console.log(this.searchQueryParent)
    },
    showParent(materialParent){
      this.parentNode = materialParent
    }
  },
  computed: {
    filteredMat() {
      const query = this.searchQuery.toLowerCase();
      if(this.searchQuery == "") { 
        return this.treeData;
      }
      return this.treeData.filter((material) => {
        return Object.values(material).some((word) => 
          String(word).toLowerCase().includes(query)
        );
      });
    },
    filteredMaterial() {
      const query = this.searchQuery.toLowerCase();
      if(this.searchQuery == "") { 
        return this.treeData;
      }
      return this.treeData.filter((material) => {
        return Object.values(material).some((word) => 
          String(word).includes(query)
        );
      });
    },
    filteredParent() {
      const query = this.searchQueryParent;
      if(this.searchQueryParent == "") { 
        return this.parentData;
      }
      return this.parentData.filter((material) => {
        return Object.values(material).some((word) => 
          String(word).includes(query)
        );
      });
    },
    filteredChild() {
      const query = this.searchQueryChild;
      if(this.searchQueryChild == "") { 
        return this.treeData;
      }
      return this.treeData.filter((material) => {
        return Object.values(material).some((word) => 
          String(word).includes(query)
        );
      });
    },
  },
}
</script>

<style>
#app {
  font-family: "Roboto",sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 00px;
}

.input-icons input{
  width: 100%;
  margin-bottom: 10px;
  padding: 0px 38px 0px 10px;
}

.icon {
  padding: 10px;
  min-width: 40px;
}

.input-field {
  width: 100%;
  padding: 10px;
  text-align: center;
}

#svgelem {
   margin-left:auto;
   margin-right:auto;
   display:block;
}

#info {
  font-size: 16px;
  font-weight: bold;
}

</style>

<style scoped lang = "scss">

.search-bar {
  min-width: 360px;
  padding: 0 0px;
}



.search-filter {
  height: 40px
}

.search-filter {
  height: 40px
}


.search-form {
  width: 100%;
  input {
    border: 0;
    font-size: 14px;
    color: #012970;
    border: 1px solid rgba(38, 105, 219, 0.2);
    padding: 7px 38px 7px 8px;
    border-radius: 10px;
    transition: 0.3s;
    width: 100%;
  }
  button {
    border: 0;
    padding: 0;
    margin-left: -30px;
    background: none;
    b-icon {
      border: 0;
      padding: 0;
      margin-left: -30px;
      background: none;
      color: #012970;
    }
  }
}

.pagetitle {
  margin-bottom: 10px;
}

.pagetitle h1 {
  font-size: 20px;
  margin-bottom: 0;
  font-weight: 500;
  color: #000000;
  letter-spacing: 0.3px;
}

.breadcrumb {
  text-align: left;
  letter-spacing: 0.3px;
  font-size: 14px;
  color: #000000;
  font-weight: bold;
  margin: 0px;
  padding: 0px ;
  height: 0px;
}

.breadcrumb a {
  color: #b5c0d6;
  transition: 0.3s;
}

.breadcrumb a:hover {
  color: #51678f;
}

.breadcrumb .breadcrumb-item::before {
  color: #899bbd;
}

.breadcrumb .active {
  color: #51678f;
  font-weight: 600;
}


#add{
  text-align: center; 
  width: 100%;
  height: 35px;
  margin: 0 auto;
  border:1px solid #0096C7;
  border-radius: 10px;
}

.center_dashboard{
  display: flex;
  justify-content: center;
  width: 100%;
  height: 35px;
  margin: 0 auto;
  border:1px solid #0096C7;
  border-radius: 10px;
}

.dotted{
  &:hover{
    text-decoration: underline 2px;
    color: #0096C7;
  }
}
.b {
  position: absolute;
  left: auto;
  height: 100%;
  width: 8px;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  background: #5386e4;
}

.hr { 
  width:100%;
  height: 2px; 
  background: linear-gradient(to top, #5386e4 100%, #6499f5 100%);
  overflow: auto;
}

.panel-body {
/* height: 480px; */
height: 580px;
overflow-y: auto; 
padding: 0px;
margin-bottom: 0px;
margin-top: 0px;

}


.panel-body-cons {
/* height: 480px; */
height: 262px;
overflow-y: auto; 
padding: 0px
}
.col-md-10 {
padding: 0px;
width: calc(100% - 380px);
margin-top: -8px; 

}

.row_search{
  padding: 0px 0px 0px 0px;
  margin: -10px 0px 0px -10px ;
  border: 1px solid black;
}

.row{
  padding: 0px 0px 0px 0px;
  margin: 5px 0px 0px -10px ;
}
.search{
  padding: 0px 0px 0px 0px;
  margin-top: 0px;
}

.form-group {
height: 100%
}

.col-md-2 {
width: 380px;
padding-left: 0px; 
margin-top: -8px; 

}

.button {
  background-color: #4CAF50; /* Green */
  border: 2px;
  color: rgb(255, 0, 0);
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

.panel-default {
border-radius: 10px;
border-width: 0.5px;
border-style: solid;
padding: 0px 0px;
margin-bottom: 10px;
}

.panel-row {
  border-radius: 10px;
  border-color: #d8d8d8;
  border-width: 0.5px;
  border-style: solid;
  margin: 5px 0px 10px 10px;
  padding: 0px;
  background: linear-gradient(to top, #e3ecff 0%, #bccff3 100%);
  // background:  #e3ecff ;
}

.col-sm-2 {
  width: calc((100% - 50px) / 4);
  height: 70px;
  margin: 10px 20px calc(40px/3px) 0px ;
  // background: linear-gradient(to right, #7f7fd5, #86a8e7, #91eae4);
}

.panel-heading {
height: 40px;
border-radius: 10px;
border-width: 0.5px;
border-style: solid;
font-size: 16px;
}

.noteBoxes
{
	border: 1px solid;
  border-radius: 5px;
	padding: 10px;
	margin: 10px 0;
	width: 300px;
  border-color: #0096C7;
	background-color: rgba(0, 150, 199, 0.1); 
}

.borderinf {
  border: 10px;
}

.form-control {
  font-size: 15px;
  padding: 0.375rem 0.875rem;
  background-color: rgba(38, 125, 207, 0.151); 
  background-clip: padding-box;
  border: 1px solid #dbe5ee;
  border-radius: 0.25rem;
  height: 100%;
  min-height: 30.74px;
  box-shadow: inset 0 1px 2px 0 rgba(8, 23, 136, 0.12);
  margin: 0px 10px 10px 0px ;
}

.form-control-tab {
  font-size: 15px;
  background-color: rgba(38, 125, 207, 0.151); 
  background-clip: padding-box;
  border: 1px solid #dbe5ee;
  border-radius: 5px;
  box-shadow: inset 0 1px 2px 0 rgba(8, 23, 136, 0.12);
}

.controlwidth {
  width: 50%
}


/* custom scrollbar */
::-webkit-scrollbar {
  width: 0px;
}

::-webkit-scrollbar-track {
  background-color: transparent;
}

::-webkit-scrollbar-thumb {
  background-color: #d6dee1;
  border-radius: 20px;
  border: 6px solid transparent;
  background-clip: content-box;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #a8bbbf;
}

.options1{
  font-family: "Roboto",sans-serif;
  width: 100%;

  span{
    font-size: 16px;
    font-weight: bold;
  }
  ul{
    border-radius: 5px;
    list-style: none;
    text-align: left;
    padding-left: 0px;
    height: 100%;
    li {
      font-size: 15px;
      border: 1px solid;
      border-radius: 5px;
      padding: 10px;
      width: 100%;
      border-color: #0096C7;
      background-color: rgba(255, 255, 255, 0.1); 
      box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.3);
      margin: 0px 8px 8px 0px;

    }
  }
}

.selected-node {
  height: 40px;
  border: 0px solid rgb(255, 255, 255);
  border-radius: 5px;
  padding: 5px 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 16px;
  font-weight: 400;
}
.dropdown-wrapper {
  max-width: 100%;
  position: relative;
  margin: 0 auto;
  

  .selected-item {
  height: 35px;
  // border: 0px solid rgb(255, 255, 255);
  border-radius: 5px;
  border-color: #0096C7;
  padding: 5px 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 16px;
  font-weight: 400;

  .drop-down-icon{
    transform: rotate(0deg);
    transition: all 0.5s ease;
    &.dropdown {
      transform: rotate(180deg);
      transition: all 0.5s ease;
    }
  }
}

  .dropdown-popover{
    position: absolute;
    border: 1px solid lightgray;
    border-radius: 10px;
    top: 50px;
    left: 0;
    right: 0;
    background-color: #fff;
    max-width: 100%;
    padding: 10px;
    visibility : hidden;
    transition: all .5s linear;
    max-height:  0px;
    overflow: hidden;

    &.visible{
      max-height: 183px;
      visibility: visible;
    }

    input {
      width: 90%;
      height: 40px;
      border: 2px solid lightgray;
      font-size: 16px;
      padding-left: center;
    }
    .options{
      width: 100%;
      height: 80%;
      ul{
        border-radius: 5px;
        list-style: none;
        text-align: left;
        padding-left: 0px;
        height: 126px;
        overflow-y: scroll;
        overflow-x: hidden;
        

        li {
          font-size: 15px;
          // padding: 0.375rem 0.875rem;
          background-color: rgba(38, 125, 207, 0.151); 
          background-clip: padding-box;
          // border: 1px solid #dbe5ee;
          // border-radius: 0.25rem;
          // height: 80%;
          box-shadow: inset 0 1px 2px 0 rgba(8, 23, 136, 0.12);
          // margin: 0px 10px 10px 0px ;

          border-radius: 5px;
          width: 100%;
          border-bottom: 1px solid rgb(136, 136, 136);
          padding: 8px;
          // background-color:  #f1f1f1;
          cursor: pointer;
          // font-size: 16px;
          &:hover{
            background-color: #6499f5;
            color: #fff;
            font-weight: bold;

          }
        }
      }
    }
    
  }
}
</style>