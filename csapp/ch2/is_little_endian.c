#include<stdio.h>

main()
{
    int ival = 12345;
    unsigned char *ptr = &ival;
    unsigned char low8bits = (unsigned char)ival&0xff;
    if (*ptr == low8bits)
    {
        printf("1\n");
    }
    else
    {
        printf("0\n");
    }


}

