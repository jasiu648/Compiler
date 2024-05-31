declare i32 @printf(ptr, ...)
declare i32 @__isoc99_scanf(i8*, ...)
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@strss = constant [5 x i8] c"%10s\00"
@strf = constant [3 x i8] c"%f\00"
@strpl = constant [5 x i8] c"%lld\00"
@strlf = constant [4 x i8] c"%lf\00"
@trueStr = constant [5 x i8] c"true\00"
@falseStr = constant [6 x i8] c"false\00"
@strps = constant [4 x i8] c"%s\0A\00"
@str_ptr = constant [2 x i8]c"\0A\00" 
@a = global i1 0
@b = global i1 0
@c = global i1 0
@d = global i1 0
@e = global i1 0
@f = global i1 0
@g = global i1 0
define i32 @main() nounwind{
store i1 1, i1* @a
store i1 0, i1* @b
%1 = load i1, ptr @a
%2 = load i1, ptr @b
%3 = alloca i1
%4 = load i1, i1* @a
br i1 %4, label %evalSecond0, label %False0
evalSecond0:
%5 = alloca i1
%6 = load i1, i1* @b
br i1 %6, label %True0, label %False0
True0:
br label %endLogicalAnd0
False0:
br label %endLogicalAnd0
endLogicalAnd0:
%7 = phi i1 [1, %True0], [0, %False0]
store i1 %7, i1* @c
%8 = load i1, ptr @a
%9 = load i1, ptr @b
%10 = alloca i1
%11 = load i1, i1* @a
br i1 %11, label %True1, label %evalSecond1
evalSecond1:
%12 = alloca i1
%13 = load i1, i1* @a
br i1 %13, label %True1, label %False1
True1:
br label %endLogicalOr1
False1:
br label %endLogicalOr1
endLogicalOr1:
%14 = phi i1 [1, %True1], [0, %False1]
store i1 %14, i1* @d
%15 = load i1, ptr @a
%16 = load i1, ptr @b
%17 = alloca i1
%18 = load i1, i1* @a
%19 = alloca i1
%20 = load i1, i1* @b
%21 = xor i1 %18, %20
store i1 %21, i1* @e
%22 = load i1, ptr @a
%23 = icmp eq i32 0, 1
store i1 %23, i1* @f
%24 = load i1, ptr @b
%25 = icmp eq i32 0, 0
store i1 %25, i1* @g
%26 = load i1, i1* @c
%27 = select i1 %26, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @trueStr, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @falseStr, i32 0, i32 0)
%28 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %27)
%29 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %29)
%31 = load i1, i1* @d
%32 = select i1 %31, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @trueStr, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @falseStr, i32 0, i32 0)
%33 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %32)
%34 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %34)
%36 = load i1, i1* @e
%37 = select i1 %36, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @trueStr, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @falseStr, i32 0, i32 0)
%38 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %37)
%39 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %39)
%41 = load i1, i1* @f
%42 = select i1 %41, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @trueStr, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @falseStr, i32 0, i32 0)
%43 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %42)
%44 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %44)
%46 = load i1, i1* @g
%47 = select i1 %46, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @trueStr, i32 0, i32 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @falseStr, i32 0, i32 0)
%48 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %47)
%49 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %49)
ret i32 0 }
