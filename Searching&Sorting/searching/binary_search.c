#include <stdio.h>
int main()
{
    int size,a[100],low,high,mid,i,j;
    printf("Size of array:");
    scanf("%d",&size);
    printf("Enter the sorted array: ");
    for(i=0;i<size;i++)
        scanf("%d",&a[i]);
    printf("Enter the element to search: ");
    scanf("%d",&j);
    low=0;
    high=size-1;
    mid=(high+low)/2;
    while(low<=high)
    {
        if(a[mid]==j)
        {
            printf("element %d found on position: %d",j,mid+1);
            break;
                
        }
        else if(j>a[mid])
            low=mid+1;
        else if(j<a[mid])
            high=mid-1;
       mid=(high+low)/2;
    }
    if(low>=high)
        printf("Not found");
    return 0;
}
