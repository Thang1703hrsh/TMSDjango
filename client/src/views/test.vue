<template>
  <div id="app" class="container-fluid">
    <div class="col-md-3">
      <div class="panel panel-default">
        <div class="panel-heading">Props</div>

        <div class="panel-body"></div>
          <div class="form-horizontal">


          <div class="form-group">
            <label for="layout-type" class="control-label col-sm-3">Layout</label>
              <div  class="col-sm-9">
                <select name="layout" class="form-control" id="layout" v-model="layout">
                  <option value="horizontal">Horizontal</option>
                  <option value="vertical">Vertical</option>
                  <option value="circular">Circular</option>
                </select>
            </div>
          </div> 

          <div class="form-group">
            <label for="type" class="control-label col-sm-3">Type</label>
              <div  class="col-sm-9">
                <select id="type" class="form-control" v-model="type">
                  <option value="tree">Tree</option>
                  <option value="cluster">Cluster</option>
                </select>
              </div>
          </div>


          <div class="form-group">
            <label for="layout-type" class="control-label col-sm-3">Link layout</label>
              <div  class="col-sm-9">
                <select id="layout-type" class="form-control" v-model="linkLayout">
                  <option value="bezier">Bezier</option>
                  <option value="orthogonal">Orthogonal</option>
                </select>
            </div>
          </div>

          <div class="form-group">
            <label for="margin-x" class="control-label col-sm-3">Margin X</label>
            <div class="col-sm-7">
              <input id="margin-x" class="form-control" type="range" min="0" max="200" v-model.number="marginX">
            </div> 
              <div class="col-sm-2">
                <p>{{marginX}}px</p>
            </div>
          </div>  

          <div class="form-group">
            <label for="margin-y" class="control-label col-sm-3">Margin Y</label>
            <div class="col-sm-7">
              <input id="margin-y" class="form-control" type="range" min="0" max="200" v-model.number="marginY">
            </div>
            <div class="col-sm-2">
              <p>{{marginY}}px</p>
            </div>
          </div>

          <div class="form-group">
            <label for="node-text-margin" class="control-label col-sm-3">Text Margin</label>
            <div class="col-sm-7">
              <input id="node-text-margin" class="form-control" type="range" min="0" max="100" v-model.number="nodeTextMargin">
            </div>
            <div class="col-sm-2">
              <p>{{nodeTextMargin}}px</p>
            </div>
          </div>

          <p class="mt-2">
            <button
              class="mt-3 focus:outline-none w-64 py-2 rounded-md font-semibold text-white bg-indigo-500 ring-4 ring-indigo-300"
              @click="resetZoom"
            >
              Reset zoom
            </button>
          </p>
          <p class="mt-2">
            <button
              class="mt-3 focus:outline-none w-64 py-2 rounded-md font-semibold text-white bg-green-500 ring-4 ring-green-300"
              @click="downloadImage"
            >
              Download image
            </button>
          </p>
        </div>
      </div>

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
      <tree
      :data= prod
      ref="tree"
      v-model="currentData"
      class="tree"
      :nodeTextDisplay="nodeTextDisplay"
      :nodeTextMargin="nodeTextMargin"
      :zoomable="zoomable"
      :leafTextMargin="leafTextMargin"
      :node-text="nodeText"
      :margin-x="marginX"
      :margin-y="marginY"
      :radius="radius"
      :layoutType="layout"
      :type="type"
      :duration="duration"
      :minZoom="minZoom"
      :maxZoom="maxZoom"
      :linkLayout="linkLayout"
      contextMenuPlacement="bottom-start"
      ></tree>
  </div>
  </div>
</template>

<script>
import { tree } from "vued3tree";
import d3ToPng from "d3-svg-to-png";
// import json_data from "@/assets/data/tree.json";

import axios from 'axios'


export default {
  name: "App",
  components: { tree
  },
  data: function() {
    return {
      treeData: [],
      type: "tree",
      layout: "horizontal",
      duration: 750,
      maxMargin: 200,
      marginX: 130,
      marginY: 100,
      radius: 7,
      leafTextMargin: 6,
      nodeTextMargin: 10,
      nodeText: "name",
      currentData: null,
      zoomable: true,
      isLoading: false,
      nodeTextDisplay: "all",
      linkLayout: "bezier",
      minZoom: 0.1,
      maxZoom: 9,
      events: [],
      searchQuery: "",
      selectedItem: null ,
      isVisible: false,
      prod: null ,
    };
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
      this.prod = material;
      console.log(material)
      this.isVisible = false;
      // this.$forceUpdate();
      
    },
    resetZoom() {
      if (!this.$refs["tree"]) {
        return;
      }
      this.isLoading = true;
      this.$refs["tree"].resetZoom().then(() => {
        this.isLoading = false;
      });
    },
    downloadImage() {
      d3ToPng("svg", "name.png", {
        scale: 3,
        format: "png",
        quality: 1,
      });
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
};
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 20px;
  }
  .tree {
    height: 950px;
  }
  .graph-root {
    height: 1000px;
    width: 100%;
  }
  .feedback{
    height: 60px;
    line-height: 50px;
    vertical-align: middle;
  }
  .log  {
    height: 200px;
    overflow-x: auto;
    overflow-y: auto;
    overflow: auto;
    text-align: left;
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