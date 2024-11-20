

function mudar(){
    const mudar = document.getElementById('mudar')
    if(mudar.innerHTML == 'DE 2020 - 2022'){
        mudar.innerHTML = 'Programador web freelancer'   
    }
    else{
        mudar.innerHTML = 'DE 2020 - 2022'
    }
    mudar.style.color = '#fff'
    mudar.style.fontSize = '18px'
    mudar.style.fontWeight = 'bold'
}

function mudarTexto(){
    const time = document.getElementById('timeline-duration')
    if(time.innerHTML == 'DE 2022 - PRESENTE'){
        time.innerHTML = 'Programador fullstack freelancer'   
    }
    else{
        time.innerHTML = 'DE 2022 - PRESENTE'
    }
    time.style.fontSize = '18px'
    time.style.color = '#fff'
    time.style.fontWeight = 'bold'
}


