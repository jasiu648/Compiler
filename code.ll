declare i32 @printf(ptr, ...)
@.str = private unnamed_addr constant [3 x i8] c"%f\00", align 1

define i32 @main() {
    entry:
  %0 = alloca float, align 4
  store float 1.000000e+00, float* %0, align 4
  %1 = load float, float* %0, align 4
  %2 = fpext float %1 to double
  %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x 
            i8], [3 x i8]* @.str, i64 0, i64 0), double %2)
  ret i32 0
}
