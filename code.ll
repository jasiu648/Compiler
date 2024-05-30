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
@strhhd = constant [5 x i8] c"%hhd\00"
@strhd = constant [4 x i8] c"%hd\00"
@trueStr = constant [5 x i8] c"true\00"
@falseStr = constant [6 x i8] c"false\00"
@strps = constant [4 x i8] c"%s\0A\00"
@str_ptr = constant [2 x i8]c"\0A\00" 
@a = global [3 x i64] zeroinitializer
@b  = global i64 0
@c  = global i64 0
@d  = global i64 0
define i32 @main() nounwind{
%1 = getelementptr inbounds[3 x i64], ptr @a, i64 0, i64 0
store i64 1, ptr %1
%2 = getelementptr inbounds[3 x i64], ptr @a, i64 0, i64 1
store i64 2, ptr %2
%3 = getelementptr inbounds[3 x i64], ptr @a, i64 0, i64 2
store i64 3, ptr %3
%4 = getelementptr inbounds[3 x i64], ptr @a, i64 0, i64 0
%5 = load i64, i64* %4
store i64 %5, i64* @b
%6 = getelementptr inbounds[3 x i64], ptr @a, i64 0, i64 2
%7 = load i64, i64* %6
store i64 %7, i64* @c
%8 = load i64, i64* @b
%9 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %8)
%10 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %10)
%12 = load i64, i64* @c
%13 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %12)
%14 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %14)
%16 = getelementptr inbounds[3 x i64], ptr @a, i64 0, i64 2
store i64 4, ptr %16
%17 = getelementptr inbounds[3 x i64], ptr @a, i64 0, i64 2
%18 = load i64, i64* %17
store i64 %18, i64* @d
%19 = load i64, i64* @d
%20 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %19)
%21 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %21)
ret i32 0 }
