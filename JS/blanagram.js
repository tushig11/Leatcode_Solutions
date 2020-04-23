function banagram(word1, word2) {
  if (word1.length != word2.length) {
    return false;
  }

  let store = new Map();

  for (let c of word1) {
    if (store.has(c)) {
      store.set(c, store.get(c) + 1);
    } else {
      store.set(c, 1);
    }
  }

  let flag = false;

  for (let c of word2) {
    if (store.has(c) && store.get(c) != 0) {
      store.set(c, store.get(c) - 1);
    } else {
      if (flag) {
        return false;
      }
      flag = true;
    }
  }

  return flag ? true : false;
}

let word1 = "listen";
let word2 = "silerr";

console.log(banagram(word1, word2));
