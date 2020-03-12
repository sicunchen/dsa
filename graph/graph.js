class Graph {
    constructor(noOfVertices) {
        this.noOfVertices = noOfVertices;
        this.AdjList = new Map();
    }

    addVertex(v) {
        this.AdjList.set(v, []);
    }

    addEdge(v,w) {
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
        for (let i = 0; i < this.noOfVertices; i++) {
            visited[i] = false;
        }
        this.dfsUtil(v, visited);
    }

    //recursive function which processes and explore all the adjacent vertex of the vertex with which it is called
    dfsUtil(v, visited) {
        visited[v] = true;
        let neighbors = this.AdjList.get(v);
        for (let neighbor of neighbors) {
            if (!visited[neighbor]) {
                this.dfsUtil(neighbor, visited);
            }
        }
    }

}

