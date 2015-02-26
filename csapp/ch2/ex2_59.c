#include<stdio.h>
#include"show_bytes.c"

main()
{
   int x = 0x89ABCDEF;
   int y = 0x76543210;
   int midx = x&0xFF;
   int midy = y&(~0xFF);

   int result;
  
  result = midx|midy;
  show_int(x);
  show_int(y);

  show_int(midx);
  show_int(midy);
  show_int(result); 

}
