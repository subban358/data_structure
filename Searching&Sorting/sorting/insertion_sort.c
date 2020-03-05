#include <stdio.h>
void sort(int arr[], int n)
{
    int k = 0;
    for(int i = 0; i < n; i ++)
    {
        int temp = arr[i];
        int hole = i;
        while (hole >= 0 && arr[hole-1] >= temp)
        {
            arr[hole] = arr[hole-1];
            hole--;
        }
        arr[hole] = temp;
    }
    while(n)
    {
        printf("%d ",arr[k++]);
        n--;
    }
}
int main()
{
    int arr[5] = {8,7,9,3,1};
    sort(arr, 5);
    return 0;
}
