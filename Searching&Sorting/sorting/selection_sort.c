#include <stdio.h>
int main()
{
    int size,a[100],min,i,j,temp;
    printf("Size of array:");
    scanf("%d",&size);
    printf("Enter the unsorted array: ");
    for(i=0;i<size;i++)
        scanf("%d",&a[i]);
    
    for(i=0;i<size;i++)
    {
        min = i;
        for(j=i+1;j<size;j++)
        {
            if(a[j]<a[min])
                min=j;
        }
        
        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
        
    }
    printf("Sorted array: ");
    for(i=0;i<size;i++)
        printf("%d ",a[i]);
    return 0;
}
