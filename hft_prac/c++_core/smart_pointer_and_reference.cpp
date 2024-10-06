#include<iostream>
#include<memory>


class MyClass {
public:
	MyClass() {
		std::cout << "MyClass Constructor\n";
	}
	
	~MyClass() {
		std::cout << "MyClass Destructor\n";
	}	
};



class MyClass2 {
public:
	std::shared_ptr<MyClass2> sharedPtr;
	std::weak_ptr<MyClass2> weakPtr;

	MyClass2() {
		std::cout << "MyClass2 Constructor\n";
	}

	~MyClass2() {
		std::cout << "MyClass2 Destructor\n";
	}

};



int main()
{

	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif


// Smart Pointers

	// Unique Pointer
		// std::unique_ptr<MyClass> ptr = std::make_unique<MyClass>();

	// Shared Pointer
		// std::shared_ptr<MyClass> ptr1 = std::make_shared<MyClass>();
		// {
		// 	std::shared_ptr<MyClass> ptr2 = ptr1;
		// 	std::cout << "ptr2 created, use count: " << ptr1.use_count() << '\n';
		// }
		// std::cout << "ptr2 out of scope, use count: " << ptr1.use_count() << '\n';


	// Weak Pointer

		std::shared_ptr<MyClass2> ptr1 = std::make_shared<MyClass2>();
		ptr1->sharedPtr = ptr1;
		ptr1->weakPtr = ptr1;

		std::cout << "Shared Pointer Use Count: " << ptr1.use_count() << '\n';
		std::cout << "Weak Pointer Expired: " << ptr1->weakPtr.expired() << '\n';


	return 0;

}