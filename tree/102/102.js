//solution 1
var levelOrder = function (root) {
  let levels = [];
  if (!root) return levels;
  const helper = (node, level) => {
    if (levels.length === level) {
      levels.push([]);
    }
    levels[level].push(node.val);
    if (node.left) helper(node.left, level + 1);
    if (node.right) helper(node.right, level + 1);
  };
  helper(root, 0);
  return levels;
};

//solution 2
var levelOrder = (root) => {
  let levels = [];
  let queue = [];
  if (root) queue.push(root);
  let level = 0;
  while (queue.length !== 0) {
    levels.push([]);
    const levelLen = queue.length;
    //can't directly use queue.length here cuz queue's length changes everytime when you pop the head node
    for (let i = 0; i < levelLen; i++) {
      const node = queue.shift();
      levels[level].push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    level++;
  }
  return levels;
};
