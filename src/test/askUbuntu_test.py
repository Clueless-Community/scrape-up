from scrape_up import askUbuntu
import json
que = askUbuntu.Questions("github")
scrape = que.scrape()
json = json.loads(scrape)
questions = json["questions"]
for q in questions:
    print("\nQuestion: ", q["question"])
    print("Views: ", q["views"])
    print("Votes: ", q["vote_count"])
    print("Answers: ", q["answer_count"])
    print("Description: ", q["description\n"])