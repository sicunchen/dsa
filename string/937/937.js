// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare

var reorderLogFiles = function(logs) {
  const getBody = s => s.slice(s.indexOf(" ") + 1);
  const isDigit = s => /\d/.test(s);
  const letterCompare = (a, b) => {
    const n = getBody(a).localeCompare(getBody(b));
    if (n !== 0) return n;
    else return a.localeCompare(b);
  };
  let letterLogs = [];
  let digitLogs = [];
  for (const log of logs) {
    if (isDigit(getBody(log))) digitLogs.push(log);
    else letterLogs.push(log);
  }
  return [...letterLogs.sort(letterCompare), ...digitLogs];
};
