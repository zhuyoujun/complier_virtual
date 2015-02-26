swap(int *xp, int *yp, int*zp)
{
	int x = *xp;
	int y = *yp;
	int z = *zp;

	*xp = y;
	*yp = z;
	*zp = x;

	int temp = x>>3;
	int t = temp;
	temp--;
	temp = -temp;
	return temp;

}