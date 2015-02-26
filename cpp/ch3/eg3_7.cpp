#include<iostream>
#include<string>
using std::string;

using std::cin;
using std::cout;
using std::endl;

int main(void)
{
	string s1("hello");
    for (auto c:s1)
    	cout<<c<<endl;
    return 0;  
}