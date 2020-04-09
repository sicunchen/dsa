//#1
var backspaceCompare = function(S, T) {
  return help(S) === help(T);
};

const help = string => {
  let result = [];
  for (ch of string) {
    if (ch === "#") {
      result.pop();
    } else {
      result.push(ch);
    }
  }
  return result.join();
};

//#2
var backspaceCompare = function(S, T) {
  let S_pointer = S.length - 1;
  let T_pointer = T.length - 1;
  while (S_pointer >= 0 || T_pointer >= 0) {
    S_pointer = findNonSkippingPoint(S, S_pointer);
    T_pointer = findNonSkippingPoint(T, T_pointer);
    //if there's still "meat" left after all the skipping, check if  the remaining characters are the same starting from the back.If not, return false
    if (S_pointer >= 0 && T_pointer >= 0 && S[S_pointer] !== T[T_pointer]) {
      return false;
    }
    //if one of the string is exhausted before the other, return false. Can't just simply use S_pointer<0||T_pointer<0, because there are situations when both strings are exhausted, e.g.("ab##","c#d#")
    if (S_pointer >= 0 !== T_pointer >= 0) {
      return false;
    }
    S_pointer--;
    T_pointer--;
  }
  return true;
};

//this helper method returns the "comparing" pointer after all the skipping
const findNonSkippingPoint = (string, i) => {
  let skip = 0;
  while (i >= 0) {
    if (string[i] == "#") {
      skip++;
      i--;
    } else if (skip > 0) {
      skip--;
      i--;
    } else {
      break;
    }
  }
  return i;
};
