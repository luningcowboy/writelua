luac hello.lua >> luac.out
luac -o hello.luac hello.lua >> hello.luac
luac -s hello.lua >> 不包含调试信息
反编译:
luac -l hello.lua >> lua源文件
luac -l hello.luac >> 二进制文件
