/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    let num = x;
    let temp = 0;
    let i = 1;
    while (num > 0) {
        temp = temp*10 + (num) % 10 ;
        num = Math.floor(num/10);

        i = i * 10;
    }
    return (temp === x);

    // var str = "" + x;
    // var rev = ""

    // for (let i = str.length-1; i >= 0; i--){
    //     rev+= str[i]
    // }
    // return rev == x;
    
};

console.log(isPalindrome(121))
console.log(isPalindrome(10))