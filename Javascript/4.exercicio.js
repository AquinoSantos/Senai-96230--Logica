const readline = require('readline-sync');

let a = readline.questionFloat('Digite a primeira nota: ');
let b = readline.questionFloat('Digite a segunda nota: ');


if(a === b){

soma = a + b;

 c = soma

console.log(`Nota C: ${c}`);
}

else{

    multi = a * b;

    c = multi;

    console.log(`Nota C: ${c}`);
}




