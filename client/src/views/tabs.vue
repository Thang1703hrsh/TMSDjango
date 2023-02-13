<template>
  <div class="bg-gradient-to-r from-blue-300 to-blue-500 min-h-screen">


    <app-tabs class="w-11/12 lg:w-10/12 mx-auto mb-16" :tabList="tabList">
      <template v-slot:tabPanel-1> Content 1 </template>
      <template v-slot:tabPanel-2> Content 2 </template>
    </app-tabs>
  </div>
</template>

<script>
import AppTabs from "../components/Tabs";

export default {
  components: {
    AppTabs,
  },
  data() {
    return {
      tabList: ["Tab 1", "Tab 2"],
    };
  },
};
</script>

