shift_left2_rightn(int x,int n)
{
    x<<= 2;
    x>>= n;
    //int y = x^x;
    return x;
}