import Vue from 'vue'
import Router from 'vue-router'
import HomeView from '@/components/HomeView'
// import CameraView from '@/components/CameraView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    }
  ]
})
