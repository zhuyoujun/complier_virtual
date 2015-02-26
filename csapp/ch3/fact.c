int fact_do(int n)
{
	int result = 1;
	do
	{
        result *= n;
        n--;
	}while(n>1);
	return result;
}