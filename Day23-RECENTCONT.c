#include <stdio.h>
#include <string.h>

int main() {
    int T; 
    scanf("%d", &T);

    while (T--) {
        int N; 
        scanf("%d", &N);

        int count_START38 = 0;
        int count_LTIME108 = 0;
        char contest_code[10]; 

        
        for (int i = 0; i < N; i++) {
            scanf("%s", contest_code);
            if (strcmp(contest_code, "START38") == 0) {
                count_START38++;
            } else if (strcmp(contest_code, "LTIME108") == 0) {
                count_LTIME108++;
            }
        }

       
        printf("%d %d\n", count_START38, count_LTIME108);
    }

    return 0;
}