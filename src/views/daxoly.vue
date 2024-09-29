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
        <main class="parallax-daxoly flex">
        <!-- seccion de presentacion  -->
            <section class="container-main flex">
                <article class="flex">
                    <img src="../image/ajolote/Proyecto Quitar fondo_transparente.png" alt="logo daoxoly" loading="lazy">
                </article>
                <article class="flex">
                    <h1>Daxoly</h1>
                    <p>Ajolote es una empresa líder en el sector de tecnología y seguridad, dedicada a proporcionar soluciones avanzadas para proteger y optimizar los entornos digitales de nuestros clientes. Fundada con el objetivo de fusionar innovación y seguridad, Ajolote ofrece una amplia gama de servicios, incluyendo ciberseguridad, desarrollo de software a medida, y consultoría tecnológica.</p>
                </article>
            </section>

            <!-- seccion de aportaciones que ha tenido -->
            <h2 class="title-innovations">Mejores aportaciones!!</h2>
            <section class="innovations flex">
                <article class="flex">
                    <h3>Las innovaciones mas sobresalientes:</h3>
                    <p>Algunas de las mejores innovaciones fueron aportadas para institutos</p>
                </article>
                <article>
                    <div>
                        <img src="../image/ajolote/main-image.webp" alt="aportacion 1" loading="lazy">
                    </div>
                    <div>
                        <h3>Plataforma de Defensa</h3>
                        <p>Ajolote ha desarrollado una plataforma avanzada de defensa cibernética que utiliza inteligencia artificial para detectar y neutralizar amenazas en tiempo real.</p>
                    </div>
                </article>
                <article>
                    <div>
                        <img src="../image/ajolote/main-image.webp" alt="aportacion 2" loading="lazy">
                    </div>
                    <div>
                        <h3>Sistema de Autenticación</h3>
                        <p>Para mejorar la seguridad de acceso, Ajolote ha implementado un sistema de autenticación multifactor biométrica que combina múltiples métodos de autenticación</p>
                    </div>
                </article>
                <article>
                    <div>
                        <img src="../image/ajolote/main-image.webp" alt="aportacion 3" loading="lazy">
                    </div>
                    <div>
                        <h3>Red de Seguridad Cibernética</h3>
                        <p>Ajolote ha creado una red de seguridad cibernética autoevolutiva que utiliza algoritmos de aprendizaje automático para actualizar automáticamente sus protocolos de seguridad.</p>
                    </div>
                </article>
            </section>
            <!-- seccion de explicacion de daxoly con los datos -->
            <section class="container-dataInfo">
                <h2>SE ADAPTA A TUS DATOS</h2>
                <h3>Analiza datos estructurados sin programar</h3>
            </section>
            <!-- fundadores de la empresa -->
            <section class="container-fundators">
                <article class="flex">
                    <div>
                        <img src="../image/ajolote/inv1.png" alt="fundador 1" oading="lazy">
                    </div>
                    <div>
                        <h2>Dr. Elisa Montenegro</h2>
                        <p>Dr. Elisa Montenegro es una experta en inteligencia artificial aplicada a la ciberseguridad. Con un doctorado en Ciencias de la Computación y más de 15 años de experiencia en el campo, Elisa ha liderado el desarrollo de la plataforma de defensa cibernética basada en IA de Ajolote.</p>
                    </div>
                </article>
                <article class="flex">
                    <div>
                        <h2>Dra. Valeria Cordero</h2>
                        <p> Dra. Valeria Cordero es una reconocida experta en encriptación y criptografía cuántica. Con un doctorado en Matemáticas Aplicadas y años de investigación en tecnologías emergentes, Valeria ha liderado el desarrollo de la solución de encriptación cuántica de Ajolote.</p>
                    </div>
                    <div>
                        <img src="../image/ajolote/inv2.png" alt="fundador 2" oading="lazy">
                    </div>
                </article>
                <article class="flex">
                    <div>
                        <img src="../image/ajolote/inv3.png" alt="fundador 3" oading="lazy">
                    </div>
                    <div>
                        <h2>Ing. Mateo Ríos</h2>
                        <p>Ingeniero en Seguridad de la Información, Mateo Ríos es el cerebro detrás del sistema de autenticación multifactor biométrica de Ajolote. Con un sólido background en criptografía y sistemas de autenticación, Mateo ha desarrollado soluciones innovadoras para mejorar la seguridad de acceso a sistemas críticos.</p>
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

.parallax-daxoly{
    flex-direction: column;
    position: relative;
    background-image: url('../image/ajolote/ajolote.png');
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    overflow: hidden;
}
.parallax-daxoly:before{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(246, 245, 250, 0.5);
}
.container-main{
    height: 80vh;
    width: 90vw;
    background-color: rgba(255, 169, 194, 0.9);
    border-radius: 10px;
    flex-direction: row;

    article{
        width: 50%;
        height: 100%;
        flex-direction: column;
        h1{
            font-size: 4rem;
            margin: 1rem;
        }
        p{
            font-size: 1.5rem;
            margin: 1rem;
        }
    }
    img{
        width: 70%;
        height: 70%;
        object-fit: cover;
        border-radius: 50%;
    }
}
/* seccion de estilos de las innovaciones */
.title-innovations{
    font-size: 2rem;
    margin-top: 2rem;
    color: 000;
    z-index: 1;
    border-bottom: 3px solid #FF6A81;
}
.innovations{
    height: 60vh;
    article{
        width: 100%;
        height: 70%;
        padding: 1rem;
        margin: 1rem;
        background-color: #FEDBD2;
        flex-direction: column;
        div{
            text-align: center;
            img{
                width: 80%;
                height: 80%;
                object-fit: cover;
                border-radius: 10px;
            };
        }
    }
}
/* estilos de la seccion de datos */
.container-dataInfo{
    display: flex;
    align-items: center;
    flex-direction: column;
    h2{
        color: #000;
        font-size: 2rem;
        margin: 1rem;
        border-bottom: 4px solid #FF6A81;
    }
    h3{
        font-size: 1.5rem;
        margin: 1rem;
    }
}
/* estilos de los fundadores */
.container-fundators{
    article{
        width: 100%;
        div{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            width: 50%;
            padding: 1rem;
            margin: 0 5rem;
            img{
                width: 40%;
                height: 40%;
                object-fit: cover;
                border-radius: 10px;
            }
        }
    }
}
</style>