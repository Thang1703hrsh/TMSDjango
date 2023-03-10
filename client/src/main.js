// import Vue from 'vue';
// // import Antd from 'ant-design-vue';
// // import 'ant-design-vue/dist/antd.css';
// import App from './App.vue';
// import axios from 'axios'
// // import router from './router'

// import 'bootstrap/dist/css/bootstrap.css'
// import './scss/app.scss';

// import "./index.css"
// // Vue.use(Antd);

// Vue.config.productionTip = false;
// // Vue.use(Antd);

// axios.defaults.baseURL = 'http://127.0.0.1:8000'

// new Vue({
//   render: h => h(App),
// }).$mount('#app')

import Vue from 'vue';

import App from './App.vue';
import axios from 'axios'
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import 'bootstrap/dist/css/bootstrap.css'
import './scss/app.scss';
import './assets/tailwind.css'
import "./index.css"
import router from './router'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import { library } from '@fortawesome/fontawesome-svg-core'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import VueLoading from 'vue-loading-template'
import vSelect from "vue-select";
import Multiselect from 'vue-multiselect'
import "vue-select/dist/vue-select.css";


Vue.component('multiselect', Multiselect)
Vue.use(VueLoading, /** options **/)
// Vue.component("v-select", VueSelect);

library.add(fas, far, fab)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component("v-select", vSelect);

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(Antd, VueLoading);

Vue.config.productionTip = false;

axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  el: '#app',
  router,
  render: h => h(App),
}).$mount('#app')