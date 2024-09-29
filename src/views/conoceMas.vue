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
            <section class="image-init flex">
                <article class="image-log">
                    <img src="../image/nosotros/Recurso 8SIN FONDO.png" alt="logo empresa">
                </article>
                <article class="text-init">
                    <h1>¡¡CONOCE UN POCO MAS SOBRE NOOSTROS!!</h1>
                </article>
            </section>
            <!-- seccion de la informacion de la mision de la empresa -->
            <h2 class="mission-text">MISION</h2>
            <section class="mission">
                <article class="card">
                    <div class="card1" href="#">
                        <p>Mision..</p>
                        <p class="small">Proveer servicios de consultoría, desarrollo y capacitación en tecnologías
                                        avanzadas, ayudando a nuestros clientes a resolver desafíos complejos, mejorar su
                                        productividad y alcanzar sus objetivos estratégicos. Nos comprometemos a entregar
                                        soluciones personalizadas y de alta calidad que promuevan la transformación digital
                                        y el crecimiento sostenible de nuestros clientes.</p>
                        <div class="go-corner" href="#">
                        <div class="go-arrow">
                            →
                        </div>
                        </div>
                    </div>
                </article>
                <article>
                    <img src="../image/nosotros/mision.jpg" alt="" loading="lazy">
                </article>
            </section>
            <!-- seccion de la informacion de la vision de la emrpesa -->
            <h2 class="mission-text">VISION</h2>
            <section class="mission">
                <article>
                    <img src="../image/nosotros/vision.jpg" alt="" loading="lazy">
                </article>
                <article class="card">
                    <div class="card1" href="#">
                        <p>Vision..</p>
                        <p class="small">Convertirnos en un referente en la transformación digital de organizaciones,
                                        ayudándolas a integrar tecnologías para mejorar su eficiencia, seguridad y
                                        competitividad. Aspiramos a establecer nuevos estándares en la industria, apoyando
                                        a nuestros clientes en la adaptación a un entorno tecnológico en constante cambio y
                                        promoviendo prácticas sostenibles y responsables que contribuyan al bienestar de
                                        la sociedad y del medio ambiente.</p>
                        <div class="go-corner" href="#">
                        <div class="go-arrow">
                            →
                        </div>
                        </div>
                    </div>
                </article>
            </section>
            <!-- seccion de los valores -->
            <h2>VALORES</h2>
            <section class="container-cards-vaL flex">
                <article class="card-v">
                    <div class="card-details">
                        <p class="text-body"> Exploramos y aplicamos tecnologías de vanguardia para ofrecer
                        soluciones que anticipen y satisfagan las necesidades cambiantes de
                        nuestros clientes</p>
                    </div>
                    <button class="card-button">Innovación</button>
                </article>
                <article class="card-v">
                    <div class="card-details">
                        <p class="text-body">Nos comprometemos a entregar servicios y productos de calidad,
                        asegurando la satisfacción de nuestros clientes y el cumplimiento de sus
                        expectativas.</p>
                    </div>
                    <button class="card-button">Calidad</button>
                </article>
                <article class="card-v">
                    <div class="card-details">
                        <p class="text-body"> Actuamos con honestidad y ética en todas nuestras operaciones,
                        construyendo relaciones de confianza y respeto con nuestros clientes,
                        empleados y socios.</p>
                    </div>
                    <button class="card-button">Integridad</button>
                </article>
                <article class="card-v">
                    <div class="card-details">
                        <p class="text-body">Ponemos a nuestros clientes en el centro de todas
                        nuestras decisiones y acciones, esforzándonos por entender y satisfacer sus
                        necesidades únicas</p>
                    </div>
                    <button class="card-button">Orientación al Cliente</button>
                </article>
            </section>
        </main>
    </div>
</template>

<style scoped>
/* estilos reutilizables */
*{
    font-family: sans-serif;
}
.flex{
    display: flex;
    justify-content: center;
    align-items: center
}
h2{
    text-align: center;
    font-size: 3rem;
    margin: 5rem 0;
}
/* contenido de iniciom imagen de presentacion */
.image-init{
    height: 100vh;
    width: 100%;
    background-image: url('../image/nosotros/somos-imagen.webp');
    background-size: cover;
    background-position: center;
    background-color: rgba(0, 0, 0, 0.9);
    background-blend-mode: multiply;
    .image-log{
        width: 30%;
        text-align: right;
    }
    .text-init{
        width: 70%;
        text-align: left;
        margin: 0 5rem;
    }
    /* imagen de la empresa en el inicio */
    img{
        max-width: 40%;
    }
    /* texto de presentacion */
    h1{
        color: white;
        font-size: 4rem;
    }
}
/* texto de mision */
.mission-text{
    text-align: center;
    font-size: 3rem;
    margin: 2rem 0;
}
/* seccion de la mision de la empresa */
.mission{
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 2rem 4vw;
    article{
        text-align: center;
        width: 50%;
        padding: 0 2rem;
    }
    img{
        text-align: left;
        max-width: 50%;
    }
    p{
        font-size: 1.5rem;
        text-align: justify;
    }
}

/* animacion de card de mision */
.card p{
    font-size: 1.4rem;
    color: #333;
    transition: all 0.3s ease-out;
}

.card p.small {
    font-size: 1.4rem;
}

.go-corner {
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    width: 42px;
    height: 42px;
    overflow: hidden;
    top: 0;
    right: 0;
    background-color: #FFD667;
    border-radius: 0 4px 0 32px;
}

.go-arrow {
    margin-top: -4px;
    margin-right: -4px;
    color: #fff;
    font-family: courier, sans;
}

.card1 {
    display: block;
    position: relative;
    background-color: #ffffff;
    border-radius: 4px;
    padding: 32px 24px;
    text-decoration: none;
    z-index: 0;
    overflow: hidden;
}

.card1:before {
    content: "";
    position: absolute;
    z-index: -1;
    top: -10%;
    right: -10%;
    background: #c7b072c9;
    height: 15%;
    width: 15%;
    border-radius: 32px;
    transform: scale(1);
    transform-origin: 50% 50%;
    transition: transform 0.25s ease-out;
}

.card1:hover:before {
    transform: scale(21);
}

.card1:hover p {
    transition: all 0.3s ease-out;
    color: rgba(255, 255, 255, 0.8);
}

.card1:hover h3 {
    transition: all 0.3s ease-out;
    color: #fff;
}

/* seccion de estilos de los valores */
.container-cards-vaL{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap: 2rem;
    margin: 2rem 6vw;
}
.card-v {
    width: 20vw;
    height: 25vh;
    border-radius: 20px;
    background: #f5f5f5;
    position: relative;
    padding: 1.8rem;
    border: 2px solid #c3c6ce;
    transition: 0.5s ease-out;
    overflow: visible;
}

.card-details {
    color: black;
    height: 100%;
    gap: .5em;
    display: grid;
    place-content: center;
}

.card-button {
    transform: translate(-50%, 125%);
    width: 60%;
    border-radius: 1rem;
    border: none;
    background-color: #8EA05D;
    color: #fff;
    font-size: 1rem;
    padding: .5rem 1rem;
    position: absolute;
    left: 50%;
    bottom: 0;
    opacity: 0;
    transition: 0.3s ease-out;
}

.text-body {
    font-size: 1.2rem;
}

/*Hover*/
.card-v:hover {
    border-color: #8EA05D;
    box-shadow: 0 4px 18px 0 rgba(0, 0, 0, 0.25);
}

.card-v:hover .card-button {
    transform: translate(-50%, 50%);
    opacity: 1;
}

</style>