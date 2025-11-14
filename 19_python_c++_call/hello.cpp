#include <iostream>

extern "C" void greet(const char* name) {
    std::fprintf(stderr, "[trace] %10s:%-5d %32s() SRIDHAR\n", __FILE__, __LINE__, __func__);
    std::cout << "Hello, " << name << " from C++" << std::endl;
}

int main (int argc, char * const argv[]) {
    // std::cout << "Hello, World CPP\n";
    greet("Chinnu");
    return 0;
}