


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
@str1 = constant [15 x i8] c"function scope\00"
define i64 @testfunction() nounwind {
%str1 = alloca [15 x i8]
%1 = bitcast [15 x i8]* %str1 to i8*
call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %1, i8* align 1 getelementptr inbounds ([15 x i8], [15 x i8]* @str1, i32 0, i32 0), i64 15, i1 false)
%ptrstr1 = alloca i8*
%2 = getelementptr inbounds [15 x i8], [15 x i8]* %str1, i64 0, i64 0
store i8* %2, i8** %ptrstr1
%h= alloca i8*
store i8* %2, i8** %h
%3 = load i8*, i8** %ptrstr1
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %3)
%5 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %5)
%testfunction = alloca i32
store i32 0, i32* %testfunction
%7 = load i64, ptr %testfunction
ret i64 %7
}
@str2 = constant [11 x i8] c"main scope\00"
@h = global [1 x i8] c"\00"
@a = global double 0.0
define i32 @main() nounwind{
%str2 = alloca [11 x i8]
%1 = bitcast [11 x i8]* %str2 to i8*
call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %1, i8* align 1 getelementptr inbounds ([11 x i8], [11 x i8]* @str2, i32 0, i32 0), i64 11, i1 false)
%ptrstr2 = alloca i8*
%2 = getelementptr inbounds [11 x i8], [11 x i8]* %str2, i64 0, i64 0
store i8* %2, i8** %ptrstr2
store i8* %2, i8** @h
%3 = call i64 @testfunction()
%4 = load i8*, i8** %ptrstr2
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %4)
%6 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %6)
store double 6.9, double* @a
%8 = load double, double* @a
%9 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %8)
%10 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %10)
ret i32 0 }
