#include <stdio.h>
void swap(int *a,int *b)
{
    int t=*a;
    *a=*b;
    *b=t;
}
int partition(int a[],int st,int end)
{
    int piviot=a[end];
    int j=st-1;
    for(int i=st;i<end;i++)
    {
        if(a[i]<=piviot)
        {
            j++;
            swap(&a[j],&a[i]);
        }
    }
    swap(&a[j+1],&a[end]);
    return j+1;
}
void quick_sort(int a[],int st,int end)
{
    if(st<end)
    {
        int j=partition(a,st,end);
        quick_sort(a,st,j-1);
        quick_sort(a,j+1,end);
    }
}
int main()
{
    int a[]={10,2,7,15,9,2,1};
    int n=sizeof(a)/sizeof(int);
    quick_sort(a,0,n-1);
    for(int i=0;i<n;i++)
        printf("%d ",a[i]);

    return 0;
}
