
from flask import Flask, render_template_string

app = Flask(__name__)

PAGINA = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Un pedacito de mi universo 🌙</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    font-family: 'Trebuchet MS', sans-serif;
    background: linear-gradient(
        180deg, #302342, #75588f, #e9abc8
    );
    color: white;
    text-align: center;
    overflow-x: hidden;
}

.pantalla {
    max-width: 550px;
    margin: auto;
    padding: 25px 18px 45px;
}

h1 {
    font-size: 28px;
    color: #ffe3ef;
    text-shadow: 0 3px 12px #412545;
}

p {
    line-height: 1.7;
}

button {
    background: #ffc2db;
    color: #683d59;
    border: 2px solid white;
    border-radius: 30px;
    padding: 13px 23px;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 5px 15px #32244755;
}

button:active {
    transform: scale(.94);
}

.oculto {
    display: none !important;
}

.tarjeta {
    background: #ffffff20;
    border: 1px solid #ffffff65;
    border-radius: 25px;
    padding: 23px;
    margin-top: 20px;
    backdrop-filter: blur(8px);
}

.pandita {
    font-size: 85px;
    animation: respirar 2s infinite alternate;
}

@keyframes respirar {
    from { transform: scale(1); }
    to { transform: scale(1.08); }
}

#juego {
    position: relative;
    height: 440px;
    overflow: hidden;
    border: 3px solid #ffd6e8;
    border-radius: 25px;
    background:
        radial-gradient(
            circle at 75% 17%,
            #fff3bd 0 23px,
            transparent 25px
        ),
        linear-gradient(
            #302342,
            #73568e 65%,
            #c98eaf
        );
    touch-action: manipulation;
    margin-top: 15px;
}

#juego::after {
    content: "🌷 🌿 🌷 🌿 🌷 🌿 🌷";
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 100%;
    font-size: 27px;
    pointer-events: none;
}

.objeto {
    position: absolute;
    top: -60px;
    font-size: 40px;
    background: transparent;
    border: none;
    box-shadow: none;
    padding: 5px;
    z-index: 2;
    animation: caer linear forwards;
    touch-action: manipulation;
}

@keyframes caer {
    from {
        transform: translateY(0) rotate(-12deg);
    }
    to {
        transform: translateY(520px) rotate(20deg);
    }
}

#puntos {
    font-size: 21px;
    font-weight: bold;
    color: #ffe1ed;
}

.barra {
    height: 15px;
    background: #ffffff55;
    border-radius: 20px;
    overflow: hidden;
    margin: 15px 0;
}

#progreso {
    width: 0%;
    height: 100%;
    background: #ffc0d9;
    transition: width .4s;
}

#mensaje {
    background: #ffffff20;
    border-radius: 18px;
    min-height: 80px;
    padding: 15px;
    margin-top: 15px;
    color: #fff5c5;
    font-weight: bold;
    line-height: 1.5;
}

.carta {
    background: #fff4f8;
    color: #774661;
    border-radius: 20px;
    padding: 25px 20px;
    margin: 20px 0;
    box-shadow: 0 10px 30px #32244755;
    animation: aparecer .8s ease;
}

@keyframes aparecer {
    from {
        opacity: 0;
        transform: scale(.7);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.ramo {
    font-size: 72px;
    margin: 15px 0;
    animation: respirar 2s infinite alternate;
}

.particula {
    position: fixed;
    pointer-events: none;
    font-size: 26px;
    z-index: 30;
    animation: flotar 1.5s forwards;
}

@keyframes flotar {
    to {
        transform: translateY(-110px);
        opacity: 0;
    }
}

.estrella {
    position: fixed;
    color: #fff5ca;
    pointer-events: none;
    animation: brillo 2s infinite alternate;
}

@keyframes brillo {
    from { opacity: .2; }
    to { opacity: 1; }
}

.firma {
    font-size: 12px;
    opacity: .85;
    margin-top: 25px;
}
</style>
</head>

<body>

<!-- PANTALLA DE BIENVENIDA -->

<section class="pantalla" id="inicio">

    <h1>Un pedacito de mi universo 🌙</h1>

    <div class="tarjeta">

        <div class="pandita">🐼🌷</div>

        <h2>Hola mi bebé bella de mi vida 💓</h2>

        <p>
            Hice un jardincito en el cual caen cositas
            mi amor, debes atraparlos, cada uno demuestra
            un poquito del inmenso amor que te tengo
            mi reinita de mi vida.
        </p>

        <button onclick="iniciar()">
            Entrar al jardincito 🌷
        </button>

    </div>

    <p class="firma">
        Hecho con muchísimo amor, solamente para ti ♡
    </p>

</section>


<!-- PANTALLA DEL JUEGO -->

<section class="pantalla oculto" id="pantallaJuego">

    <h1>Mi jardincito para ti 🌷</h1>

    <div style="font-size:45px">🐼💓</div>

    <p>
        Atrapa todas las cositas que caen,
        mi amor bello.
    </p>

    <div id="puntos">0 / 15 ✨</div>

    <div class="barra">
        <div id="progreso"></div>
    </div>

    <div id="juego"></div>

    <div id="mensaje">
        Atrapa una cosita para descubrir su mensaje ♡
    </div>

</section>


<!-- PANTALLA FINAL -->

<section class="pantalla oculto" id="final">

    <h1>WIWIWWI lo hiciste mi bebé eres la mejor 💓</h1>

    <div class="tarjeta">

        <div class="ramo">💐🌷💐</div>

        <h2>Cultivaste nuestro jardincito 🌷</h2>

        <p>
            Cada cosita que atrapaste representa
            un pedacito del inmenso amor que te tengo,
            mi bebé bella.
        </p>

        <h3>Abre la carita mi amor 💌</h3>

        <button onclick="abrirCarta()">
            Abrir la cartita 💓
        </button>

        <div id="carta" class="carta oculto">

            <h2>Para mi bebé bella de mi vida 💓</h2>

            <p>
                Sabes lo mucho que me preocupo por tu
                bienestar mi amor de mi vida, por esta
                razón quiero acompañarte en todo momento,
                siempre quiero estar contigo y ahora
                no es la excepción, me darías el privilegio
                de poder acompañarte de nuevo mi amor
                de mi vida bella y no dejarte solita,
                eres todo para mí y necesito, quiero
                y deseo cuidarte como la bebé que eres
                mi amor bello de mi vida, te amito
                como no tienes idea mi brillitos bello
                bebé 💓💓💓💓💓
            </p>

            <div style="font-size:45px">🌷🌙🦋🍓</div>

            <button onclick="mostrarPregunta()">
                Una última cosita, mi amor...
            </button>

            <div id="ultima" class="oculto">

                <h2>
                    Me permites poder estar contigo
                    mi amor bello de mi vida?
                </h2>

                <button onclick="respuestaFinal()">
                    Me responde en instagram mi amor de mi vida
                </button>

                <p id="respuesta"></p>

            </div>

        </div>

    </div>

</section>


<script>

// LOS 15 OBJETOS DEL JUEGO
// Cada uno tiene su propio identificador.
// Así evitamos que se repitan los mensajes.

const objetosOriginales = [

    // CUATRO TULIPANES

    {
        id: 1,
        emoji: "🌷",
        mensaje: "Me encanta tu sonrisita piciosa"
    },

    {
        id: 2,
        emoji: "🌷",
        mensaje: "Eres la mujer más capaz e inteligente del mundo, te amito mi bebé."
    },

    {
        id: 3,
        emoji: "🌷",
        mensaje: "Me encanta cuando estás mimida y haces el suspirito final"
    },

    {
        id: 4,
        emoji: "🌷",
        mensaje: "Te amito por todo lo que eres mi amor, por lo valiente, asombrosa y talentosa que eres, me encanta tu personalidad mi amor hermoso y tu carisma único"
    },


    // CUATRO LUNITAS

    {
        id: 5,
        emoji: "🌙",
        mensaje: "BESITOOOOOOOO"
    },

    {
        id: 6,
        emoji: "🌙",
        mensaje: "Recuerdo nuestro primer beso, que salvaje de mi parte pero que bonito fue mi amor"
    },

    {
        id: 7,
        emoji: "🌙",
        mensaje: "Te extraño como no tienes idea, quiero abrazarte y que estés en paz junto a mi."
    },

    {
        id: 8,
        emoji: "🌙",
        mensaje: "Recuerdo nuestras risas incómodas después de un chiste malo que dije, me encanta mi amor verte reír con ellos, eres la mejor."
    },


    // CUATRO MARIPOSAS

    {
        id: 9,
        emoji: "🦋",
        mensaje: "Gracias por ser tú y solo tú, no quiero a nadie más mi amor"
    },

    {
        id: 10,
        emoji: "🦋",
        mensaje: "Eres lo más preciado que tengo mi bebé, te amito más que a nadie💓"
    },

    {
        id: 11,
        emoji: "🦋",
        mensaje: "Gracias mi amor por llenarme de alegría todos los días."
    },

    {
        id: 12,
        emoji: "🦋",
        mensaje: "Gracias por todo lo que haces por mí brillitos de mi vida, me falta vida para agradecerte mi amor bello."
    },


    // TRES FRESITAS

    {
        id: 13,
        emoji: "🍓",
        mensaje: "-1 objeto que recolectar"
    },

    {
        id: 14,
        emoji: "🍓",
        mensaje: "-1 objeto que recolectar"
    },

    {
        id: 15,
        emoji: "🍓",
        mensaje: "-1 objeto que recolectar"
    }

];


let pendientes = [];
let activos = new Set();
let puntos = 0;
let intervalo = null;
let terminado = false;


// INICIAR EL JUEGO

function iniciar() {

    document.getElementById("inicio").classList.add("oculto");

    document.getElementById("pantallaJuego")
        .classList.remove("oculto");

    pendientes = [...objetosOriginales];

    activos.clear();

    puntos = 0;
    terminado = false;

    document.getElementById("juego").innerHTML = "";

    document.getElementById("puntos").textContent = "0 / 15 ✨";

    document.getElementById("progreso").style.width = "0%";

    document.getElementById("mensaje").textContent =
        "Atrapa una cosita para descubrir su mensaje ♡";

    clearInterval(intervalo);

    crearObjeto();

    intervalo = setInterval(crearObjeto, 1000);

}


// CREAR OBJETOS QUE CAEN

function crearObjeto() {

    if (terminado) return;

    // Solo elegimos objetos que aún no están en pantalla.
    const disponibles = pendientes.filter(
        objeto => !activos.has(objeto.id)
    );

    if (disponibles.length === 0) return;

    const elegido = disponibles[
        Math.floor(Math.random() * disponibles.length)
    ];

    activos.add(elegido.id);

    const juego = document.getElementById("juego");

    const elemento = document.createElement("button");

    elemento.className = "objeto";

    elemento.textContent = elegido.emoji;

    elemento.setAttribute(
        "aria-label",
        "Atrapar " + elegido.emoji
    );

    const ancho = Math.max(0, juego.clientWidth - 65);

    elemento.style.left = Math.random() * ancho + "px";

    elemento.style.animationDuration =
        (6 + Math.random() * 2) + "s";

    elemento.onclick = function(evento) {

        evento.stopPropagation();

        atrapar(elegido, elemento, evento);

    };

    // Si no consigue atraparlo, volverá a aparecer.
    elemento.addEventListener("animationend", function() {

        activos.delete(elegido.id);

        elemento.remove();

    });

    juego.appendChild(elemento);

}


// ATRAPAR UN OBJETO

function atrapar(objeto, elemento, evento) {

    if (terminado || elemento.dataset.atrapado) return;

    elemento.dataset.atrapado = "si";

    elemento.remove();

    activos.delete(objeto.id);

    // El objeto atrapado se elimina de los pendientes.
    pendientes = pendientes.filter(
        item => item.id !== objeto.id
    );

    puntos++;

    const restantes = pendientes.length;

    document.getElementById("puntos").textContent =
        puntos + " / 15 ✨";

    document.getElementById("progreso").style.width =
        (puntos / 15 * 100) + "%";

    // Mostrar el mensaje correspondiente.
    if (objeto.emoji === "🍓") {

        document.getElementById("mensaje").textContent =
            "🍓 -1 objeto que recolectar. Faltan " +
            restantes + " cositas, mi amor.";

    } else {

        document.getElementById("mensaje").textContent =
            objeto.emoji + " " + objeto.mensaje;

    }

    crearParticula(
        evento.clientX,
        evento.clientY,
        objeto.emoji
    );

    // Cuando no queda ningún objeto, termina el juego.
    if (pendientes.length === 0) {

        terminar();

    }

}


// ANIMACIÓN AL ATRAPAR

function crearParticula(x, y, simbolo) {

    const particula = document.createElement("div");

    particula.className = "particula";

    particula.textContent = simbolo + " ✨";

    particula.style.left = x + "px";

    particula.style.top = y + "px";

    document.body.appendChild(particula);

    setTimeout(function() {

        particula.remove();

    }, 1500);

}


// FINALIZAR EL JUEGO

function terminar() {

    terminado = true;

    clearInterval(intervalo);

    setTimeout(function() {

        document.getElementById("pantallaJuego")
            .classList.add("oculto");

        document.getElementById("final")
            .classList.remove("oculto");

        window.scrollTo(0, 0);

        lluvia();

    }, 1300);

}


// ABRIR LA CARTA

function abrirCarta() {

    const carta = document.getElementById("carta");

    carta.classList.remove("oculto");

    carta.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });

}


// MOSTRAR LA PREGUNTA FINAL

function mostrarPregunta() {

    const ultima = document.getElementById("ultima");

    ultima.classList.remove("oculto");

    ultima.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });

}


// BOTÓN FINAL

function respuestaFinal() {

    document.getElementById("respuesta").textContent =
        "Te amito muchísimo mi bebé bella 💓🌷";

    lluvia();

}


// LLUVIA DE COSITAS BONITAS

function lluvia() {

    const simbolos = [
        "🌷", "🌙", "🦋", "🍓", "💓", "✨"
    ];

    for (let i = 0; i < 45; i++) {

        setTimeout(function() {

            const elemento = document.createElement("div");

            elemento.className = "particula";

            elemento.textContent = simbolos[
                Math.floor(Math.random() * simbolos.length)
            ];

            elemento.style.left =
                Math.random() * 90 + "vw";

            elemento.style.top =
                (20 + Math.random() * 70) + "vh";

            document.body.appendChild(elemento);

            setTimeout(function() {

                elemento.remove();

            }, 1500);

        }, i * 75);

    }

}


// ESTRELLITAS DECORATIVAS

for (let i = 0; i < 35; i++) {

    const estrella = document.createElement("span");

    estrella.className = "estrella";

    estrella.textContent = "✦";

    estrella.style.left = Math.random() * 100 + "vw";

    estrella.style.top = Math.random() * 100 + "vh";

    estrella.style.fontSize =
        (5 + Math.random() * 9) + "px";

    estrella.style.animationDelay =
        Math.random() * 3 + "s";

    document.body.appendChild(estrella);

}

</script>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(PAGINA)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)