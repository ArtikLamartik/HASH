1. get:$var1$; -> import $var1$
2. wait:$var1$; -> ATH.wait($var1$)
3. show:$var1$; -> print("$var1$")
4. show:$var1$> -> print($var1$)
5. tts:$var1$; -> ATH.tts("$var1$")
6. tts:$var1$> -> ATH.tts($var1$)
7. inp:$var1$; -> inp = input("$var1$")
8. inp:$var1$> -> inp = input($var1$)
9. rand:$var1$; -> rand = random.randint($var1$)
10. endkey:$var1$; -> keyboard.wait($var1$)
11. openw:$var1$,$var2$; -> with open($var1$, "w") as $var2$:
12. openr:$var1$,$var2$; -> with open($var1$, "r") as $var2$:
13. write:$var1$,$var2$; -> $var1$.write($var2$)
14. read:$var1$,$var2$; -> $var1$ = $var2$.read()
15. raise.error:$var1$,$var2$; -> print(f"{$var1$}: {$var2$}")
16. console.run:$var2$; -> subprocess.run($var1$, shell=True)
17. .popup:$var1$,$var2$,$var3$; -> messagebox.show$var1$($var2$,$var3$)
18. argm:$var1$,$var2$; -> $var1$ = sys.argv[$var2$]
19. $var1$:$var2$ = $var3$ -> $var1$ = lambda $var2$: $var3$
20. memory.push:$var1$,$var2$; -> memory_array[$var1$] = $var2$
21. memory.pull:$var1$,$var2$; -> $var1$ = memory_array[$var2$]
22. memory.del:$var2$; -> del memory_array[$var1$]
23. include:$var1$,$var2$; -> inclusion = "$var1$"\nimport subprocess\nimport importlib\nsubprocess.run(["Hash", inclusion])\ninclusion = inclusion.replace(".hash", "")\n$var2$ = importlib.import_module(inclusion)
24. ret $var1$; -> return $var1$
25. $var1$ = "$var2$"; -> $var1$ = "$var2$"
26. $var1$ = '$var2$';": "$var1$ = '$var2$'
27. loopy $var1$; { -> while $var1$:
28. func $var1$:$var2$; { -> def $var1$($var2$):
29. .cnt() -> .count()
30. .upr() -> .upper()
31. .lwr() -> .lower()
32. over -> pass
33. ranger -> range
34. stop -> break
35. stwr: -> if __name__ === "__main__":
36. true -> True
37. false -> False
38. none -> None
39. #c. -> #
40. ifnotif -> elif
41. ifnot -> else
42. into -> append
43. +++ -> ' += 1'
44. ++ -> ' += '
45. --- -> ' -= 1'
46. -- -> ' -= '
47. ">>" -> >
48. << -> <
49. ">=>" -> >=
50. <=< -> <=
51. === -> ==
52. =!= -> !=
53. && -> and
54. || -> or
55. abc -> str
56. nr -> int
57. flt -> float
58. lst -> list
59. dct -> dict
60. tup -> tuple
61. hashgame -> pygame
62. .Memory() -> memory_array = {}
