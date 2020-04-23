let data = "hello world";

let reverse = str => {
  if (str.length < 2) {
    return str;
  }
  return reverse(str.substring(1) + str[0]);
};
