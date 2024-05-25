from survey import AnonymousSurvey

# Define a question & make a survey
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question & store responses 
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results
print("\nThank you, here are the results:")
language_survey.show_results()

