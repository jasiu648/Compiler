declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%a = alloca i32
%b = alloca i32
br i1 0, label %true1, label %false1
true1:
%1 = load i32, i32* %b
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %1)
br label %false1
false1:
ret i32 0 }

