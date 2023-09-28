



// La función tiene 3 casos posibles:
//     1.- Si todavía no empieza el Kahoot (hay que usar el botón de comenzar):
//         En este caso, esconde el botón y muestra el siguiente div con la pregunta
//         y sus respuestas, además del fondo.
//     2.- Si ya ha comenzado el Kahoot:
//         En ese caso, esconde el div con la pregunta y respuestas actuales y muestra
//         las siguientes.
//     3.- Si ya ha terminado el quiz:
//         Hace un Submit del form.

var numDePregunta = 0

function cambiarPregunta() {  

    if (numDePregunta===0) {
        const divContainer = document.getElementById(`pregunta_1`)
        const primerBoton = document.getElementById('comenzar')
        const backgroundStuff = document.getElementById('backgroundStuff')
    
        primerBoton.setAttribute('hidden', 'true')
        divContainer.removeAttribute('hidden')
        backgroundStuff.removeAttribute('hidden')

    } else if (numDePregunta >= 1 && numDePregunta < 15) {
        const divContainer = document.getElementById(`pregunta_${numDePregunta}`)
        const sigDivContainer = document.getElementById(`pregunta_${numDePregunta + 1}`)

        divContainer.setAttribute('hidden', 'true')
        sigDivContainer.removeAttribute('hidden')

    } else {

        document.getElementById('formContainer').submit()
    }

    numDePregunta++
}