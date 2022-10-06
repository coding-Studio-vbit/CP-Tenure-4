/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
    
    let string = "";
    let j = 0;
    for (i in t) {
        if (t[i] === s[j]) {
            string += t[i];
            j++;
        }
    }
    return string === s;
};

console.log(isSubsequence("abc", "ahbgdc"));
console.log(isSubsequence("axc", "ahbgdc"));