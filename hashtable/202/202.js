/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
  let set = new Set();
  while (n !== 1 && !set.has(n)) {
    set.add(n);
    n = getNext(n);
  }
  return n === 1;
};

const getNext = n => {
  let sum = 0;
  while (n > 0) {
    sum += (n % 10) * (n % 10);
    n = Math.floor(n / 10);
  }
  return sum;
};
