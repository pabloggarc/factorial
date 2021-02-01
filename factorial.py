def factorial(n): 
    """
    int--->int
    OBJ: Devuelve el factorial de un número.
    PRE: n debe ser un número natural 
    """
    if(n!=0): 
        return n*factorial(n-1)
    else: 
        return 1
