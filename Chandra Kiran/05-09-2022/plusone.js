var plusOne = function (digits) {
    let num = "";
    for (let i = digits.length - 1; i >= 0; i--){
        num += digits[digits.length - 1 - i]
    }
    num = "" + (BigInt(num) + BigInt(1))
    // console.log(BigInt(num))
    let output = new Array((num).length)

    for (let i = (num).length - 1; i >= 0; i--){
        output[i] = parseInt(num[i]) % 10;
        // num = Math.floor(parseInt(num[i]) / 10)
        num[i] = '\0';
    }
   

    return output
    // recurrsion solution

    // return output;
    length = digits.length;
    if(digits[length - 1]+1<=9){
        digits[length - 1] += 1;
        return digits;
    }
    else{
        if(digits[length-1]===9 && length ===1){
            digits[length-1] = 0;
            digits.unshift(1)
            return digits;
        }
        else{
            digits[length-1] = 0;
            let digit = plusOne(digits.slice(0, length-1));
            digit.push(digits[digits.length-1]);
            return digit;
        }
    } 
};

console.log(plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]))

