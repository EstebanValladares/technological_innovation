// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import nez from '../views/nez.vue';
import Home from '@/views/home.vue';
import Daxoly from '@/views/daxoly.vue'
import conoceMas from '@/views/conoceMas.vue';
import prueba1 from '@/views/prueba1.vue';
import prueba2 from '@/views/prueba2.vue';
const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/nez',
        name: 'nez',
        component: nez
    },
    {
        path: '/daoxoly',
        name:'daoxoly',
        component: Daxoly
    },
    
    {
        path: '/conoceMas',
        name:'conoceMas',
        component: conoceMas
    },
    {
        path: '/prueba1',
        name:'prueba1',
        component: prueba1
    },
    {
        path: '/prueba2',
        name:'prueba2',
        component: prueba2
    }

];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;