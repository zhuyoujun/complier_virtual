int dw_loop(int x,int y,int n)
{
	do
	{
       x += n;
       y *= n;
       n--;
	}while(n>0&&y<n);
	return x;
}