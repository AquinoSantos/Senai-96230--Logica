// criando funcao
function somar(a, b) {
    return a + b;

}

function subtrair(a, b) {
    return a - b;
}

function multiplicar(a, b) {
    return a * b;
}

function dividir(a, b) {
    return a / b;
}

// chamando a funcao
 // Adiciona o resultado da soma na constante
const soma = somar(2,3)

const subtracao = subtrair(5,2)

const multiplicacao = multiplicar(4,3)  

const divisao = dividir(10,2)

// Mostra o conteudo da constante 
console.log(`Soma: ${soma}`); 
console.log(`Subtração: ${subtracao}`);
console.log(`Multiplicação: ${multiplicacao}`);
console.log(`Divisão: ${divisao}`);