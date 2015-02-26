#include<stdio.h>
#include"show_bytes.c"

/*suppose int x,if all bits in x is 1,or all bits in x is 0,or
the most significant byte is all 1 or the least significant bitbyte is all 0,return 1
otherwise return 0.
*/
void byte_judge(int x)
{
  int a = !(~x);
  int b = !(x);
  int c = (x>>(sizeof(int)-1))^(0xFF);
  int d = !(x&0xFF);
  printf("x = %x\n",x);
  printf("a = %d\n",a);
  printf("b = %d\n",b);
  printf("c = %x\n",c);
  printf("d = %d\n",d);
  printf("\n");
}

main()
{ 
  int x = 0xFF000001;
  byte_judge(x);

  x = 0x0;
  byte_judge(x);

  x = 0xFF000000;
  byte_judge(x);

  x = ~0x0;
  byte_judge(x);
}
