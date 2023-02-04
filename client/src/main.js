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

Vue.use(Antd);

Vue.config.productionTip = false;

axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  render: h => h(App),
}).$mount('#app')