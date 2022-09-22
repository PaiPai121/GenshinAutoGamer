// #include "iostream.h"
#include  <stdio.h>
#include <stdlib.h>
int main()
{
    char *s = "Intel is a \0 good company.";
    // cout << s;
    printf("%d\n",sizeof(s));
    return 1;
}