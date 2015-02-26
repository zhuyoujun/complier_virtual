#include<iostream>
#include<string>
using std::string;

using std::cin;
using std::cout;
using std::endl;

int main(void)
{
	string s1("hello");
    string s2 = "hello world!";
    string s3 = "hiya.";
    cout<<"s1 = "<<s1<<endl;
    cout<<"s2 = "<<s2<<endl;
    cout<<"s3 = "<<s3<<endl;
    cout<<"compare s1 and s2?"<<(s1<s2)<<endl;
    cout<<"compare s2 and s3?"<<(s1>s2)<<endl; 
    cout<<s1+s2<<endl;

    for (auto c:s1)
    	cout<<c<<endl;
    return 0;  
}