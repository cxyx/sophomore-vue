import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import User from '@/components/User'
import Ele from '@/components/ele'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/user',
      name: 'User',
      component: User,
    },
    {
      path: '/ele',
      name: 'Ele',
      component: Ele,
    }
  ]
})


