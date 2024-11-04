<script setup>
import { ref, onMounted } from 'vue';
import Loading from '../components/loader.vue';

const isLoading = ref(true);
const dats = ref([]);

async function getData(){
    try{
        const response = await fetch('http://127.0.0.1:5000/chilveryData')
        if(response.ok){
            dats.value = await response.json()
        }else{
            console.log('error', response.statusText)
        }
    } catch(error){
        console.log('error', error)
    }
}

onMounted(() => {
    setTimeout(() => {
        isLoading.value = false;
    }, 3000);
    getData();
}); 

</script>

<template>
    <div v-if="isLoading">
        <Loading></Loading>
    </div>
    <div v-else>
        <main>
            <!-- seccion del presentacion, imagen logo y texto -->
            <section class="container-logo flex" v-for="(title,index) in dats" :key="index">
                <article>
                    <img src="../image/chubby/ChubbyDeliberyNetwork (CDN).png" alt="logo empresa">
                </article>
                <article>
                    <h1> {{ title.home[0].imageTitle }} </h1>
                    <p> {{ title.home[0].textTitle }} </p>
                </article>
            </section>

            <!-- segunda seccion de datos y contenido con imagenes -->
            <h2 class="title-section">Comunicacion en su entorno</h2>
            <!-- seccion de cards para datos de la empresa -->
            <section class="flex container-cadsDinamic" v-for="(item,html) in dats" :key="html">
                <article v-for="(info,html) in item.cards" :key="html">
                    <div class="card">
                        <div class="content flex">
                            <img :src="info.imageCard" alt="">
                            <p class="para"> {{ info.textCard }} </p>
                        </div>
                    </div>
                </article>
            </section>

            <!-- espacio que determinara si tiene informacion o es una imagen -->
            <!-- espacio que determinara si tiene informacion o es una imagen -->

            <!-- titulo 3 -->
            <h2 class="title-section">Gran seguridad para la comunidad</h2>
            <!-- seccion de imagenes informativas -->
            <!-- <section class="container-image-info">
                <article class="flex">
                    <h3>Maneja y comparte tus servicios de e-salud</h3>
                    <div class="flex">
                        <img src="../image/nez/servicios-salud1.png" alt="servicio de salud">
                    </div>
                </article>
                <article class="flex">
                    <h3>Sistema de e-salud inter institucional</h3>
                    <div class="flex">
                        <img src="../image/nez/sistema-esalud1.png" alt="sistema de salud">
                    </div>
                </article>
            </section> -->

            <section class="container-image-info" >
                <article class="flex">
                    <div class="card-infoCloud">
                        <div class="tools">
                            <div class="circle-cloud">
                                <span class="red box"></span>
                                <span class="yellow box"></span>
                                <span class="green box"></span>
                            </div>
                        </div>
                        <div class="card__content">
                            <ul v-for="(info,index) in dats[0].information.container1" :key="index">
                                <li> {{ info.itemText }} </li>
                            </ul>
                        </div>
                    </div>
                </article>
                <article class="flex">
                    <div class="card-infoCloud">
                        <div class="tools">
                            <div class="circle-cloud">
                                <span class="red box"></span>
                                <span class="yellow box"></span>
                                <span class="green box"></span>
                            </div>
                        </div>
                        <div class="card__content">
                            <ul v-for="(info,index) in dats[0].information.container2" :key="index">
                                <li> {{ info.itemText }} </li>
                            </ul>
                        </div>
                    </div>
                </article>
            </section>
        </main>
    </div>
</template>

<style scoped>
/* estilos reutilizables */
.flex{
    display: flex;
    justify-content: center;
    align-items: center
}

/* seccion del main, logo y titulo */
/* seccion del main, logo y titulo */
article{
    margin: 1rem;
}
.container-logo{
    height: 100vh;
    width: auto;
    background-color: rgba(0, 0, 0, 0.9);
    background-blend-mode: multiply;
    background-image: url('../image/chubby/chubby-home.webp');
    background-size: cover;
    background-position: center;
    flex-direction: column;

    article{
        text-align: center;
    }
    h1{
        color: rgb(255, 255, 255);
        font-size: 3rem;
        font-weight: 700;
        margin-top: 1rem;
    }
    p{
        color: #ffffff;
        font-size: 1.5rem;
        margin: 1rem 10vw;
    }
    img{
        max-width: 25%;
        border-radius: 50%;
    }
}

/* seccion de la segunda parte de la pagina */
/* seccion de la segunda parte de la pagina */

.title-section{
    color: black;
    font-size: 2rem;
    font-weight: 700;
    text-align: center;
    margin: 2rem 0;
}

.card {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 20vw;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    padding: 32px;
    overflow: hidden;
    border-radius: 10px;
    transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
}

.content {
    flex-direction: column;
    align-items: flex-start;
    text-align: center;
    gap: 20px;
    color: #000000;
    transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
}

.content .para {
    line-height: 1.5;
}
img{
    margin: auto;
    max-width: 50%;
}
.card::before {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 5px;
    height: 100%;
    background: linear-gradient(-45deg, #FFBD88 0%, #91B8FD 100% );
    z-index: -1;
    transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
}
.content:hover {
    color: #ffffff;
}
.card:hover::before {
    width: 100%;
}

.card:hover {
    box-shadow: none;
}

/* seccion de estilos del contenido de las imagenes con informacion */
/* seccion de estilos del contenido de las imagenes con informacion */
.container-image-info{
    width: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    article{
        width: 50%;
        flex-direction: column;
    }
    div{
        width: 100%;
        height: 100%;
    }
    img{
        max-width: 70%;
        object-fit: cover;
        margin-top: 1rem;
    }
}

/* seccion de cards de datos generados, informacion */
/* seccion de cards de datos generados, informacion */
.container-dataGenerations{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    article{
        width: 50vw;
        height: 60vh;
        background-color: #ffffff;
    }
}

/* seccion de cards de informacion de la empresa, de la nuble */
/* seccion de cards de informacion de la empresa, de la nuble */
.card-infoCloud {
    width: 40vw;
    margin: 0 auto;
    background-color: #011522;
    border-radius: 8px;
    z-index: 1;
}
.circle-cloud{
    display: flex;
}
.tools {
    display: flex;
    padding: 9px;
}

.box{
    display: inline-block;
    width: 10px;
    height: 10px;
    padding: 1px;
    margin: 0 5px;
    border-radius: 50%;
}

.red {
    background-color: #ff605c;
}

.yellow {
    background-color: #ffbd44;
}

.green {
    background-color: #00ca4e;
}
li{
    color: #ffffff;
    margin: 10px 10px;
}
@media (max-width: 768px){
    .container-logo{
        h1{
            font-size: 2rem;
        }
        p{
            font-size: 1rem;
        }
        img{
            max-width: 70%;
        }
    }

    /* segunda seccion de la pagina(movile) */
    /* segunda seccion de la pagina(movile) */
    .title-section{
        font-size: 1.2rem;
    }
    .container-cadsDinamic{
        flex-direction: column;
        article{
            width: 60%;
            height: 40vh;
            margin: 1rem;
        }
        .card{
            width: 100%;
            height: 100%;   
        }
        .para{
            font-size: 1rem;
        }
        
    }
    /* seccion de texto informativos (movil)*/
    /* seccion de texto informativos (movil)*/
    .container-image-info{
        flex-direction: column;
        
    }
}
</style>