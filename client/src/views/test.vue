<template >
  <div id="app" class="container-fluid">
    <div class="col-md-2">
      <div class="panel panel-default">
        <div class="panel-heading">Thông tin nguyên phụ liệu</div>
        <div class="panel-body">
          <div class="form-group">
            <div @node-click="selectNode(material)">
              <div  v-if = "selectedNode" class = "options1">
                <ul>
                  <li>
                    <b>Mã NPL:</b> {{ selectedNode.name}} <br>
                  </li>
                  <li>
                    <b>Tên NPL:</b> {{selectedNode.title}} <br>
                  </li>
                  <li>
                    <b>Tồn kho:</b> {{selectedNode.quantity}}
                  </li>
                  <li>
                    <b>Đã đặt:</b> {{selectedNode.ordered_quantity}}
                  </li>
                  <li>
                    <b>SL cần:</b> {{selectedNode.need_quantity}}
                  </li>
                  <li>
                    <b>SL cần theo TC:</b> {{selectedNode.need_for_outsourcing}}
                  </li>
                  <li>
                    <b>Đã xuất kho GCN:</b> {{selectedNode.outsourcing_stock_out}}
                  </li>

                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="panel panel-default">
        <section class = "dropdown-wrapper">
          <div @click="isVisible = !isVisible" class="selected-item">
            <!-- <span v-if = "selectedItem" >{{ selectedItem.name }}</span> -->
            <input v-model = "searchQuery" type = "text" placeholder="Tìm nguyên phụ liệu">
            <!-- <span v-else>Tìm nguyên phụ liệu</span> -->
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
            <!-- <input id = 'add' v-model = "searchQuery" type = "text" placeholder="Nhập mã NPL"> -->
            <span v-if = "filteredMat.length == 0"><br><br>No Data Available<br></span>
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
      <div class="col-md-10 panel panel-default">
        <org-chart 
          :datasource="ds" 
          @node-click="selectNode"
          :pan = "true"
          :zoom = "true"
          :zoomin-limit = "1"
          :zoomout-limit = "0.5"
          >
        </org-chart>
      </div>
    </div>
</template>

<script>
import OrgChart from '../components/OrganizationChartContainer.vue'
import axios from 'axios'

export default {
  components: {
    OrgChart
  },
  data () {
    return {
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
      selectedItem: null ,
      selectedNode: null,
      isVisible: false,
    }
  },
  mounted() {
    this.getOutsourcingProductMaterials()
  },
  methods: {
    getOutsourcingProductMaterials() {
      axios
        .get('/api/v1/outsourcing_product_materials/')
        .then(response => {
          this.treeData = response.data['children'];
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
    },
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
height: 460px;
overflow-y: auto; 
}
.col-md-10 {
border-radius: 15px;
border-width: 0.5px;
border-style: solid;
}
.panel-default {
border-radius: 15px;
border-width: 0.5px;
border-style: solid;
}

.panel-heading {
border-radius: 15px;
border-width: 0.5px;
border-style: solid;
font-size: 16px;
}

.options1{
  width: 100%;
  ul{
    border-radius: 10px;
    list-style: none;
    text-align: left;
    padding-left: 0px;
    max-height: 300px;

    li {
      color: #333333;
      border: 1px solid  #b8b8b8;
      background-color: #dddddd;
      line-height: 20px;
      width: 100%;
      box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.3);
      
      margin: 0 6px 6px 0;
      border-radius: 10px;
      width: 100%;
      padding: 10px;
      background-color:  #f1f1f1;
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
      max-height: 400px;
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
        max-height: 180px;
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