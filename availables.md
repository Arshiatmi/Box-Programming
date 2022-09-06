These Are Current Boxes That Are Available...

# Type Casts

### Cast Number To Text

### Cast Number To Bool

### Cast Bool To Number

### Cast Bool To Text

### Cast Text To Number

### Cast Text To Bool

### Cast Array To Text

### Cast Text To Array

### Cast Any Variable Type To Text

All Cast Boxes Are Like :

```
Input0 : Execute (Types.executable)
Input1 : Object (Types.variable)
Output0 : Execute If Cast Done (Types.executable)
Output1 : Execute If Cast Failed (Types.executable)
Output2 : Casted Object (Types.variable)
```

# Array Functions

### Parse

```
Input0 : Array (Types.array)
Output0 : Array Length (Types.number)
Output1 : Array Elements (Types.array)
Output2 : Reversed Array (Types.array)
```

### Append

```
Input0 : Array (Types.array)
Input1 : Element To Append (Types.variable)
Output0 : Output (Types.array)
```

### Prepend

```
Input0 : Array (Types.array)
Input1 : Element To Prepend (Types.variable)
Output0 : Output (Types.array)
```

### Count

```
Input0 : Array (Types.array)
Input1 : Element To Count (Types.variable)
Output0 : Output (Types.number)
```

### Index

```
Input0 : Array (Types.array)
Input1 : Element To Get Index (Types.variable)
Output0 : Output (Types.number)
```

### Insert

```
Input0 : Array (Types.array)
Input1 : Element To Get Index (Types.variable)
Input2 : Index That You Want To Insert (Types.number)
Output0 : Output (Types.array)
Output1 : Success (Types.boolean)
```

### Remove

```
Input0 : Array (Types.array)
Input1 : Element Or Index Of Element Depends On Input2 (Types.variable)
Input2 : True If You Want To Remove By Index (Types.boolean)
Output0 : Output (Types.array)
Output1 : Success (Types.boolean)
```

# File Boxes

### ReadFile

```
Input0 : Execute (Types.executable)
Input1 : File name (Types.text)
Output0 : Execute (Types.executable)
Output1 : Full Text Of File (Types.text)
Output2 : Lines Of File As Array (Types.array)
```

### WriteFile

```
Input0 : Execute (Types.executable)
Input1 : File name (Types.text)
Input2 : Text That You Want To Write Or Append (Types.text)
Input3 : True If You Want To Append And False If You Dont Want To Append (Types.boolean)
Output0 : Execute Next (Types.executable)
Output1 : Succsessful Or Not (Types.boolean)
```

### RemoveFile

```
Input0 : Execute (Types.executable)
Input1 : File name (Types.text)
Output0 : Execute Next (Types.executable)
Output1 : Succsessful Or Not (Types.boolean)
```

### FileList

```
Input0 : Execute (Types.executable)
Input1 : Path That You Want To Get File List Of There (Types.text)
Input2 : True If You Want To Contains Files (Types.boolean)
Input3 : True If You Want To Contains Directories (Types.boolean)
Output0 : Execute Next (Types.executable)
Output1 : List Of Files (Types.array)
Output2 : Succsessful Or Not (Types.boolean)
```

# Executables

### If

```
Input0 : Execute (Types.executable)
Input1 : Condition (Types.boolean)
Output0 : Execute Next If Condition Was True (Types.executable)
Output1 : Execute Next If Condition Was False (Types.executable)
```

### Input

```
Input0 : Execute (Types.executable)
Input1 : Input Prompt ( Question That Asks For User Input ) (Types.text)
Output0 : Execute Next (Types.executable)
Output1 : User Input Text (Types.text)
```

### Print

```
Input0 : Execute (Types.executable)
Input1 : Text That You Want To Print (Types.text)
Output0 : Execute Next (Types.executable)
```

### For

```
Input0 : Execute (Types.executable)
Input1 : Start Index Of For Loop (Types.number)
Input2 : End Index Of For Loop (Types.number)
Input3 : Step Of For Loop (Types.number)
Input4 : Array If You Want To Loop On Array (Types.array)
Output0 : Execute Next If Loop Finished (Types.executable)
Output1 : Execute In Each Iteration (Types.executable)
Output2 : Index Of Each Iteration (Types.number)
Output3 : Element Of Array In Each Iteration ( If You Are Iterating Array ) (Types.variable)
```
