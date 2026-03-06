
// #include <stdio.h>

// int main(){
//     printf("Hello, C!\n");
//     return 0;
//     int a;
//     int b;
//     a = 2;
//     b = 3;
//     printf("%d\n", a);
//     printf("%d\n", b);
//     printf("%d\n", a + b);
//     printf("a: %d, b: %d, a + b: %d\n", a, b, a + b);
// }

// #include <stdio.h>

// main () {
//     char x;
//     x = 'A';
//     printf("%c\n", x);
// }

// #include <stdio.h>

// main () {
//     int p;
//     char x;
//     p = 5;
//     x = 'A';
//     printf("p: %d, x: %c\n", p, x);
// }

// #include <stdio.h>

// main (){
//     char x = 'A';
//     char y = '1';
//     int z = 1;
//     printf("x: %c, y: %c, z: %d\n", x, y, z);
// }

// #include <stdio.h>

// main () {
//     int num;
//     puts ("Enter a number:");
//     scanf("%d", &num); 
//     printf("You entered: %d\n", num);
// }

// #include <stdio.h>

// int main (void) {
//     int num;
//     puts ("Enter a number:");
//     scanf("%d", &num);
//     if (num%2 == 0) {
//         printf("짝수");
//     } else {
//         printf("홀수");
//     }
//     return 0;
// }

#include <stdio.h>

int main (void) {
    int num;
    char name[10];
    int select;
    printf("name: ");
    scanf("%s", name);
    printf("name is [%s]. \n yes 1, no 2", name);
    scanf("%d", &select);
    if (select == 1) {  
        printf("%s yes", name);
    } else {
        printf("%s no", name);
    }
        return 0;
}

