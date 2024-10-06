#include<iostream>
#include<memory>


class Child;

class Parent {
public:
	std::shared_ptr<Child> childPtr;
	~Parent() {
		std::cout << "Parent Destructor\n";
	}
};


class Child {
public:
	std::weak_ptr<Parent> parentPtr;
	~Child() {
		std::cout << "Child Destructor\n";
	}
};


int main() {

	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif


	std::shared_ptr<Parent> parent = std::make_shared<Parent>();
	std::shared_ptr<Child> child = std::make_shared<Child>();

	parent->childPtr = child;
	child->parentPtr = parent;

	return 0;
}









