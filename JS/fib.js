function Foo(bar) {
  this.a = bar;
  this.b = new Array(bar[0], bar[1], bar[2]);
}

const bar = [10, 10, 10];
const zzz = new Foo(bar);

bar[0] = 100;
bar[3] = 100;

const qux = bar[0] + zzz.a[3] + zzz.b[0];
console.log(qux);
