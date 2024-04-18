from utils import *

class LLVMGenerator():

    header_text = ""
    main_text = ""
    reg = 1
    br = 0
    brstack = Stack()

    def func_decl_int(self, id):
        self.header_text += f"define i32 @{id} nouwind {{\n"

    def func_return_int(self):
        self.header_text += f"ret i32 0 }}\n"

    def icmp(self, id, value):
        pass
    
    def if_start(self):
        self.br += 1
        self.main_text += f"br i1 {self.reg - 1}, label %true{self.br}, label %false{self.br}\n"
        self.main_text += f"true{self.br}:\n"
        self.brstack.push(self.br)
        pass

    def if_end(self):
        b = self.brstack.pop()
        self.main_text += f"br label %false{b}\n"
        self.main_text += f"false{b}:\n"
        pass

    def printf_id_int(self, id):
        self.main_text += f"%{self.reg} = load i32, i32* %{id}\n"
        self.reg += 1
        self.main_text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %{self.reg-1})\n"
        self.reg += 1

    def printf_id_float(self, id):
        self.main_text += f"%{self.reg} = load float, float* %{id}\n"
        self.reg += 1
        self.main_text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i64 0, i64 0), float %{self.reg-1})\n"
        self.reg += 1
    
    def printf(self, id):
        if '.' in id:
            self.main_text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 {id})\n"
        else:
            self.main_text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 {id})\n"
        self.reg += 1

    def read(self, id):
        
        self.main_text += f"%{self.reg} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{id})\n"
        self.reg += 1

    def declare_int(self, id):
        self.main_text += f"%{id} = alloca i32\n"

    def declare_float(self, id):
        self.main_text += f"%{id} = alloca float\n"

    def declare_bool(self, id):
        self.main_text += f"%{id} = alloca i32"

    def assignInt(self, id, value):
        self.main_text += f"store i32 {value}, i32* %{id}\n"

    def assignFloat(self, id, value):
        self.main_text += f"store float {value}, float* %{id}\n"

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