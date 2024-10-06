#include<bits/stdc++.h>



int main()
{

	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif

	// Pointer
		// int a = 10;
		// int *p = &a;
		// std::cout << "Value of a: " << a << '\n';
		// std::cout << "Address of a: " << &a << '\n';
		// std::cout << "Value of p (address of a): " << p << '\n';
		// std::cout << "Value pointed to by p: " << *p << '\n';


	// Null pointer
		// int *p = nullptr;

		// if(p == nullptr) {
		// 	std::cout << "p is a null pointer\n";
		// }


	// Void Pointer
		// int a = 10;
		// float b = 5.5;
		// void *ptr; // void pointer

		// ptr = &a; // Point to int
		// std::cout << "Value of a: " << *(static_cast<int*>(ptr)) << '\n';

		// ptr = &b;
		// std::cout << "Value of b: " << *(static_cast<float*>(ptr)) << '\n';


	// Dangling Pointer
		// int *ptr = new int(10);
		// delete ptr; // Free memory
		// ptr = nullptr;



	// Wild Pointer
		// int *ptr; // Wild pointer
		// p = nullptr; // Avoid wild pointer by initializing 





	// Pointer Arithmetic
		// int arr[5] = {1, 2, 3, 4, 5};
		// int *p = arr;

		// for(int i = 0; i < 5; i++) {
		// 	std::cout << "Value at arr[" << i << "]: " << *p << '\n';
		// 	p++;
		// }






	// Dynamic Memory Allocation
		// int *p = new int; // Allocate memory or an integer
		// *p = 10;
		// std::cout << "Value: " << *p << '\n';
		// delete p; // Free allocated memory


		// int *arr = new int[5]; // Allocate memory for an array of 5 integers
		// for(int i = 0; i < 5; i++) {
		// 	arr[i] = i + 1;
		// }

		// for(int i = 0; i < 5; i++) {
		// 	std::cout << arr[i] << " ";
		// }

		// delete[] arr; // Free allocated memory for array



	// Advanced Dynamic Memory Allocation
	int rows = 3, cols = 4;
	int **arr = new int*[rows];

	for(int i = 0; i < rows; i++) {
		arr[i] = new int[cols];
	}


	// Initialize the 2D array
	for(int i = 0; i < rows; i++)  {
		for(int j = 0; j < cols; j++) {
			arr[i][j] = i * cols + j + 1;
		}
	}

	// Print the 2D array
	for(int i = 0; i < rows; i++) {
		for(int j = 0; j < cols; j++) {
			std::cout << arr[i][j] << " ";
		}
		std::cout << '\n';
	}



	// Deallocated memory
	for(int i = 0; i < rows; i++) {
		delete[] arr[i];
	}

	delete[] arr;













	return 0;
}