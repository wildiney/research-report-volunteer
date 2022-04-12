partcipationItems = ["Participo sempre", "Participo bastante",
                     "Participo eventualmente", "Participo pouco", "Não participo"]

satisfactionItems = ["Muito satisfeito", "Pouco Satisfeito",
                     "Neutro", "Insatisfeito", "Muito insatisfeito"]


def participation_items():
    return partcipationItems


def participation(number):
    if(number == 0 or number == 1):
        probability = partcipationItems[0]
    elif(number == 2 or number == 3):
        probability = partcipationItems[1]
    elif(number == 4 or number == 5 or number == 6):
        probability = partcipationItems[2]
    elif(number == 7 or number == 8):
        probability = partcipationItems[3]
    else:
        probability = partcipationItems[4]
    return probability


def participateNextActions(number):
    if(number == 0 or number == 1):
        probability = "Participarei com certeza"
    elif(number == 2 or number == 3):
        probability = "Provavelmente participarei"
    elif(number == 4 or number == 5 or number == 6):
        probability = "Talvez participe"
    elif(number == 7 or number == 8):
        probability = "Provavelmente não participarei"
    else:
        probability = "Não participarei"
    return probability


def probability(number):
    if(number == 0 or number == 1):
        probability = "Muito Provável"
    elif(number == 2 or number == 3):
        probability = "Provável"
    elif(number == 4 or number == 5 or number == 6):
        probability = "Talvez"
    elif(number == 7 or number == 8):
        probability = "Improvável"
    else:
        probability = "Muito Improvável"

    return probability


def satisfaction(number):
    if(number == 0 or number == 1):
        satisfaction = satisfactionItems[0]
    elif(number == 2 or number == 3):
        satisfaction = satisfactionItems[1]
    elif(number == 4 or number == 5 or number == 6):
        satisfaction = satisfactionItems[2]
    elif(number == 7 or number == 8):
        satisfaction = satisfactionItems[3]
    else:
        satisfaction = satisfactionItems[4]

    return satisfaction
