<template>
	<div id="app">
		<router-view></router-view>
	</div>
</template>

<script>

import Dashboard from './views/Dashboard.vue';
import Traceback from './views/Traceback.vue';

	export default ({
		computed: {
			'dashboard': Dashboard,
      'traceback': Traceback
		},
    data() {
      return {

      }
    }
	})
	
</script>

<style lang="scss">
</style>