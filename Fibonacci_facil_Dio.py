n = int(input())
fib_list = [ ]

for i in range(  n  ):
    # Metodo recursivo - https://www.delftstack.com/pt/howto/python/fibonacci-sequence-python/
    # Recursive method
  if i > 1:
    fib_list.append( fib_list[i-1] + fib_list[i-2] )
  else:
    fib_list.append( i )
# Converter a lista de números para texto
# Convert list to string
fib_string = ' '.join( str (e) for e in fib_list)
print(fib_string)