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
%myStr = type {double, double}
@s = global %myStr zeroinitializer
@a = global double 0.0
@b = global double 0.0
define i32 @main() nounwind{
%1 = getelementptr %myStr, %myStr* @s, i32 0, i32 0
store double 4.0, double* %1
%2 = getelementptr %myStr, %myStr* @s, i32 0, i32 1
store double 3.14, double* %2
%3 = getelementptr %myStr, %myStr* @s, i32 0, i32 0
%4 = load double, double* %3
store double %4, double* @a
%5 = load double, double* @a
%6 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %5)
%7 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %7)
%9 = getelementptr %myStr, %myStr* @s, i32 0, i32 1
%10 = load double, double* %9
store double %10, double* @b
%11 = load double, double* @b
%12 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %11)
%13 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %13)
ret i32 0 }
