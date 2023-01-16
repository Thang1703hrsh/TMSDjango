// import { Vue } from 'vue'
// import App from './App.vue'
// import axios from 'axios'

// import 'bootstrap/dist/css/bootstrap.css'

// import "./index.css"
// Vue.config.productionTip = false;


// axios.defaults.baseURL = 'http://127.0.0.1:8000'
// Vue(App).use(axios).mount('#app')



import Vue from 'vue';

import App from './App.vue';
import axios from 'axios'

import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

import 'bootstrap/dist/css/bootstrap.css'
import './scss/app.scss';
import './assets/tailwind.css'

// import "./index.css"

Vue.use(Antd);

Vue.config.productionTip = false;

axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  render: h => h(App),
}).$mount('#app')


// import Vue from 'vue'
// import App from './App.vue'

// Vue.config.productionTip = false

// new Vue({
//   render: h => h(App)
// }).$mount('#app')
