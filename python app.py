import requests
import csv 
import json
import unittest
import requests



# Define the API endpoint and access key
endpoint = "https://api.openai.com/v1/engines/text-davinci-002/jobs"
access_key = "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"

# Function to query the API
def query_chatgpt(question):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_key}"
    }
    data = {
        "prompt": question,
        "max_tokens": 100,
        "temperature": 0.5,
    }
    response = requests.post(endpoint, headers=headers, json=data)
    answer = response.json()['choices'][0]['text']
    return answer
def get_answer(question):
    headers = {
        'Authorization': 'Bearer <API_KEY>',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': question,
        'max_tokens': 1024,
        'temperature': 0.5,
    }
    response = requests.post('https://api.openai.com/v1/engines/davinci/jobs', headers=headers, json=data)
    response_json = response.json()
    answer = response_json['choices'][0]['text']
    return answer
def store_answer(question, answer):
    with open('answers.csv', mode='a') as csv_file:
        fieldnames = ['question', 'answer']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'question': question, 'answer': answer})
def handle_request(request):
    question = request.json['question']
    answer = get_answer(question)
    store_answer(question, answer)
    return {'answer': answer}
def test_get_answer():
    question = 'What is the capital of France?'
    answer = get_answer(question)
    assert answer == 'Paris'
def get_user_question():
    return input("What is your question? ")
def test_store_answer():
    question = 'What is the capital of France?'
    answer = 'Paris'
    store_answer(question, answer)
    with open('answers.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        row = next(reader)
        assert row['question'] == question
        assert row['answer'] == answer


def main():
    question = get_user_question()
    answer = query_chatgpt(question)
    store_answer(question, answer)

if __name__ == '__main__':
    main()

class TestChatGPTMicroservice(unittest.TestCase):
    def test_get_answer(self):
        response = app.get_answer("What is the capital of France?")
        self.assertEqual(response, "Paris")

    def test_write_to_csv(self):
        app.write_to_csv("What is the capital of France?", "Paris")
        with open("answers.csv", "r") as file:
            data = file.readlines()[-1]
            self.assertEqual(data, "What is the capital of France?,Paris\n")

if __name__ == '__main__':
    unittest.main()
