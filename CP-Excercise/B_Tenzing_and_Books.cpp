#include<bits/stdc++.h>
using namespace std;

int main() {
    int t; cin>>t;
    while(t--){
        int n,x; 
        cin>>n>>x;
        int stack1[n+5] = {0},stack2[n+5] = {0},stack3[n+5] = {0};
        for (int i=0;i<n;i++) cin>>stack1[i];
        for (int i=0;i<n;i++) cin>>stack2[i]; 
        for (int i=0;i<n;i++) cin>>stack3[i]; 
        int ans=0;
        for (int i=0;i<n;i++) 
        {
            if(stack1[i]>x) break;
            int store=x;
            int stacking =stack1[i];
            bool checker=true;
            while(store>0 and stacking>0) {
                int bit1 = store&1;
                int bit2 =stacking&1;
                if (bit1==0 and bit2==1) {checker=false; break; }
                store>>=1;
                stacking>>=1;
                }
            if(checker) ans|=stack1[i];
            else break;
        }
        for (int i=0;i<n;i++) 
        {
            if(stack2[i]>x) break;
            int store=x;
            int stacking =stack2[i];
            bool checker=true;
            while(store>0 and stacking>0) {
                int bit1 = store&1;
                int bit2 =stacking&1;
                if (bit1==0 and bit2==1) 
                {
                    checker=false;
                    break;
                }
                store>>=1;
                stacking>>=1;
                }
            if(checker) ans|=stack2[i];
            else break;
        }
        for (int i=0;i<n;i++) 
        {
            if(stack3[i]>x) break;
            int store=x;
            int stacking =stack3[i];
            bool checker=true;
            while(store>0 and stacking>0) {
                int bit1 = store&1;
                int bit2 =stacking&1;
                if (bit1==0 and bit2==1) 
                {
                    checker=false;
                    break;
                }
                store>>=1;
                stacking>>=1;
                }
            if(checker) ans|=stack3[i];
            else break;
        }
        if(ans==x) cout<<"Yes\n";
        else cout<<"No\n";
    }
    return 0;
}  