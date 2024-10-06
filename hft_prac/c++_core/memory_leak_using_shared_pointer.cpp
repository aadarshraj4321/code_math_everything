#include <iostream>
#include <memory>

class NodeB;

class NodeA {
public:
    std::shared_ptr<NodeB> nodeB;
    NodeA() { std::cout << "NodeA Constructor" << std::endl; }
    ~NodeA() { std::cout << "NodeA Destructor" << std::endl; }
};

class NodeB {
public:
    std::shared_ptr<NodeA> nodeA;
    NodeB() { std::cout << "NodeB Constructor" << std::endl; }
    ~NodeB() { std::cout << "NodeB Destructor" << std::endl; }
};

int main() {


    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    
    


    std::shared_ptr<NodeA> a = std::make_shared<NodeA>();
    std::shared_ptr<NodeB> b = std::make_shared<NodeB>();

    a->nodeB = b;
    b->nodeA = a;

    return 0;
}
