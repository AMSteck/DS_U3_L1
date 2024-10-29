#Alannah Steck
#U3L1
#While vs Recursion
#ʕ •ᴥ•ʔ good luck bear 

def sample(num):
    if num == 0:
        print("\nBASE CASE REACHED\n")
        return

    print(f"Recursing; num = {num}")
    sample(num-1)
    print(f"Returning; num = {num}")
    return

def whileSubstitute(num):
  numCopy = num
  while numCopy > 0:
    print(f"Recursing; num = {numCopy}")
    numCopy -= 1
  print("\nBASE CASE REACHED\n")
  numCopy += 1
  while numCopy <= num:
    print(f"Returning; num = {numCopy}")
    numCopy += 1


def main():
  print("\n\nRecursion\n")
  sample(5)
  print("\n\nWhile Loops\n")
  whileSubstitute(5)

if __name__ == "__main__":
  main()