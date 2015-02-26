#include<stdio.h>
#include"show_bytes.c"
unsigned replace_bytes(unsigned x,unsigned char b,int i)
{
  unsigned unb = (unsigned)b<<(8*i);
  unsigned mask = ~(0xFF<<(8*i));
  unsigned result;
  result = (x&mask)|unb;
  return result;

}
main()
{
   unsigned int x = 0x12345678;
   unsigned char b = 0xAB;
   unsigned result1 = replace_bytes(x,b,2);
   unsigned result2 = replace_bytes(x,b,0);
  
   show_int(x);
   show_int(result1);
   show_int(result2); 

}
