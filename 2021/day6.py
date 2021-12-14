import collections
import math


def calc_family_size(fish_age_at_0, respawn_time, time):
    math.e ** (math.log(2 ^ (1 / respawn_time) * (time + fish_age_at_0)))


test_input = """3,4,3,1,2"""

day6_input = "1,3,4,1,1,1,1,1,1,1,1,2,2,1,4,2,4,1,1,1,1,1,5,4,1,1,2,1,1,1,1,4,1,1,1,4,4,1,1,1,1,1,1,1,2,4,1,3,1,1,2,1,2,1,1,4,1,1,1,4,3,1,3,1,5,1,1,3,4,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,5,5,3,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,1,1,1,1,5,1,1,1,1,1,4,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,3,1,2,4,1,5,5,1,1,5,3,4,4,4,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,5,3,1,4,1,1,2,2,1,2,2,5,1,1,1,2,1,1,1,1,3,4,5,1,2,1,1,1,1,1,5,2,1,1,1,1,1,1,5,1,1,1,1,1,1,1,5,1,4,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,4,5,1,1,1,1,1,1,1,5,1,1,3,1,1,1,3,1,4,2,1,5,1,3,5,5,2,1,3,1,1,1,1,1,3,1,3,1,1,2,4,3,1,4,2,2,1,1,1,1,1,1,1,5,2,1,1,1,2"

if __name__ == '__main__':
    initial_state = [int(x) for x in day6_input.split(',')]
    age_dict = collections.defaultdict(int)
    for i in initial_state:
        age_dict[i] += 1
    print(age_dict)
    days = 256

    for i in range(days):
        new_age_dict = collections.defaultdict(int)
        for old_age, value in age_dict.items():
            new_age_dict[old_age - 1] = value
        minus = 0
        if -1 in new_age_dict.keys():
            minus = new_age_dict.pop(-1)
        new_age_dict[6] += minus
        new_age_dict[8] = minus

        print(new_age_dict)
        print(sum(new_age_dict.values()))
        age_dict = new_age_dict
