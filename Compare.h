#include<iostream>
using namespace std;
//float marks=0;
template<class T,class U>
int CompareTest_EQ(T a,U b,float w=10)
{
    //cout<<"hello";
   // cout<<a<<","<<b<<endl;
    if(a==b)
    {
        cout<<"Test Passed"<<endl;
	return 1;
       //marks+=w;
    }
    else{
        cout<<"One Test Failed.."<<endl;
	return 0;
    }
    //cout<<marks<<endl;
}
template<class T,class U>
int CompareTest_LT(T a,U b,float w=10)
{
    if(a<b)
    {
//       marks+=w;
return 1;
    }
    else{
        cout<<"One Test Failed.."<<endl;
	return 0;
    }
}
template<class T,class U>
int CompareTest_GT(T a,U b,float w=10)
{
    if(a>b)
    {
       //marks+=w;
	return 1;
    }
    else{
        cout<<"One Test Failed.."<<endl;
return 0;
    }
}