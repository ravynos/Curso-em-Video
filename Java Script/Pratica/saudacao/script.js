function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    //var hora = data.getHours()
    var min = data.getMinutes()
    var hora = 6
    msg.innerHTML = `Agora são ${hora}: ${min}`
    if (hora >= 0 && hora < 12) {
        //BOM DIA!
        img.src = 'Manhã.jpg'
        document.body.style.background = '#e3dacb'
    } else if (hora >= 12 && hora < 18) {
        //BOA TARDE!
        img.src = 'tarde.jpg'
    }else {
        //BOA NOITE!
        img.src = "noite.jpg"
    }
}
