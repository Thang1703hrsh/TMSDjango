<template>
    <a-card :bordered="false" class="dashboard-bar-chart">
        <org-chart 
          :datasource="ds" 
          @node-click="selectNode">
        </org-chart>
    </a-card>
</template>

<script>
import OrgChart from './components/OrganizationChartContainer.vue'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    OrgChart,
  },
  data () {
    return {
      treeData: [],
      ds: null , 
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

