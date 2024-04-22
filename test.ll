; ModuleID = 'test.c'
source_filename = "test.c"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msvc19.39.33521"

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 1, ptr %1, align 4
  store i32 2, ptr %2, align 4

  %4 = load i32, ptr %1, align 4
  %5 = load i32, ptr %2, align 4
  %6 = mul nsw i32 %4, %5
  
  %7 = load i32, ptr %2, align 4
  %8 = sub nsw i32 0, %7
  %9 = load i32, ptr %1, align 4
  %10 = sub nsw i32 0, %9
  %11 = mul nsw i32 %8, %10
  %12 = add nsw i32 %6, %11
  %13 = load i32, ptr %1, align 4
  %14 = load i32, ptr %2, align 4
  %15 = sub nsw i32 0, %14
  %16 = sdiv i32 %13, %15
  %17 = add nsw i32 %12, %16
  store i32 %17, ptr %3, align 4
  ret i32 0
}

attributes #0 = { noinline nounwind optnone uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}

!0 = !{i32 1, !"wchar_size", i32 2}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"uwtable", i32 2}
!3 = !{i32 1, !"MaxTLSAlign", i32 65536}
!4 = !{!"clang version 17.0.1"}
