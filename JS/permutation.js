let data = "1234";
const store = new Set();
var count = 0;
let permutation = (word, perm = "") => {
  if (word.length == 0) {
    store.add(perm);
  }
  for (let i = 0; i < word.length; i++) {
    let sub = word.slice(0, i) + word.slice(i + 1, word.length);
    permutation(sub, perm + word[i]);
  }
  return store;
};

let result = permutation(data);
console.log(result, result.size);
