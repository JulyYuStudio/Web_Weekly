import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Weekly from '../views/Weekly.vue'
import About from '../views/About.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/weekly/:id',
    name: 'weekly',
    component: Weekly,
    props: true
  },
  {
    path: '/about',
    name: 'about',
    component: About
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router