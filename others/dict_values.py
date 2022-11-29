# demonstrates the wide variety of object types that can be used as
# A dictionary key must be an immutable object (more precisely, it must be hashable)
example_dict = {-1: 10,
                "moo": True,
                (1, 2): print,
                3.4: "cow",
                False: []
                }

print(example_dict[-1],

      example_dict["moo"],

      example_dict[(1, 2)],

      example_dict[3.4],

      example_dict[False])
