import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import StudyList from '@/views/StudyList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
     {
      path: '/study',
      name: 'study',
      component: StudyList,
    },
  ],
})

export default router
