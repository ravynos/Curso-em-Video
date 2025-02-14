function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var saud = document.getElementById('saudacao')
    var data = new Date()
    var hora = data.getHours()
    var min = data.getMinutes()
    msg.innerHTML = `Agora são ${hora}: ${min}`
    if (hora >= 0 && hora < 12) {
        //BOM DIA!
        saud.innerHTML = "Bom dia!!!"
        img.src = 'Manhã.jpg'
        document.body.style.background = '#ffc265'
    } else if (hora >= 12 && hora < 18) {
        //BOA TARDE!
        saud.innerHTML = "Boa tarde!!!"
        img.src = 'tarde.jpg'
        document.body.style.background = '#ebebe9'
    }else {
        //BOA NOITE!
        saud.innerHTML = "Boa noite!!!"
        img.src = "noite.jpg"
        document.body.style.background = '#0f496f'
    }
}
