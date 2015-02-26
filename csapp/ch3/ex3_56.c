int loop(int x, int n)
{
	int result = 0X55555555;
	int mask;
	for(mask = 0XFFFFFFFF;mask!=0;mask = mask>>n)
	{
		result ^= (x&mask);
	}
	return result;
}