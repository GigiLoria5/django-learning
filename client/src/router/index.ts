import { createRouter, createWebHistory } from 'vue-router'
import UploadView from '@/views/UploadView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/upload', // send root straight to the upload page
    },
    {
      path: '/upload',
      name: 'upload',
      component: UploadView,
    },
  ],
})

export default router
