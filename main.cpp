#include <bits/stdc++.h>
#include <fstream>
 

#define f first
#define s second

using namespace std;

const int N = (int)1e6 + 10;

int n; // number of articles
unordered_map<string, int> cnt[N];
pair<double, int> vals[N]; //{value and id of article} double becouse we will add coefficients later

void precalc () { // to count tags in each articles. Interact with python
  freopen("output.txt", "r", stdin);
  string s;
  int i = 0;
  while(getline(cin, s)){
    for(auto x : s){
      if(x == '~'){
        cnt[i][s]++;
        s.clear();
      }else s += x;  
    }
    i++;
    //assert(i < N);
    //if(i == 100) break;         
  } 
  n = i;
  cin.clear();
}
vector<string> get_tags(){
  freopen("getTag.txt", "r", stdin);
  string s, t;   
  getline(cin, s);
  vector<string> cur;
  for(auto x : s){
    if(x == ' '){
      cur.push_back(t);
      t.clear();
    }else t += x; 
  }
  cin.clear();
  return cur;       
}

int main () {
  precalc();
  freopen("KeyWords.in", "r", stdin);
  string s;
  getline(cin, s);
  cin.clear();
  
  vector<string> tags = get_tags(); // get tags from python
  
  for(int i = 0; i < n; i++){
    int sum = 0, mn = (int)1e9;
    for(auto x : tags){
      sum += cnt[i][x];

    }
    vals[i].f = sum;
    vals[i].s = i; 
  }
  sort(vals, vals + n);     
  reverse(vals, vals + n);     
  freopen("KeyWords.out", "w", stdout);
  for(int i = 0; i < 5; i++)
    cout << vals[i].s << " - article\n";
  
}     