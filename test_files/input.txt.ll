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
@d  = global i64 0
@g  = global i64 0
@e  = global i64 0
@AA = global i32 0
@BB = global i32 0
@CC = global i32 0
@DD  = global i64 0
@EE  = global i64 0
@A  = global i64 0
@B  = global i64 0
@C  = global i64 0
@D  = global i64 0
@E  = global i64 0
@F  = global i64 0
define i32 @main() nounwind{
store i64 2, i64* @a
store i64 3, i64* @b
%1 = load i64, ptr @a
%2 = load i64, ptr @b
%3 = add i64 2, 3
store i64 %3, i64* @c
%4 = load i64, i64* @c
%5 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %4)
%6 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %6)
store i64 10, i64* @d
%8 = load i64, ptr @c
%9 = load i64, ptr @d
%10 = add i64 %3, 10
store i64 %10, i64* @g
%11 = load i64, ptr @g
%12 = load i64, ptr @b
%13 = add i64 %10, 3
store i64 %13, i64* @e
%14 = load i64, i64* @e
%15 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %14)
%16 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %16)
store i32 3, i32* @AA
store i32 7, i32* @BB
%18 = load i32, ptr @AA
%19 = load i32, ptr @BB
%20 = add i32 3, 7
store i32 %20, i32* @CC
%21 = load i32, i32* @CC
%22 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i32 %21)
%23 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %23)
store i64 10, i64* @DD
%25 = load i32, ptr @CC
%26 = load i64, ptr @DD
%27 = sext i32 %20 to i64
%28 = add i64 %27, 10
store i64 %28, i64* @EE
%29 = load i64, i64* @EE
%30 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %29)
%31 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %31)
store i64 3, i64* @A
store i64 7, i64* @B
%33 = load i64, ptr @A
%34 = load i64, ptr @B
%35 = add i64 3, 7
store i64 %35, i64* @C
%36 = load i64, i64* @C
%37 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %36)
%38 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %38)
store i64 5, i64* @D
store i64 92233720368547758, i64* @E
%40 = load i64, ptr @D
%41 = load i64, ptr @E
%42 = add i64 5, 92233720368547758
store i64 %42, i64* @F
%43 = load i64, i64* @F
%44 = call i32 (ptr, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpl, i32 0, i32 0), i64 %43)
%45 = getelementptr [2 x i8], [2 x i8]* @str_ptr, i32 0, i32 0
call i32 (i8*, ...) @printf(i8* %45)
ret i32 0 }

