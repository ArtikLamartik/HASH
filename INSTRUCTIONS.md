get:<var1>; -> import <var1>
wait:<var1>; -> ATH.wait(<var1>)
show:<var1>; -> print("<var1>")
show:<var1>> -> print(<var1>)
tts:<var1>; -> ATH.tts("<var1>")
tts:<var1>> -> ATH.tts(<var1>)
inp:<var1>; -> inp = input("<var1>")
inp:<var1>> -> inp = input(<var1>)
rand:<var1>; -> rand = random.randint(<var1>)
endkey:<var1>; -> keyboard.wait(<var1>)
openw:<var1>,<var2>; -> with open(<var1>, "w") as <var2>:
openr:<var1>,<var2>; -> with open(<var1>, "r") as <var2>:
write:<var1>,<var2>; -> <var1>.write(<var2>)
read:<var1>,<var2>; -> <var1> = <var2>.read()
raise.error:<var1>,<var2>; -> print(f"{<var1>}: {<var2>}")
console.run:<var2>; -> subprocess.run(<var1>, shell=True)
.popup:<var1>,<var2>,<var3>; -> messagebox.show<var1>(<var2>,<var3>)
argm:<var1>,<var2>; -> <var1> = sys.argv[<var2>]
<var1>:<var2> = <var3> -> <var1> = lambda <var2>: <var3>
memory.push:<var1>,<var2>; -> memory_array[<var1>] = <var2>
memory.pull:<var1>,<var2>; -> <var1> = memory_array[<var2>]
memory.del:<var2>; -> del memory_array[<var1>]
include:<var1>,<var2>; -> inclusion = "<var1>"\nimport subprocess\nimport importlib\nsubprocess.run(["Hash", inclusion])\ninclusion = inclusion.replace(".hash", "")\n<var2> = importlib.import_module(inclusion)
ret <var1>; -> return <var1>
<var1> = "<var2>"; -> <var1> = "<var2>"
<var1> = '<var2>';": "<var1> = '<var2>'
loopy <var1>; { -> while <var1>:
func <var1>:<var2>; { -> def <var1>(<var2>):
.cnt() -> .count()
.upr() -> .upper()
.lwr() -> .lower()
over -> pass
ranger -> range
fory -> for
stop -> break
stwr: -> if __name__ === "__main__":
true -> True
false -> False
none -> None
#c. -> #
ifnotif -> elif
ifnot -> else
into -> append
+++ -> ' += 1'
++ -> ' += '
--- -> ' -= 1'
-- -> ' -= '
>> -> >
<< -> <
>=> -> >=
<=< -> <=
=== -> ==
=!= -> !=
&& -> and
|| -> or
abc -> str
nr -> int
flt -> float
lst -> list
dct -> dict
tup -> tuple
hashgame -> pygame
.IsPrime() -> def IsPrime(x):\n\tif x <= 1:\n\t\treturn False\n\tif x <= 3:\n\t\treturn True\n\tif x%2 == 0 or x%3 == 0:\n\t\treturn False\n\ti = 5\n\twhile i * i <= x:\n\t\tif x%i == 0 or x%(i+2) == 0:\n\t\t\treturn False\n\t\ti += 6\n\treturn True
.RomanToInt()':'def RomanToInt(s):\n\tRoman_Number_Dict_With_Values = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}\n\tNumber_Minus_One = 0\n\tEnd_Number = 0\n\tfor Roman_Number in s.lower():\n\t\tNumber = Roman_Number_Dict_With_Values[Roman_Number]\n\t\tif Number > Number_Minus_One:\n\t\t\tEnd_Number += Number - Number_Minus_One * 2\n\t\telse:\n\t\t\tEnd_Number += Number\n\t\tNumber_Minus_One = Number\n\treturn End_Number
.IntToRoman() -> def IntToRoman(num):\n\tm = {"M": 1000, "CM": 900, "D": 500, "CD":400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1,}\n\tans = ""\n\tfor k, v in m.items():\n\t\twhile num >= v:\n\t\t\tans += k\n\t\t\tnum -= v\n\treturn ans
.AbcToBinary() -> def AbcToBinary(a):\n\treturn " ".join(format(ord(c), "08b") for c in a)
.BinaryToAbc() -> def BinaryToAbc(b):\n\tbinary_values = b.split(" ")\n\treturn "".join(chr(int(bv, 2)) for bv in binary_values)
.DecimalToBinary() -> def DecimalToBinary(d):\n\treturn bin(d).replace("0b", "")
.BinaryToDecimal() -> def BinaryToDecimal(b):\n\treturn int(b, 2)
.Memory() -> memory_array = {}
.FizzBuzz() -> def FizzBuzz(n):\n\ti = 1\n\twhile i <= n:\n\t\tif i%3==0 and i%5==0:\n\t\t\tprint("FizzBuzz", str(i))\n\t\telif i%3==0:\n\t\t\tprint("Fizz    ", str(i))\n\t\telif i%5==0:\n\t\t\tprint("Buzz    ", str(i))\n\t\telse:\n\t\t\tprint("        ", str(i))\n\t\ti+=1
