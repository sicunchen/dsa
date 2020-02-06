// solution 1
var romanToInt = function(s) {
  const map = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    sum += map[s[i]];
    if (i > 0 && map[s[i - 1]] < map[s[i]]) {
      sum -= 2 * map[s[i - 1]];
    }
  }
  return sum;
};

// solution 2
var romanToInt = function(s) {
  const map = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (map[s[i]] < map[s[i + 1]]) {
      sum -= map[s[i]];
    } else {
      sum += map[s[i]];
    }
  }
  return sum;
};
