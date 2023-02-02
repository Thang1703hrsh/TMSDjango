import Vue from 'vue'
//Dòng này để import vue-router
import VueRouter from 'vue-router'

Vue.use(VueRouter)

let routes= [ // bao gồm danh sách route
    {
      path: '/dashboard', ///path của route
      name: 'dashboard', // tên route
      component: () => import('../views/Dashboard.vue'),
    },
    {
      path: '/traceback',
      name: 'traceback',
      component: () => import('../views/Traceback.vue'),
    }
]

function addLayoutToRoute( route, parentLayout = "default" )
{
	route.meta = route.meta || {} ;
	route.meta.layout = route.layout || parentLayout ;
	
	if( route.children )
	{
		route.children = route.children.map( ( childRoute ) => addLayoutToRoute( childRoute, route.meta.layout ) ) ;
	}
	return route ;
}

routes = routes.map( ( route ) => addLayoutToRoute( route ) ) ;

const router = new VueRouter({
	mode: 'hash',
	base: process.env.BASE_URL,
	routes,
	scrollBehavior (to, from, savedPosition) {
		if ( to.hash ) {
			return {
				selector: to.hash,
				behavior: 'smooth',
			}
		}
		return {
			x: 0,
			y: 0,
			behavior: 'smooth',
		}
	}
})

export default router
