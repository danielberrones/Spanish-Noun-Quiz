## Spanish Noun Quiz
## Created by Daniel Berrones (email: Daniel.A.Berrones@gmail.com)

class Quiz:
	''' This creates the quiz '''
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

spanishQuestions = [

]

questionsList = [
Quiz(spanishQuestions[0], "a"),
Quiz(spanishQuestions[1], "c"),
Quiz(spanishQuestions[2], "c"),
Quiz(spanishQuestions[3], "a"),
Quiz(spanishQuestions[4], "a"),
Quiz(spanishQuestions[5], "a"),         
Quiz(spanishQuestions[6], "c"),    
Quiz(spanishQuestions[7], "b"),   
Quiz(spanishQuestions[8], "c"),
Quiz(spanishQuestions[9], "d"),
Quiz(spanishQuestions[10], "a"),

]

def main(spanishQuestions):

	score = 0
	counter = 1
	total = int(len(questionsList))

	for question in questionsList:
		print(f"Question #{counter}:")
		counter += 1 
		answer = input(question.prompt + "\n>>> ")
		if answer == question.answer:
			score += 1
	print("Congrats!  You guessed {:.0%} percent correctly.".format(score/total))

main(questionsList)
