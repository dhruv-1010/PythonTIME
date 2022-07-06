#include <iostream>
using namespace std;
void encrpyt(char s[],int keys,int length){
    int i;

    for(i = 0;i<length;i++){
        s[i] = s[i]+keys;
    }
    cout<<s;
}


int main(){
    char s[1000];
    int key,i=0;
    cout<<"Enter your string :"<<endl;
    for (i = 0;s[i]=='\0'; i++)
    {
        cin >> s[i];
    }    
    cout<<"Enter your key :"<<endl;
    cin>>key;
    cout<<"Your Encrypted string is :"<<endl;
    encrpyt(s,key,i);

    return 0;
}