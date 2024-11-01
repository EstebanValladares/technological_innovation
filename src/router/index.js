// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/home.vue';
import conoceMas from '@/views/conoceMas.vue';
import bleader from '@/views/bleader.vue';
import quetzacloud from '@/views/quetzacloud.vue';
import Lizlock from '@/views/lizlock.vue';
import Chilvery from '@/views/chilvery.vue';
import Daxoly from '@/views/daxoly.vue';
const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },    
    {
        path: '/conoceMas',
        name:'conoceMas',
        component: conoceMas
    },
    {
        path: '/bleader',
        name:'bleader',
        component: bleader
    },
    {
        path: '/quetzacloud',
        name:'quetzacloud',
        component: quetzacloud
    },
    {
        path: '/lizlock',
        name:'lizlock',
        component: Lizlock
    },
    {
        path: '/chilvery',
        name:'chilvery',
        component: Chilvery
    },
    {
        path: '/daxoly',
        name:'daxoly',
        component: Daxoly
    }

];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;