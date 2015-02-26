int loop_while(int a,int b)
{
	int result = 1;
	while (a<b)
	{
		result *= (a+b);
		a++;
	}
	return result;
}