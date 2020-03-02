var compress = function(chars) {
  let read = (write = 0);
  while (read < chars.length) {
    let currChar = chars[read];
    let currCount = 0;
    while (read < chars.length && chars[read] === currChar) {
      currCount++;
      read++;
    }
    chars[write] = currChar;
    write++;
    if (currCount > 1) {
      for (let d of String(currCount).split("")) {
        chars[write] = d;
        write++;
      }
    }
  }
  return write;
};
