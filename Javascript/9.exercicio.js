const readline = require('readline-sync');

let numero = readline.questionInt('Digite um número: ');


function verificaNumero(numero) {
    if (numero > 0) {
        return 'positivo';

    } else if(numero < 0) {
        return 'negativo';
    }
    else{
        console.log('Erro')
    }
}

let resultado = verificaNumero(numero);

console.log(`${resultado}`);
