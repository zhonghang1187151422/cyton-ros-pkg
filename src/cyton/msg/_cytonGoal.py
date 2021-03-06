"""autogenerated by genmsg_py from cytonGoal.msg. Do not edit."""
import roslib.message
import struct


class cytonGoal(roslib.message.Message):
  _md5sum = "047c252d377a2ef76ab6ac84f488d43c"
  _type = "cyton/cytonGoal"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#goal definition
float32[] position
float32[] rate
float32 time
uint32 eeindex
uint32 home
float32 gripper_value
float32 gripper_rate

"""
  __slots__ = ['position','rate','time','eeindex','home','gripper_value','gripper_rate']
  _slot_types = ['float32[]','float32[]','float32','uint32','uint32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       position,rate,time,eeindex,home,gripper_value,gripper_rate
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(cytonGoal, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.position is None:
        self.position = []
      if self.rate is None:
        self.rate = []
      if self.time is None:
        self.time = 0.
      if self.eeindex is None:
        self.eeindex = 0
      if self.home is None:
        self.home = 0
      if self.gripper_value is None:
        self.gripper_value = 0.
      if self.gripper_rate is None:
        self.gripper_rate = 0.
    else:
      self.position = []
      self.rate = []
      self.time = 0.
      self.eeindex = 0
      self.home = 0
      self.gripper_value = 0.
      self.gripper_rate = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      length = len(self.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.position))
      length = len(self.rate)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.rate))
      _x = self
      buff.write(_struct_f2I2f.pack(_x.time, _x.eeindex, _x.home, _x.gripper_value, _x.gripper_rate))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.position = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.rate = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 20
      (_x.time, _x.eeindex, _x.home, _x.gripper_value, _x.gripper_rate,) = _struct_f2I2f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      length = len(self.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.position.tostring())
      length = len(self.rate)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.rate.tostring())
      _x = self
      buff.write(_struct_f2I2f.pack(_x.time, _x.eeindex, _x.home, _x.gripper_value, _x.gripper_rate))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.rate = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 20
      (_x.time, _x.eeindex, _x.home, _x.gripper_value, _x.gripper_rate,) = _struct_f2I2f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_f2I2f = struct.Struct("<f2I2f")
