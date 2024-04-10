class LLVMGenerator():

    header_text = ""
    main_text = ""
    reg = 1

    def printf(self, id):
        self.main_text += f"%{self.reg} = load i32, i32* %{id}\n"
        self.reg += 1
        self.main_text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %{self.reg-1})\n"
        self.reg += 1

    def read(id):
        global main_text, reg
        main_text += f"%{reg} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{id})\n"
        reg += 1

    def declare(id):
        global main_text
        main_text += f"%{id} = alloca i32\n"

    def assign(id, value):
        global main_text
        main_text += f"store i32 {value}, i32* %{id}\n"

    def generate(self):
        text = ""
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@strp = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        print(text)
        return text