<script setup>
import { ref, onMounted } from 'vue';
import Loading from '../components/loader.vue';

const isLoading = ref(true);

onMounted(() => {
    setTimeout(() => {
        isLoading.value = false;
    }, 3000);
}); 

</script>

<template>
    <div v-if="isLoading">
        <Loading></Loading>
    </div>
    <div v-else>
        <main>
        <!-- SECCION DE INICIO, CARGA DE IMAGEN  -->
            <section class="dates-main">
                <article class="main-info">
                    <h1>BLEADER</h1>
                    <p>Servicio de construcción automatica de sistemas para grandes volumenes de datos</p>
                    <div class="main-btons flex">
                        <button>Poster cualitativo</button>
                        <button>Poster cuantitativo</button>
                        <button>Infografia tecnica</button>
                        <button>Infografia general</button>
                    </div>
                </article>
            </section>
            <!-- SECCION DE PUNTOS CLAVE -->
            <section class="aut-col flex">
                <article class="info-nez flex">
                    <div class="aut-nez">
                        <h2>AUTOMATIZACION</h2>
                        <p>Revoluciona tus sistemas con nuestrp servicio autmatico de construccion automatica</p>
                        <p>Un extenso catalogo de aplicaciones, agilizando el despliegue y la innovación</p>
                    </div>
                    <div class="col-nez">
                        <h2>COLABORATIVO</h2>
                        <p>Facilita la colaboracion con un sistema compartido por multiples usuarios e instituciones, integrando patrones de procesamiento avanzado para una operatividad eficiente</p>
                    </div>
                </article>
                <section class="flex">
                    <img src="../image/nez/BeaverBuilder.png" alt="logo breaver" loading="lazy">
                </section>
            </section>
            <!-- DATOS DE SERVICIO DE CONSTRUCCION AUTOMATICO -->
            <h2 class="title-construction">Servicio de construcción automático de sistemas e-salud para el manejo de datos y contenidos en la práctica médica</h2>
            <section class="nez-construction flex">
                <article>
                    <div>
                        <img src="../image/nez/nez-0.png" alt="bloque nez" loading="lazy">
                    </div>
                    <div>
                        <p>Crea tus bloques de construccion sin necesidad de programar aplicaciones extras</p>
                    </div>
                </article>
                <article>
                    <div>
                        <img src="../image/nez/nez-1.png" alt="bloques nez" loading="lazy">
                    </div>
                    <div>
                        <p>Une tus bloques y crea un sistema de e-Salud</p>
                    </div>
                </article>
                <article>
                    <div>
                        <img src="../image/nez/nez-2.png" alt="bloque conexiones" loading="lazy">
                    </div>
                    <div>
                        <p>Despliega tu servicio en la nube o tu computadora personal</p>
                    </div>
                </article>
            </section>
            <!-- seccion de datos que se pueden compartir de forma segura -->
            <h2 class="title-data-Esalud">Seguridad y rapidez</h2>
            <section class="flex">
                <section class="container1-esalud flex">
                    <p>¡Puedes compartir tu servicio de e-salud, y los datos generados, entre!:</p>
                </section>
                <section class="container2-esalud flex">
                    <article>
                        <h3>multiples usuarios</h3>
                        <div>
                            <ul>
                                <li>Sistemas de compartición de imagenología.</li>
                                <li>Datos de múltiples fuentes (sensores, y bases de datos).</li>
                                <li>Medición de signos vitales.</li>
                            </ul>
                        </div>
                    </article>
                    <article>
                        <h3>Múltiples niveles de atención</h3>
                        <div>
                            <ul>
                                <li>Diagnósticos</li>
                                <li>Imagenología</li>
                                <li>Métricas de pacientes</li>
                            </ul>
                        </div>
                    </article>
                </section>
            </section>
        </main>
    </div>
    

</template>

<style scoped>



/* estilos reciclables */
.flex{
    display: flex;
    justify-content: center;
    align-items: center;
}
main{
    background-color: #FFE7D6;
}
/* ESTILOS DEL MAIN */
.dates-main{
    width: 100%;
    height: 100vh;
    background-image: 
    linear-gradient(rgba(40,54,143,0.7), rgba(178,98,87,0.7)),
    url('../image/nez/main.webp');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    display: flex;
}
.main-info{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: #fff;
    margin: 0 3vw;
    text-align: center;
    h1{
        font-size: 3rem;
        font-weight: 700;
    }
    p{
        font-size: 1.5rem;
        font-weight: bold;
    }
}
/* ESTILOS DE LOS BOTONES DEL MAIN */
.main-btons{
    height: 20vh;
    button{
        width: 200px;
        height: 50px;
        background-color: #f3c49c;
        color: #000;
        border: none;
        border-radius: 10px;
        margin: 10px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        transition: 1s;
    }
    button:hover{
        background-color: #fff;
        transition: 1s;
    }
}
/* SECCION DE PUNTOS CLAVE AUT-COL(AUTOMATIZACION-COLABORACION) */
.aut-col{

    article{
        width: 50%;
        color: #000;
        margin: 0 3vw;

        h2{
            font-size: 2rem;
            font-weight: 700;
        }
        p{
            font-size: 1.2rem;
            font-weight: bold;        }
    }
    div{
        padding: 20px;
        margin: 10px;
        border-radius: 10px;
        color: #ffffff;
    }
    img{
        width: 50%;
    }
}
.info-nez{
    flex-direction: column;
}
.aut-nez{
    background-color: #72DDD0;
}
.col-nez{
    background-color: #FF9C77;
}
/* SECCION DE ESTILOS DE KIS SERVICIOS DE CONSTRUCCION*/
.title-construction{
    text-align: center;
    font-size: 2rem;
    font-weight: bold;
    margin: 3rem;
}
.nez-construction{
    article{
        width: 20%;
        height: 40vh;
        display: flex;
        flex-direction: column;
        text-align: center;
        background-color: #fff;
        border-radius: 15px;
        margin: 1rem;
        div{
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
        }
        img{
            width: 50%;
        }
        p{
            font-size: 1.2rem;
            font-weight: bold;
        }
    }
}
/* SECCION DE DATOS QUE SE PUEDEN COMPARTIR DE FORMA SEGURA */
.title-data-Esalud{
    text-align: center;
    font-size: 2rem;
    font-weight: bold;
    margin: 3rem;
}
.container1-esalud,.container2-esalud{
    width: 50%;
    height: 40vh;
}
.container1-esalud{
    p{
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin:  0 5vw;
    }
}
.container2-esalud{
    article{
        width: 50%;
        height: 30vh;
        display: flex;
        flex-direction: column;
        text-align: center;
        background-color: #fff;
        margin: 1rem;
        div{
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
        }
        h3{
            font-size: 1.5rem;
            font-weight: bold;
            background-color: #391E34;
            color: #fff;
            width: 100%;
            padding: 10px;
        }
        ul{
            text-align: left;
            li{
                font-size: 1.2rem;
                font-weight: bold;
            }
        }
    }
}


</style>