from questions import QUESTIONS;


def isAnswerCorrect(question, answer):
    #print("ind",question ,QUESTIONS[question])

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if QUESTIONS[question]['answer']==answer:
        return True 
    False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    quelevel=0   
    life_line=1 
    while(quelevel<15):
        print("Quetion NO. {} :  {} ".format(quelevel+1,QUESTIONS[quelevel]['name']))
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[quelevel]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[quelevel]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[quelevel]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[quelevel]["option4"]}')



        ans = (input('Kripaya anpa answer dale (<1-4> or ?): '))
        #print(ans<'5',ans>'0')

        while(ans != '1' and ans != '2' and  ans != '3' and ans != '4'):
            if life_line and  ans=="?":
                break
            ans=(input("kripya sahi ans dale :"))
        if ans=="?":
            if life_line:
                life_line=0
                ind=1
                key=QUESTIONS[quelevel].keys()
                key=list(key)
                #print("key",key)
                rm=1
                
                print("New options are")
                ind=1
                while(ind != 5):
                    if int(key[ind][-1]) != int(QUESTIONS[quelevel]["answer"]) :
                        if rm:
                            print("\t\t\t option {} : {}".format(ind,QUESTIONS[quelevel]["option"+str(ind)]))
                            rm=0
                        else:
                            print("\t\t\t option {}: This ans is removed".format(ind))
                    else:
                    
                        print("\t\t\t option {} : {}".format(ind,QUESTIONS[quelevel]["option"+str(ind)]))
                    ind+=1
            ans = (input('Kripaya anpa answer dale <1-4>: '))
        #print(ans<'5',ans>'0')

            while(ans != '1' and ans != '2' and  ans != '3' and ans != '4'):
                if life_line and  ans=="?":
                   break
                ans=(input("kripya sahi ans dale :"))




       

    # check for the input validations

        if isAnswerCorrect(quelevel, int(ans) ):
        # print the total money won.
        # See if the user has crossed a level, print that if yes
            print('\n Sahi jawab !')
            print(" Arun aap jeet chuke hai :",QUESTIONS
            [quelevel]['money'])

        else:
        # end the game now.
        # also print the correct answer
            print('\nGalat jawab !')
            print("Your amount is : ",end="")
            if (quelevel>=11):
                print(320000)
            elif quelevel >=5:
                print(1000)
            else:
                print(0)
            print("Correct answer was :",QUESTIONS[quelevel]['answer'])
            break
        quelevel+=1
        if quelevel==15:
            print("Bahut bahut badhai aap jeet chuke hai poore 10000000 rupye !!!")

    # print the total money won in the end'''


kbc()
