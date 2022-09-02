![license](https://img.shields.io/github/license/Arshiatmi/Box-Programming.svg)
![last-commit](https://img.shields.io/github/last-commit/Arshiatmi/Box-Programming.svg)

# Functions

You Can Define Functions Like :

```
Function("name",lambda x:x,[Option("Execute",Types.executable)],[])
```

Arguments Are :

**The Name Of Function**,

**The Function You Want To Execute On This Box**,

**All Input Options In Box**,

**All Output Options In Box**,

# Options

Define Options Like :

```
Option("text",Types.executable)
```

Arguments Are :

**The Name Of Option**,

**Type Of Option**,

## Option Types

**Types.boolean**,

**Types.number**,

**Types.text**,

**Types.empty**,

**Types.executable**,

# Boxes

You Can Define Boxes Like :

```
Box(name="", Type=BoxTypes.Executable, function=Function("pass", lambda x: x))
```

Arguments Are :

**The Name Of Box**,

**The Type Of Box**,

**The Function Of Box**
