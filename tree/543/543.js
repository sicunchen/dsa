var diameterOfBinaryTree = function(root) {
  if (!root) return 0;
  const lh = getHeight(root.left);
  const rh = getHeight(root.right);
  const ld = diameterOfBinaryTree(root.left);
  const rd = diameterOfBinaryTree(root.right);
  return Math.max(lh + rh, Math.max(ld, rd));
};

const getHeight = root => {
  if (!root) return 0;
  const lh = getHeight(root.left);
  const rh = getHeight(root.right);
  return 1 + Math.max(lh, rh);
};

//more compact solution
var diameterOfBinaryTree = function(root) {
  let lp = 0;

  const getHeight = root => {
    if (!root) return 0;
    const lh = getHeight(root.left);
    const rh = getHeight(root.right);
    lp = Math.max(lp, lh + rh);
    return 1 + Math.max(lh, rh);
  };
  getHeight(root);

  return lp;
};
