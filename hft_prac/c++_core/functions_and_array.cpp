#include<bits/stdc++.h>



int fact(int n);
int add(int a, int b);
double add(double a, double b);



int main()
{

	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif


	int n; std::cin >> n;
	std::cout << fact(n) << '\n';


	return 0;
}




int fact(int n) {
	if(n <= 0) {
		return 1;
	}

	return n * fact(n - 1);
} 