<script setup>
import { ref, watch, onMounted } from 'vue'

// Definir la prop "mensaje"
const props = defineProps({
    mensaje: {
        type: String,
        default: ''
    },
    duracion: {
        type: Number,
        default: 8000 // Duración en milisegundos (3 segundos)
    }
})

// Estado para controlar la visibilidad
const visible = ref(false)

// Función para mostrar el mensaje y ocultarlo después de un tiempo
const mostrarAlerta = () => {
    visible.value = true
    setTimeout(() => {
        visible.value = false
    }, props.duracion)
}

// Observa cambios en la prop "mensaje" y muestra la alerta cada vez que cambie
watch(() => props.mensaje, (nuevoMensaje) => {
    if (nuevoMensaje) {
        mostrarAlerta()
    }
});

</script>

<template>
    <div v-if="isVisible" class="alert" :class="alertType" role="alert">
        {{ message }}
        <button @click="hideAlert" class="close-btn">Cerrar</button>
    </div>
</template>

<style scoped>

.alerta {
    padding: 1rem;
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
    border-radius: 4px;
    margin: 1rem 0;
    text-align: center;
    font-weight: bold;
    opacity: 0.9;
}

</style>