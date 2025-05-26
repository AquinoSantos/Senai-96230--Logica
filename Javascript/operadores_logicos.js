// Operadores lógicos

let nome1 = 'Marta'
let nome2 = 'Marta'

let idade1 = 10
let idade2 = '10'

console.log('Igual')
console.log(nome1 === nome2)
console.log(idade1 == idade2) // verifica se o conteudo é igual, nao leva em conta o tipo
console.log(idade1 === idade2) // verifica se o conteudo e o tipo sao iguais

console.log('\nDiferente')
console.log(nome1 != nome2) // verifica se o conteudo é diferente, nao leva em conta o tipo
console.log(idade1 != idade2) // verifica se o conteudo é diferente, nao leva em conta o tipo


console.log('\nAND')
console.log(1 < 2 && 1 < 3) // &&  é o E (And)
console.log(10 < 2 && 1 < 3) 

console.log('\nOR')
console.log(10 < 2 || 1 < 3) // ||  é o OU (Or)
