#include <stdio.h>
int main(void){
float x;
float y;
float z;
float result;
float counter;
float i;
x = 10;
y = 5;
printf("Testing the compiler\n");
printf("%.2f\n", (float)(x));
printf("%.2f\n", (float)(y));
printf("%.2f\n", (float)(x+y));
printf("%.2f\n", (float)(x*y));
printf("Enter a number:\n");
if(0 == scanf("%f", &z)) {
z = 0;
scanf("%*s");
}
if(z>10){
printf("z is greater than 10\n");
result = z*2;
printf("%.2f\n", (float)(result));
}
else if(z==10){
printf("z equals 10\n");
result = z+50;
printf("%.2f\n", (float)(result));
}
else {
printf("z is less than 10\n");
result = z/2;
printf("%.2f\n", (float)(result));
}
start:
printf("This is a label test\n");
goto end;
counter = 1;
while(counter<=5){
printf("%.2f\n", (float)(counter));
counter = counter+1;
}
for(i = 1; i <= 5; i += 1){
printf("%.2f\n", (float)(i*10));
}
if(x>5 && y<10){
printf("Both conditions are true\n");
}
if(x<5 || y>2){
printf("At least one condition is true\n");
}
if(!x==y){
printf("x and y are not equal\n");
}
end:
printf("End of program\n");
return 0;
}
