from vm.consts import Consts

class LuaStack:
    MAX_STACK_SIZE = 1000

    def __init__(self, lua_state):
        self.slots = []
        self.varargs = None
        self.pc = 0
        self.caller = None
        self.lua_state = lua_state
        self.open_upvalues = {}

    def top(self):
        return len(self.slots)

    def check(self, n):
        return len(self.slots) + n <= LuaStack.MAX_STACK_SIZE

    def push(self, val):
        if len(self.slots) > LuaStack.MAX_STACK_SIZE:
            raise Exception('Stack Over Flow')
        self.slots.append(val)

    def pop(self):
        ret = self.slots[-1]
        self.slots.pop()
        return ret

    def abs_index(self, idx):
        if idx <= Consts.LUA_RIGISTRYINDEX:
            return idx
        return idx if idx >= 0 else idx + len(self.slots) + 1

    def is_valid(self, idx):
        if idx < Consts.LUA_RIGISTRYINDEX:
            uvidx = Consts.LUA_RIGISTRYINDEX - idx - 1
            return self.closure is not None and uvidx < len(self.closure.upvals)
        if idx == Consts.LUA_RIGISTRYINDEX:
            return True

        idx = self.abs_index(idx)
        return (idx > 0) and (idx <= len(self.slots))
