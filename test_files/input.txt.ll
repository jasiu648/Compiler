declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%1 = alloca i32
store i32 2, ptr %1
%2 = load i32, ptr %1
%3 = sub nsw i32 0, %2
%4 = alloca i32
store i32 %3, ptr %4
%5 = load i32, i32* %4
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %5)
ret i32 0 }

