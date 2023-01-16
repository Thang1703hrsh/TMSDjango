<template>
    <div id="app" class="container-fluid">
      <div class="col-md-3">
  
        <div class="panel panel-default">
          <section class = "dropdown-wrapper">
            <div @click="isVisible = !isVisible" class="selected-item">
              <span v-if = "selectedItem" >{{ selectedItem.name }}</span>
              <span v-else>Select Material</span>
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
              <input v-model = "searchQuery" type = "text" placeholder="Search for Material">
              <span v-if = "filteredMat.length == 0"><br>No Data Available<br></span>
              <div class = "options">
                <ul>
                  <li 
                    v-on:click="selectItem(material)" 
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
        <div class="col-md-9 panel panel-default">
          <org-chart 
            :datasource="ds" 
            @node-click="selectNode">
          </org-chart>
        </div>
      </div>
  </template>
  
  <script>
  import OrgChart from './components/OrganizationChartContainer.vue'
  import axios from 'axios'
  
  export default {
    name: 'app',
    components: {
      OrgChart
    },
    data () {
      return {
        treeData: [],
        ds: {
          "name": "4-MICRIN-WHI-D7-30",
          "title": "Đai Microfiber 4 đường 3.0cm White in sub ép lưới màn 80G White úp mí lót gòn - lót giấy 80G White",
          "children": [
              {
                  "name": "9-MICRIN-WHI-L2-78",
                  "title": "BTP 7.8cm vải Microfiber White in sub ép lưới màn 80G Black",
                  "children": [
                      {
                          "name": "1-MICRIN-WHI-L1-HV",
                          "title": "Vải Microfiber White in sub ép lưới màn 80G White",
                          "children": [
                              {
                                  "name": "1-MICRIN-WHI-00-HV",
                                  "title": "Vải Microfiber White in sub",
                                  "children": [
                                      {
                                          "name": "1-MICRO0-WHI-00-HV",
                                          "title": "Vải Microfiber White"
                                      }
                                  ]
                              },
                              {
                                  "name": "1-LUOIMA-WHI-80-CM",
                                  "title": "Lưới màn 80G White"
                              }
                          ]
                      }
                  ]
              },
              {
                  "name": "9-GIA80G-WHI-30-TA",
                  "title": "BTP 3.0cm Giấy 80g White",
                  "children": [
                      {
                          "name": "9-GIA80G-WHI-00-TQ",
                          "title": "Giấy 80g White"
                      }
                  ]
              },
              {
                  "name": "9-GOLDAI-WHI-30-TA",
                  "title": "BTP 3.0cm Goong lót đai",
                  "children": [
                      {
                          "name": "1-GOLDAI-WHI-00-EP",
                          "title": "Goong lót đai (Gòng 2SRVHNP màu trắng 100g/m2 khổ 60\")"
                      }
                  ]
              }
          ]
      }, 
        searchQuery: "",
        selectedItem: null ,
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
            this.treeData = response.data
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
  
    // methods: {
    //   selectNode (nodeData) {
    //     alert('node ' + nodeData.name + ' is selected')
    //   }
    // }
  }
  </script>
  
  <style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  </style>
  
  <style scoped lang = "scss">
  .dropdown-wrapper {
    max-width: 100%;
    position: relative;
    margin: 0 auto;
  
    .selected-item {
    height: 40px;
    border: 2px solid lightgray;
    border-radius: 5px;
    padding: 5px 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 18px;
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
        max-height: 450px;
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
        width: 95%;
        ul{
          list-style: none;
          text-align: left;
          padding-left: 21px;
          max-height: 300px;
          overflow-y: scroll;
          overflow-x: hidden;
  
          li {
            width: 100%;
            border-bottom: 1px solid lightgray;
            padding: 10px;
            background-color:  #f1f1f1;
            cursor: pointer;
            font-size: 16px;
            &:hover{
              background-color: #70878a;
              color: #fff;
              font-weight: bold;
  
            }
          }
        }
      }
    }
  }
  </style>
  
  