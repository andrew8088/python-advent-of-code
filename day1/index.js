var fs = require('fs');
var pair = /\(\)/g;
var reversePair = /\)\(/g;

var input = fs.readFileSync('./input.txt').toString();

method2(input);

function method2 (input) {
  var floor = 0;
  input.split('').forEach(function (i) {
    if (i === '(') floor++;
    if (i === ')') floor--;
  });
  console.log(floor);
}

function method1 (input) {
  var l = input.length;

  do {
    input = input.replace(pair, '');
    input = input.replace(reversePair, '');
  } while(pair.test(input) || reversePair.test(input));

  console.log(input);
  console.log(l, input.length);
}
