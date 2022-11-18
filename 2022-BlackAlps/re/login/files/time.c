/*
 * gcc -Wall -ldl -shared -o rand.so rand.c
 */
#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <time.h>


time_t time( time_t * pTime );
time_t time( time_t * pTime ){
	return 1668632762+300;

}
