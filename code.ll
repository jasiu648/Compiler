


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
@str1 = constant [20 x i8] c"hello from function\00"
define i64 @myFunc() nounwind {
%str1 = alloca [20 x i8]
%1 = bitcast [20 x i8]* %str1 to i8*
call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %1, i8* align 1 getelementptr inbounds ([20 x i8], [20 x i8]* @str1, i32 0, i32 0), i64 20, i1 false)
%ptrstr1 = alloca i8*
%2 = getelementptr inbounds [20 x i8], [20 x i8]* %str1, i64 0, i64 0
store i8* %2, i8** %ptrstr1
%h= alloca i8*
store i8* %2, i8** %h
%3 = load i8*, i8** %ptrstr1
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %3)
%5 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %5)
%myFunc = alloca i32
store i32 0, i32* %myFunc
%7 = load i64, ptr %myFunc
ret i64 %7
}
@str2 = constant [16 x i8] c"hello from main\00"
@h = global [1 x i8] c"\00"
@a = global i32 0
@b  = global i64 0
define i32 @main() nounwind{
%str2 = alloca [16 x i8]
%1 = bitcast [16 x i8]* %str2 to i8*
call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %1, i8* align 1 getelementptr inbounds ([16 x i8], [16 x i8]* @str2, i32 0, i32 0), i64 16, i1 false)
%ptrstr2 = alloca i8*
%2 = getelementptr inbounds [16 x i8], [16 x i8]* %str2, i64 0, i64 0
store i8* %2, i8** %ptrstr2
store i8* %2, i8** @h
%3 = call i64 @myFunc()
%4 = load i8*, i8** %ptrstr2
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %4)
%6 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %6)
store i32 5, i32* @a
%8 = load i32, i32* @a
%9 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i32 %8)
%10 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %10)
store i64 4, i64* @b
%12 = load i64, i64* @b
%13 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %12)
%14 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %14)
ret i32 0 }
