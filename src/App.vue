<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

/* rutas de las paginas */

const informacion = () => {
    router.push('/conoceMas');
};
const homePage = () => {
    router.push('/');
};
const prueba1 = () => {
    router.push('/prueba1');
};
const prueba2 = () => {
    router.push('/prueba2');
};
const lizlock = () => {
    router.push('/lizlock');
};

/* despliegue de la barra de navegacion de telefono */
const openBar = ref(false);

function openOptions() {
    openBar.value = !openBar.value;
}
const openBar2 = ref(false);

function openOptions2() {
    openBar2.value = !openBar2.value;
}

</script>

<template>
        <main>
            <!-- barra de navegacion en escritorio -->
            <nav class="navDesktop">
                <div class="navBar flex">
                    <ul>
                        <li>
                            <img src="./image/appVue/simbolo4.png" alt="" class="logo" @click="homePage">
                        </li>
                    </ul>
                    <ul :class="{ 'elements-movil':true, 'open': openElementMovil }">
                        <li class="dropdown">INICIO
                        <ul class="dropdown-content">
                            <li><button @click="prueba1">Bleader</button></li>
                            <li><button @click="prueba2">Quetzacloud</button></li>
                            <li><button @click="lizlock">Lizlock</button></li>
                        </ul>
                        </li>
                        <li>SERVICIOS</li>
                        <li @click="informacion">INFORMACION</li>
                    </ul>
                </div>
            </nav>
            <!-- barra de navegacion en movil -->
            <nav class="navMobil">
                    <ul class="icons-mobil">
                        <li>
                            <img src="./image/appVue/simbolo4.png" alt="" class="logo1" @click="homePage">
                        </li>
                        <li class="iconMobil">
                            <img src="../src/image/icons/navbarmovil.webp" alt="icono navegacion" class="nav1"
                            @click="openOptions">
                        </li>
                    </ul>
                    <ul class="elements-movil">
                        <div v-if="openBar">
                            <li @click="openOptions2">INICIO
                                <div class="optionsMovil" v-if="openBar2">
                                    <li><button @click="prueba1">Bleader</button></li>
                                    <li><button @click="prueba2">Quetzacloud</button></li>
                                </div>
                            </li>
                            <li>SERVICIOS</li>
                            <li @click="informacion">INFORMACION</li>
                        </div>
                    </ul>
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
</template>

<style scoped>
*{
    font-family: sans-serif;
}

/* estilos reutilizables */
/* estilos reutilizables */
.flex{
    display: flex;
    justify-content: center;
    align-items: center
}

/* cancelacion de estilos de barra de navegacion escritorio */
/* cancelacion de estilos de barra de navegacion escritorio */
.navDesktop{
    display: none;
}

/* seccion de la barra de navegacion */
/* seccion de la barra de navegacion */
.navMobil{
    display: flex;
    flex-direction: column;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 10;

    .icons-mobil{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background-color: #fff;
        border-bottom: 1px solid #000;
        .iconMobil{
            cursor: pointer;
        }
        .logo1{
            width: 2.5rem;
        }
        .nav1{
            width: 4rem;
        }
        li{
            cursor: pointer;
            list-style: none;
        }
    }

    .elements-movil{
        width: 100%;
        background-color: #fff;
        text-align: center;
        li{
            width: 100%;
            padding: 1rem;
            transition: 0.5s;
        }
        li:hover{
            background-color: #8EA05D;
            color: #fff;
            transition: 0.5s;
        }
        ul{
            display: none;
        }
        .optionsMovil{
            li{
                width: 100%;
                list-style: none;
            }
            li:hover{
                color: #fff;
                transition: 0.5s;
            }
            button{
                width: 100%;
                padding: 1rem;
                text-align: center;
                border: none;
                color: #000;
                font-size: 1rem;
                cursor: pointer;
            }
        }
    }
}


/* estilos del footer */
/* estilos del footer */
.footer{
    background-color: #000;
    color: #fff;
    padding: 1rem 2rem;
    flex-direction: column;
    img{
        max-width: 20%;
        height: auto;
    }
    .iconsFooter{
        margin: 1rem 0;
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
        margin: 1rem 0;
        text-align: center;
        display: flex;
        align-items: center;
    }
    .info-footer{
        text-align: center;
        margin: 0 1rem;
        flex-direction: column;
    }
}


/* estilos responsivos */
/* estilos responsivos */
/* estilos responsivos */

@media (min-width:720px){
/* estilos reutilizables */
.flex{
    display: flex;
    justify-content: center;
    align-items: center
}

/* cancelacion de estilos de barra de navegacion movil */
/* cancelacion de estilos de barra de navegacion movil */
.navMobil{
    display: none;
}
/* activacion estilos de desktop */
/* activacion estilos de desktop */
.navDesktop{
    display: block;
}

/* barra de navegacion escritorio, secciones anidadas */
/* barra de navegacion escritorio, secciones anidadas */
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
        /* Mostrar dropdown al pasar el cursor */
        .dropdown:hover .dropdown-content {
        display: block;
        }
    }
}
/* estilos del footer */
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
    
}
</style>
