#include <iostream>
#include<vector>
#include<algorithm>
#include <map>
#include<utility>
#include<cmath>

using namespace std;
vector<pair< double , pair<int,int>>> galaxy2;
vector<pair<double, double>> coord;
int parent[102];
int n;
double ans;

double findRoot(int x){
    if(parent[x] == x){
        return x;
    }
    parent[x] = findRoot(parent[x]);

    return findRoot(parent[x]);
}

void doUnion(int a, int b){
    int rootA = findRoot(a);
    int rootB = findRoot(b);

    if(rootA < rootB){
        parent[rootB] = rootA;
    }
    else parent[rootA] = rootB;
}

void input(){
    double a,b;
    cin >> n;

    for(int i = 0; i < n; i++ ){
        cin >> a >> b;
        parent[i] = i;
        coord.push_back(make_pair(a,b));
    }

}

double findDist(double x, double y, double xx, double yy){
    double dx = (x - xx) * (x-xx);

    double dy = (y - yy) * (y - yy);
    double Dist = sqrt(dx + dy);
 
    return Dist;
}

void solution(){

    for(int i =0; i < n - 1; i++){
        double x = coord[i].first;
        double y = coord[i].second;

        for(int j= i + 1; j < n; j ++){
            double xx = coord[j].first;
            double yy = coord[j].second;

            double dist = findDist(x,y,xx,yy);
            galaxy2.push_back(make_pair(dist ,make_pair(i,j)));
        }
    }

    sort(galaxy2.begin(), galaxy2.end());

    for(int i =0; i < galaxy2.size(); i ++){
        if (findRoot(galaxy2[i].second.first) == findRoot(galaxy2[i].second.second)){
            continue;
        }
        ans += galaxy2[i].first;
        doUnion(galaxy2[i].second.first,galaxy2[i].second.second);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    input();
    solution();

    cout << ans << "\n";
}