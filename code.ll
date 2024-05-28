


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
@a  = global i64 0
@b  = global i64 0
@c  = global i64 0
define i32 @main() nounwind{
store i64 4, i64* @a
store i64 3, i64* @b
%1 = load i64, ptr @a
%2 = load i64, ptr @b
%3 = add i64 4, 3
store i64 %3, i64* @c
%4 = load i64, ptr @b
%5 = load i64, i64* @c
%6 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %5)
%7 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %7)
ret i32 0 }
