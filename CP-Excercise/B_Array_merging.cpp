#include <iostream>
#include <vector> 
#include <unordered_map> 
using namespace std; 
void solve() 
{ 
    int n ; 
    cin >> n; 
    vector<int> arr(n); 
    vector<int> brr(n);
    for (int i = 0; i < n; i++)
    { 
        cin >> arr[i];
    } 
    for (int i = 0; i < n; i++)
    { 
        cin >> brr[i];
    } 
    unordered_map<int, int> a; 
    unordered_map<int, int> b; 
    int count = 1; 
    for (int i = 1; i <= n; i++) 
    {
        if (i == n) 
        {
            a[arr[i - 1]] = max(count, a[arr[i - 1]]); 
            break; 
        } 
        if (arr[i] == arr[i - 1])
            count++;
        else 
        {
            a[arr[i - 1]] = max(count, a[arr[i - 1]]);
            count=1;
        }
    }


    count = 1;
    for (int i = 1; i <= n; i++) 
    { 
        if (i == n) 
        { 
            b[brr[i - 1]] = max(count, b[brr[i - 1]]); 
            break; 
        } 
        if (brr[i] == brr[i - 1]) 
        { 
            count++; 
        } 
        else
        {
            b[brr[i - 1]] = max(count, b[brr[i - 1]]); 
            count = 1;
        } 
    } 
    int ans = 0; 
    for (int e : arr)
        {
            ans = max(ans, a[e] + b[e]); 
        }
    for (int e : brr)  
        ans = max(ans, b[e] + a[e]);
    cout << ans << endl; 
}

int main()
{
    int tc;
    cin>>tc;
    while(tc--)
    solve();
}
