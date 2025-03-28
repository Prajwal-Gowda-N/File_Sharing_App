import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ShareView from '@/views/ShareView.vue'
import Filetransfer from '@/views/Filetransfer.vue'
import SummerizerView from '@/views/SummerizerView.vue'
import Signupview from '@/views/Signupview.vue'
import LoginView from '@/views/LoginView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
     {
      path : '/',
      name : 'home',
      component : HomeView,
      meta: { requiresAuth: true }

     },
     {
      path : '/share',
      name : 'share',
      component : ShareView,
      meta: { requiresAuth: true }

     },
     {
      path : '/convert',
      name : 'convert',
      component : Filetransfer,
      meta: { requiresAuth: true }

     },
     {
      path : '/summarize',
      name : 'summarize',
      component : SummerizerView,
      meta: { requiresAuth: true }

     },
     {
      path: '/signup',
      name: 'SignUp',
      component: Signupview
    },
    {
      path: '/signin',
      name: 'SignIn',
      component: LoginView
    },
    { path: '/', redirect: '/signin' }
  ],
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const accessToken = localStorage.getItem('access_token');
    if (!accessToken) {
      next('/signin');
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router
