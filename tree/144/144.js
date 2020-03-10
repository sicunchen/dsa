// solution 1
var preorderTraversal = function(root) {
  let ans = [];
  traverse(root, ans);
  return ans;
};

const traverse = (root, ans) => {
  if (root === null) return;
  ans.push(root.val);
  traverse(root.left, ans);
  traverse(root.right, ans);
};

// solution 2
var preorderTraversal = function(root) {
  let ans = [];
  let stack = [];
  if (root) stack.push(root);
  while (stack.length !== 0) {
    const curr = stack.pop();
    ans.push(curr.val);
    if (curr.right) stack.push(curr.right);
    if (curr.left) stack.push(curr.left);
  }
  return ans;
};
