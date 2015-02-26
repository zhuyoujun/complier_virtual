#include<iostream>
#include<string>
using std::string;

using std::cin;
using std::cout;
using std::endl;

int main(void)
{
	string s1;
	string s2 = s1;
	string s3 = "hiya";
	string s4(10,'c');

	/*input hello world!*/
	cin>>s1>>s2;
	cout<<s1<<s2<<endl;
}