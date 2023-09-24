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