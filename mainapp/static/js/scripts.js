var numDePregunta = 1

function cambiarPregunta() {
    const divContainer = document.getElementById(`pregunta_${numDePregunta}`)

    if (numDePregunta===1) {
        const primerBoton = document.getElementById('comenzar')
        const backgroundStuff = document.getElementById('backgroundStuff')
    
        primerBoton.setAttribute('hidden', 'true')
        divContainer.removeAttribute('hidden')
        backgroundStuff.removeAttribute('hidden')

    } else if (numDePregunta > 1 && numDePregunta < 15) {
        const sigDivContainer = document.getElementById(`pregunta_${numDePregunta + 1}`)
        
        divContainer.setAttribute('hidden', 'true')
        sigDivContainer.removeAttribute('hidden')

        console.log(divContainer)
        console.log(sigDivContainer)
    } else {
        document.getElementById('formContainer').submit()
    }

    numDePregunta++
    console.log(numDePregunta)
}