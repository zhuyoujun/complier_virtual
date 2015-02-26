#include<stdio.h>
#include"show_bytes.c"

/*return 1 when any bit of x equals 1,otherwise return 0.
*/
int any_even_one(unsigned int x)
{
  return !(!(x&(0x5555)));
}

main()
{ 
  unsigned int x = 2;
  int result = any_even_one(x);
  printf("result = %d\n",result);
}
