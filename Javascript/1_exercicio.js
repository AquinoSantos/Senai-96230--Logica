// digite no terminal o comando a baixo:
//npm install readline-sync


const readlineSync = require('readline-sync')

let numero = parseInt(readlineSync.question("Digite um número: " ))

console.log('Tabela do numero ${numero}:')

for(let i = 1; i <= 10; i++) {
    resultado = numero * i;
    console.log(`${numero} x ${i} = ${resultado}`);
}





