from .helpers import *
from .enums import BoxTypes,Types
from .blocks import Function,Box

Box(Type=BoxTypes.Start)
Box(Type=BoxTypes.End)
Box(Type=BoxTypes.Variable,function=Function("Get Number Variable",getNumberVariable,[Types.text],[Types.number]))
Box(Type=BoxTypes.Variable,function=Function("Get Boolean Variable",getBooleanVariable,[Types.text],[Types.boolean]))
Box(Type=BoxTypes.Variable,function=Function("Get Text Variable",getTextVariable,[Types.text],[Types.text]))
Box(Type=BoxTypes.Executable,function=Function("Set Number Variable",setNumberVariable,[Types.text,Types.number],[]))
Box(Type=BoxTypes.Executable,function=Function("Set Boolean Variable",setBooleanVariable,[Types.text,Types.boolean],[]))
Box(Type=BoxTypes.Executable,function=Function("Set Text Variable",setTextVariable,[Types.text,Types.text],[]))
