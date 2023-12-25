#include<iostream>
#include<map>
using namespace std;

string crypt(string cipher, int key)
{
    int n = cipher.length();
    string ans;
    char p;
    for(int i=0;i<n;i++)
    {
        if(cipher[i]>='A' && cipher[i]<='Z')
        {
            p = (cipher[i]-'A'+key)%26+'A';
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
    // string cipher_text = "Wuymul wcjbyl  Gynbix ch qbcwb yuwb fynnyl ch nby jfuchnyrn cm lyjfuwyx vs u fynnyl migy zcryx hogvyl iz jimcncihm xiqh nby ufjbuvyn. Nby gynbix cm hugyx uznyl Dofcom Wuymul, qbi omyx cn ch bcm jlcpuny willymjihxyhwy.";

    string cipher_text = "lzwhdsaflwplzsktwwfwfujqhlwvloauwoalzskzaxluahzwjmkafylogvaxxwjwflcwqkgfuwoalzkwnwfsfvsysafoazwdwnwfozauzakksewskwfujqhlafygfuwoalzlzwugetafwvcwqwayzlwwf";

    map<char, int> mp;

    for(int i=0;i<cipher_text.size();i++)
    {
        cipher_text[i] = toupper(cipher_text[i]);
    }

    cout<<cipher_text<<'n';

    for(int i=0;i<cipher_text.size();i++)
    {
        mp[cipher_text[i]]++;
    }

    int m = 0;
    char c;

    for(auto i: mp)
    {
        cout<<i.first<<" "<<i.second<<'\n';
    }

    for(auto i: mp)
    {
        if(i.second>m && i.first != ' '){
            m=i.second;
            c=i.first;
        }
    }

    int key;
    key = abs(c-'E');
    cout<<"Key: "<<key<<'\n';
    cout<<"Text: ";
    cout<<crypt(cipher_text,key)<<'\n';

    
    key = abs(c-'T');
    cout<<"Key: "<<key<<'\n';
    cout<<"Text: ";
    cout<<crypt(cipher_text,key)<<'\n';

    
    key = abs(c-'A');
    cout<<"Key: "<<key<<'\n';
    cout<<"Text: ";
    cout<<crypt(cipher_text,key)<<'\n';
  
    
    key = abs(c-'O');
    cout<<"Key: "<<key<<'\n';
    cout<<"Text: ";
    cout<<crypt(cipher_text,key)<<'\n';

    
    key = abs(c-'I');
    cout<<"Key: "<<key<<'\n';
    cout<<"Text: ";
    cout<<crypt(cipher_text,key)<<'\n';

    
    key = abs(c-'N');
    cout<<"Key: "<<key<<'\n';
    cout<<"Text: ";
    cout<<crypt(cipher_text,key)<<'\n';

    
    key = abs(c-'S');
    cout<<"Key: "<<key<<'\n';
    cout<<"Text: ";
    cout<<crypt(cipher_text,key)<<'\n';

    
    // key = abs(c-'H');
    // cout<<"Key: "<<key<<'\n';
    // cout<<"Text: ";
    // cout<<crypt(cipher_text,key)<<'\n';

    

    return 0;
}