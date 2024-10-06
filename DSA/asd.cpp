#include<bits/stdc++.h>



bool isSorted(const std::vector<int>&arr) {
	int n = arr.size();
	for(int i = 0; i < n - 1; i++) {
		if(arr[i] > arr[i + 1]) {
			return false;
		}
	}
	return true;
}

int main()
{

	std::vector<int>arr = {1, 2, 3, 4, 5};
	if(isSorted(arr)) {
		std::cout << "Array sorted\n";
	} else {
		std::cout << "Array not sorted\n";
	}


	return 0;
}