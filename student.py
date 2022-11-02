__all__ = [homework_average]


def homework_average(grades, student_id):
    if student_id not in grades:
        return 0
    
    holder = 0

    holder = int(grades[student_id]['homework'][0])
    holder = int(grades[student_id]['homework'][1])
    holder = int(grades[student_id]['homework'][2])

    return holder / 3




def laboratory_average(grades, student_id):
    if student_id not in grades:
      return 0
    holder = 0
    holder += int(grades[student_id]['laboratory'][0])
    holder += int(grades[student_id]['laboratory'][1])

    return round(holder / 2)

def total_weighted_average(grades, student_id):
    if student_id not in grades:
        return 0

#print(g[52392]['homework'])
