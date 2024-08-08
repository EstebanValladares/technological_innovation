<script setup>
import { ref } from 'vue';

const title = ref('TECNOLOGY');
const textInit = ref('La tecnología ha transformado nuestras vidas de manera fundamental, mejorando la comunicación, la eficiencia y el acceso a la información. Desde los teléfonos inteligentes hasta la inteligencia artificial, nos permite resolver problemas complejos y conectar con personas en todo el mundo.');

</script>

<template>
    <!-- BARRA DE NAVEGACION -->
    <header>
        <nav class="nav-bar">
            <ul>
                <li>
                <a href="">INICIO</a>
                </li>
                <li>
                <a href="">PRODUCTOS</a>          
                </li>
                <li>
                <a href="">CONTACTO</a>
                </li>
            </ul>
        </nav>
    </header>
    <!-- CUERPO DE LA PAGINA -->
    <body>
        <!-- VISTA DE LA PANPALLA DE CARGA, TEXTO DE INICIO E IMAGENES -->
        <section class="viewInit">
            <article class="viewInit--1">
                <h1> {{ title }} </h1>
                <p> {{ textInit }} </p>
                <button>Conoce mas</button>
            </article>
            <article class="viewInit--2">
                <div class="circle1"></div>
                <div class="circle2"></div>
                <div class="circle3"></div>
                <div class="circle4"></div>
                <div class="circle5"></div>
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 261.76 226.69"><path d="M161.096.001l-30.225 52.351L100.647.001H-.005l130.877 226.688L261.749.001z" fill="#41b883"/><path d="M161.096.001l-30.225 52.351L100.647.001H52.346l78.526 136.01L209.398.001z" fill="#34495e"/></svg>
                </div>
            </article>
        </section>
        <section class="iconsTecnology">
            <article>
                <i class="fa-solid fa-database"></i>
                <p>DATABASES</p>
            </article>
            <article>
                <i class="fa-solid fa-folder"></i>
                <P>DOCUMENTS</P>
            </article>
            <article>
                <i class="fa-solid fa-network-wired"></i>
                <P>NETWORKS</P>
            </article>
            <article>
                <i class="fa-solid fa-wifi"></i>
                <P>WIFI</P>
            </article>
        </section>
        <section class="cardsDinamic">
            <article class="container-card">
                <h2>01</h2>
                <h3>Tecnology</h3>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cum magni dicta nemo enim impedit quos. Cum officiis, magnam natus beatae quae perferendis </p>
                <button>Mas</button>
            </article>
            <article class="container-card">
                <h2>02</h2>
                <h3>Tecnology</h3>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cum magni dicta nemo enim impedit quos. Cum officiis, magnam natus beatae quae perferendis </p>
                <button>Mas</button>
            </article>
            <article class="container-card">
                <h2>03</h2>
                <h3>Tecnology</h3>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cum magni dicta nemo enim impedit quos. Cum officiis, magnam natus beatae quae perferendis </p>
                <button>Mas</button>
            </article>
            <article class="container-card">
                <h2>04</h2>
                <h3>Tecnology</h3>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cum magni dicta nemo enim impedit quos. Cum officiis, magnam natus beatae quae perferendis </p>
                <button>Mas</button>
            </article>
        </section>
    </body>
    <footer>

    </footer>
</template>

<style>
/* PALETA DE COLORES PARA TODO EL PROYECTOI */
:root{
    --colorNegroClaro: #838080;
    --colorAmarillo1: #FED36C;
    --colorBlanco: #FFFFFF;
    --colorAmarillo2: rgba(255,211, 108, .66);
    --colorAmarillo3: rgba(255,211, 108, .75);
    --colorAmarillo4: rgba(255,211, 108, .85);
    --colorIconosInicio: #4F8C98;
}

/* ESTILOS REUTILIZABLES */
.flex{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

header{
    /* BARRA DE NAVEGACION */
    .nav-bar{
        width: 100%;
        margin-top: 3vh;
        /* OPCIONES DE LA BARRA DE NAVEGACION */
        & ul{
            display: flex;
            justify-content: space-around;
            text-align: center;
            margin: 0 10vw;
            box-shadow: 0px 5px 10px 1px var(--colorNegroClaro);
            border-radius: 10px;
            padding: 2vh 0;
            font-size: 1.2rem;
        }

    }
}
body{
    /* CONTENEDOR DE IMAGEN Y FIGURAS FLOTANTES */
    .viewInit{
        width: 100%;
        height: 65vh;
        display: flex;
        justify-content: center;
        align-items: center;
        /* contenido texto inicio */
        .viewInit--1{
            width: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            h1{
                margin: 10px;
                font-size: 3rem;
            }
            p{
                margin: 0 10vw;
                font-size: 1.2rem;
            }
            button{
                margin: 10px;
                padding: 10px 20px;
                background-color: var(--colorAmarillo1);
                color: var(--colorBlanco);
                border: none;
                border-radius: 10px;
                font-size: 1.2rem;
            }
        }
        /* contenido decorativo flotante */
        .viewInit--2{
            width: 50%;
            text-align: center;
            /* figuras flotantes */
            .circle1{
                width: 22%;
                height: 44%;
                border-radius: 100%;
                background-color: var(--colorAmarillo2);
                position: absolute;
                top: 30%;
                right: 20%;
                z-index: -1;
            }
            .circle2{
                width: 8%;
                height: 16%;
                border-radius: 100%;
                background-color: var(--colorAmarillo1);
                position: absolute;
                top: 31%;
                right: 39%;
                z-index: -1;
            }
            .circle3{
                width: 9%;
                height: 18%;
                border-radius: 100%;
                background-color: var(--colorAmarillo2);
                position: absolute;
                top: 13%;
                right: 15%;
                z-index: -1;
            }
            .circle4{
                width: 7%;
                height: 14%;
                border-radius: 100%;
                background-color: var(--colorAmarillo3);
                position: absolute;
                top: 33%;
                right: 10%;
                z-index: -1;
            }
            .circle5{
                width: 5%;
                height: 10%;
                border-radius: 100%;
                background-color: var(--colorAmarillo4);
                position: absolute;
                top: 48%;
                right: 7%;
                z-index: -1;
            }
            /* imagen inicio */
            svg{
                max-width: 40%;
                z-index: 10;
            }
        }

    }
    /* ICONOS DE TECNOLOGIA */
    .iconsTecnology{
        width: 100%;
        height: 25vh;
        display: flex;
        justify-content: space-around;
        align-items: center;
        article{
            text-align: center;
            i{
                background-color: var(--colorIconosInicio);
                color: var(--colorBlanco);
                padding: 25px;
                margin: 10px;
                border-radius: 50%;
                font-size: 2rem;
            }
            p{
                font-size: 1.2rem;
                font-weight: bold;
            }
        }
    }
    /* TARGETAS DINAMICAS EN DESKTOP */
    .cardsDinamic{
        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        .container-card{
            border: 1px solid var(--colorNegroClaro);
            width: 20vw;
            height: 80vh;
            display: flex;
            justify-content: center;
            flex-direction: column;
            padding: 0 4vw;
            position: relative;
            overflow: hidden;
            h2{
                font-size: 6rem;
                position: relative;
                z-index: 2;
            }
            h3{
                font-size: 2rem;
                margin-bottom: 2vh;
                position: relative;
                z-index: 2;
            }
            button{
                margin-top: 2vh;
                background-color: var(--colorAmarillo1);
                border: none;
                color: var(--colorBlanco);
                font-size: 1rem;
                padding: 5px 0;
                border-radius: 10px;
            }
        }
        .container-card::before{
            content: '';
            position: absolute;
            top: -20%;
            left: 0;
            background-image: url('../image/tecnology.jpg');
            background-size: cover;
            background-position: center;
            width: 100%;
            height: 140%;
            opacity: 0;
            transition: opacity .5s ease;
            filter: blur(5px);
            z-index: -1;
            h2{
                color: var(--colorBlanco);
            }
            h3{
                color: var(--colorBlanco);
            }
        }
        .container-card:hover::before{
            opacity: 1;
        }
        .container-card:hover h2, .container-card:hover h3, .container-card:hover p{
            color: var(--colorBlanco);
        }
    }
}
</style>
