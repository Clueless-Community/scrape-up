import unittest
import json
from scrape_up.askubuntu.questions import Questions


class AskUbuntuTest(unittest.TestCase):
    def setUp(self):
        self.topic = "github"
        self.questions = Questions(self.topic)

    def test_getNewQuestions(self):
        result = self.questions.getNewQuestions()
        data = json.loads(result)

        self.assertIsInstance(data, dict)
        self.assertIn("questions", data)
        self.assertIsInstance(data["questions"], list)

        questions = data["questions"]
        self.assertTrue(questions)  # Ensure the list of questions is not empty

        # Check the first question in the list
        first_question = questions[0]
        self.assertIsInstance(first_question, dict)
        self.assertIn("question", first_question)
        self.assertIn("views", first_question)
        self.assertIn("vote_count", first_question)
        self.assertIn("answer_count", first_question)
        self.assertIn("description", first_question)

        # Additional specific assertions for data types or values
        self.assertIsInstance(first_question["question"], str)
        self.assertIsInstance(first_question["views"], str)
        self.assertIsInstance(first_question["vote_count"], str)
        self.assertIsInstance(first_question["answer_count"], str)
        self.assertIsInstance(first_question["description"], str)

    def test_getActiveQuestions(self):
        result = self.questions.getActiveQuestions()
        data = json.loads(result)

        self.assertIsInstance(data, dict)
        self.assertIn("questions", data)
        self.assertIsInstance(data["questions"], list)

        questions = data["questions"]
        self.assertTrue(questions)  # Ensure the list of questions is not empty

        # Check the first question in the list
        first_question = questions[0]
        self.assertIsInstance(first_question, dict)
        self.assertIn("question", first_question)
        self.assertIn("views", first_question)
        self.assertIn("vote_count", first_question)
        self.assertIn("answer_count", first_question)
        self.assertIn("description", first_question)

        # Additional specific assertions for data types or values
        self.assertIsInstance(first_question["question"], str)
        self.assertIsInstance(first_question["views"], str)
        self.assertIsInstance(first_question["vote_count"], str)
        self.assertIsInstance(first_question["answer_count"], str)
        self.assertIsInstance(first_question["description"], str)

    def test_getUnansweredQuestions(self):
        result = self.questions.getUnansweredQuestions()
        data = json.loads(result)

        self.assertIsInstance(data, dict)
        self.assertIn("questions", data)
        self.assertIsInstance(data["questions"], list)

        questions = data["questions"]
        self.assertTrue(questions)  # Ensure the list of questions is not empty

        # Check the first question in the list
        first_question = questions[0]
        self.assertIsInstance(first_question, dict)
        self.assertIn("question", first_question)
        self.assertIn("views", first_question)
        self.assertIn("vote_count", first_question)
        self.assertIn("answer_count", first_question)
        self.assertIn("description", first_question)

        # Additional specific assertions for data types or values
        self.assertIsInstance(first_question["question"], str)
        self.assertIsInstance(first_question["views"], str)
        self.assertIsInstance(first_question["vote_count"], str)
        self.assertIsInstance(first_question["answer_count"], str)
        self.assertIsInstance(first_question["description"], str)

    def test_getBountiedQuestions(self):
        result = self.questions.getBountiedQuestions()
        data = json.loads(result)

        self.assertIsInstance(data, dict)
        self.assertIn("questions", data)
        self.assertIsInstance(data["questions"], list)

        questions = data["questions"]
        self.assertTrue(questions)  # Ensure the list of questions is not empty

        # Check the first question in the list
        first_question = questions[0]
        self.assertIsInstance(first_question, dict)
        self.assertIn("question", first_question)
        self.assertIn("views", first_question)
        self.assertIn("vote_count", first_question)
        self.assertIn("answer_count", first_question)
        self.assertIn("description", first_question)

        # Additional specific assertions for data types or values
        self.assertIsInstance(first_question["question"], str)
        self.assertIsInstance(first_question["views"], str)
        self.assertIsInstance(first_question["vote_count"], str)
        self.assertIsInstance(first_question["answer_count"], str)
        self.assertIsInstance(first_question["description"], str)

    def test_getFrequentQuestions(self):
        result = self.questions.getFrequentQuestions()
        data = json.loads(result)

        self.assertIsInstance(data, dict)
        self.assertIn("questions", data)
        self.assertIsInstance(data["questions"], list)

        questions = data["questions"]
        self.assertTrue(questions)  # Ensure the list of questions is not empty

        # Check the first question in the list
        first_question = questions[0]
        self.assertIsInstance(first_question, dict)
        self.assertIn("question", first_question)
        self.assertIn("views", first_question)
        self.assertIn("vote_count", first_question)
        self.assertIn("answer_count", first_question)
        self.assertIn("description", first_question)

        # Additional specific assertions for data types or values
        self.assertIsInstance(first_question["question"], str)
        self.assertIsInstance(first_question["views"], str)
        self.assertIsInstance(first_question["vote_count"], str)
        self.assertIsInstance(first_question["answer_count"], str)
        self.assertIsInstance(first_question["description"], str)

    def test_getHighScoredQuestions(self):
        result = self.questions.getHighScoredQuestions()
        data = json.loads(result)

        self.assertIsInstance(data, dict)
        self.assertIn("questions", data)
        self.assertIsInstance(data["questions"], list)

        questions = data["questions"]
        self.assertTrue(questions)  # Ensure the list of questions is not empty

        # Check the first question in the list
        first_question = questions[0]
        self.assertIsInstance(first_question, dict)
        self.assertIn("question", first_question)
        self.assertIn("views", first_question)
        self.assertIn("vote_count", first_question)
        self.assertIn("answer_count", first_question)
        self.assertIn("description", first_question)

        # Additional specific assertions for data types or values
        self.assertIsInstance(first_question["question"], str)
        self.assertIsInstance(first_question["views"], str)
        self.assertIsInstance(first_question["vote_count"], str)
        self.assertIsInstance(first_question["answer_count"], str)
        self.assertIsInstance(first_question["description"], str)


if __name__ == "__main__":
    unittest.main()
