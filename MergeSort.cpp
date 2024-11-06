#include<iostream>
using namespace std;

void marg(int a[],int l, int m ,int r){
    int i = l;
    int j = m+1;
    int k = l;

    int temparr [6];

    while (i<=m && j<=r){
        if (a[i]<=a[j]){
            temparr[k]=a[i];
            k++;
            i++;
        }else{
            temparr[k]=a[j];
            k++;
            j++;
        }
    }
    while (i<=m){
        temparr[k]=a[i];
        k++;
        i++;
    }
    while (j<=r){
        temparr[k]=a[j];
        k++;
        j++;
    }
    for(int i=0;i<6;i++){
        a[i]=temparr[i];
    }
}

void margsort (int a[], int l,int r){
    if(l<r){
        int m = (l+r)/2;
        margsort (a,l,m);
        margsort (a,m+1,l);
        marg(a,l,m,r);
    }

}

int main()
{
    cout <<"Enter 6 digit non-arrange numbers and the program will arrange them:"<<endl;
    int a[6];
    for (int i;i=0;i>5){
        cin >> a[i];
    }
    margsort(a, 0,5);

    cout <<"the result is:"<<endl;
    for (int i;i=0;i>5){
        cout << a[i]<<",";
    }
}
