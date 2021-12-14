test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

corrupted_points_dict = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
incomplete_points_dict = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def get_corrupted(lines):
    corrupted_tuples = []
    for i, line in enumerate(lines):
        stack = []
        for char in line:
            if char in "([{<":
                stack.append(char)
            else:
                opening = stack.pop()
                if (opening == "(" and char != ")") or (opening == "[" and char != "]") or (
                        opening == "{" and char != "}") or (opening == "<" and char != ">"):
                    corrupted_tuples.append((i, char))
                    break
    return corrupted_tuples

def get_missing(lines):
    missing_tuples = []
    for i, line in enumerate(lines):
        stack = []
        corrupted = False
        for char in line:
            if char in "([{<":
                stack.append(char)
            else:
                opening = stack.pop()
                if (opening == "(" and char != ")") or (opening == "[" and char != "]") or (
                        opening == "{" and char != "}") or (opening == "<" and char != ">"):
                    corrupted = True
                    break
        if not corrupted:
            missing_tuples.append((i, list(reversed(stack))))
    return missing_tuples

if __name__ == '__main__':

    lines = test_input.split("\n")
    with open("input10.txt", "r") as f:
        lines = f.read().split("\n")


    corrupted_tuples = get_corrupted(lines)
    print(corrupted_tuples)
    print(sum([corrupted_points_dict[x] for _, x in corrupted_tuples]))

    missing_tuples = get_missing(lines)
    print(missing_tuples)
    scores = []
    for i, brackets in missing_tuples:
        score = 0
        for b in brackets:
            score *= 5
            score += incomplete_points_dict[b]
        scores.append(score)

    print(scores)
    print(sorted(scores))
    print(sorted(scores)[int((len(scores)/2))])

