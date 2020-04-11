// solution 1
class MinStack {
  constructor() {
    this.stack = [];
  }

  push(x) {
    let currMin = this.getMin();
    if (currMin === null || x < currMin) {
      currMin = x;
    }
    this.stack.push([x, currMin]);
  }

  pop() {
    this.stack.pop();
  }

  top() {
    return this.stack[this.stack.length - 1][0];
  }

  getMin() {
    if (this.stack.length === 0) {
      return null;
    } else {
      return this.stack[this.stack.length - 1][1];
    }
  }
}

// solution 2
class Node {
  constructor(x, currMin, next) {
    this.val = x;
    this.currMin = currMin;
    this.next = next;
  }
}
class MinStack {
  constructor() {
    this.head = null;
  }
  push(x) {
    let currMin = this.getMin();
    if (currMin === null || x < currMin) {
      currMin = x;
    }
    this.head = new Node(x, currMin, this.head);
  }
  pop() {
    const topVal = this.head.val;
    this.head = this.head.next;
    return topVal;
  }
  top() {
    return this.head.val;
  }
  getMin() {
    return this.head ? this.head.currMin : null;
  }
}

//solution 3
class MinStack {
  constructor() {
    this.stack = [];
    this.mins = [Infinity];
  }

  push(x) {
    if (x <= this.getMin()) {
      this.mins.push(x);
    }
    this.stack.push(x);
  }
  pop() {
    const elem = this.stack.pop();
    if (elem === this.getMin()) {
      this.mins.pop();
    }
  }
  top() {
    return this.stack[this.stack.length - 1];
  }

  getMin() {
    return this.mins[this.mins.length - 1];
  }
}
