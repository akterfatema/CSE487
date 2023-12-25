#include<iostream>
using namespace std;

string caesar_cipher (string plain_text, int shift)
{
    int n = plain_text.length();
    string ans;
    char p;
    for(int i=0;i<n;i++)
    {
        if(plain_text[i]>='a' && plain_text[i]<='z')
        {
            p = (plain_text[i]-'a'+shift)%26+'a';
        }
        else 
        {
            p = (plain_text[i]-'A'+shift)%26+'A';
        }
        
        ans.push_back(p);
    }
    return ans;
}

string caesar_cipher_decode (string plain_text, int shift)
{
    int n = plain_text.length();
    string ans;
    char p;
    for(int i=0;i<n;i++)
    {
        if(plain_text[i]>='a' && plain_text[i]<='z')
        {
            p = (plain_text[i]-'a'+shift)%26+'a';
        }
        else if(plain_text[i]>='A' && plain_text[i]<='Z')
        {
            p = (plain_text[i]-'A'+shift)%26+'A';
        }
        else{
            ans.push_back(' ');
            continue;
        }
        
        ans.push_back(p);
    }
    return ans;
}

int main()
{
    string plain_text;
   // cout<<"Enter Plain text: ";
    plain_text = "Fahad Ahammed";
   // getline(cin, plain_text);
    cout<<"Enter key: ";
    int shift;
    cin>>shift;
    string cipher_text = caesar_cipher (plain_text, shift);
    cout<<"Cipher Text: ";
    cout<<cipher_text<<'\n';

    cout<<"Decode: "<<'\n';
    for(int i=1;i<=25;i++)
    {
        cout<<i<<" ";
        cout<<caesar_cipher_decode(cipher_text,i)<<'\n';
    }
    cout<<'\n';
    return 0;
}