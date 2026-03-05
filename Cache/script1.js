// //2

// let password = prompt('password').length
// if(password < 5 || password > 10){
//   console.log('придумайте новый пароль')
// } else{
//     console.log('пароль подходит')
// }

//3.1

let str = 'css html php'
console.log(str.substring(0,3))
console.log(str.substring(4,8))
console.log(str.substring(9,12))

//3.2

str = 'http://youtube'
if(str.startsWith('http://')){
    console.log('да')
} else{
    console.log('нет')
}

//3.3

str = 'photo.jpg'
if(str.startsWith('.png') || str.endsWith('.jpg')){
    console.log('да')
} else{
    console.log('нет')
}

//3.4

str = 'явно больше чем пять символов';
if(str.length > 5){
    console.log(str.substring(0, 5) + '...');
}else{
    console.log(str);
}

//6

str = 'evnghepro;bjht';
console.log(str.substring(0,3) + '!!!' + str.substring(8, str.length))

//8.1
str = 'html css php'
console.log(str.split(' '))

//8.2
str = ["html", "css", "php"]
console.log(str.join(','))

//8.3
let $date = "2013-12-31"
console.log($date.split('-').join('.'))
//13
let number = 12345678
console.log(new Intl.NumberFormat("ru-RU").format(number))

// Доп

//1
console.log(('var_test_text'.split('_')).map((el) => el = (el.slice(0,1)).toUpperCase() + el.slice(1)).join(''))
//2
let arr = [1, 2, 3, 4, 43, 53, 65]
console.log(arr.filter((int) => (int.toString()).includes('3')))


