import Vue from 'vue'

import VueRouter from 'vue-router'
import Traceback from '../views/Traceback.vue' 
import Dashboard from '../views/Dashboard.vue' 
import test from '../views/test.vue' 
import tabs from '../views/tabs.vue' 
import loading from '../views/loading.vue'

Vue.use(VueRouter)

const router = new VueRouter({
    routes:[
        { path:'/traceback', component: Traceback },
        { path:'/dashboard', component: Dashboard },
        { path:'/test', component: test }, 
        { path:'/tabs', component: tabs },
        { path:'/loading', component: loading }
    ]
    
})
export default router

// import { createRouter, createWebHistory } from 'vue-router'

// import store from '../store'

// import Home from '../views/Home.vue'

// const routes = [
//     {
//       path: '/',
//       name: 'Home',
//       component: Home
//     }
// ]
  
// const router = createRouter({
//     history: createWebHistory(process.env.BASE_URL),
//     routes
// })

// router.beforeEach((to, from, next) => {
// if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
//     next({ name: 'LogIn', query: { to: to.path } });
// } else {
//     next()
// }
// })

// export default router

