import random

capitals = capitals = {
    'Abia': 'Umuahia',
    'Adamawa': 'Yola',
    'Akwa Ibom': 'Uyo',
    'Anambra': 'Awka',
    'Bauchi': 'Bauchi',
    'Bayelsa': 'Yenagoa',
    'Benue': 'Makurdi',
    'Borno': 'Maiduguri',
    'Cross River': 'Calabar',
    'Delta': 'Asaba',
    'Ebonyi': 'Abakaliki',
    'Edo': 'Benin City',
    'Ekiti': 'Ado-Ekiti',
    'Enugu': 'Enugu',
    'Gombe': 'Gombe',
    'Imo': 'Owerri',
    'Jigawa': 'Dutse',
    'Kaduna': 'Kaduna',
    'Kano': 'Kano',
    'Katsina': 'Katsina',
    'Kebbi': 'Birnin Kebbi',
    'Kogi': 'Lokoja',
    'Kwara': 'Ilorin',
    'Lagos': 'Ikeja',
    'Nasarawa': 'Lafia',
    'Niger': 'Minna',
    'Ogun': 'Abeokuta',
    'Ondo': 'Akure',
    'Osun': 'Osogbo',
    'Oyo': 'Ibadan',
    'Plateau': 'Jos',
    'Rivers': 'Port Harcourt',
    'Sokoto': 'Sokoto',
    'Taraba': 'Jalingo',
    'Yobe': 'Damaturu',
    'Zamfara': 'Gusau'
}

for quizNum in range(5):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answer%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + 'State Capital Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #shuffle the order of the states

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(36):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 
1, 
               states[questionNum])) 
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i])) 
        quizFile.write('\n') 
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[ 
            answerOptions.index(correctAnswer)])) 
    quizFile.close()
    answerKeyFile.close()