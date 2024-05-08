if __name__ == '__main__':
    records = [["chi",20.0],["beta",50.0],["alpha",50.0]]
    grade = []
    names = []

    for record in records:
        grade.append(record[1])
    grade = list(set(grade))
    grade.sort()

    #return second lowest grade
    # if only 1 (shouldn't happen but ...) or two students 2nd lowest will be in [-1]
    if len(grade) <= 2:
        second_lowest = grade[-1]
    else:
        second_lowest = grade[1]

    #grab all the names that match the grade, sort, print
    for record in records:
        if record[1] == second_lowest:
            names.append(record[0])
    names.sort()
    for name in names:
        print(name)