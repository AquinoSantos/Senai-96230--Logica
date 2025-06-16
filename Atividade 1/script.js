function calcularMedia() {
    const n1 = parseFloat(document.getElementById('nota1').value);
    const n2 = parseFloat(document.getElementById('nota2').value);
    const n3 = parseFloat(document.getElementById('nota3').value);

    if (isNaN(n1) || isNaN(n2) || isNaN(n3)) {
        document.getElementById('resultado').innerText = "Erro, preencha todas as notas!";
        esconderImagem();
        return;
    }

    const media = (n1 + n2 + n3) / 3;
    let status;

    if (media >= 7) {
        status = 'aprovado';
        document.getElementById('resultado').innerText = "Aprovado! Média: " + media.toFixed(2);
    } else if (media >= 5) {
        status = 'recuperacao';
        document.getElementById('resultado').innerText = "Recuperação! Média: " + media.toFixed(2);
    } else {
        status = 'reprovado';
        document.getElementById('resultado').innerText = "Reprovado! Média: " + media.toFixed(2);
    }

    mostrarImagem(status);
}

function mostrarImagem(status) {
    const img = document.getElementById('imagemStatus');

    if (status === 'aprovado') {
        img.src = 'aprovado.gif';
        img.alt = 'Aprovado';
    } else if (status === 'recuperacao') {
        img.src = 'recuperacao.gif';
        img.alt = 'Recuperação';
    } else if (status === 'reprovado') {
        img.src = 'reprovado.gif';
        img.alt = 'Reprovado';
    }

    img.style.display = 'block';
}

function esconderImagem() {
    const img = document.getElementById('imagemStatus');
    img.style.display = 'none';
}