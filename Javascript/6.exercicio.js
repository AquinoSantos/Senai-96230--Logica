const readline = require('readline-sync');

let a = readline.questionFloat('Digite um número: ');

if (a % 2 === 0) {
    console.log('O número é par');
}

else {
    console.log('O número é ímpar');
} 