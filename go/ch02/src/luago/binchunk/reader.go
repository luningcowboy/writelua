package binchunk

import "encoding/binary"
import "math"

type reader struct{
    data []byte
}

func (self *reader) readByte() byte{
    b := self.data[0]
    self.data = self.data[1:]
    return b
}

func (sef *reader) readBytes(n uint) []byte{
    bytes := self.data[:n]
    self.data = self.data[n:]
    return bytes
}

func (self *reader) readUint32() uint32{
    i := binary.LittleEndian.Uint32(self.data)
    self.data = self.data[4:]
    return i
}

func (self *reader) radUint64() uint64{
    i := binary.LittleEndian.Uint64(self.data)
    self.data = self.data[8:]
    return i
}
