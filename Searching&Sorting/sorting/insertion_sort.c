#include <stdio.h>
int main()
{
    int size,a[100],min,i,j,temp;
    printf("Size of array:");
    scanf("%d",&size);
    printf("Enter the unsorted array: ");
    for(i=0;i<size;i++)
        scanf("%d",&a[i]);
    
    for(i=1;i<size;i++)
    {
        temp=a[i];
        j=i-1;
        while(j>=0 && a[j]>temp)
        {
            a[j+1]=a[j--];
        }
        a[j+1]=temp;
    }
    printf("Sorted array: ");
    for(i=0;i<size;i++)
        printf("%d ",a[i]);
    return 0;
}
