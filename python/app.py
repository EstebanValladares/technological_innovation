from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

quetzacloud = [
    {
        'image-title':'',
        'text-title': 'Elevate Your Potential: Unlock Limitless Opportunities and Drive Success with Our Cloud-Based Motivational Solutions'
    },
    {
        'cards':[
            {
                'image-card':'',
                'text-card':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi laboriosam at voluptas minus culpa deserunt delectus sapiente inventore pariatur'
            },
            {
                'image-card':'',
                'text-card':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi laboriosam at voluptas minus culpa deserunt delectus sapiente inventore pariatur'
            },
            {
                'image-card':'',
                'text-card':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi laboriosam at voluptas minus culpa deserunt delectus sapiente inventore pariatur'
            },
            {
                'image-card':'',
                'text-card':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi laboriosam at voluptas minus culpa deserunt delectus sapiente inventore pariatur'
            }
        ]
    },
    {
        'option-img':[
            {'img1':''},
            {'img2':''}
        ],
        'option-info':{
            'container1':[
                {'itemText':'1.- Acceso global: Usa la plataforma desde cualquier dispositivo con internet.'},
                {'2.- Experiencia personalizada: Ajusta las herramientas a tus metas.'},
                {'3.- Actualizaciones automáticas: Siempre con las últimas mejoras sin esfuerzo.'},
                {'4.- Colaboración: Comparte y trabaja en equipo de forma motivacional.'}
            ],
            'container1':[
                {'1.- Seguridad: Tus datos protegidos con encriptación avanzada.'},
                {'2.- Escalabilidad: Crece con la plataforma según tus necesidades.'},
                {'3.- Análisis inmediato: Revisa tu progreso en tiempo real.'},
                {'4.- Soporte continuo: Ayuda disponible 24/7 para cualquier duda.'}
            ],
        }
        
    }
]

nez = [
    {
        'image-title':'',
        'text-title': 'Con un enfoque proactivo y personalizado, te ayudamos a mantener la tranquilidad en un entorno digital en constante evolución. ¡Tu seguridad es nuestra prioridad!'
    },
    {
        'cards':[
            {
                'image-card':'',
                'text-card':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi laboriosam at voluptas minus culpa deserunt delectus sapiente inventore pariatur'
            },
            {
                'image-card':'',
                'text-card':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi laboriosam at voluptas minus culpa deserunt delectus sapiente inventore pariatur'
            },
            {
                'image-card':'',
                'text-card':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi laboriosam at voluptas minus culpa deserunt delectus sapiente inventore pariatur'
            }
        ]
    },
    {
        'option-img':[
            {'img1':''},
            {'img2':''}
        ],
        'option-info':{
            'container1':[
                {'itemText':''},
            ],
            'container1':[
                {'itemText':''},
            ],
        }
        
    }
]


#pagina de quetzacloud
@app.route('/quetacloud.vue',methods=['GET'])
def data_quetza():
    return jsonify(quetzacloud)

#pagina nez
@app.route('/nez.vue',methods=['GET'])
def data_nez():
    return jsonify(nez)

if __name__ == '__main__': 
    app.run(host= '0.0.0.0',port=5000,debug=False,use_reloader=False) 