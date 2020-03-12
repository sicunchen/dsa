class Graph {
    constructor(noOfVertices) {
        this.noOfVertices = noOfVertices;
        this.AdjList = new Map();
    }

    addVertex(v) {
        this.AdjList.set(v, []);
    }

    addEdge(v, w) {
        this.AdjList.get(v).push(w);
        this.AdjList.get(w).push(v);
    }

    printGraph() {
        for (let key of this.AdjList.keys()) {
            let conc = "";

            for (let value of this.AdjList.get(key)) {
                conc += value + " ";
            }

            console.log(key + "->" + conc);
        }
    }

    //main DFS method
    dfs(startingNode) {
        let visited = [];
        for (let key of this.AdjList.keys()) {
            visited[key] = false;
        }
        this.dfsUtil(startingNode, visited);
    }

    //recursive function which processes and explore all the adjacent vertex of the vertex with which it is called
    dfsUtil(v, visited) {
        visited[v] = true;
        console.log(v)
        let neighbors = this.AdjList.get(v);
        for (let neighbor of neighbors) {
            if (!visited[neighbor]) {
                this.dfsUtil(neighbor, visited);
            }
        }
    }

}
var g = new Graph(6);

var vertices = ['A', 'B', 'C', 'D', 'E', 'F'];

// adding vertices 
for (var i = 0; i < vertices.length; i++) {
    g.addVertex(vertices[i]);
}

// adding edges 
g.addEdge('A', 'B');
g.addEdge('A', 'D');
g.addEdge('A', 'E');
g.addEdge('B', 'C');
g.addEdge('D', 'E');
g.addEdge('E', 'F');
g.addEdge('E', 'C');
g.addEdge('C', 'F');
// prints all vertex and 
// its adjacency list 
// A -> B D E 
// B -> A C 
// C -> B E F 
// D -> A E 
// E -> A D F C 
// F -> E C 
g.printGraph();
g.dfs('A'); 