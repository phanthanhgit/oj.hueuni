using namespace std;
#include <bits/stdc++.h>
#define FIO ios_base::sync_with_stdio(false); //cin.tie(NULL); cout.tie(NULL)
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
//#define MULTITEST

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

int Month[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};


void omae_wa_mou_shindeiru(){
	ll n; cin >> n;
	for (ll i=1; i<=n; ++i){
		if (i*(i+1)/2>=n){
			ll k = i*(i+1)/2 - n;
			for (int j=1; j<=i; ++j){
				if (j != k) cout << j << endl;
			}
			return;
		}
	}
}

int main(){FIO;
    int t = 1; 
    #ifdef MULTITEST 
        cin >> t;
    #endif
    while(t--){
		omae_wa_mou_shindeiru();
		if (t) cout << "\n";
	}
return 0;}
