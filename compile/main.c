#include <stdio.h>
#include <windows.h>

int main(){
    int a, i;
    scanf("%d", &a);
    for(i = 1; i <= 9; i++){
        printf("%d * %d = %d\n", a, i, a*i);
    }
    printf("\n\n");
	system("pause");
    return 0;
}