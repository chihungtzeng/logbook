#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
#include <chook.h>
#include <util_cpp.h>

static void *(*malloc_std)(size_t nSize);
static void *(*realloc_std)(void *ptr, size_t nSize);
static void (*free_std)(void *ptr);

void *malloc_hooked(size_t);
void *realloc_hooked(void *, size_t);
void free_hooked(void *);

void *malloc(size_t nSize){
    return malloc_hooked(nSize);
}

void free(void *ptr){
    free_hooked(ptr);
}

void *realloc(void *ptr, size_t nSize){
    return realloc_hooked(ptr, nSize);
}

void __attribute__((constructor))
init_malloc_std(){
    malloc_std = dlsym(RTLD_NEXT, "malloc");
    free_std = dlsym(RTLD_NEXT, "free");
    realloc_std = dlsym(RTLD_NEXT, "realloc");
}

void __attribute__((destructor))
dtor_show_peak(){
    printf("peak memory: %zu\n", get_peak());
}


void *malloc_hooked(size_t nSize){
    void *ptr = malloc_std(nSize);
    //printf("allocate %zu bytes at %p\n", nSize, ptr);
    add_record((size_t)ptr, nSize);
    return ptr;
}

void *realloc_hooked(void *ptr, size_t nSize){
    void *new_ptr = 0;
    if (ptr == NULL){
        return malloc_hooked(nSize);
    }
    if (nSize == 0){
        free_hooked(ptr);
    }
    new_ptr = (void *) realloc_std(ptr, nSize);
    if (new_ptr != NULL){
        delete_record((size_t)ptr);
        add_record((size_t)new_ptr, nSize);
    }
    return new_ptr;
}

void free_hooked(void *ptr){
    if (ptr){
       // printf("free %p\n", ptr);
        free_std(ptr);
        delete_record((size_t) ptr);
    }
}
