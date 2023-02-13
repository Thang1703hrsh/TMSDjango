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
  