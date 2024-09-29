<script setup>
import { ref, onMounted } from 'vue';

    const isVisible = ref(true);

    onMounted(() => {
        setTimeout(() => {
            isVisible.value = false;
        }, 3000);
    });
</script>
<template>
    <div class="container-loader">
        <div>
        <img src="../image/loader/Recurso 16SIN FONDO.png" alt="logo mistix">
    </div>
    <div class="loader-3">
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
    </div>
    </div>
</template>
<style scoped>
.container-loader{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f8f9fa;
    flex-direction: column;
}
div{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}
img{
    max-width: 30%;
}
.loader-3 {
    width: 10em;
    display: flex;
    justify-content: space-evenly;
}

.circle {
width: 1.2em;
height: 1.2em;
border-radius: 50%;
position: relative;
}

.circle:nth-child(1) {
background-color: #8FA05D;
}

.circle:nth-child(2) {
background-color: #518D9A;
}

.circle:nth-child(3) {
background-color: #3D4B59;
}

.circle:nth-child(4) {
background-color: #3D4B59;
}

.circle:nth-child(5) {
background-color: #518D9A;
}

.circle::before {
content: "";
width: 100%;
height: 100%;
position: absolute;
border-radius: 50%;
opacity: 0.5;
animation: animateLoader38 2s ease-out infinite;
}

.circle:nth-child(1)::before {
background-color: #8FA05D;
}

.circle:nth-child(2)::before {
background-color: #518D9A;
animation-delay: 0.2s;
}

.circle:nth-child(3)::before {
background-color: #3D4B59;
animation-delay: 0.4s;
}

.circle:nth-child(4)::before {
background-color: #3D4B59;
animation-delay: 0.6s;
}

.circle:nth-child(5)::before {
background-color: #518D9A;
animation-delay: 0.8s;
}

@keyframes animateLoader38 {
0% {
    transform: scale(1);
}

50%,
75% {
    transform: scale(2.5);
}

80%,
100% {
    opacity: 0;
}
}
</style>