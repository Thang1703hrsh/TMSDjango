import Vue from 'vue'

import VueRouter from 'vue-router'
import Traceback from '../views/Traceback.vue' 
import Dashboard from '../views/Dashboard.vue' 

Vue.use(VueRouter)

const router = new VueRouter({
    routes:[
        { path:'/traceback', component: Traceback },
        { path:'/dashboard', component: Dashboard }
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

