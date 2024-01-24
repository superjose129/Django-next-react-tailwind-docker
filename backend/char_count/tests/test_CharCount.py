from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from char_count import views


class TestCharCount(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.CharCount.as_view()

    def tests(self):
        test_dict = [
            {"input": {"text": "asdf"}, "answer": 4},
            {"input": {"text": 1}, "answer": None},
            {"input": {"text": "asdfasdfasdf"}, "answer": 12},
            {"input": {"text": None}, "answer": None},
        ]

        for test in test_dict:
            request = self.factory.post("/char_count/", test["input"], format="json")
            response = self.view(request)

            assert (
                test["answer"] == response.data["count"]
            ), f"{response} not equal to {test['answer']}"
