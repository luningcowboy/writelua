from vm.lua_type import LuaType

class LuaValue:
    @staticmethod
    def type_of(val):
        from vm.lua_talbe import LuaTable
        from vm.closure import Closure
