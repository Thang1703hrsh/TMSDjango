<template>
  <table>
    <tbody>
      <tr>
       <td :colspan="datasource.children && datasource.children.length ? datasource.children.length*2 : null">
          <div class="node" :id="datasource.id">
            <button class = "btn" v-on:click="handleClick(datasource) ; handleClick1()">
              <slot :node-data="datasource">
                <div class="title">
                  <font-awesome-icon icon="fas fa-cogs" /> 
                  {{ datasource.name }}
                </div>
                <div>
                  <p v-if = "active === false" class="content">{{ datasource.title }}</p>
                  <p v-else class="contentclick">{{ datasource.title }}</p>
                </div>
              </slot>
            </button>
          </div>
       </td>
      </tr>
      <template v-if="datasource.children && datasource.children.length">
        <tr class="lines">
          <td :colspan="datasource.children.length*2">
            <div class="downLine"></div>
          </td>
        </tr>
        <tr class="lines">
          <td class="rightLine"></td>
         <template v-for="n in (datasource.children.length-1)">
            <td class="leftLine topLine"></td>
            <td class="rightLine topLine"></td>
         </template>
          <td class="leftLine"></td>
        </tr>
        <tr class="nodes">
          <td colspan="2" v-for="child in datasource.children" :key="child.id">
            <node :datasource="child" :handle-click="handleClick">
              <template v-for="slot in Object.keys($scopedSlots)" :slot="slot" slot-scope="scope">
                <slot :name="slot" v-bind="scope"/>
              </template>
            </node>
          </td>
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
    handleClick: Function,
    active: Boolean,
  },
  methods: {
    handleClick1() {
      this.active = true;
      console.log(this.active);
    },
  },
};
</script>

<style >

.btn {
  white-space: normal;
  min-width: 100%;
  max-width: 100%;
  border-radius: 10px;
  cursor: pointer;
  border: 2px black;
  padding: 0px ;
}

</style>
