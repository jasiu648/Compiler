declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%1 = alloca i32
store i32 4, ptr %1
%2 = alloca i32
store i32 2, ptr %2
%3 = alloca i32
store i32 5, ptr %3
%4 = load i32, ptr %3
%5 = load i32, ptr %2
%6 = mul nsw i32 %5, %4
%7 = load i32, ptr %6
%8 = load i32, ptr %1
%9 = add nsw i32 %8, %7
%10 = alloca i32
store i32 %9, ptr %10
%11 = load i32, i32* %10
%12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %11)
ret i32 0 }

