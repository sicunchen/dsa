//have trouble compiling
// const searchBigSortedArray = function (reader, target) {
//   // write your code here
//   let start = 0;
//   let index = 1;
//   let end;
//   while (reader.get(index) < target) {
//     index = index * 2;
//   }
//   start = Math.floor(index / 2);
//   end = index;

//   while (start + 1 < end) {
//     let mid = start + Math.floor((end - start) / 2);
//     if (target <= reader.get(mid)) {
//       end = mid;
//     } else {
//       start = mid;
//     }
//   }
//   if (reader.get(start) === target) {
//     return start;
//   } else if (reader.get(end) === target) {
//     return end;
//   }
//   return -1;
// };
