#include<stdio.h>
#include<string.h>

typedef unsigned char *byte_pointer;

void show_bytes(byte_pointer start,int len)
{
    int i;
    for(i = 0; i<len;i++)
    {
	printf(" %.2x",start[i]);
    }
    printf("\n");
}

void show_int(int x)
{
  show_bytes((byte_pointer)&x,sizeof(int));
}

void show_float(float f)
{
  show_bytes((byte_pointer)&f,sizeof(float));
}

void show_pointer(void *x)
{
  show_bytes((byte_pointer)&x,sizeof(void *));
}

/*
 main(void)
{
    int ival = 12345;
    float fval = (float)ival;
    int *pval = &ival;
    char *s = "abcdef";
    show_int(ival);
    show_float(fval);
    show_pointer(pval);
    show_bytes((byte_pointer)s,strlen(s));

}
*/
