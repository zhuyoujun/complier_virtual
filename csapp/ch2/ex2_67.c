#include<stdio.h>
#include"show_bytes.c"

/*return 1 when any bit of x equals 1,otherwise return 0.
*/
int int_size_is32()
{
  int set_msb = 1<<31;
  //int beyond_msb = 1<<32;
  int beyond_msb = set_msb<<1;
  printf("set_msb = %x,beyond_msb = %x\n",set_msb,beyond_msb);
  return set_msb && (!beyond_msb);
}

main()
{ 
  printf("result = %d\n",int_size_is32());
}
