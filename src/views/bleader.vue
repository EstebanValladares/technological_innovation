<script setup>
    import { ref, onMounted } from 'vue';
    import Loading from '../components/loader.vue';

    const isLoading = ref(true);
    const dats = ref([]);
    const showError = ref(false);

    // conexion a la base de datos
    // conexion a la base de datos
async function getData() {
try {
    const response = await fetch('http://127.0.0.1:5000/bleaderData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "home.textHome.title": "BLEADER"
        }),
    });
    if (response.ok) {
        showError.value = true;
        dats.value = await response.json();
        console.log(response);
        mostrarMensaje('Datos cargados correctamente', 'green');
    } else {
        console.log('error', response.statusText);
        mostrarMensaje('Error al cargar datos', 'red');
    }
    } catch (error) {
        console.log('error', error);
        mostrarMensaje(`Error: ${error.message}`, 'red');
    }
}

onMounted(() => {
        getData();
        setTimeout(() => {
            isLoading.value = false;
        }, 1000);
    });
    
</script>
<template>
    <div v-if="isLoading">
        <Loading></Loading>
    </div>
    <div v-else>
        <main>
            <div v-if="showError">
                <!-- seccion del presentacion, imagen logo y texto -->
                <section class="container-logo flex" v-for="(item, index) in dats" :key="index">
                    <article>
                        <img src="../image/nez/BeaverBuilder.png" alt="logo empresa">
                    </article>
                    <article>
                        <h1> {{ item.home.textHome.title }} </h1>
                        <p> {{ item.home.textHome.text }} </p>
                    </article>
                </section>
                
                <!-- segunda seccion de datos y contenido con imagenes -->
                <!-- segunda seccion de datos y contenido con imagenes -->
                <section v-for="(item, index) in dats" :key="index">
                    <h2 class="title-section"> {{ item.titles[0].title1 }} </h2>
                </section>
                <!-- seccion de cards para datos de la empresa -->
                <section class="flex container-cadsDinamic">
                    <article v-for="(item, index) in dats" :key="index">
                        <div class="card" v-for="(card, cardIndex) in item.cards" :key="cardIndex">
                            <div class="content flex">
                                <img :src="card.src" alt="">
                                <p class="para"> {{ card.description }} </p>
                            </div>
                        </div>
                    </article>
                </section>
                
                <!-- tercera seccion -->
                <!-- tercera seccion -->
                <!-- titulo 3 -->
                <section v-for="(item, index) in dats" :key="index">
                    <h2 class="title-section"> {{ item.titles[0].title2 }} </h2>
                </section>
                <!-- seccion de imagenes informativas -->
                <section class="container-image-info" v-for="(item, index) in dats" :key="index">
                    <article class="flex" v-for="(info, index) in item.information" :key="index">
                        <h3>Maneja y comparte tus servicios de e-salud</h3>
                        <div class="flex">
                            <img :src="info.src" alt="servicio de salud">
                        </div>
                    </article>
                    <!-- <article class="flex">
                        <h3>Sistema de e-salud inter institucional</h3>
                        <div class="flex">
                            <img src="../image/nez/sistema-esalud1.png" alt="sistema de salud">
                        </div>
                    </article> -->
                </section>
            </div>
            <!-- pantalla de error -->
            <!-- pantalla de error -->
            <div v-else >
                <!-- seccion de error en pantalla -->
                <!-- seccion de error en pantalla -->
                <section class="messageError">
                    <article>
                        <img src="../image/icons/Recurso 10SIN FONDO.png" alt="">
                    </article>
                    <article>
                        <h2>Oops! This page couldn’t be displayed</h2>
                        <p>It seems something went wrong. Please try refreshing the page, or come back later.</p>
                    </article>
                </section>
            </div>  
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

/* estilos de mensaje de alerta */
/* estilos de mensaje de alerta */
.alert {
    position: fixed;
    right: 0;
    bottom: 0;
    margin: 1rem;
    padding: 1rem;
    border: 1px solid #000;
    border-radius: 5px;
    background-color: #fff;
    color: #000;
}


/* mensaje de error en pantalla */
/* mensaje de error en pantalla */
.messageError{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    & article{
        text-align: center;
        img{
            max-width: 80%;
        }
        h2{
            font-size: 2rem;
            font-weight: 700;
            margin: 1rem;
        }
        p{
            font-size: 1rem;
            margin: 1rem;
        }
    }
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
    background-image: url('../image/1.jpg');
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

.container-cadsDinamic article{
    display: flex;
}

.card {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 20vw;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    padding: 32px;
    margin: 1rem;
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
        height: 60vh;
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

/* From Uiverse.io by javierBarroso */ 
/* From Uiverse.io by javierBarroso */ 
.card-data {
    width: 30vw;
    height: 60vh;
    margin: 0 auto;
    background-color: #f4f4f3;
    border-radius: 8px;
    z-index: 1;
    position: relative;
    display: flex;
    flex-direction: column;
}
.card-data::after {
    position: absolute;
    content: '';
    background-color: #454a50;
    width: 50px;
    height: 100px;
    z-index: -1;
    border-radius: 8px;
}
.tools {
    display: flex;
    align-items: center;
    padding: 9px;
    border-radius: 8px;
    background: #454a50;
    margin-top: -2px;
}
.circle {
    padding: 0 4px;
}
.card__content {
    height: 100%;
    margin: 0px;
    border-radius: 8px;
    background: #f4f4f3;
    padding: 10px;
}
.title-data {
    font-size: 20px;
}
.content-data {
    margin-top: 10px;
    font-size: 14px;
}
.box {
    display: inline-block;
    align-items: center;
    width: 10px;
    height: 10px;
    padding: 1px;
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

/* SECCION DE ESTILOS MOVIL */
/* SECCION DE ESTILOS MOVIL */
/* SECCION DE ESTILOS MOVIL */

@media (max-width: 768px) {
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

    /* seccion de imagenes informativas (movil)*/
    /* seccion de imagenes informativas (movil)*/
    .container-image-info{
        flex-direction: column;
        article{
            width: 80%;
            height: auto;
        }
        div{
            width: 100%;
        }
        img{
            max-width: 100%;
        }
        h3{
            text-align: center;
        }
    }
}

</style>