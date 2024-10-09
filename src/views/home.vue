<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Loading from '../components/loader.vue';

const router = useRouter();
const isLoading = ref(true);

const titulo = ref('Innovación y Seguridad para un Futuro Digital')
const descripcion = ref('Quetza es una empresa pionera en el desarrollo de soluciones tecnológicas avanzadas para la protección de la información y la seguridad digital. Con un enfoque en la innovación, Quetza combina herramientas de última generación con estrategias personalizadas.')
const logro1 = ref('Desarrollo del Protocolo de Seguridad QTZ-256')
const logro2 = ref('Implementación de Redes Auto-Reparables')
const logro3 = ref('Liderazgo en la Adopción de Criptografía Cuántica')

onMounted(() => {
    setTimeout(() => {
        isLoading.value = false;
    }, 1000);
});

const conoceMas = () => {
    router.push('/conoceMas');
};

const infoQuetza = () => {
    titulo.value = dataEmp[0].titulo
    descripcion.value = dataEmp[0].descripcion
    logro1.value = dataEmp[0].logros[0][0]
    logro2.value = dataEmp[0].logros[0][1]
    logro3.value = dataEmp[0].logros[0][2]
}

const infoChubby = () => {
    titulo.value = dataEmp[1].titulo
    descripcion.value = dataEmp[1].descripcion
    logro1.value = dataEmp[1].logros[0][0]
    logro2.value = dataEmp[1].logros[0][1]
    logro3.value = dataEmp[1].logros[0][2]
}
const infoLizLock = () => {
    titulo.value = dataEmp[2].titulo
    descripcion.value = dataEmp[2].descripcion
    logro1.value = dataEmp[2].logros[0][0]
    logro2.value = dataEmp[2].logros[0][1]
    logro3.value = dataEmp[2].logros[0][2]
}
const infoAjolote = () => {
    titulo.value = dataEmp[3].titulo
    descripcion.value = dataEmp[3].descripcion
    logro1.value = dataEmp[3].logros[0][0]
    logro2.value = dataEmp[3].logros[0][1]
    logro3.value = dataEmp[3].logros[0][2]
}
const dataEmp = [
{
        titulo: 'Innovación y Seguridad para un Futuro Digital',
        descripcion: 'Quetza es una empresa pionera en el desarrollo de soluciones tecnológicas avanzadas para la protección de la información y la seguridad digital. Con un enfoque en la innovación, Quetza combina herramientas de última generación con estrategias personalizadas.',
        logros:[
            [
                'Desarrollo del Protocolo de Seguridad QTZ-256',
                'Implementación de Redes Auto-Reparables',
                'Liderazgo en la Adopción de Criptografía Cuántica',
            ]
        ]
    },
    {
        titulo: 'Soluciones Eficientes para el Mantenimiento de Bases de Datos',
        descripcion: 'Chubby es una empresa líder en el mantenimiento y optimización de bases de datos empresariales. Con un enfoque en la eficiencia y la estabilidad, Chubby se encarga de asegurar que las bases de datos de sus clientes funcionen sin interrupciones, garantizando un acceso rápido y seguro a la información crítica.',
        logros:[
            [
                'Implementación de Sistemas de Respaldo Automatizado',
                'Optimización de Bases de Datos para Grandes Corporaciones',
                'Migración Exitosa a Plataformas en la Nube',
            ]
        ]
    },
    {
        titulo: 'Protección y Seguridad para el Mundo Digital',
        descripcion: 'LizLock es una empresa especializada en soluciones avanzadas de seguridad digital, enfocada en brindar protección integral a sus clientes. Con tecnologías de vanguardia, LizLock ofrece servicios de cifrado, autenticación segura, y protección contra amenazas cibernéticas, asegurando que la información de las empresas esté resguardada en todo momento.',
        logros:[
            [
                'Desarrollo de Sistemas de Cifrado Dinámico',
                'Implementación de Autenticación Multinivel',
                'Protección Integral contra Amenazas Zero-Day',
            ]
        ]
    },
    {
        titulo: 'Innovación en Tecnología y Seguridad',
        descripcion: 'En Ajolote, entendemos la importancia de la seguridad en un mundo cada vez más conectado, y nos comprometemos a brindar un servicio excepcional que combine la última tecnología con un enfoque centrado en el cliente.',
        logros:[
            [
                'Plataforma de Defensa Cibernética Basada en IA',
                'Sistema de Autenticación Multifactor Biométrica',
                'Red de Seguridad Cibernética Autoevolutiva',
            ]
        ]
    },
    {
        titulo: 'Ingeniería y Gestión Eficiente de Proyectos Tecnológicos',
        descripcion: 'Beaver es una empresa dedicada a la ingeniería y gestión de proyectos tecnológicos. Con un equipo de expertos en optimización de procesos y desarrollo de infraestructuras tecnológicas, Beaver ofrece soluciones adaptadas a las necesidades específicas de cada cliente.',
        logros:[
            [
                'Automatización de Procesos Empresariales en Gran Escala',
                'Desarrollo de Infraestructura para Sistemas de Alto Rendimiento',
                'Integración Completa de Plataformas Multinube',
            ]
        ]
    },
];

</script>

<template>
    <div v-if="isLoading">
        <Loading></Loading>
    </div>
    <div v-else>
        <header>
            <section>
                <section class="content-main flex">
                    <img src="../image/home/Recurso 12SIN FONDO.png" alt="imagen de fondo mistix" loading="lazy">
                    <p>Plataforma tecnológica para la gestión, aseguramiento, intercambio y preservación de grandes volúmenes de datos en salud y construcción de un repositorio nacional de servicios de análisis de datos de salud.</p>
                    <button class="button" @click="conoceMas">Conocer mas</button>
                </section>
            </section>
        </header>
        <main>
            <!-- seccion de que somos -->
            <section class="container-info">
                <article class="info-text flex">
                    <h2>¡QUE SOMOS!</h2>
                    <p>empresa líder en el ámbito de la ciberseguridad y soluciones en la nube, comprometida con proteger los datos y la infraestructura digital de organizaciones de todos los tamaños. Con más de 10 años de experiencia en el sector, nuestro equipo de expertos se especializa en diseñar, implementar y mantener sistemas de seguridad robustos que protegen contra amenazas cibernéticas en constante evolución.</p>
                </article>
                <article class="info-logo"></article>
            </section>

            <!-- seccion de collage en hexagonos -->
            <section class="container-collage">
                <article class="container-collage-image">
                    <div class="logo-quetza img1" @click="infoQuetza"></div>
                    <div class="logo-Chubby img2" @click="infoChubby"></div>
                    <div class="logo-LizLock img3" @click="infoLizLock"></div>
                    <div class="logo-ajolote img4" @click="infoAjolote"></div>
                    <div class="logo-Beaver img5"></div>
                </article>
                <article class="container-collage-text">
                    <h2> {{ titulo }}</h2>
                    <p> {{ descripcion }} </p>
                    <ul>
                        <li> {{ logro1 }} </li>
                        <li> {{ logro2 }} </li>
                        <li> {{ logro3 }} </li>
                    </ul>
                </article>
            </section>

            <!-- seccion de inovaciones en el campo de la salud -->
            <section class="container-proyects">
                <h2>NUESTRAS APORTACIONES</h2>
                <section class="proyects-cards flex">
                    <article class="proyect1">
                        <div class="proyects-mosaic">   </div>
                        <div class="proyects-text">
                            <h3>SecureHealth Cloud Platform</h3>
                            <p> una solución integral en la nube diseñada para la gestión segura de datos médicos. Esta plataforma permite a hospitales y clínicas almacenar y acceder a registros de pacientes con alta disponibilidad y seguridad</p>
                        </div>
                    </article>
                    <article class="proyect2">
                        <div class="proyects-mosaic"></div>
                        <div class="proyects-text">
                            <h3> MedGuard Cyber Defense Suite</h3>
                            <p>es un sistema de protección especializado en la ciberseguridad para dispositivos médicos conectados. Dado el aumento de la conectividad en equipos médicos, este proyecto se enfoca en proteger contra ataques cibernéticos.</p>
                        </div>
                    </article>
                    <article class="proyect3">
                        <div class="proyects-mosaic"></div>
                        <div class="proyects-text">
                            <h3>TeleHealth Secure Gateway</h3>
                            <p>Con el crecimiento de la telemedicina, InnovateSec ha desarrollado el TeleHealth Secure Gateway, una solución que asegura las comunicaciones entre pacientes y profesionales de la salud a través de plataformas de teleconsulta. </p>
                        </div>
                    </article>
                </section>
            </section>
        </main>
    </div>

    
</template>

<style scoped>
/* estilos reutilizables */
/* estilos reutilizables */
.flex{
    display: flex;
    justify-content: center;
    align-items: center
}
/* seccion del main*/
/* seccion del main*/
.content-main{
    height: 100vh;
    background-image: url('../image/home/image-main.webp');
    background-size: cover;
    background-position: center;
    background-color: rgba(0, 0, 0, 0.7);
    background-blend-mode: multiply;
    flex-direction: column;  
    
    img{
        max-width: 90%;
        object-fit: cover;
        z-index: 1;
    }
    p{
        color: #fff;
        font-size: 1rem;
        text-align: center;
        margin: 2rem 8vw;
    }

    /* estilos del boton*/
    /* estilos del boton*/
    .button {
        padding: 0.5em 1.5em;
        border: none;
        border-radius: 5px;
        font-weight: bold;
        letter-spacing: 5px;
        text-transform: uppercase;
        cursor: pointer;
        color: #8EA05D;
        transition: all 1000ms;
        font-size: 15px;
        position: relative;
        overflow: hidden;
        outline: 2px solid #8EA05D;
    }
    button:hover {
        color: #ffffff;
        transform: scale(1.1);
        outline: 2px solid #aec472;
        box-shadow: 4px 5px 17px -4px #76854e;
    }
    button::before {
        content: "";
        position: absolute;
        left: -50px;
        top: 0;
        width: 0;
        height: 100%;
        background-color: #8EA05D;
        transform: skewX(45deg);
        z-index: -1;
        transition: width 1000ms;
    }
    button:hover::before {
        width: 250%;
    }
}
/* estilos de la seccion del main */
/* estilos de la seccion del main */

.container-info{
    height: 60vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    .info-text{
        flex-direction: column;
        text-align: justify;
        margin: 0 2rem;
        h2{
            font-size: 2rem;
            color: #8EA05D;
            margin: 1rem 0;
        }
    }
}
.info-logo{
    margin-top: 4rem;
    height: 5vh;
    width: 100%;
    background-color: #8EA05D;
    background-image: url('../image/home/Recurso 8SIN FONDO.png');
    background-repeat: repeat;
    background-size: 30px;
    background-position: 10px 10px;
    padding: 10px;
}

/* estilos del collage hexagonal */
/* estilos del collage hexagonal */
    .container-collage{
        height: 100vh;
    }
    .container-collage-image{
        height: 30vh;
    }
    .container-collage-text{
        height: 70vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        h2{
            font-size: 1.3rem;
            color: #8EA05D;
            margin: 1rem;
        }
        p{
            font-size: 1rem;
            color: #000;
            margin: 1rem 1rem;
            text-align: justify;
        }
        li{
            text-align: center;
            list-style: none;
        }
    }
    .logo-quetza{
        background-image: url('../image/home/quetzacloud.png');
        width: 28vw;
        height: 14vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        position: absolute;
        transition: 0.8s;
    }
    .logo-quetza:hover{
        transition: 0.8s;
        background-color: rgba(110, 191, 181, 0.7);
        background-blend-mode: multiply;
    }
    .logo-Chubby{
        background-image: url('../image/home/ChubbyDeliberyNetwork (CDN).png');
        width: 28vw;
        height: 14vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        transition: 0.8s;
        position: absolute;
    }
    .logo-Chubby:hover{
        transition: 0.8s;
        background-color: rgba(255, 178, 198, 0.7);
        background-blend-mode: multiply;
    }
    .logo-LizLock{
        background-image: url('../image/home/LizLock.png');
        width: 28vw;
        height: 14vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        position: absolute;
        transition: 0.8s;
    }
    .logo-LizLock:hover{
        transition: 0.8s;
        background-color: rgba(145, 185, 251, 0.7);
        background-blend-mode: multiply;
    }
    .logo-ajolote{
        background-image: url('../image/home/ajolote.png');
        width: 30vw;
        height: 15vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        transition: 0.8s;
        position: absolute;
    }
    .logo-ajolote:hover{
        transition: 0.5s;
        background-color: rgba(255, 200, 161, 0.7);
        background-blend-mode: multiply;
    }
    .logo-Beaver{
        background-image: url('../image/home/BeaverBuilder.png');
        width: 28vw;
        height: 14vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        position: absolute;
        transition: 0.8s;
    }
    .logo-Beaver:hover{
        transition: 0.5s;
        background-color: rgba(212, 106, 105, 0.7);
        background-blend-mode: multiply;
    }
    .img1 {
    top: 192%;
    left: 33%;
    transform: translate(-50%, -50%);
    }
    .img2 {
    top: 170%;
    left: 33%;
    transform: translate(-50%, -50%);
    }
    .img3 {
    top: 181%;
    left: 49%;
    transform: translate(-50%, -50%);
    }
    .img4 {
    top: 192%;
    left: 65%;
    transform: translate(-50%, -50%);
    }
    .img5 {
    top: 170%;
    left: 65%;
    transform: translate(-50%, -50%);
    }

    /* seccion de los proyectos */
    /* seccion de los proyectos */
    .container-proyects{
        h2{
            font-size: 2rem;
            margin: 1rem 0;
            text-align: center;
        }
        .proyects-cards{
            justify-content: space-around;
            display: flex;
            flex-direction: column;
        }
        article{
            margin: 1rem 1rem;
            height: 30vh;
            display: flex;
            align-items: center;
            border: 1px solid #8EA05D;
            border-radius: 0.5rem;
            transition: 0.5s;
            .proyects-mosaic{
                width: 30%;
                height: 100%;
                background-color: #8EA05D;
                background-image: url('../image/home/Recurso 8SIN FONDO.png');
                background-repeat: repeat;
                background-size: 40px;
                background-position: 10px 10px;
                padding: 10px;
                border-radius: 0.5rem 0 0 0.5rem;
            }
            .proyects-text{
                padding: 1rem;
                h3{
                    font-size: 1.5rem;
                    color: #8EA05D;
                    margin: 1rem 0;
                }
                p{
                    font-size: 1rem;
                    color: #000;
                    text-align: justify;
                }
            }
        }
        .proyect1:hover{
            background-image: url('../image/home/vision.webp');
            background-size: cover;
            background-position: center;
            background-color: rgba(0, 0, 0,0.7);
            background-blend-mode: multiply;
            color: #fff;
            transition: 0.5s;
            .proyects-text{
                h3{
                    color: #fff;
                }
                p{
                    color: #fff;
                }
            }
        }
        .proyect2:hover{
            background-image: url('../image/home/mission.webp');
            background-size: cover;
            background-position: center;
            background-color: rgba(0, 0, 0,0.7);
            background-blend-mode: multiply;
            color: #fff;
            transition: 0.5s;
            .proyects-text{
                h3{
                    color: #fff;
                }
                p{
                    color: #fff;
                }
            }
        }
        .proyect3:hover{
            background-image: url('../image/home/main-image.webp');
            background-size: cover;
            background-position: center;
            background-color: rgba(0, 0, 0,0.5);
            background-blend-mode: multiply;
            color: #fff;
            transition: 0.5s;
            .proyects-text{
                h3{
                    color: #fff;
                }
                p{
                    color: #fff;
                }
            }
        }
    }

/* estilos responsivos escritorio*/
/* estilos responsivos escritorio*/
/* estilos responsivos escritorio*/

@media (min-width:720px){
/* estilos reutilizables */
.flex{
    display: flex;
    justify-content: center;
    align-items: center
}

/* contenedor main, informacion e imagen de fondo */
.content-main{
    height: 100vh;
    background-image: url('../image/home/image-main.webp');
    background-size: cover;
    background-position: center;
    background-color: rgba(0, 0, 0, 0.7);
    background-blend-mode: multiply;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    p{
        color: #fff;
        font-size: 1.5rem;
        text-align: center;
        margin: 2rem 8vw;
    }
    /* estilos del boton*/
    .button {
        padding: 1em 2em;
        border: none;
        border-radius: 5px;
        font-weight: bold;
        letter-spacing: 5px;
        text-transform: uppercase;
        cursor: pointer;
        color: #8EA05D;
        transition: all 1000ms;
        font-size: 15px;
        position: relative;
        overflow: hidden;
        outline: 2px solid #8EA05D;
    }
    button:hover {
        color: #ffffff;
        transform: scale(1.1);
        outline: 2px solid #aec472;
        box-shadow: 4px 5px 17px -4px #76854e;
    }
    button::before {
        content: "";
        position: absolute;
        left: -50px;
        top: 0;
        width: 0;
        height: 100%;
        background-color: #8EA05D;
        transform: skewX(45deg);
        z-index: -1;
        transition: width 1000ms;
    }
    button:hover::before {
        width: 250%;
    }
}



/* estilos del main */
main{
.container-info{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 70vh;
    flex-direction: row;
    .info-text{
        width: 60%;
        margin: 0 4rem;
        h2{
            font-size: 4rem;
            color: #8EA05D;
            margin: 1rem 0;
        }
        p{
            font-size: 1.2rem;
            color: #000;
            margin: 1rem 0;
            text-align: justify;
        }
    }
    .info-logo{
        height: 70vh;
        width: 40%;
        background-color: #8EA05D;
        height: 100%;
        background-image: url('../image/home/Recurso 8SIN FONDO.png');
        background-repeat: repeat;
        background-size: 100px;
        background-position: 10px 10px;
        padding: 10px;
        }
    }

    /* seccion de collage en hexagonal */
    .container-collage{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 70vh;
    }
    .container-collage-image{
        width: 60%;
    }
    .container-collage-text{
        width: 40%;
        margin: 0 4rem;
        h2{
            font-size: 2rem;
            color: #8EA05D;
            margin: 1rem 0;
        }
        p{
            font-size: 1.2rem;
            color: #000;
            margin: 1rem 0;
            text-align: justify;
        }
        ul{
            li{
                font-size: 1rem;
                color: #000;
                margin: 1rem 0;
            }
        }
    }
    .logo-quetza{
        background-image: url('../image/home/quetzacloud.png');
        width: 13vw;
        height: 26vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        position: absolute;
        transition: 0.8s;
    }
    .logo-quetza:hover{
        transition: 0.8s;
        background-color: rgba(110, 191, 181, 0.7);
        background-blend-mode: multiply;
    }
    .logo-Chubby{
        background-image: url('../image/home/ChubbyDeliberyNetwork (CDN).png');
        width: 13vw;
        height: 26vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        transition: 0.8s;
        position: absolute;
    }
    .logo-Chubby:hover{
        transition: 0.8s;
        background-color: rgba(255, 178, 198, 0.7);
        background-blend-mode: multiply;
    }
    .logo-LizLock{
        background-image: url('../image/home/LizLock.png');
        width: 13vw;
        height: 26vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        position: absolute;
        transition: 0.8s;
    }
    .logo-LizLock:hover{
        transition: 0.8s;
        background-color: rgba(145, 185, 251, 0.7);
        background-blend-mode: multiply;
    }
    .logo-ajolote{
        background-image: url('../image/home/ajolote.png');
        width: 13vw;
        height: 26vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        transition: 0.8s;
        position: absolute;
    }
    .logo-ajolote:hover{
        transition: 0.5s;
        background-color: rgba(255, 200, 161, 0.7);
        background-blend-mode: multiply;
    }
    .logo-Beaver{
        background-image: url('../image/home/BeaverBuilder.png');
        width: 13vw;
        height: 26vh;
        background-size: cover;
        background-position: center;
        clip-path: polygon(
            50% 0%,
            100% 25%,
            100% 75%,
            50% 100%,
            0% 75%,
            0% 25%
        );
        position: absolute;
        transition: 0.8s;
    }
    .logo-Beaver:hover{
        transition: 0.5s;
        background-color: rgba(212, 106, 105, 0.7);
        background-blend-mode: multiply;
    }
    .img1 {
    top: 210%;
    left: 15%;
    transform: translate(-50%, -50%);
    }
    .img2 {
    top: 190%;
    left: 36%;
    transform: translate(-50%, -50%);
    }
    .img3 {
    top: 210%;
    left: 43%;
    transform: translate(-50%, -50%);
    }
    .img4 {
    top: 210%;
    left: 29%;
    transform: translate(-50%, -50%);
    }
    .img5 {
    top: 190%;
    left: 22%;
    transform: translate(-50%, -50%);
    }
}

/* seccion de proyects */
.container-proyects{
        height: 50vh;
        h2{
            font-size: 2rem;
            margin: 1rem 0;
            text-align: center;
        }
        .proyects-cards{
            justify-content: space-around;
            display: flex;
            flex-direction: row;
        }
        article{
            width: 30%;
            height: 30vh;
            display: flex;
            align-items: center;
            border: 1px solid #8EA05D;
            border-radius: 0.5rem;
            transition: 0.5s;
            .proyects-mosaic{
                width: 30%;
                height: 100%;
                background-color: #8EA05D;
                background-image: url('../image/home/Recurso 8SIN FONDO.png');
                background-repeat: repeat;
                background-size: 40px;
                background-position: 10px 10px;
                padding: 10px;
                border-radius: 0.5rem 0 0 0.5rem;
            }
            .proyects-text{
                width: 60%;
                padding: 1rem;
                h3{
                    font-size: 1.5rem;
                    color: #8EA05D;
                    margin: 1rem 0;
                }
                p{
                    font-size: 1rem;
                    color: #000;
                    margin: 1rem 0;
                    text-align: justify;
                }
            }
        }
        .proyect1:hover{
            background-image: url('../image/home/vision.webp');
            background-size: cover;
            background-position: center;
            background-color: rgba(0, 0, 0,0.7);
            background-blend-mode: multiply;
            color: #fff;
            transition: 0.5s;
            .proyects-text{
                h3{
                    color: #fff;
                }
                p{
                    color: #fff;
                }
            }
        }
        .proyect2:hover{
            background-image: url('../image/home/mission.webp');
            background-size: cover;
            background-position: center;
            background-color: rgba(0, 0, 0,0.7);
            background-blend-mode: multiply;
            color: #fff;
            transition: 0.5s;
            .proyects-text{
                h3{
                    color: #fff;
                }
                p{
                    color: #fff;
                }
            }
        }
        .proyect3:hover{
            background-image: url('../image/home/main-image.webp');
            background-size: cover;
            background-position: center;
            background-color: rgba(0, 0, 0,0.5);
            background-blend-mode: multiply;
            color: #fff;
            transition: 0.5s;
            .proyects-text{
                h3{
                    color: #fff;
                }
                p{
                    color: #fff;
                }
            }
        }
    }

}
</style>