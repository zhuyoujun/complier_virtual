#include<stdio.h>
#include<string.h>
main()
{
    int sum,i;
    char string[20];

    sum = 0;
    strcpy(string,"Hello");

    for (i = 1;i<=10;i++){
       sum +=i;
       sum = square(sum,i);
    }
    printf("sum= %d\n",sum);

}

    square(int big, int temp)
    {
      int i;

      i = big;
      if (big>10) i = i%10;
      return (i*temp);
    }
