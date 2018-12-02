#include <cstdlib>

void leak_func(){
	long double *p = new long double(5.0);
	int *i = new int(5);
}

int main(int argc, char *argv[]){
    leak_func();
	return EXIT_SUCCESS;
}
