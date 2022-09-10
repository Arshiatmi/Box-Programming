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

### Array Parse

```
Input0 : Array (Types.array)
Output0 : Array Length (Types.number)
Output1 : Array Elements (Types.array)
Output2 : Reversed Array (Types.array)
```

### Array Append

```
Input0 : Array (Types.array)
Input1 : Element To Append (Types.variable)
Output0 : Output (Types.array)
```

### Array Prepend

```
Input0 : Array (Types.array)
Input1 : Element To Prepend (Types.variable)
Output0 : Output (Types.array)
```

### Array Count

```
Input0 : Array (Types.array)
Input1 : Element To Count (Types.variable)
Output0 : Output (Types.number)
```

### Array Sort

```
Input0 : Array (Types.array)
Output0 : Sorted Array (Types.array)
```

### Array Index

```
Input0 : Array (Types.array)
Input1 : Element To Get Index (Types.variable)
Output0 : Output (Types.number)
```

### Array Insert

```
Input0 : Array (Types.array)
Input1 : Element To Get Index (Types.variable)
Input2 : Index That You Want To Insert (Types.number)
Output0 : Output (Types.array)
Output1 : Success (Types.boolean)
```

### Array Remove

```
Input0 : Array (Types.array)
Input1 : Element Or Index Of Element Depends On Input2 (Types.variable)
Input2 : True If You Want To Remove By Index (Types.boolean)
Output0 : Output (Types.array)
Output1 : Success (Types.boolean)
```

### Array Minimum Element

```
Input0 : Array (Types.array)
Output0 : Minimum Element (Types.variable)
Output1 : Index Of Minimum Element (Types.number)
Output2 : True If Getting Minimum Was Successfull (Types.boolean)
```

### Array Maximum Element

```
Input0 : Array (Types.array)
Output0 : Maximum Element (Types.variable)
Output1 : Index Of Maximum Element (Types.number)
Output2 : True If Getting Maximum Was Successfull (Types.boolean)
```

# Text Boxes

### Text Capitalize

```
Input0 : Text That You Want To Capitalize (Types.text)
Output0 : Output Text (Types.text)
```

### Text Count

```
Input0 : Full Text That You Want To Search Into (Types.text)
Input1 : Text That You Want To Search For And Get Count Of It (Types.text)
Output0 : Count How Many Input1 Is In Input0 (Types.number)
```

### Text EndsWith

```
Input0 : Full Text That You Want To Search Into (Types.text)
Input1 : Text That You Want To Search And Check If Input0 Endswith (Types.text)
Output0 : Checks if Input0 ends with Input1 Or Not (Types.boolean)
```

### Text Find

```
Input0 : Full Text That You Want To Search Into (Types.text)
Input1 : Text That You Want To Search And Get Index From Input0. (Types.text)
Input2 : Reverse Search That Will Count From Latest Character To First Character.Given Index In Reverse Mode Is In Normal Index Not Reversed Index (Types.boolean)
Output0 : Search And Get Input1 Index From Input0. ( Returns -1 If Not Found ) (Types.number)
```

### Text Strip

```
Input0 : Full Text That You Want To Strip It (Types.text)
Input1 : You Can Give Characters That You Want To Strip From Them Here. Default Is All Whitespaces. (Types.text)
Input2 : True If You Want To Strip Left.Default Is True. (Types.boolean)
Input3 : True If You Want To Strip Right.Default Is True. (Types.boolean)
Output0 : Returns Output That Is Stripped Text. (Types.text)
```

### Text Split

```
Input0 : Full Text That You Want To Split It (Types.text)
Input1 : The Splitter Character Or Text. Input0 Will Split With Input0. (Types.text)
Input2 : Max Split Count. For Example If Its 3, Input0 Will Try To Split Data Until 3 Times. (Types.number)
Input3 : Start Index That Split Will Start On That Index.Default Is 0 (Types.number)
Input4 : End Index That Split Will End On That Index. Default Is Inpu0 Length (Types.number)
Output0 : Returns Splitted Text. (Types.array)
```

### Text SwapCase

```
Input0 : Full Text That You Want To SwapCase It (Capital letters to Small letters and oposite of that) (Types.text)
Output0 : Returns Swapcased Text. (Types.text)
```

### Text ZeroFill

```
Input0 : Text That You Want To ZeroFill It. ( Fill Text With Zeros That You Specify ) (Types.text)
Input1 : Count Of Full Text That You Want To Output (Types.text)
Output0 : Returns A Text With Length (max(Input0.length,Input1)) That Is Zerofilled Text (Types.text)
```

### Text Is Alphabet

```
Input0 : Full Text That You Want To Check If Its Alphabet Or Not. (Types.text)
Output0 : Returns Output. (Types.boolean)
```

### Text Is Alphabet Or Number Or Both

```
Input0 : Full Text That You Want To Check If Its (Alphabet Or Number Or Both) Or Not. (Types.text)
Output0 : Returns Output. (Types.boolean)
```

### Text Is Digits ( Number )

```
Input0 : Full Text That You Want To Check If Its Digits(Number) Or Not. (Types.text)
Output0 : Returns Output. (Types.boolean)
```

### Text To Lowercase

```
Input0 : Full Text That You Want To Make Them LowerCase (Types.text)
Output0 : Returns Output. (Types.text)
```

### Text To Uppercase

```
Input0 : Full Text That You Want To Make Them UpperCase (Types.text)
Output0 : Returns Output. (Types.text)
```

### Text Is Lowercase

```
Input0 : Full Text That You Want To Check If They Are LowerCase (Types.text)
Output0 : Returns Output. (Types.boolean)
```

### Text Is Uppercase

```
Input0 : Full Text That You Want To Check If They Are UpperCase (Types.text)
Output0 : Returns Output. (Types.boolean)
```

### Text Join Array

```
Input0 : Text That You Want To Join Array With It (Types.text)
Input1 : Array That You Want To Join Them (Types.array)
Output0 : Input1 Elements Joined With Input0. (Types.boolean)
```

### Text Replace

```
Input0 : Full Text That You Want To Replace Data (Types.text)
Input1 : The Text That You Want To Replace It. (Types.text)
Input2 : The Text That You Want To Replace Data With It. (Types.text)
Output0 : Replaced Text. (Types.text)
```

# File Boxes

### Read File

```
Input0 : Execute (Types.executable)
Input1 : File name (Types.text)
Output0 : Execute (Types.executable)
Output1 : Full Text Of File (Types.text)
Output2 : Lines Of File As Array (Types.array)
```

### Write File

```
Input0 : Execute (Types.executable)
Input1 : File name (Types.text)
Input2 : Text That You Want To Write Or Append (Types.text)
Input3 : True If You Want To Append And False If You Dont Want To Append (Types.boolean)
Output0 : Execute Next (Types.executable)
Output1 : Succsessful Or Not (Types.boolean)
```

### Remove File

```
Input0 : Execute (Types.executable)
Input1 : File name (Types.text)
Output0 : Execute Next (Types.executable)
Output1 : Succsessful Or Not (Types.boolean)
```

### Get File List

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

# Others

### Run Os Command

```
Input0 : Execute (Types.executable)
Input1 : The Text That You Want To Run It On Os (Types.text)
Input2 : True If You Want To Run Os Command As Another Child Process ( To Run Some Commands Like 'clear', It Must Be False.) (Types.text)
Output0 : Execute Next (Types.executable)
Output1 : Output If You Run As Process. (Types.text)
```

# Box Functions

### Get Length

```
Input0 : Execute (Types.executable)
Input1 : Object That You Want To Get Length Of It. (Types.variable)
Output0 : Execute Next (Types.executable)
Output1 : Length Of Input0. (Types.number)
Output2 : True If Length Number Is Successfully Done (Types.boolean)
```

### Range

```
Input0 : Execute (Types.executable)
Input1 : Start Index (Types.number)
Input2 : End Index (Types.number)
Input3 : Step (Types.number)
Output0 : Execute Next (Types.executable)
Output1 : Output (Types.array)
```

### Ord

```
Input0 : Execute (Types.executable)
Input1 : Text That You Want To Get Ord Of Them ( ASCII Code ) (Types.text)
Output0 : Execute Next (Types.executable)
Output1 : Output (Types.array)
Output2 : True If Ord Of Number Successfully Computed. (Types.array)
```

### Chr

```
Input0 : Execute (Types.executable)
Input1 : Each Ascii Code As An Element Of an Array. Like [72 ,101 ,108 ,108 ,111] (Types.text)
Input2 : True If Returns Answer As Text. (Types.boolean)
Output0 : Execute Next (Types.executable)
Output1 : Output That Will Convert All Ascii Codes To Character Ans Concat Them (Types.text)
Output2 : True If Chr Of Arrays Successfully Done. (Types.boolean)
```

### Map -> ( Like Python map Function )

```
Input0 : Execute (Types.executable)
Input1 : The Array That You Want To Map Data (Types.array)
Output0 : Execute After Mapping (Types.executable)
Output1 : Execute In Each Mapping Index (Types.executable)
Output2 : Element Of Input1 That Currently Mapping On (Types.variable)
Output3 : Index Of Input1 That Currently Mapping On (Types.number)
```

### Min

```
Input0 : Execute (Types.executable)
Input1 : First Element For Getting Minimum Element Between Datas. (Types.variable)
Input2 : Second Element For Getting Minimum Element Between Datas. (Types.variable)
# More Inputs Are Addable

Output0 : Execute After Calculation (Types.executable)
Output1 : Minimum Element Between Elements That Specified. (Types.variable)
Output2 : Index Of Minimum Element Between Elements. (Types.number)
```

### Max

```
Input0 : Execute (Types.executable)
Input1 : First Element For Getting Maximum Element Between Datas. (Types.variable)
Input2 : Second Element For Getting Maximum Element Between Datas. (Types.variable)
# More Inputs Are Addable

Output0 : Execute After Calculation (Types.executable)
Output1 : Maximum Element Between Elements That Specified. (Types.variable)
Output2 : Index Of Maximum Element Between Elements. (Types.number)
```

### Zip

```
Input0 : Execute (Types.executable)
Input1 : First Element For Zipping Elements. (Types.array)
Input2 : Second Element For Zipping Elements. (Types.array)
# More Inputs Are Addable

Output0 : Execute After Calculation (Types.executable)
Output1 : The Functionallity Over Zipping Elements (Types.executable)
Output2 : Elements That Are Zipped. (Types.array)
Output3 : Index Of Elements That Are Zipped Over Output1 Function. (Types.number)
```

### Exit

```
Input0 : Execute (Types.executable)
```
