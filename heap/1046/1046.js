//solution 1
var lastStoneWeight = function (stones) {
  const removeLargest = () => {
    const largestIndex = stones.indexOf(Math.max(...stones));
    let temp = stones[largestIndex];
    stones[largestIndex] = stones[stones.length - 1];
    stones[stones.length - 1] = temp;
    return stones.pop();
  };
  while (stones.length > 1) {
    const stone1 = removeLargest();
    const stone2 = removeLargest();
    if (stone1 !== stone2) {
      stones.push(stone1 - stone2);
    }
  }
  return stones.length > 0 ? stones[0] : 0;
};
