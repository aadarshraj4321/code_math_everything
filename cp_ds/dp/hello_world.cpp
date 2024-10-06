#include<bits/stdc++.h>



int fact(int n) 
{
	if(n == 0) return 1;
	return n * fact(n - 1);
}


int main()
{

	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif


	int n; std::cin >> n;
	std::cout << fact(n);

	return 0;
}