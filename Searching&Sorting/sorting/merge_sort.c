#include <stdio.h>

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}
void merge_sort(int a[],int st,int end)
{
    if(st<end)
    {
        int mid = st+(end-st)/2;
        merge_sort(a,st,mid);
        merge_sort(a,mid+1,end);
        merge(a,st,mid,end);
    }
}
int main()
{
    int a[]={5,8,3,4,8,2,6};
    int n=sizeof(a)/sizeof(int);
    merge_sort(a,0,n-1);
    for(int i=0;i<n;i++)
        printf("%d ",a[i]);

    return 0;
}
