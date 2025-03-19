#include <bits/stdc++.h>
#define Int int
using namespace std;
#define lli long long int 
#define int lli
#define ff(i,a,b) for(int i=a;i<=b;i++)
#define fb(i,b,a) for(int i=b;i>=a;i--)
#define fast ios_base::sync_with_stdio(false);
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define nl cout<<"\n";
#define minus cout<<"-1\n";
#define vi vector<int>
#define pb push_back
#define pp pair<int,int>
#define p(n) cout << n << endl;
#define i(n) int n; cin >> n;
#define all(v) v.begin(),v.end()
vi input(int n){vi v; for(int i = 0; i < n; i++){int x; cin >> x; v.pb(x);} return v;};
#define N 1000000007;
void file(){
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin) ;
  freopen("output.txt", "w", stdout) ;
  #endif
}
  void ohio()
{
  int n,k; cin >> n >> k;
  if(n & 1){
    int cnt = 1;
    n-= k;
    cnt += (n+(k-1)-1)/(k-1);
    p(cnt);
  }
  else{
        int  cnt = (n+(k-1)-1)/(k-1);
        p(cnt);
  }
}   
signed main(){
    fast;
    file();
    int hawktuah;   cin >> hawktuah;  while (hawktuah--)
   ohio();
}