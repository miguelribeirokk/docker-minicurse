import time

while True:
    for c in range(1, 11):
        f = open(r"data/for.txt", "a")
        print(c)
        f.write(str(c))
        f.write("\n")

        f.close()

        time.sleep(2)
