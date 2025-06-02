const readline = require('readline-sync');

let diadasemana = readline.questionInt('Digite um número de 1 a 7: ');

switch(diadasemana){

    case 1:
        console.log('Domingo- Final de Semana'
        );
        break;

    case 2:
        console.log('Segunda-Feira- Dia Útil');
        break;

    case 3:
        console.log('Terça-Feira- Dia Útil');
        break;

    case 4:
        console.log('Quarta-Feira- Dia Útil');
        
        break;

    case 5:
        console.log('Quinta-Feira - Dia Útil');
        break;

    case 6:
        console.log('Sexta-Feira - Dia Útil');
        break;

    case 7:
        console.log('Sábado - Final de Semana');
        break;

    default:
        console.log('Número inválido.');
        break;

}