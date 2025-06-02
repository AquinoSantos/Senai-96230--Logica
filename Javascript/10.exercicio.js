
const readline = require('readline-sync');

function calcularMedia(num1, num2) {
    return (num1 + num2) / 2;
}
let numero1 = readline.questionFloat('Digite o primeiro número: ');
let numero2 = readline.questionFloat('Digite o segundo número: ');
let media = calcularMedia(numero1, numero2);
console.log(`A média dos números é: ${media.toFixed(2)}`);

