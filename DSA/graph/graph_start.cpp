#include<iostream>



void printDFSGraph(int** edges, int n, int start, bool* visitedArr) {
	std::cout << start << '\n';
	visitedArr[start] = true;
	for(int i = 0; i < n; i++) {
		if(i == start) {
			continue;
		}
		if(edges[start][i] == 1) {
			if(visitedArr[i]) {
				continue;
			}
			printGraph(edges, n, i, visitedArr);
			//edges[start][i] = 0;
		}
	}
}



int main()
{

	// #ifndef ONLINE_JUDGE
	// 	freopen("input.txt", "r", stdin);
	// 	freopen("output.txt", "w", stdout);
	// #endif


	int n, e;
	std::cin >> n >> e;
	int** edges = new int*[n];
	for(int i = 0; i < n; i++) {
		edges[i] = new int[n];
		for(int j = 0; j < n; j++) {
			edges[i][j] = 0;
		}
	}


	for(int i = 0; i < e; i++) {
		int f, s;
		std::cin >> f >> s;
		edges[f][s] = 1;
		edges[s][f] = 1;
	}

	bool* visitedArr = new bool[n];
	for(int i = 0; i < n; i++) {
		visitedArr[i] = false;
	}


	printGraph(edges, n, 0, visitedArr);


}