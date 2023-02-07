<template>
    <table>
      <tbody>
        <tr>
         <td :rowspan="datasource.children && datasource.children.length ? datasource.children.length*2 : null">
          <div class="node" :id="datasource.id" @click.stop="handleClick(datasource)">
            <slot :node-data="datasource">
              <div class="title">
                <i class="fa fa-users symbol"></i>
                {{ datasource.name }}
              </div>
              <div class="content">{{ datasource.title }}</div>
            </slot>
          </div>
         </td>
        </tr>
        <template v-if="datasource.children && datasource.children.length">
          <tr class="lines">
            <th :rowspan="datasource.children.length*2">
              <div class="topLine"></div>
            </th>
          </tr>
          <!-- <tr class="lines">
            <th class="leftLine"></th>
           <template v-for="n in (datasource.children.length-1)" >
              <th class="rightLine downLine" :key="n"></th>
              <th class="leftLine downLine" :key="n"></th>
           </template>
            <th class="rightLine"></th>
          </tr> -->
          <!-- <tr class="nodes">
            <th row:rowspan="2" v-for="child in datasource.children" :key="child.id">
              <node :datasource="child" :handle-click="handleClick">
                <template v-for="slot in Object.keys($scopedSlots)" :slot="slot" slot-scope="scope">
                  <slot :name="slot" v-bind="scope"/>
                </template>
              </node>
            </th>
          </tr> -->
        </template>
      </tbody>
    </table>
  </template>
  
  <script>
  export default {
    name: 'node',
    props: {
      datasource: Object,
      handleClick: Function
    },
    methods: {
    }
  };
  </script>
  
  <style>
  </style>
  