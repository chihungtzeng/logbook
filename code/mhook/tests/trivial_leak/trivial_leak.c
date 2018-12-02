#include <stdio.h>
#include <stdlib.h>

void leak_func(){
	int *p = (int *) malloc(sizeof(int));
}

int main(int argc, char *argv[]){
    leak_func();
	return EXIT_SUCCESS;
}
