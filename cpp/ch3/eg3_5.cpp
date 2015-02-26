#include<iostream>
#include<string>
using std::string;

using std::cin;
using std::cout;
using std::endl;

int main(void)
{
	string s1;
    while(getline(cin,s1))
    {
    	if(!s1.empty())
    	{
    		cout<<s1<<endl;
    	}
    	
    }
    return 0;
}