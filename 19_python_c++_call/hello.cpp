#include <iostream>

extern "C" void greet(const char* name) {
    std::cout << "Hello, " << name << " from C++" << std::endl;
}
