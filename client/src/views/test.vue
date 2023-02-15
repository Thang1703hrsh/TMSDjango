<template >
  <div id="app" class="container-fluid">
    <div class="col-md-2">
      <div class="panel panel-default">
        <div class="panel-body">
          <div>
            <div @node-click="selectNode(material)">
              <app-tabs class="w-11/12 lg:w-11/12 mx-auto mb-16" :tabList="tabList">
                <template v-slot:tabPanel-1> 
                  <div  v-if = "selectedNode" class = "options1">
                    <ul>
                      <li>
                        <b><u class = "dotted">Mã NPL:</u></b> <br> {{ selectedNode.name}}
                      </li>
                      <li>
                        <b><u class = "dotted">Tên NPL:</u></b> <br> {{selectedNode.title}} <br>
                      </li>
                      <li>
                        <b><u class = "dotted">Tồn kho:</u></b> {{selectedNode.quantity}}
                      </li>
                      <li>
                        <b><u class = "dotted">Đã đặt:</u></b> {{selectedNode.ordered_quantity}}
                      </li>
                      <li>
                        <b><u class = "dotted">SL cần:</u></b> {{selectedNode.need_quantity}}
                      </li>
                      <li>
                        <b><u class = "dotted">SL cần theo TC:</u></b> {{selectedNode.need_for_outsourcing}}
                      </li>
                      <li>
                        <b><u class = "dotted">Đã xuất kho GCN:</u></b> {{selectedNode.outsourcing_stock_out}}
                      </li>

                    </ul>
                  </div>
                </template>
                <template v-slot:tabPanel-2> 
                  <div v-if = "searchQueryParent" class = "options1">
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
                          <b><u class = "dotted">Mã NPL:</u></b> {{materialParent.name}}
                        </li> 
                      </div>
                    </ul>
                  </div>
                </template>
              </app-tabs>
            </div>
          </div>
        </div>
      </div>

      <div class="panel panel-default">
        <section class = "dropdown-wrapper">
          <div @click="isVisible = !isVisible" class="selected-item">
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

          </div>
          <!-- <div v-if="isVisible" class="dropdown-popover"> -->
          <div :class="isVisible ? 'visible' : 'invisible'" class="dropdown-popover">
            <input id = 'add' v-model = "searchQuery" type = "text" placeholder="Nhập mã NPL">
            <span v-if = "filteredMat.length == 0"><br><br>Không tồn tại NPL<br></span>
            <div class = "options">
              <ul>
                <li 
                  @click="selectItem(material)" 
                  v-for="material in filteredMat" 
                  :key="material.name">
                    {{material.name}}
                </li>
              </ul>
            </div>
          </div>
        </section>
      </div>
    </div>
      <div class="col-md-10">
        <div class="panel panel-default">
          <org-chart 
            :datasource="ds" 
            @node-click="selectNode"
            :pan = "true"
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

export default {
  components: {
    OrgChart,
    AppTabs
  },
  data () {
    return {
      tabList: ["Chi tiết NPL", "NPL gia công"],
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
                                    "children": [
                                        {
                                            "name": "1-MICRO0-WHI-00-HV",
                                            "title": "Vải Microfiber White",
                                            "quantity": 768.84,
                                            "ordered_quantity": 0.0,
                                            "need_quantity": 0.0,
                                            "need_for_outsourcing": 1.5,
                                            "outsourcing_stock_out": 1.5,
                                            "temporary_quantity": 768.84
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
                                    "temporary_quantity": -6221.020621
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
                    "children": [
                        {
                            "name": "9-GIA80G-WHI-00-TQ",
                            "title": "Giấy 80g White",
                            "quantity": 1004.0046,
                            "ordered_quantity": 14.4,
                            "need_quantity": 113.8,
                            "need_for_outsourcing": 1285.706756,
                            "outsourcing_stock_out": 0.0,
                            "temporary_quantity": -381.102156
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
                    "children": [
                        {
                            "name": "1-GOLDAI-WHI-00-EP",
                            "title": "Goong lót đai (Gòng 2SRVHNP màu trắng 100g/m2 khổ 60\")",
                            "quantity": 695.3951,
                            "ordered_quantity": 0.0,
                            "need_quantity": 91.51,
                            "need_for_outsourcing": 169.614934,
                            "outsourcing_stock_out": 25.0,
                            "temporary_quantity": 459.270166
                        }
                    ]
                }
            ]
        },
      searchQuery: "",
      searchQueryParent: "",
      selectedItem: null ,
      selectedNode: null,
      parentNode: [],
      isVisible: true,
      parentData: [],
    }
  },
  mounted() {
    this.getOutsourcingProductMaterials()
    this.getParent()
  },
  methods: {
    getOutsourcingProductMaterials() {
      axios
        .get('/api/v1/outsourcing_product_materials/')
        .then(response => {
          this.treeData = response.data;
        })
        .catch(error => {
          console.log(error)
        })
    },
    getParent() {
      axios
        .get('/api/v1/outsourcing_product/')
        .then(response => {
          this.parentData = response.data;
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
      this.selectedItem = material;
      this.ds = material;
      console.log(material)
      this.isVisible = false;
      // this.$forceUpdate();
      
    },
    selectNode (material){
      this.selectedNode = material;
      this.searchQueryParent = material.name;
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
    
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 00px;
}

#add{
      text-align: center; 
      width: 100%;
      height: 35px;
      margin: 0 auto;
      border: none;
      border:solid 1px #ccc;
      border-radius: 10px;
    }

</style>

<style scoped lang = "scss">

.panel-body {
/* height: 480px; */
height: 580px;
overflow-y: auto; 
padding: 0px
}
.col-md-10 {
width: calc(100% - 380px);
padding: 0px;
}

.form-group {
height: 100%
}


.col-md-2 {
width: 380px;
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
border-radius: 15px;
border-width: 0.5px;
border-style: solid;
padding: 0px 0px;
}

.panel-heading {
height: 40px;
border-radius: 15px;
border-width: 0.5px;
border-style: solid;
font-size: 16px;
}

.dotted{
  border-bottom: 1px dashed #999;
  text-decoration: none; 
}

.focus {
  background: rgb(255, 0, 0);
}

#svgelem {
   margin-left:auto;
   margin-right:auto;
   display:block;
}

.options1{
  width: 100%;

  span{
    font-size: 20px;
    font-weight: bold;
  }
  ul{
    border-radius: 10px;
    list-style: none;
    text-align: left;
    padding-left: 0px;
    height: 100%;

    li {
      color: #333333;
      border: 1px solid  #b8b8b8;
      background-color: rgb(238, 238, 238);
      line-height: 20px;
      width: 100%;
      box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.3);
      margin: 0 12px 12px 0;
      border-radius: 10px;
      width: 100%;
      padding: 10px;
      cursor: pointer;
      font-size: 16px;
      &:hover{
        background-color: #6499f5;
        color: #fff;
      }
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
  height: 40px;
  border: 0px solid rgb(255, 255, 255);
  border-radius: 5px;
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
    border: 2px solid lightgray;
    border-radius: 15px;
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
      max-height: 175px;
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
      ul{
        border-radius: 10px;
        list-style: none;
        text-align: left;
        padding-left: 0px;
        max-height: 150px;
        overflow-y: scroll;
        overflow-x: hidden;

        li {
          border-radius: 10px;
          width: 100%;
          border-bottom: 1px solid lightgray;
          padding: 8px;
          background-color:  #f1f1f1;
          cursor: pointer;
          font-size: 16px;
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