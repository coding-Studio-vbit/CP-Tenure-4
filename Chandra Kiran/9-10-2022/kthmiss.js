var findKthPositive = function (arr, k) {
    let miss = [], offset = 0;
    for (let i = 1; i <= 1000; i++) {
        if (arr[i + offset - 1] !== i) {
            miss.push(i);
            offset--;
        }
        if(miss.length > k){
            break;
        }
    }
    console.log(miss.length, miss[miss.length - 2])
    return miss.length > k? miss[k - 1]: 1000+(k - miss.length);
};
