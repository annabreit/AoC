test_input = "16,1,2,0,4,2,7,1,2,14"

if __name__ == '__main__':
    crab_pos = [int(x) for x in test_input.split(",")]
    with open("input7.txt", "r") as f:
        crab_pos = [int(x) for x in f.read().split(",")]
    crab_pos = sorted(crab_pos)

    fuel_cost = []
    for opt_pos in range(crab_pos[0], crab_pos[-1]+1):
        this_fuel_cost = [abs(crab-opt_pos) for crab in crab_pos]
        fuel_cost.append(sum(this_fuel_cost))
    print(fuel_cost)
    print(min(fuel_cost))

    fuel_cost = []
    for opt_pos in range(crab_pos[0], crab_pos[-1]+1):
        this_fuel_cost = [sum(range(1,abs(crab-opt_pos)+1)) for crab in crab_pos]
        fuel_cost.append(sum(this_fuel_cost))
    print(fuel_cost)
    print(min(fuel_cost))