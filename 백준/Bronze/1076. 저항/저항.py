import sys

colors = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
inputs = sys.stdin.readlines()

values = dict()
powers = dict()

for i in range(10):
    values[colors[i]] = i
    powers[colors[i]] = 10**i

print(
    (values[inputs[0].rstrip()] * 10 + values[inputs[1].rstrip()])
    * powers[inputs[2].rstrip()]
)
