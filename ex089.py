from statistics import mean

infos_students = list()

def get_name():
    return input("Nome do aluno: \n")

def get_grades(student_name):
    grades = list()
    counter = 1
    grades.append(student_name)
    while counter < 3:
        grade = int(input(f"{counter}ª nota: \n"))
        grades.append(grade)
        counter += 1
    infos_students.append(grades)
    return infos_students

def display_infos():
    return infos_students

while True:
    get_grades(get_name())
    question = input("Deseja adicionar mais um aluno? \n").lower()
    if question[0] == "n":
        break

def calculate_mean(students_infos):
    students_means = list()
    new_infos = list()

    for item in students_infos:
        students_means.append(item[0])
        students_means.append(mean(item[1:]))
        new_infos.append(students_means)
        del students_means
        students_means = list()

    return new_infos

def display_school_report():
    pass

# display_school_report(display_infos())

print(calculate_mean(display_infos()))

'''
Este programa lê nome e duas notas de vários alunos e armazena tudo em uma lista composta. Em seguida, ele calcula a média das notas de cada aluno e exibe um boletim com a média de cada um. O programa permite ao usuário mostrar as notas de cada aluno individualmente.
'''
