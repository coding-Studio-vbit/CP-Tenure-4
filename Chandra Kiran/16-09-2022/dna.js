// var findRepeatedDnaSequences = function (s) {
//     let i = 0, j = 0;
//     let res = [];
//     while (i + 10 <= s.length) {
//         j = i+1
//         let key = s.slice(i, i + 10)
//         while(j+10 <= s.length){
//             if(key==s.slice(j,j+10)){
//                 res.push(key)
//                 break
//             }
//             j++
//         }
//         i++
//     }
//     return [...new Set(res)]
// };

var findRepeatedDnaSequences = function (s) {
    let map = new Map();
    let res = [];
    for (let i = 0; i + 10 <= s.length; i++) {
        let key = s.slice(i, i + 10)
        if (map.has(key)) {
            map.set(key, map.get(key) + 1)
        } else {
            map.set(key, 1)
        }
    }
    for (let [key, value] of map) {
        if (value > 1) {
            res.push(key)
        }
    }
    return res

};

console.log(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
console.log(findRepeatedDnaSequences("AAAAAAAAAAA"))
