// solution 1
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} s
 * @param {TreeNode} t
 * @return {boolean}
 */
var isSubtree = function(s, t) {
  let s1 = preOrder(s);
  let s2 = preOrder(t);
  return s1.includes(s2);
};

var preOrder = function(node) {
  if (node == null) return "X";
  // # and space are for single node cases, e.g. [12] and [2]
  return (
    "#" + node.val + " " + preOrder(node.left) + " " + preOrder(node.right)
  );
};

//solution 2: https://www.youtube.com/watch?v=SffOawHju1Y&feature=emb_logo
var isSubtree = function(s, t) {
  if (s == null) return false;
  return equalTrees(s, t) || isSubtree(s.left, t) || isSubtree(s.right, t);
};

var equalTrees = function(s, t) {
  if (s == null && t == null) {
    return true;
  } else if (s == null || t == null) {
    return false;
  } else if (s.val !== t.val) {
    return false;
  } else {
    return equalTrees(s.left, t.left) && equalTrees(s.right, t.right);
  }
};
