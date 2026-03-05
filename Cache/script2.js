// 1
let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
console.log(array[array.length - 1])

//2
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
if(array.includes(3)){
    console.log('Присутствует 3')
} else{
    console.log('Отсутствует 3')
}

//6
array = [1, 2, 3, 4, 5]
console.log(array.slice(1,4))

//10
array = ['a', '-', 'b', '-', 'c', '-', 'd']
array.splice(array.indexOf('-'), 1)
console.log(array)

//11
array = ['a', 'b', 'c', 'd', 'e']
console.log(array.map((el, key) => key == 0 ? '!' : key == 3 ? '!!' : el))

//Доп

//1
let str = "1234567890"
array = Array.from(str)
console.log((array.map((el) => parseInt(el))).reduce((x1, x2) =>
 x1 + x2));

//2
const alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
              'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
console.log(alph.reduce((result, el, key) => {result[el] = key+1 ; return result}, {}))

//3
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(array.reduce((array3, el, key) =>
  {
   if(el % 3 == 0){
   array3 = [...array3, [ array[key-2], array[key-1], array[key]]];
   }
   return array3
},
[]))

//4
array = [1, 2, 4, 5, 5].sort((a, b) => a + b)
console.log(array.filter((el, key) => el > array[key+1])[1])

