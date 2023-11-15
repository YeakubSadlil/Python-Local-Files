#include<bits/stdc++.h>
using namespace std;

long long fr,last,tc,n,x,tru=0;
string solution;

int main(){
    cin>>tc;
    tru=0;
    for (int i=0;i<tc; ++i) {
        cin>>n;
        tru=0;
        solution="";
        for(int j=0;j<n;++j) {
            cin>>x;
            if(j==0){
                last=x;
                fr=x;
                solution+= '1';
            }
            else if(!tru and x>=fr and last<=x){
                last=x;
                solution+= '1';
            }
            
            else if(!tru and x<=fr and last>x){
                tru=1;
                last=x;
                solution+= '1';
            }
            else if(tru and x>=last and x<=fr){
                last=x;
                solution+='1';
            }
            else solution+='0';
        }
        cout<<solution<<endl;
    }
}