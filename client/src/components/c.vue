<template>
  <a-card :bordered="false" class="dashboard-bar-chart">
  <div v-bind="{ scopedSlots: $scopedSlots }"
    @wheel="zoom && zoomHandler($event)"
    @mouseup="pan && panning && panEndHandler($event)"
  >
  <div class="titlechart" align="left">Cây cấu trúc nguyên phụ liệu</div> <hr />
    <div
      class="orgchart"
      :style="{ transform: transformVal, cursor: cursorVal }"
      @mousedown="pan && panStartHandler($event)"
      @mousemove="pan && panning && panHandler($event)"

    >
      <organization-chart-node 
        :datasource="datasource" 
        :handle-click="handleClick" 
        >
        <template v-for="slot in Object.keys($scopedSlots)" 
                  :slot="slot" slot-scope="scope">
          <slot :name="slot" v-bind="scope"/>
        </template>
      </organization-chart-node>
    </div>
  </div>
</a-card>
</template>

<script>
import $ from 'jquery'
import OrganizationChartNode from './OrganizationChartNode.vue'
export default {
  name: 'Container',
  props: {
    datasource: {
      type: Object,
      required: true
    },
    pan: {
      type: Boolean,
      required: false
    },
    zoom: {
      type: Boolean,
      required: false
    },
    zoomoutLimit: {
      type: Number,
      required: false,
      default: 0.5
    },
    zoominLimit: {
      type: Number,
      required: false,
      default: 7
    }
  },
  data () {
    return {
      cursorVal: 'default',
      panning: false,
      startX: 0,
      startY: 0,
      transformVal: ''
    }
  },
  components: {
    OrganizationChartNode
  },
  methods: {
    handleClick (nodeData) {
      this.$emit('node-click', nodeData);
    },
    panEndHandler () {
      this.panning = false
      this.cursorVal = 'default'
    },
    panHandler (e) {
        let newX = 0
        let newY = 0
        if (!e.targetTouches) { // pand on desktop
          newX = e.pageX - this.startX
          newY = e.pageY - this.startY
        } else if (e.targetTouches.length === 1) { // pan on mobile device
          newX = e.targetTouches[0].pageX - this.startX
          newY = e.targetTouches[0].pageY - this.startY
        } else if (e.targetTouches.length > 1) {
          return;
        }
        if (this.transformVal === '') {
          if (this.transformVal.indexOf('3d') === -1) {
            this.transformVal = 'matrix(1,0,0,1,' + newX + ',' + newY + ')'
          } else {
            this.transformVal = 'matrix3d(1,0,0,0,0,1,0,0,0,0,1,0,' + newX + ', ' + newY + ',0,1)'
          }
        } else {
          let matrix = this.transformVal.split(',')
          if (this.transformVal.indexOf('3d') === -1) {
            matrix[4] = newX
            matrix[5] = newY + ')'
          } else {
            matrix[12] = newX
            matrix[13] = newY
          }
          this.transformVal = matrix.join(',')
        }
    },
    panStartHandler (e) {
      if ($(e.target).closest('.node').length) {
        this.panning = false
        return
      } else {
        this.cursorVal = 'move'
        this.panning = true
      }
      let lastX = 0
      let lastY = 0
      if (this.transformVal !== '') {
        let matrix = this.transformVal.split(',')
        if (this.transformVal.indexOf('3d') === -1) {
          lastX = parseInt(matrix[4])
          lastY = parseInt(matrix[5])
        } else {
          lastX = parseInt(matrix[12])
          lastY = parseInt(matrix[13])
        }
      }
      if (!e.targetTouches) { // pand on desktop
        this.startX = e.pageX - lastX
        this.startY = e.pageY - lastY
      } else if (e.targetTouches.length === 1) { // pan on mobile device
        this.startX = e.targetTouches[0].pageX - lastX
        this.startY = e.targetTouches[0].pageY - lastY
      } else if (e.targetTouches.length > 1) {
        return
      }
    },
    setChartScale (newScale) {
      let matrix = ''
      let targetScale = 1
      if (this.transformVal === '') {
        this.transformVal = 'matrix(' + newScale + ', 0, 0, ' + newScale + ', 0, 0)'
      } else {
        matrix = this.transformVal.split(',')
        if (this.transformVal.indexOf('3d') === -1) {
          targetScale = Math.abs(window.parseFloat(matrix[3]) * newScale)
          if (targetScale > this.zoomoutLimit && targetScale < this.zoominLimit) {
            matrix[0] = 'matrix(' + targetScale
            matrix[3] = targetScale
            this.transformVal = matrix.join(',')
          }
        } else {
          targetScale = Math.abs(window.parseFloat(matrix[5]) * newScale)
          if (targetScale > this.zoomoutLimit && targetScale < this.zoominLimit) {
            matrix[0] = 'matrix3d(' + targetScale
            matrix[5] = targetScale
            this.transformVal = matrix.join(',')
          }
        }
      }
    },
    zoomHandler (e) {
      let newScale  = 1 + (e.deltaY > 0 ? -0.2 : 0.2)
      this.setChartScale(newScale)
    }
  }
};
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


hr { 
  width:100%;
  height:1px; 
  background: #ddd9d9 
}


.titlechart {
  height: 40px;
  padding: 10px 20px;
  font-size: 18px;
  font-weight: bold
}

.sub_div {
  font-size: 16px;
  position:absolute;
  left: 50%;
  bottom: 10px;
  transform: translateX(-50%);
}

.rectangle1 {
  border-radius: 3px;
  position: relative;
  height: 13px;
  width: 19px;
  background-color: rgb(255, 255, 166);
}

.rectangle2 {
  border-radius: 3px;
  border: 2px solid rgb(0, 0, 0);
  position: relative;
  height: 13px;
  width: 19px;
  background-color: rgb(255, 255, 166);
}

.rectangle3 {
  border-radius: 3px;
  border: 2px solid #b8b8b8;
  position: relative;
  height: 13px;
  width: 19px;
  background-color: #ececec;
}




.orgchart-container {
  position: relative;
  display: inline-block;
  height: 825.46px;
  width: 100%;
  border: 0px dashed #aaa;
  border-radius: 15px;
  overflow: auto;
  text-align: center;
  background-color: rgba(241, 241, 241, 0.8);
}
.orgchart {
  box-sizing: border-box;
  display: inline-block;
  min-height: 21px;
  min-width: 202px;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  border: 1px dashed rgba(0, 0, 0, 0);
  padding: 2px;
}
.orgchart .hidden,
.orgchart ~ .hidden {
  display: none;
}
.orgchart.b2t {
  transform: rotate(180deg);
}
.orgchart.l2r {
  position: absolute;
  transform: rotate(-90deg) rotateY(180deg);
  transform-origin: left top;
}
.orgchart .verticalNodes ul {
  list-style: none;
  margin: 0;
  padding-left: 18px;
  text-align: left;
}
.orgchart .verticalNodes ul:first-child {
  margin-top: 2px;
}
.orgchart .verticalNodes > td::before {
  content: "";
  border: 1px solid rgba(0, 0, 0, 0.8);
}

.orgchart .verticalNodes > td > ul > li:first-child::before {
  box-sizing: border-box;
  top: -4px;
  height: 30px;
  width: calc(50% - 2px);
  border-width: 2px 0 0 2px;
}
.orgchart .verticalNodes ul > li {
  position: relative;
}
.orgchart .verticalNodes ul > li::before,
.orgchart .verticalNodes ul > li::after {
  box-sizing: border-box;
  content: "";
  position: absolute;
  left: -6px;
  border-color: rgba(0, 0, 0, 0.8);
  border-style: solid;
  border-width: 0 0 2px 2px;
}

.orgchart .verticalNodes ul > li::after {
  box-sizing: border-box;
  content: "";
  position: absolute;
  left: -6px;
  border-color: rgba(0, 0, 0, 0.8);
  border-style: solid;
  border-width: 0 0 2px 2px;
}


.orgchart .verticalNodes ul > li::before {
  top: -4px;
  height: 30px;
  width: 11px;
}
.orgchart .verticalNodes ul > li::after {
  top: 1px;
  height: 100%;
}
.orgchart .verticalNodes ul > li:first-child::after {
  box-sizing: border-box;
  top: 21x;
  width: 11px;
  border-width: 2px 0 0 2px;
}
.orgchart .verticalNodes ul > li:last-child::after {
  box-sizing: border-box;
  border-width: 2px 0 0;
}
.orgchart.r2l {
  position: absolute;
  transform: rotate(90deg);
  transform-origin: left top;
}
.orgchart > .spinner {
  font-size: 100px;
  margin-top: 30px;
  color: rgba(68, 157, 68, 0.8);
}
.orgchart table {
  border-spacing: 0;
  border-collapse: separate;
}
.orgchart > table:first-child {
  margin: 20px auto;
}
.orgchart td {
  text-align: center;
  vertical-align: top;
  padding: 0;
  
}
.orgchart .lines:nth-child(3) td {
  box-sizing: border-box;
  height: 20px;
}
.orgchart .lines .topLine {
  border-top: 1px solid rgba(65, 65, 65, 0.8);
  
}
.orgchart .lines .leftLine {
  border-left: 1px solid rgba(65, 65, 65, 0.8);
  float: none;
  border-radius: 0;
}
.orgchart .lines .rightLine {
  border-right: 1px solid rgba(65, 65, 65, 0.8);
  float: none;
  border-radius: 0;
  
}
.orgchart .lines .downLine {
  background-color: rgba(65, 65, 65, 0.8);
  margin: 0 auto;
  height: 25px;
  width: 2px;
  float: none;
  
}
/* node styling */
.orgchart .node {
  box-sizing: border-box;
  display: inline-block;
  position: relative;
  margin: 0;
  padding: 1px;
  border: 3px dashed transparent;
  text-align: center;
  width: 260px;
}
.orgchart.l2r .node,
.orgchart.r2l .node {
  width: 50px;
  height: 10px;
}
.orgchart .node > .spinner {
  position: absolute;
  top: calc(50% - 15px);
  left: calc(50% - 15px);
  vertical-align: middle;
  font-size: 30px;
  color: rgba(68, 157, 68, 0.8);
}

.orgchart .node:hover {
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.5);
  transition: 0.5s;
  cursor: pointer;
  z-index: 20;
  transform: scale(1.15);
}

/* .orgchart .node:focus {
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.5);
  transition: 0.5s;
} */

.orgchart .ghost-node {
  position: fixed;
  left: -10000px;
  top: -10000px;
}
.orgchart .ghost-node rect {
  fill: #ffffff;
  stroke: #bf0000;
}

.orgchart .node.allowedDrop {
  border-color: rgba(68, 157, 68, 0.9);
}

.orgchart .node .title {
  text-align: center;
  font-size: 15px;
  font-weight: bold;
  height: 28px;
  line-height: 25px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  background: linear-gradient(to top, #5386e4 100%, #6499f5 100%);
  color: #fff;
  border-radius: 8px 8px 0 0;
}

.orgchart.b2t .node .title {
  transform: rotate(-180deg);
  transform-origin: center bottom;
}
.orgchart.l2r .node .title {
  transform: rotate(-90deg) translate(-40px, -40px) rotateY(180deg);
  transform-origin: bottom center;
  width: 120px;
}
.orgchart.r2l .node .title {
  transform: rotate(-90deg) translate(-40px, -40px);
  transform-origin: bottom center;
  width: 120px;
}
.orgchart .node .title .symbol {
  float: left;
  margin-top: 4px;
  margin-left: 2px;
}

.orgchart .node .contentclick {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #333333;
  border: 1px solid  #b8b8b8;
  background-color: rgb(255, 255, 166);
  font-size: 14px;
  line-height: 20px;
  width: 100%;
  padding: 4px;
  height: 75px;
  border-radius: 0px 0px 10px 10px;
  box-shadow: 4px 4px 8px 0px rgba(0, 0, 0, 0.3);
}

.orgchart .node .content {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #333333;
  border: 1px solid  #b8b8b8;
  background-color: #ececec;
  font-size: 14px;
  line-height: 20px;
  width: 100%;
  padding: 4px;
  height: 75px;
  border-radius: 0px 0px 10px 10px;
  box-shadow: 4px 4px 8px 0px rgba(0, 0, 0, 0.3);
}

.orgchart.b2t .node .content {
  transform: rotate(180deg);
  transform-origin: center top;
}
.orgchart.l2r .node .content {
  transform: rotate(-90deg) translate(-40px, -40px) rotateY(180deg);
  transform-origin: top center;
  width: 120px;
}
.orgchart.r2l .node .content {
  transform: rotate(-90deg) translate(-40px, -40px);
  transform-origin: top center;
  width: 120px;
}
.orgchart .node .edge {
  font-size: 15px;
  position: absolute;
  color: rgba(68, 157, 68, 0.5);
  cursor: default;
  transition: 0.2s;
}
.orgchart.noncollapsable .node .edge {
  display: none;
}
.orgchart .edge:hover {
  color: #449d44;
  cursor: pointer;
}
.orgchart .node .verticalEdge {
  width: calc(100% - 10px);
  width: -webkit-calc(100% - 10px);
  width: -moz-calc(100% - 10px);
  left: 5px;
}
.orgchart .node .topEdge {
  top: -4px;
}
.orgchart .node .bottomEdge {
  bottom: -4px;
}
.orgchart .node .horizontalEdge {
  width: 15px;
  height: calc(100% - 10px);
  height: -webkit-calc(100% - 10px);
  height: -moz-calc(100% - 10px);
  top: 5px;
}
.orgchart .node .rightEdge {
  right: -4px;
}
.orgchart .node .leftEdge {
  left: -4px;
}
.orgchart .node .horizontalEdge::before {
  position: absolute;
  top: calc(50% - 7px);
}
.orgchart .node .rightEdge::before {
  right: 3px;
}
.orgchart .node .leftEdge::before {
  left: 3px;
}
.orgchart .node .toggleBtn {
  position: absolute;
  left: 5px;
  bottom: -2px;
  color: rgba(68, 157, 68, 0.6);
}
.orgchart .node .toggleBtn:hover {
  color: rgba(68, 157, 68, 0.8);
}
.oc-export-btn {
  display: inline-block;
  position: absolute;
  right: 5px;
  top: 5px;
  padding: 6px 12px;
  margin-bottom: 0;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.42857143;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  user-select: none;
  color: #fff;
  background-color: #5cb85c;
  border: 1px solid transparent;
  border-color: #4cae4c;
  border-radius: 4px;
}
.oc-export-btn[disabled] {
  cursor: not-allowed;
  box-shadow: none;
  opacity: 0.3;
}
.oc-export-btn:hover,
.oc-export-btn:focus,
.oc-export-btn:active {
  background-color: #449d44;
  border-color: #347a34;
}
.orgchart ~ .mask {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 999;
  text-align: center;
  background-color: rgba(0, 0, 0, 0.3);
}
.orgchart ~ .mask .spinner {
  position: absolute;
  top: calc(50% - 54px);
  left: calc(50% - 54px);
  color: rgba(255, 255, 255, 0.8);
  font-size: 108px;
}
.orgchart .node {
  transition: transform 0.3s, opacity 0.3s;
}
.orgchart .slide-down {
  opacity: 0;
  transform: translateY(40px);
}
.orgchart.l2r .node.slide-down,
.orgchart.r2l .node.slide-down {
  transform: translateY(130px);
}
.orgchart .slide-up {
  opacity: 0;
  transform: translateY(-40px);
}
.orgchart.l2r .node.slide-up,
.orgchart.r2l .node.slide-up {
  transform: translateY(-130px);
}
.orgchart .slide-right {
  opacity: 0;
  transform: translateX(130px);
}
.orgchart.l2r .node.slide-right,
.orgchart.r2l .node.slide-right {
  transform: translateX(40px);
}
.orgchart .slide-left {
  opacity: 0;
  transform: translateX(-130px);
}
.orgchart.l2r .node.slide-left,
.orgchart.r2l .node.slide-left {
  transform: translateX(-40px);
}
</style>