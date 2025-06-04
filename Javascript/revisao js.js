const listaNumeros = [1, 2, 3]

console.log('Listando todos os números da lista:')
console.log(listaNumeros)

console.log('\ncalculando media aritmética:')
const media = listaNumeros.reduce((soma, total) => soma + total, 0) / listaNumeros.length
console.log(media)


