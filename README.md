# web

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).


<!-- modulos y ejecucion de codigo -->

### creacion proyecto vue

```sh
npm install -g @vue/cli

```
### instalation node_modules en caso de falla

```sh
npm init -y

```
## modulo a utilizar vue-router

```sh
npm install vue-router

```
### ejecucion aplicacion web

```sh
cd mistix && npm run dev

```

<!-- requerimientos y ejecucion de python  -->
### flask python

```sh
cd mistix
cd python && pip install flask

```
### uso de CORS python

```sh
cd mistix
cd python && pip install flask-cors

```
### uso de biblioteca de mongoDB en python

```sh
cd mistix
cd python && pip install pymongo

```
### ejecucion de documento python

```sh
cd mistix
cd python && python app.py

```
### ejecucion de volumen en docker compose

```sh
docker-compose up -d

```
### creacion de contenedor

```sh
docker build -t loggermistix .

### url puerto en uso: http://127.0.0.1:5000

```
### ejecucion de volumen en docker contenedor

```sh
docker run -p 5000:5000 loggermistix

### url puerto en uso: http://127.0.0.1:5000

```