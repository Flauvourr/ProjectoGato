
var numDePregunta = 1
var sigPregunta = 2
const primerBoton = document.getElementById('comenzar')

function cambiarPregunta() {
    const divContainer = document.getElementById(`pregunta_${numDePregunta}`)
    const sigDivContainer = document.getElementById(`pregunta_${sigPregunta}`)
    console.log(divContainer)
    console.log(sigDivContainer)
    console.log(numDePregunta)
    console.log(sigPregunta)

    if (numDePregunta >= 1 && numDePregunta < 15) {
        divContainer.setAttribute('hidden', 'true')
        sigDivContainer.removeAttribute('hidden')
    } else {
        document.getElementById('formContainer').submit()
    }
    numDePregunta++
    sigPregunta++
}

function comenzarQuiz () {
    const divContainer = document.getElementById(`pregunta_${numDePregunta}`)
    divContainer.removeAttribute('hidden')
    comenzar.setAttribute('hidden', 'true')
     
}