#include <stdio.h>
int main()
{
    int size,a[100],min,i,j,temp;
    printf("Size of array:");
    scanf("%d",&size);
    printf("Enter the array: ");
    for(i=0;i<size;i++)
        scanf("%d",&a[i]);
    printf("Enter the element to search: ");
    scanf("%d",&j);
    
    for(i=0;i<size;i++)
    {
        if(a[i]==j)
        {
            printf("%d is found on location %d ",j,i+1);
            break;
        }
    }
    
    return 0;
}
