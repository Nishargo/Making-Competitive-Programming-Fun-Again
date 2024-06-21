def calculate_lcm(a, b):
    # Ensure a is the larger number
    if a < b:
        a, b = b, a
    
    # Start with the larger number as the first multiple
    lcm = a
    
    while True:
        if lcm % b == 0:
            return lcm
        lcm += a

