
a = {1 : 10}
x = {1 : 100000}
for y in x :
    y = y
    while y <= 100000:
        print(f"\nTable of {y}")
        for b in x:
            while b <= 10 :
                print(f"{y}x{b} = {y * b}")
                b += 1
        y += 1