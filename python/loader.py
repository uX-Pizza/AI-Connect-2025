import pandas as pd
from constraint import Constraint


pd.set_option("display.width", None)


n = 0
puzzle = {
    "id": "",
    "dim": [],
    "entities": [],
    "constraints": []}
constraint_counter = 0



def flatten_2d(arr):
    res = []
    for i in arr:
        res.extend(i)
    return res



df = pd.read_parquet("../data/Gridmode-00000-of-00001.parquet")
print(df.columns)
puzzle["id"] = df.iloc[n, 0]
puzzle["dim"] = df.iloc[n, 1].split("*")


lines = df.iloc[n, 2].split("\n")
for line in lines:
    if line.startswith(" - "):
        args = line.split(": ")[1].split(", ")
        for i in range(len(args)):
            args[i] = args[i].strip("`")
        puzzle["entities"].append(args)
    elif line[:1].isdigit():
        constraint_counter += 1
        args = line.split(" ")
        args.pop(0)

        entities = flatten_2d(puzzle["entities"])
        constraint = Constraint()

        for entity in entities:
            if entity.lower() in line.lower():
                if constraint.a is None:
                    constraint.a = entity
                else:
                    constraint.b = entity

        # type of constraint missing

        if constraint.complete():
            puzzle["constraints"].append(constraint)
        else:
            print(f"INVALID CONSTRAINT {constraint}, AT {constraint_counter}")


print(df.iloc[n, 2])
print(puzzle["id"], puzzle["dim"], puzzle["entities"])
print(puzzle["constraints"])
print(constraint_counter, len(puzzle["constraints"]))