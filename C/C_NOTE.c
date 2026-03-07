
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

// #include <stdio.h>

// int main (void) {
//     int num;
//     char name[10];
//     int select;
//     printf("name: ");
//     scanf("%s", name);
//     printf("name is [%s]. \n yes 1, no 2", name);
//     scanf("%d", &select);
//     if (select == 1) {  
//         printf("%s yes", name);
//     } else {
//         printf("%s no", name);
//     }
//         return 0;
// }

// #include <stdio.h>

// main() {
//     int x;
//     puts ("select number: 1, 2, 3");
//     scanf("%d", &x);
//     if (x == 1) {
//         printf("you select 1");
//     } else if (x == 2) {
//         printf("you select 2");
//     } else if (x == 3) {
//         printf("you select 3");
//     } else {
//         printf("you select wrong number");
//     }
// }

// #include <stdio.h>

// main (){
//     int value;
//     printf("10이하의 숫자면 무한반복 \n");
//     do {
//         scanf ("%d", &value);
//     } while (value <=10);
// printf("10보다 큰 숫자입니다.");    
// }

// #include <stdio.h>

// main (){
//     int i;
//     for (i = 0; i < 10; i++) {
//         printf("%d\n", i);
//     }
// }

// #include <stdio.h>

// main(){
//     int i;
//     int sum = 0;
//     for (i = 0; i < 10; i++) {
//         printf("%d \n", sum = sum + i);
//     }
//     printf ("\n 1부터 10까지 수의 합: %d", sum);
// }

// #include <stdio.h>

// main (){
//     int i, n, sum = 0;
//     printf("Enter a number: ");
//     scanf("%d", &n);
//     for (i = 0; i < 10; i++) {
//         printf("%d \n", sum = sum + i);
//     }
//     printf ("\n 1부터 %d까지 수의 합: [%d]", n, sum);
// }

// #include <stdio.h>

// main (){
//     int i, x, n;
//     printf("반복하고 싶은 숫자는 ?: ");
//     scanf("%d", &x);
//     printf("몇 번 반복할까요 ?: ");
//     scanf("%d", &n);
//     for (i = 0; i < n; i++) {
//         printf("%d \n", x);
//     }
//     printf ("\n %d를 %d번 반복했습니다.", x, n);
// }

// #include <stdio.h>

// main (){
//     int i, sum;
//     sum = 0;
//     for (i=1; i<=10; i++){
//         if (i%2==0)
//         sum = sum + i;
//     }
//     printf ("짝수의 합 : %d\n", sum);
// }

// #include <stdio.h>

// main (void){
//     int i, n, m, sum;
//     sum = 0;
//     puts ("첫 번째 숫자 입력:");
//     scanf("%d", &n);
//     puts ("마지막 숫자 입력:");
//     scanf("%d", &m);
//     for (i=n; i<=m; i++){
//         if (i%2!=0)
//         sum = sum + i;
//     }
//     printf ("%d부터 %d까지의 홀수의 합 : %d\n", n, m, sum);
// }

// #include <stdio.h>

// main (){
//     int i, n;
//     printf("몇 단을 할까요?: ");
//     scanf("%d", &n);
//     for (i=1; i<=10; i++){
//         printf("%d x %d = %d\n", n, i, n*i);
//     }
// }


// #include <stdio.h>

// main (){
//     int i, j;
//     for (i=1; i<=10; i++){
//         for (j=1; j<=10; j++){
//             printf("%d x %d = %d\n", i, j, i*j);
//         }
//     }
// }

// #include <stdio.h>
// #include <windows.h>

// main (){
//     int i;
//     for (i=1; i<11; i++){
//         printf("*\n");
//         Sleep(10);
//     }
// }

