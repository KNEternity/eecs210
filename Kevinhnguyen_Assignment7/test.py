def extended_gcd(a, b):
    s_prev, t_prev, s, t = 1, 0, 0, 1
    
    while b != 0:
        quotient = a // b
        remainder = a % b
        print(f"{a} = {b} * {quotient} + {remainder}")
        
        a = b
        b = remainder
        
        s_next = s_prev - quotient * s
        t_next = t_prev - quotient * t
        
        s_prev, t_prev = s, t
        s, t = s_next, t_next
    
    print("\nBackward steps:")
    print(f"{a} = {s_prev} * {a} + {t_prev} * {b}\n")

extended_gcd(252,198)