var isIsomorphic = function (s, t) {
    
    let map = new Map();
    let set = new Set();
    for (let i = 0; i < s.length; i++) {
        if (map.has(s[i])) {
            if (map.get(s[i]) != t[i]) {
                return false;
            }
        } else {
            if (set.has(t[i])) {
                return false;
            }
            map.set(s[i], t[i]);
            set.add(t[i]);
        }
    }
    return true;
}
console.log(isIsomorphic("egg", "add"));
console.log(isIsomorphic("paper", "title"));
console.log(isIsomorphic("leet", "code"));

// console.log("a".charCodeAt(0));