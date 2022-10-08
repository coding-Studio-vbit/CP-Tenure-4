/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
    let map = {};

    for (let key in s) {
        map[s[key]] = (map[s[key]] + 1) || 1;
    }
    console.log(map)
    const elements = new Set(s.split(""));
    let count = 0;
    elements.forEach(e => {
        if (map[e] % 2 === 0) {
            count += map[e]
            elements.delete(e)
        }
        else if (map[e] % 2 === 1 && map[e] !== 1) {
            count += map[e] - 1;
            map[e] = 1;
        }
    })
    if (count % 2 === 0 && (Array.from(elements).length > 0)) {
        console.log(666)
        count++;
    }

    return count;

};

longestPalindrome("ssseeeeeeeer")
console.log(longestPalindrome("bb"))


//        seeeereeees