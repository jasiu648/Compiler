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
%testClass = type {i64, double, i1}
define i64 @testClass_Create_Default(%testClass* %this) nounwind {
%1 = getelementptr %testClass, %testClass* %this, i32 0, i32 0
store i64 5, i64* %1
%2 = getelementptr %testClass, %testClass* %this, i32 0, i32 1
store double 78.98, double* %2
%3 = getelementptr %testClass, %testClass* %this, i32 0, i32 2
store i1 true, i1* %3
%testClass_Create_Default = alloca i32
store i32 0, i32* %testClass_Create_Default
%4 = load i64, ptr %testClass_Create_Default
ret i64 %4
}
define i64 @testClass_writeClass(%testClass* %this) nounwind {
%1 = getelementptr %testClass, %testClass* %this, i32 0, i32 0
%2 = load i64, i64* %1
%a = alloca i64
store i64 %2, i64* %a
%3 = getelementptr %testClass, %testClass* %this, i32 0, i32 1
%4 = load double, double* %3
%ab = alloca double
store double %4, double* %ab
%5 = load i64, i64* %a
%6 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %5)
%7 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %7)
%9 = load double, double* %ab
%10 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %9)
%11 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %11)
%testClass_writeClass = alloca i32
store i32 0, i32* %testClass_writeClass
%13 = load i64, ptr %testClass_writeClass
ret i64 %13
}
@test = global %testClass zeroinitializer
define i32 @main() nounwind{
%1 = getelementptr %testClass, %testClass* @test
%2 = call i64 @testClass_Create_Default (ptr %1)
%3 = getelementptr %testClass, %testClass* @test
%4 = call i64 @testClass_writeClass (ptr %3)
ret i32 0 }
