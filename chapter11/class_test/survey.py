class AnonymousSurvey():
	"""收集匿名调查问卷的答案"""

	def __init__(self, question):
		self.question = question
		self.responses = []

	def show_question(self):
		print(question)

	def store_response(self, new_response):
		"""存储单份调查问卷"""
		self.responses.append(new_response)

	def show_results(self):
		"""显示收集到的所有答卷"""
		print("Survey results:")
		for response in responses:
			print('- ' + response)

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()

print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

#显示调查结果
print("\nThank you to everyone who particated in the survey!")
my_survey.show_results()

