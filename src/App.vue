<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Loading from './components/loader.vue';

const router = useRouter();
const isLoading = ref(true);

/* rutas de las paginas */
const vistaNez = () => {
    router.push('/nez');
};

const vistaDao = () => {
    router.push('/daoxoly');
};

const informacion = () => {
    router.push('/conoceMas');
};
const homePage = () => {
    router.push('/');
};
const prueba1 = () => {
    router.push('/prueba1');
};

/* tiempo de carga del loader */
onMounted(() => {
    setTimeout(() => {
        isLoading.value = false;
    }, 1000);
});

</script>

<template>
    <!-- seccion de carga del loader -->
    <div v-if="isLoading">
        <Loading></Loading>
    </div>
    <div v-else>
        <main>
            <nav>
                <div class="navBar flex">
                <ul>
                    <li>
                    <img src="./image/appVue/simbolo4.png" alt="" class="logo" @click="homePage">
                    </li>
                </ul>
                <ul>
                    <li class="dropdown">INICIO
                    <ul class="dropdown-content">
                        <li><button @click="vistaNez">Nez</button></li>
                        <li><button @click="vistaDao">Daxoly</button></li>
                        <li><button @click="prueba1">Prueba</button></li>
                    </ul>
                    </li>
                    <li>SERVICIOS</li>
                    <li @click="informacion">INFORMACION</li>
                </ul>
                </div>
            </nav>
        </main>
    <router-view></router-view>

    <!-- seccion del footer -->
    <footer class="footer flex">
        <section class="image-footer flex">
            <img src="./image/appVue/Recurso 8SIN FONDO.png" alt="logo footer">
        </section>
        <section class="info-footer flex">
            <p>Contáctanos a través de nuestros diferentes canales y conoce más sobre la Plataforma tecnológica para la gestión, aseguramiento, intercambio y preservación de grandes volúmenes de datos en salud y construcción de un repositorio nacional de servicios de análisis de datos de salud.</p>
            <p>© 2021 InnovateSec. Todos los derechos reservados.</p>
        </section>
        <section class="flex iconsFooter">
            <i class="fa-brands fa-google"></i>
            <i class="fa-brands fa-github"></i>
            <i class="fa-solid fa-gamepad"></i>
        </section>
    </footer>

    </div>
</template>

<style scoped>
*{
    font-family: sans-serif;
}
/* estilos reutilizables */
.flex{
    display: flex;
    justify-content: center;
    align-items: center
}

/* seccion de la barra de navegacion */
nav{
    display: flex;
    justify-content: center;
}

/* barra de navegacion, secciones anidadas */
.navBar{
    text-align: center;
    width: 100%;
    justify-content: space-between;
    background-color: #fff;
    padding: 1.2rem;
    position: fixed;
    top: 0;
    z-index: 10;
    border-bottom: 1px solid #000;
    .logo{
        width: 3rem;
    }
    ul {
        display: flex;
        list-style: none;
        li{
            cursor: pointer;
            margin: 0 1rem;
            display: flex;
            align-items: center;
            position: relative;
            i{
                margin-left: 0.5rem;
                font-size: 0.8rem;
            }
        }
        /* Estilo básico para el dropdown */
        .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 160px;
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
        top: 100%;
            button{
                width: 100%;
                padding: 1rem;
                text-align: left;
                border: none;
                background-color: #fff;
                color: #000;
                font-size: 1rem;
                cursor: pointer;
            }
            button:hover{
                border-bottom: 1px solid #8EA05D;
            }
        }
        .dropdown-content a:hover {
            border-bottom: 2px solid #8EA05D;
            width: 100%;
        }
        /* Mostrar dropdown al pasar el cursor */
        .dropdown:hover .dropdown-content {
        display: block;
        }
    }
}
/* estilos del footer */
.footer{
    background-color: #000;
    color: #fff;
    padding: 1rem 2rem;
    img{
        max-width: 20%;
        height: auto;
    }
    .iconsFooter{
        width: 30%;
        text-align: center;
        i{
            font-size: 2rem;
            margin: 0 1rem;
            color: #fff;
            transition: 0.5s;
        }
        i:hover{
            color: #8EA05D;
            transition: 0.5s;
        }
    }
    .image-footer{
        text-align: center;
        width: 30%;
        display: flex;
        align-items: center;
    }
    .info-footer{
        text-align: center;
        width: 40%;
        margin: 0 2rem;
        flex-direction: column;
    }
}
</style>
