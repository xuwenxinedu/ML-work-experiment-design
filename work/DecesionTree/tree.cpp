#include <iostream>
#include <string>
#include <math.h>

class tree
{
private:
    /* data */
    std::string s = "this is class tree";
public:
    tree(std::string s);
    ~tree();
};

tree::tree(std::string s)
{
    this->s = s;
    std::cout << s << std::endl;
}

tree::~tree()
{
}


void print()
{
    std::cout << "tree.cpp print\n";
}

// int main()
// {
//     std::cout << "yep" << std::endl;
    
//     return 0;
// }