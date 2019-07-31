#include <stdio.h>
int main()
{
    int size,a[100],min,i,j,temp;
    printf("Size of array:");
    scanf("%d",&size);
    printf("Enter the unsorted array: ");
    for(i=0;i<size;i++)
        scanf("%d",&a[i]);
    
    for(i=0;i<size-1;i++)
    {
        for(j=0;j<size-1;j++)
        {
            if(a[j+1]<a[j])
            {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }    
        }
    }
    printf("Sorted array: ");
    for(i=0;i<size;i++)
        printf("%d ",a[i]);
    return 0;
}
