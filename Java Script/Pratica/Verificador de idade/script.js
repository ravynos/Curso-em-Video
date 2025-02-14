function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    var img = document.getElementById('imagem')
    if (fano.value.length == 0 || Number(fano.value) > ano) { 
        res.innerHTML = 'Valor incorreto'
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var gen = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            if (idade >= 0 && idade <= 2) {
                gen = 'um bebê'
                img.setAttribute('src', 'imagens/bebe-m.png')
            } else if (idade > 2 && idade <= 10) {
                gen = 'uma criança'
                img.setAttribute('src', 'imagens/crianca-m.png')
            } else if (idade < 21) {
                gen = 'um jovem'
                img.setAttribute('src', 'imagens/jovem-m.png')
            } else if (idade < 60) {
                gen = 'um homem'
                img.setAttribute('src', 'imagens/adulto-m.png')
            } else {
                gen = 'um idoso'
                img.setAttribute('src', 'imagens/idoso.png')
            }
        } else if (fsex[1].checked) {
            if (idade >= 0 && idade <= 2) {
                gen = 'uma bebê'
                img.setAttribute('src', 'imagens/bebe-f.png')
            } else if (idade > 2 && idade <= 10) {
                gen = 'uma criança'
                img.setAttribute('src', 'imagens/crianca-f.png')
            } else if (idade < 21) {
                gen = 'uma jovem'
                img.setAttribute('src', 'imagens/jovem-f.png')
            } else if (idade < 60) {
                gen = 'uma mulher'
                img.setAttribute('src', 'imagens/adulta-f.png')
            } else {
                gen = 'uma idosa'
                img.setAttribute('src', 'imagens/idosa.png')
            }
        }
        res.innerHTML = `Você é ${gen} com ${idade} anos.`
        res.appendChild(img)
    }
}