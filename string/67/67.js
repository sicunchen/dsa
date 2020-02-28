// solution 1
var addBinary = function(a, b) {
  let n = Math.max(a.length, b.length);
  a = a.padStart(n, "0");
  b = b.padStart(n, "0");
  let carry = 0;
  let answer = [];
  for (let i = n - 1; i > -1; i--) {
    if (a[i] == "1") {
      carry += 1;
    }
    if (b[i] == "1") {
      carry += 1;
    }
    if (carry % 2 == 0) {
      answer.push("0");
    } else {
      answer.push("1");
    }
    carry = Math.floor(carry / 2);
  }
  if (carry == 1) {
    answer.push("1");
  }
  return answer.reverse().join("");
};

// solution 2. failed at #194 test case, don't know why
var addBinary = function(a, b) {
  let x = parseInt(a, 2);
  let y = parseInt(b, 2);
  while (y) {
    let carry = (x & y) << 1;
    let answer = x ^ y;
    x = answer;
    y = carry;
  }

  return x.toString(2);
};
