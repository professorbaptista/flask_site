
// Selecionando os elementos
const firstDiv = document.querySelector('.parte1');
const secondDiv = document.querySelector('.parte2');
const finalDiv = document.querySelector('.final');

// Criando a função para alternar os divs

function go(currentStep, nextStep) {

    let dNone, dBlock;
    if (currentStep == 1) {
        dNone = firstDiv;
    }

    else if (currentStep == 2) {
        dNone = secondDiv;
    }

    else {
        dNone = finalDiv;
    }
    dNone.style.display = 'none';


    if (nextStep == 1) {
        dBlock = firstDiv;
    }

    else if (nextStep == 2) {
        dBlock = secondDiv;
    }
    else {
        dBlock = finalDiv;
    }

    dBlock.style.display = 'block'
}

//Função para validar os dados.
function validate() {
    const peso = document.querySelector('#peso');
    const altura = document.querySelector('#altura');
    // Para retirar as bordas vervelhas em cada um dos campos. 
    peso.style.border = 'none';
    altura.style.border = 'none';

    if ((!peso.value || (!altura.value))) {
        // Bloco if
        if ((!peso.value) && (!altura.value)) {
            // alert('Não tem peso nem altura')
            peso.style.border = '2px solid red';
            altura.style.border = '2px solid red';

        }
        else if (!peso.value) {
            // alert('Digite o peso')
            peso.style.border = '2px solid red'
        }

        else {
            // alert('Digite a altura')
            altura.style.border = '2px solid red'
        }
    }

    // Bloco else
    else {
        // Calcular o IMC

        const imc = peso.value / (altura.value * altura.value)

        const resultado = document.querySelector('.resultado');
        

        if (imc < 18.5) {
            resultado.innerHTML = ('Magreza | Obesidade grau: 0');
            resultado.style.color = 'green'
            resultado.style.fontWeight = '900'
            
        }

        else if (imc >= 18.5 && imc < 25) {
            resultado.innerHTML = ('Normal | Obesidade grau: 0');
            resultado.style.color = 'green'
            resultado.style.fontWeight = '900'
        }

        else if (imc >= 25 && imc < 30) {
            resultado.innerHTML = ('Sobrepeso | Obesidade grau: I');
            resultado.style.color = 'yellow'
            resultado.style.fontWeight = '900'
        }

        else if (imc >= 30 && imc < 35) {

            resultado.innerHTML = ('Obsidade | Obesidade grau II');
            resultado.style.color = 'red'
            resultado.style.fontWeight = '900'
        }

        else {
            resultado.innerHTML = ('Obesidade grave | Obesidade grau: III');
            resultado.style.color = 'red'
            resultado.style.fontWeight = '900'
        }

        go(2, 3);

    }
}



