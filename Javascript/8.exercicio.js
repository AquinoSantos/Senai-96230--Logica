const readline = require('readline-sync');

let numero = readline.questionInt('Digite um número: ');


for (let i = 15; i <= 20; i++) {
    if (i === numero) {
        console.log(`O número ${numero} está entre 15 e 20.`);
        break;
    }
    if (i === 20) {
        console.log(`O número ${numero} não está entre 15 e 20.`);
    }
}