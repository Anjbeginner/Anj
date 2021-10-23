#include <iostream>

int main() {
    // Write C++ code here
    int input;
    int number;
    int i;
    std::cout<<"enter number";
    std::cin>>input;
    number=input;
    for(i=input-1;i>0;i--){
        number=number*i;
    }
    std::cout<<"factorial is:"<<number;
    return 0;
}
