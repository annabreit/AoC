from collections import defaultdict
from copy import deepcopy

test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

input12 = """yw-MN
wn-XB
DG-dc
MN-wn
yw-DG
start-dc
start-ah
MN-start
fi-yw
XB-fi
wn-ah
MN-ah
MN-dc
end-yw
fi-end
th-fi
end-XB
dc-XB
yw-XN
wn-yw
dc-ah
MN-fi
wn-DG"""



def get_paths_for_node(node, path_dict, current_path=None, all_paths=None, visited_small_caves=None):
    if all_paths is None:
        all_paths = []
    if current_path is None:
        current_path = []
    if visited_small_caves is None:
        visited_small_caves = []
    if len(path_dict[node]) < 1:
        current_path.append(node)
        all_paths.append(current_path)
        return all_paths

    for next_node in path_dict[node]:
        new_current_path = current_path + [node]
        new_path_dict = deepcopy(path_dict)
        if next_node.islower():
            if len(visited_small_caves)==0 and next_node != 'end':
                new_visited_small_caves = visited_small_caves + [next_node]
                new_new_current_path = current_path + [node]
                new_new_path_dict = deepcopy(new_path_dict)
                get_paths_for_node(next_node, new_new_path_dict, new_new_current_path, all_paths, new_visited_small_caves)
            for k, v in new_path_dict.items():
                if next_node in v:
                    v.remove(next_node)
        get_paths_for_node(next_node, new_path_dict, new_current_path, all_paths, visited_small_caves)
    return all_paths

if __name__ == '__main__':

    cave_sys_dict = defaultdict(list)
    lines = input12.split("\n")
    for line in lines:
        left = line.split("-")[0]
        right = line.split("-")[1]
        if left != "end" and right !="start":
            cave_sys_dict[left].append(right)
        if left != "start" and right !="end":
            cave_sys_dict[right].append(left)
    for k,v in cave_sys_dict.items():
        cave_sys_dict[k] = list(set(v))
    print(cave_sys_dict)
    paths = get_paths_for_node('start', cave_sys_dict)
    print(paths)
    non_dead_ends = [p for p in paths if p[-1]=="end"]
    unique_data = [list(x) for x in set(tuple(x) for x in non_dead_ends)]

    print(non_dead_ends)
    print(len(non_dead_ends))
    print(len(unique_data))
    paths = []
