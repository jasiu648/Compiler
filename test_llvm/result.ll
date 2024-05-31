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
@a1 = global i32 0
@a2  = global i64 0
@a3  = global i64 0
@b1 = global double 0.0
@b2 = global double 0.0
@b3 = global double 0.0
@c1  = global i64 0
@c2 = global double 0.0
@c3 = global double 0.0
@d1  = global i64 0
@d2  = global i64 0
@d3  = global i64 0
@d4 = global double 0.0
@d5 = global double 0.0
@d6 = global double 0.0
@e1  = global i64 0
@e2  = global i64 0
@e3  = global i64 0
define i32 @main() nounwind{
store i32 2, i32* @a1
store i64 2, i64* @a2
%1 = load i32, ptr @a1
%2 = load i64, ptr @a2
%3 = sext i32 2 to i64
%4 = add i64 %3, 2
store i64 %4, i64* @a3
%5 = load i64, i64* @a3
%6 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %5)
%7 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %7)
store double 21.37, double* @b1
store double 6.9, double* @b2
%9 = load double, ptr @b1
%10 = load double, ptr @b2
%11 = fsub double 21.37, 6.9
store double %11, double* @b3
%12 = load double, double* @b3
%13 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %12)
%14 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %14)
store i64 3, i64* @c1
store double 4.5, double* @c2
%16 = load i64, ptr @c1
%17 = load double, ptr @c2
%18 = uitofp i64 3 to double
%19 = fmul double %18, 4.5
store double %19, double* @c3
%20 = load double, double* @c3
%21 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %20)
%22 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %22)
store i64 10, i64* @d1
store i64 2, i64* @d2
%24 = load i64, ptr @d1
%25 = load i64, ptr @d2
%26 = sdiv i64 10, 2
store i64 %26, i64* @d3
%27 = load i64, i64* @d3
%28 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %27)
%29 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %29)
store double 44.4, double* @d4
store double 11.4, double* @d5
%31 = load double, ptr @d4
%32 = load double, ptr @d5
%33 = fdiv double 44.4, 11.4
store double %33, double* @d6
%34 = load double, double* @d6
%35 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %34)
%36 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %36)
store i64 3, i64* @e1
store i64 5, i64* @e2
%38 = load i64, ptr @e1
%39 = load i64, ptr @e2
%40 = srem i64 3, 5
store i64 %40, i64* @e3
%41 = load i64, i64* @e3
%42 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %41)
%43 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %43)
ret i32 0 }
