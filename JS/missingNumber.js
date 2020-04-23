function solution(A) {
  let j = 0;
  let temp;
  for (let i = 0; i < A.length; i++) {
    if (A[i] <= 0) {
      temp = A[i];
      A[i] = A[j];
      A[j] = temp;
      j++;
    }
  }

  console.log(A, j);
}

let a = [-1, 3, -3, 5, -2];

solution(a);
