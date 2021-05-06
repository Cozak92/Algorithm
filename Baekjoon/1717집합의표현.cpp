#include<stdio.h>
#include<string>

int findUnion(int x, int arr[]){
    if(arr[x] == x){
        return x;
    }
    arr[x] = findUnion(x,arr);

    return findUnion(arr[x],arr);
}

void makeUnion(int a, int b,int arr[]){
    int rootA,rootB;

    rootA = findUnion(a,arr);
    rootB = findUnion(a,arr);


    if(rootA < rootB){
        arr[a] = rootA;
        arr[b] = rootA;
    }
    else{
        arr[a] = rootB;
        arr[b] = rootB;
    }
    return;
}


bool isSame(int a,int b){
    if(a==b){
        return true;
    }
    else{
        return false;
    }
}

int main(){

    int n,m;
    scanf("%d %d",&n,&m);
    int arr[1000000];
    for (int i =0; i < n; i++){
        arr[i] = i + 1;
    }
    int order,a,b;
    for(int i =0; i < m; i++){
        scanf("%d %d %d", &order,&a,&b);

        if(order == 0){
            makeUnion(a,b,arr);
        }
        else if(order == 1){
            if (isSame(findUnion(a,arr),findUnion(b,arr))){
                printf("YES");
            }else{
                printf("NO");
            }
        }

    }
    return 0;

}