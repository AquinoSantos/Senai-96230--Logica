const readline = require('readline-sync');

let a = readline.questionFloat('Digite a primeira nota: ');
let b = readline.questionFloat('Digite a segunda nota: ');
let c = readline.questionFloat('Digite a terceira nota: ');

if (a + b < c){
    c = a + b;
    console.log('A soma de A e B é  menor que C');
}

else{
    console.log('A soma de A e B é maior que C');
}





