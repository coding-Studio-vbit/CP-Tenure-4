// let arr = [15, 49, 10, 9, 500, 1000]
let arr = [3 ,1 ,4 ,1 ,5 ,9 ,2 ,6]
let diff = Infinity, diff2 = Infinity,index = 0
arr.sort(key = (a, b) => a - b)

for (let i = 0; i < arr.length - 2; i++) {
    let val = arr[i + 1] - arr[i] + arr[i + 2] - arr[i + 1]
    if ( val < diff) {
        diff = val; 
        index = i;
    }
}
console.log(diff)
