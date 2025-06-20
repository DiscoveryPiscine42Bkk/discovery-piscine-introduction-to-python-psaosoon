import sys
def main():

    parameters = sys.argv[1:]
    num_parameters = len(parameters)

    if num_parameters == 0:
         print("none")
    else:
         print(f"parameters: {num_parameters}")
         for param in parameters:
              print(f"{param}: {len(param)}")

if__name__=="__main__":
main