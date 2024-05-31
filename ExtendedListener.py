from antlr4 import ParseTreeWalker
from antlr_generated.CSoftListener import CSoftListener
from antlr_generated.CSoftParser import CSoftParser

from llvm_generator import LLVMGenerator

from utils import Value, VarType, string_to_type, get_llvm_type_str, llvm_to_type


class ExtendedListener(CSoftListener):

    def __init__(self):

        self.stack = []
        self.variables = []
        self.local_variables = []
        self.functions = []
        self.structs = []
        self.brstack = []
        self.class_variables = []

        self.generator = LLVMGenerator()
        self.funType = 'i64'
        self.classId = ''
        self.globalScope = True
        self.function = None

    def exitExpr(self, ctx: CSoftParser.ExprContext):
        
        if ctx.OrOper():
            l = ctx.condXorStm(0).children[0].children[0].children[0].children[0].children[0].children[0]
            r = ctx.condXorStm(0).children[0].children[0].children[0].children[0].children[0].children[0]

            if l.BOOL():
                left = l.BOOL().symbol.text
            elif l.ID():
                left = l.ID().symbol.text
            else:
                left = self.stack.pop()
            
            if r.BOOL():
                right = r.BOOL().symbol.text
            elif r.ID():
                right = r.ID().symbol.text
            else:
                right = self.stack.pop()
            
            sym1 = self._get_bool_sym(left)
            sym2 = self._get_bool_sym(right)

            self.generator.or_operation(left, right, sym1, sym2)
            self.stack.append(Value("%" + str(self.generator.reg - 1), VarType.BOOL))
    
    
    def exitCondXorStm(self, ctx: CSoftParser.CondXorStmContext):
        if ctx.XorOper():
            l = ctx.condStmAnd(0).children[0].children[0].children[0].children[0].children[0]
            r = ctx.condStmAnd(1).children[0].children[0].children[0].children[0].children[0]
            if l.BOOL():
                left = l.BOOL().symbol.text
            elif l.ID():
                left = l.ID().symbol.text
            else:
                left = self.stack.pop()
            
            if r.BOOL():
                right = r.BOOL().symbol.text
            elif r.ID():
                right = r.ID().symbol.text
            else:
                right = self.stack.pop()
            
            sym1 = self._get_bool_sym(left)
            sym2 = self._get_bool_sym(right)
            
            self.generator.xor_operation(left, right, sym1, sym2)
            self.stack.append(Value("%" + str(self.generator.reg - 1), VarType.BOOL))
    
    def exitCondStmAnd(self, ctx: CSoftParser.CondStmAndContext):
        
        if ctx.AndOper():
            l = ctx.condStmRel(0).children[0].children[0].children[0].children[0]
            r = ctx.condStmRel(1).children[0].children[0].children[0].children[0]
            if l.BOOL():
                left = l.BOOL().symbol.text
            elif l.ID():
                left = l.ID().symbol.text
            else:
                left = self.stack.pop()
            
            if r.BOOL():
                right = r.BOOL().symbol.text
            elif r.ID():
                right = r.ID().symbol.text
            else:
                right = self.stack.pop()
            
            sym1 = self._get_bool_sym(left)
            sym2 = self._get_bool_sym(right)

            self.generator.and_operation(left, right, sym1, sym2)
            self.stack.append(Value("%" + str(self.generator.reg - 1), VarType.BOOL))
    
    def exitCondStmRel(self, ctx: CSoftParser.CondStmRelContext):
        if ctx.RelOper():
            l = ctx.addExpr(0).children[0].children[0].children[0]
            r = ctx.addExpr(1).children[0].children[0].children[0]
            if l.ID():
                left = l.ID().symbol.text
            elif l.INT():
                left = l.INT().symbol.text
            elif l.FLOAT():
                left = l.FLOAT().symbol.text
            else:
                left = self.stack.pop()
            
            if r.ID():
                right = r.ID().symbol.text
            elif r.INT():
                right = r.INT().symbol.text
            elif r.FLOAT():
                right = r.FLOAT().symbol.text
            else:
                right = self.stack.pop()
            
            sym = self._get_bool_sym(left)
            
            self.generator.rel_operation(left, right, ctx.RelOper().symbol.text, sym)
            self.stack.append(Value("%" + str(self.generator.reg - 1), VarType.BOOL))
    
    def _get_bool_sym(self, ident):
        sym = ''
        temp = [(x, y) for x, y in self.variables if x == ident]
        if len(temp) != 0:
            sym = '@' 
        else:
            temp = [(x, y) for x, y in self.local_variables if x == ident]
            if len(temp) != 0:
                sym = '%' 
        return sym

    def exitAddExpr(self, ctx: CSoftParser.AddExprContext):
        if ctx.AddOper():
            l = ctx.multExpr(0).children[0].children[0]
            r = ctx.multExpr(1).children[0].children[0]

            if l.BOOL() or r.BOOL():
                print(f"Error on line {ctx.start.line}: Bool in arithmetic operation")
            elif l.STRING() or r.STRING():
                print(f"Error on line {ctx.start.line}: String in arithmetic operation")
            else:
                if l.ID():
                    left = l.ID().symbol.text
                elif l.INT():
                    left = l.INT().symbol.text
                elif l.FLOAT():
                    left = l.FLOAT().symbol.text
                else:
                    left = self.stack.pop()
                
                
                if r.ID():
                    right = r.ID().symbol.text
                elif r.INT():
                    right = r.INT().symbol.text
                elif r.FLOAT():
                    right = r.FLOAT().symbol.text
                else:
                    right = self.stack.pop()
                
                type = self.generator.add_operation(left, right, ctx.AddOper().symbol.text)
                self.stack.append(Value("%" + str(self.generator.reg - 1), type))

    def exitMultExpr(self, ctx: CSoftParser.MultExprContext):
        if ctx.MultOper():
            l = ctx.negFactor(0).children[0]
            r = ctx.negFactor(1).children[0]
            
            if l.BOOL() or r.BOOL():
                # raise Exception(ctx.start.line, "Bool is not multiplicatable")
                print(f"Error on line {ctx.start.line}: Bool in arithmetic operation")
            elif l.STRING() or r.STRING():
                print(f"Error on line {ctx.start.line}: String in arithmetic operation")
                
            else:
                if l.ID():
                    left = l.ID().symbol.text
                elif l.INT():
                    left = l.INT().symbol.text
                elif l.FLOAT():
                    left = l.FLOAT().symbol.text
                else:
                    left = self.stack.pop()

                if r.ID():
                    right = r.ID().symbol.text
                elif r.INT():
                    right = r.INT().symbol.text
                elif r.FLOAT().symbol.text:
                    right = r.FLOAT().symbol.text
                else:
                    right = self.stack.pop()
                    
                type = self.generator.mult_operation(left, right, ctx.MultOper().symbol.text)
                self.stack.append(Value("%" +str(self.generator.reg - 1), type))
            
        
    def exitNegFactor(self, ctx: CSoftParser.NegFactorContext):
        if ctx.NegOper(): 
            test = ctx.factor()
            if ctx.factor().ID():
                factor = ctx.factor().ID().symbol.text
            elif ctx.factor().BOOL():
                factor = ctx.factor().BOOL().symbol.text
            else:
                factor = self.stack.pop()
            
            # self.generator.unary_operation(factor)
            self.generator.neg_operation(factor)
            self.stack.append(Value("%" + str(self.generator.reg - 1), type))
    
    def exitFactor(self, ctx: CSoftParser.FactorContext):
        if ctx.ID():
            ident = str(ctx.ID())
            temp = [(x, y) for x, y in self.variables if x == ident]
            if len(temp) == 0:
                temp = [(x, y) for x, y in self.local_variables if x == ident]
                type = get_llvm_type_str(temp[0][1])
                self.generator.load("%" + str(ident), type)
                self.stack.append(Value("%" + str(self.generator.reg - 1), temp[0][1]))
            else:
                type = get_llvm_type_str(temp[0][1])
                if type == None:
                    type = get_llvm_type_str(temp[0][1][1])
                self.generator.load("@" + str(ident), type)
                self.stack.append(Value("%" + str(self.generator.reg - 1), temp[0][1]))
        elif ctx.INT():
            value = ctx.INT().symbol.text
            self.stack.append(Value(value, VarType.LONG))
        elif ctx.FLOAT():
            value = ctx.FLOAT().symbol.text
            self.stack.append(Value(value, VarType.DOUBLE))
        elif ctx.STRING():
            # value = ctx.STRING().symbol.text
            # self.stack.append(Value(value, VarType.STRING))

            self.stack.append(Value(ctx.STRING().symbol.text, VarType.STRING) )
            tmp = ctx.STRING().getText()
            content = tmp[1:-1]
            self.generator.constant_string(content)
            n = "ptrstr"+str(self.generator.str-1)
            self.stack.append(Value(n, VarType.STRING))
        elif ctx.BOOL():
            value = ctx.BOOL().symbol.text
            self.stack.append(Value(value, VarType.BOOL))
        elif ctx.arrayAccess():
            ident = ctx.arrayAccess().ID().symbol.text
            indx = ctx.arrayAccess().INT().symbol.text
            temp = [(x, y) for x, y in self.variables if x == ident]
            global_var = True

            if len(temp) != 0:
                _, type, size = temp[0][1]
                if int(indx) >= size:
                    print(f"Error on line {ctx.start.line}: index out of bounds.")
                    return
            else:
                temp = [(x, y) for x, y in self.local_variables if x == ident]
                if len(temp) != 0:
                    global_var = False
                    _, type, size = temp[0][1]

            if global_var:
                ident = '@' + ident
            else:
                ident = '%' + ident
            self.generator.array_access(ident, indx, type, size=size)
            self.stack.append(Value("%" + str(self.generator.reg - 1), llvm_to_type(type)))
        elif ctx.funcCall():
            ident = str(ctx.funcCall().ID())

            temp = [(x, y) for x, y in self.functions if x == ident]
            if len(temp) != 0:
                self.generator.function_call(ident, temp[0][1])
                self.stack.append(Value("%" + str(self.generator.reg - 1), llvm_to_type(temp[0][1])))
        elif ctx.structFieldAccess():
            structID = ctx.structFieldAccess().ID().symbol.text
            memberID = ctx.structFieldAccess().ident().ID().symbol.text

            isSelf = False
            if structID == 'self':
                structName = self.classId
                isSelf = True 
            is_global = self.globalScope

            if not isSelf:
                temp = [(x, y) for x, y in self.variables if x == structID]
                if len(temp) != 0:
                    is_global = True
                else:
                    temp = [(x, y) for x, y in self.local_variables if x == structID]
                    if len(temp) != 0:
                        is_global = False
            
                struct = [(x, y, z) for x, y, z in self.structs if temp[0][1][1] == x]
            else:
                struct = [(x, y, z) for x, y, z in self.structs if structName == x]
            
            variables = struct[0][2]
            structName = struct[0][0]
            structVarCount = struct[0][1]
            type = None
            i = 0
            for i in range(structVarCount):
                if memberID == variables[i].name:
                    type = variables[i].type
                    break

            if is_global:
                structID = '@' + structID
            else:
                structID = '%' + structID
           
            if isSelf:
                structID = '%this'

            self.generator.struct_field_access(structID, structName, i, type)
            self.stack.append(Value("%" + str(self.generator.reg - 1), llvm_to_type(type)))
        elif ctx.methodCall():
            ident = str(ctx.methodCall().ID())
            methodID = str(ctx.methodCall().ident().ID())
            isSelf = False
            if ident == 'self':
                isSelf = True
                ident = "%this"

            is_global = self.globalScope
            if not isSelf:
                if is_global:
                    ident = '@' + ident
                else:
                    ident = '%' + ident
                temp = [(x, y) for x, y in self.class_variables if x == ident]
                classID = temp[0][1]
            else:
                classID = self.classId
            temp = [(x, y) for x, y in self.functions if x == classID + '_' + methodID]
            if len(temp) != 0:
                if not isSelf:
                    self.generator.call_method(classID, classID + '_' + methodID, ident, temp[0][1])
                else:
                    self.generator.call_method(classID, classID + '_' + methodID, ident, temp[0][1])
          
            self.stack.append(Value("%" + str(self.generator.reg - 1), string_to_type(temp[0][1])))
     

    def exitArrayAssign(self, ctx: CSoftParser.ArrayAssignContext):
        i = 0
        for _ in ctx.factor():
            i += 1
        self.stack.append(Value(i, VarType.ARRAY))
    
    def exitArrAssign(self, ctx: CSoftParser.ArrAssignContext):
        ident = ctx.ident().ID().symbol.text
        try:
            type = ctx.ident().type_().getText()
            if type == 'int':
                type = VarType.INT
            elif type == 'long':
                type = VarType.LONG
            elif type == 'float32':
                type = VarType.FLOAT32
            elif type == 'double':
                type = VarType.DOUBLE
            elif type == 'bool':
                type = VarType.BOOL
            elif type == 'string':
                type = VarType.STRING
        except AttributeError:
            type = None

        global_var = self.globalScope
        temp = [(x, y) for x, y in self.variables if x == ident]
        if len(temp) != 0:
            global_var = True
            if type != temp[0][1][1]:
                type = temp[0][1][1]
                type = string_to_type(type)
        else:
            temp = [(x, y) for x, y in self.local_variables if x == ident]
            if len(temp) != 0:
                global_var = False
                if type != temp[0][1][1]:
                    type = temp[0][1][1]
                    type = string_to_type(type)
       
        arr = self.stack.pop()

        if arr.type != VarType.ARRAY:
            print(f"Error on line {str(ctx.start.line)}: variable is not an array")

        if type is None:
            type = self.stack[-1].type
            
        values = []
        for _ in range(arr.name):
            v = self.stack.pop()
            values.append(v.name)
        values.reverse()

        type = get_llvm_type_str(type)

        if len(temp) == 0:
            self.generator.declare_array(ident, type = type, size = arr.name, global_arr=global_var)
            self.variables.append((ident, (arr.type, string_to_type(type), arr.name)))
        
        self.generator.symbol_table[ident] = arr  #tu
        
        if global_var:
            ident = '@' + ident
        else:
            ident = '%' + ident

        self.generator.assign_array(ident, type = type, size = arr.name, values = values)
    
    def exitElementAssign(self, ctx: CSoftParser.ElementAssignContext):
        ident = ctx.ID().symbol.text
        indx = ctx.INT().symbol.text

        temp = [(x, y) for x, y in self.variables if x == ident]
        global_var = True
        if len(temp) != 0:
            arr_type, type, size = temp[0][1]

            if size <= int(indx):
                print(f"Error on line: {ctx.start.line}: index out of bounds.")
                return
        else:
            temp = [(x, y) for x, y in self.local_variables if x == ident]
            if len(temp) != 0:
                global_var = False
                arr_type, type, size = temp[0][1]
            else:
                print(f"Error on line: {ctx.start.line}: array does not exist.")
                return

        if int(indx) >= size:
            print(f"Error on line {ctx.start.line}: index out of bounds.")
            return
        if len(temp) == 0 or arr_type != VarType.ARRAY:
            print(f"Line: {ctx.start.line}, variable {ident} not declared")
            return

        if global_var:
            ident = '@' + ident
        else:
            ident = '%' + ident

        value = self.stack.pop()
        self.generator.element_assign(ident, indx, value.name, type, size=size)


    def exitPrint(self, ctx:CSoftParser.PrintContext):
        ident = ctx.print_statement().ID().symbol.text

        sym = ''
        temp = [(x, y) for x, y in self.variables if x == ident]
        if len(temp) != 0:
            sym = '@' 
        else:
            temp = [(x, y) for x, y in self.local_variables if x == ident]
            if len(temp) != 0:
                sym = '%' 
      
        self.generator.print_operation(ident, ctx.start.line, sym)
    
    def exitAssign(self, ctx:CSoftParser.AssignContext):
        ID = ctx.ident().ID().symbol.text
        try:
            type = ctx.ident().type_().getText()
            type = string_to_type(type)
        except AttributeError:
            type = None

        value = self.stack.pop()

        temp = [(x, y) for x, y in self.variables if x == ID]
        global_var = self.globalScope
        if len(temp) != 0:
            type = temp[0][1]
            global_var = True
        else:
            temp = [(x, y) for x, y in self.local_variables if x == ID]
            if len(temp) != 0:
                global_var = False
                type = temp[0][1]
        
        if type is None:
            type = value.type

        if len(temp) == 0:
            if global_var:
                if type:
                    self.variables.append((ID, type))
                    value.type = type
                else:
                    self.variables.append((ID, value.type))
            else:
                if type:
                    self.local_variables.append((ID, type))
                    value.type = type
                else:
                    self.local_variables.append((ID, value.type))
        
        self.generator.symbol_table[ID] = value  #tu

        if global_var:
            ID = '@' + ID
        else:
            ID = "%" + ID


        if type == VarType.INT:
            self.generator.assign_i32(ID, value, global_var)
        elif type == VarType.LONG:
            self.generator.assign_i64(ID, value, global_var)
        elif type == VarType.FLOAT32:
            self.generator.assign_float32(ID, value, global_var)
        elif type == VarType.DOUBLE:
            self.generator.assign_double(ID, value, global_var)
        elif type == 'bool' or type == VarType.BOOL:
            if value.name == 'true':
                self.generator.assign_bool(ID, 1, global_var)
            elif value.name == 'false':
                self.generator.assign_bool(ID, 0, global_var)
            else:
                self.generator.assign_bool(ID, value.name, global_var)
        elif type == VarType.STRING:
            self.generator.assign_string(ID, value, global_var)


    def exitProg(self, ctx:CSoftParser.ProgContext):
        self.generator.finish()
        res = self.generator.generate_code()
        print(res)
        with open("code.ll", "w") as f:
            f.write(res)
    
   
        
    def exitRead(self, ctx:CSoftParser.ReadContext):

        var = ctx.read_statement().ID().symbol.text
        temp = [(x, y) for x, y in self.variables if x == var]
        if len(temp) != 0:
            var = '@' + var
        else:
            temp = [(x, y) for x, y in self.local_variables if x == var]
            if len(temp) != 0:
                var = '%' + var
            else:
                print(f"Error on line {str(ctx.start.line)}: Unknown ident")

        var_type = temp[0][1]
        if var_type == VarType.INT:
            self.generator.read_INT(var)
        elif var_type == VarType.LONG:
            self.generator.read_LONG(var)
        elif var_type == VarType.FLOAT32:
            self.generator.read_float32(var)
        elif var_type == VarType.DOUBLE:
            self.generator.read_double(var)
        elif var_type == 'bool' or var_type == VarType.BOOL:
            self.generator.read_bool(var)
        elif var_type == VarType.STRING:
            self.generator.read_string(var)
        else:
            print(f"Error on line {str(ctx.start.line)}: Unknown ident type")

    def enterBlockIf(self, ctx: CSoftParser.BlockIfContext):
        self.generator.if_start()
    
    def exitBlockIf(self, ctx: CSoftParser.BlockIfContext):
        self.generator.if_end()

    def enterWhileLoop(self, ctx: CSoftParser.WhileLoopContext):
        self.generator.whileL_start()

    def enterBlockWhile(self, ctx: CSoftParser.BlockWhileContext):
        self.generator.while_start()
    
    def exitBlockWhile(self, ctx: CSoftParser.BlockWhileContext):
        self.generator.while_end()
        

    def exitBlockRepeat(self, ctx: CSoftParser.BlockRepeatContext):
        self.generator.repeat_end()
    
    def exitRepNum(self, ctx: CSoftParser.RepNumContext):
        if ctx.factor().ID():
            ident = ctx.factor().ID().getText()

            temp = [(x, y) for x, y in self.variables if x == ident]
            if len(temp) != 0:
                sym = '@' 
            else:
                temp = [(x, y) for x, y in self.local_variables if x == ident]
                if len(temp) != 0:
                    sym = '%' 
            ident = sym + ident

            self.generator.load(ident, 'i32')
            val = '%' + str(self.generator.reg - 1)
        else:
            val = ctx.factor().INT().getText()
        
        self.generator.repeat_start(val)

    def exitFunType(self, ctx: CSoftParser.FunTypeContext):
        fun_type = ctx.type_().getText()
        type = get_llvm_type_str(string_to_type(fun_type))
        self.funType = type
    
    def exitFunName(self, ctx: CSoftParser.FunNameContext):
        name = str(ctx.ID())
        self.functions.append((name, self.funType))
        self.function = name
        self.generator.func_start(name, self.funType)
    
    def exitFunction(self, ctx:CSoftParser.FunctionContext):
        self.funType = 'i64'

    def enterBlockFun(self, ctx: CSoftParser.BlockFunContext):
        self.globalScope = False
    
    def exitBlockFun(self, ctx: CSoftParser.BlockFunContext):
        temp = [(x, y) for x, y in self.local_variables if x == self.function]
        if len(temp) == 0:
            self.generator.declare_INT("%"+str(self.function), False)
            self.generator.assign_func("%"+str(self.function), 0)

        self.generator.load("%"+str(self.function), self.funType)
        self.generator.func_end(self.funType)
        self.local_variables = []
        self.globalScope = True


    def enterClassDecl(self, ctx: CSoftParser.ClassDeclContext):
        ident = ctx.className().ID().symbol.text
        self.classId = ident

        i = 0
        variables = []
        for declaration in ctx.blockClass().structVarDecl():
            _type = declaration.ident().type_().getText()
            _type = get_llvm_type_str(string_to_type(_type))
            variables.append(Value(declaration.ident().ID().symbol.text, _type))
            i += 1

        self.generator.declare_struct(ident, variables)

        self.structs.append((self.classId, i, variables))


    def exitBlockClass(self, ctx: CSoftParser.BlockClassContext):
        self.classId = ''
        i = 0
        for var in ctx.structVarDecl():
            i += 1
        self.stack.append(Value(i, VarType.STRUCT))
     

    def exitClassAssign(self, ctx: CSoftParser.ClassAssignContext):
        ID = ctx.ident().ID().symbol.text
        classID = ctx.className().ID().symbol.text

        try:
            type = ctx.ident().type_().getText()
        except:
            type = None
        if type is not None:
            raise Exception(ctx.start.line, "class variable can't have type definition")

        temp = [(x, y, z) for x, y, z in self.structs if x == classID]
        if len(temp) == 0:
            print(f"Line: {ctx.start.line}, class not defined")
            return
        
        is_global = self.globalScope
        temp = [(x, y) for x, y in self.variables if x == ID]
        if len(temp) != 0:
            is_global = True
        else:
            temp = [(x, y) for x, y in self.local_variables if x == ID]
            if len(temp) != 0:
                is_global = False
        

        if is_global:
            self.variables.append((ID, (VarType.STRUCT, classID)))
            ID = '@' + ID
        else:
            self.local_variables.append((ID, (VarType.STRUCT, classID)))
            ID = '%' + ID

        self.class_variables.append((ID, classID))

        self.generator.assign_struct(ID, classID, is_global)

        
        temp = [(x, y) for x, y in self.functions if x == classID + '_Create_Default']
        if len(temp) != 0:
            self.generator.call_method(classID, classID + '_Create_Default', ID, temp[0][1])
        else:
            raise Exception(ctx.start.line, "constructor not defined")
        

    def exitMethodName(self, ctx: CSoftParser.MethodNameContext):
        ident = str(ctx.ID())
        if ident == self.classId:
            ident = self.classId + '_Create_Default'
        else:
            ident = self.classId + '_' + str(ctx.ID())
        self.functions.append((ident, self.funType))
        self.function = ident
        self.generator.method_start(ident, self.funType, self.classId)

    def enterBlockMethod(self, ctx: CSoftParser.BlockMethodContext):
        self.globalScope = False

    def exitBlockMethod(self, ctx: CSoftParser.BlockMethodContext):
        temp = [(x, y) for x, y in self.local_variables if x == self.function]
        if len(temp) == 0:
            self.generator.declare_INT("%"+str(self.function), False)
            self.generator.assign_func("%"+str(self.function), 0)

        self.generator.load("%"+str(self.function), self.funType)
        self.generator.func_end(self.funType)
        self.local_variables = []
        self.globalScope = True
    

    def exitStructDecl(self, ctx: CSoftParser.StructDeclContext):
        ID = ctx.structName().ID().symbol.text
        struct = self.stack.pop()
       
        variables = []
        for _ in range(struct.name):
            v = self.stack.pop()
            variables.append(v)
        variables.reverse()
        self.structs.append((ID, struct.name, variables))
        for v in variables:
            v.type = get_llvm_type_str(v.type)

        self.generator.declare_struct(ID, variables)

    def exitStructVarDecl(self, ctx: CSoftParser.StructVarDeclContext):
        ident = ctx.ident().ID().symbol.text
        type = ctx.ident().type_().getText()
        type = string_to_type(type)
        if self.classId == '':
            self.stack.append(Value(ident, type))

    def exitBlockStruct(self, ctx: CSoftParser.BlockStructContext):
        i = 0
        for _ in ctx.structVarDecl():
            i += 1
        self.stack.append(Value(i, VarType.STRUCT))

    def exitStructAssign(self, ctx: CSoftParser.StructAssignContext):
        ident = ctx.ident().ID().symbol.text
        structName = ctx.structName().ID().symbol.text

        temp = [(x, y, z) for x, y, z in self.structs if x == structName]
        if len(temp) == 0:
            print(f"Line: {ctx.start.line}, struct not defined")
            return
        
        is_global = self.globalScope
        temp = [(x, y) for x, y in self.variables if x == ident]
        if len(temp) != 0:
            is_global = True
        else:
            temp = [(x, y) for x, y in self.local_variables if x == ident]
            if len(temp) != 0:
                is_global = False
        

        if is_global:
            self.variables.append((ident, (VarType.STRUCT, structName)))
            ident = '@' + ident
        else:
            self.local_variables.append((ident, (VarType.STRUCT, structName)))
            ident = '%' + ident

        self.generator.assign_struct(ident, structName, is_global)


    def exitStructFieldAssign(self, ctx: CSoftParser.StructFieldAccessContext):
        structID = ctx.ID().symbol.text
        memberID = ctx.ident().ID().symbol.text
        value = self.stack.pop()

        isSelf = False
        if structID == 'self':
            structName = self.classId
            isSelf = True
           
        is_global = self.globalScope
        if not isSelf:
            temp = [(x, y) for x, y in self.variables if x == structID]
            if len(temp) != 0:
                is_global = True
            else:
                temp = [(x, y) for x, y in self.local_variables if x == structID]
                if len(temp) != 0:
                    is_global = False
            struct = [(x, y, z) for x, y, z in self.structs if temp[0][1][1] == x]
        else:
            struct = [(x, y, z) for x, y, z in self.structs if structName == x]

        variables = struct[0][2]
        structName = struct[0][0]
        structVarCount = struct[0][1]
        type = None
        i = 0
        for i in range(structVarCount):
            if memberID == variables[i].name:
                type = variables[i].type
                break
        if value.type != llvm_to_type(type):
            print(f"Line: {ctx.start.line} wrong type of value")
            return


        if is_global:
            structID = '@' + structID
        else:
            structID = '%' + structID

        if isSelf:
            structID = '%this'
        self.generator.assign_struct_field(structID, structName, i, value.name, type)

  

del CSoftParser