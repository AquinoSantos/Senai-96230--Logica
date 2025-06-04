const readline = require('readline-sync');

const listaNumeros = []

for (let i = 0; i < 5; i++) {
  const numero = readline.questionInt(`Digite o ${i + 1}º número: `)
  listaNumeros.push(numero)
}

const negativos = listaNumeros.filter(numero => numero < 0);
const positivos = listaNumeros.filter(numero => numero >= 0);




const somaPositivos = positivos.reduce((soma, total) => soma + total, 0);

console.log(`\nSoma dos números positivos: ${somaPositivos}`);
console.log(`Negativos: ${negativos,length}`);



