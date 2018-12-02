#include <cstdlib>
#include <iostream>
#include <new>

extern void *(*malloc_hooked)(size_t nSize);
extern void (*realloc_hooked)(void *ptr, size_t nSize);
extern void (*free_hooked)(void *ptr);


void *operator new(size_t nSize) throw (std::bad_alloc) {
//    std::cout << "new " << nSize << " bytes at " <<  std::endl;
    void *ptr = malloc(nSize);
    if (!ptr) {
        throw std::bad_alloc();
    }
    return ptr;
}

void *operator new [] (size_t nSize) throw (std::bad_alloc) {
//    std::cout << "new [] " << nSize << " bytes at " << std::endl;
    void *ptr = malloc(nSize);
    if (!ptr) {
        throw std::bad_alloc();
    }
    return ptr;
}

