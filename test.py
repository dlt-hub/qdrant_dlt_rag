
from ragas.metrics import AnswerSimilarity
answer_similarity = AnswerSimilarity()
from datasets import Dataset

from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def similarity():


#    truth = "Andrew Knox lives in Bolivia. His spending history shows that he has made 12 purchases with a total spend of 351.49. His primary type of purchases is jeans, and his last purchase date was on October 22, 2023.",
#    answer = "Andrew Knox lives in South Amanda. His spending history is as follows:\n- Spend on Shoes: $184.75\n- Spend on Jeans: $17.98\n- Spend on Shirts: $148.76"

    truth = "1"
    answer = "2"

    data = {
        'answer': truth,
        'ground_truths': answer
    }
                    
    dataset = Dataset.from_dict(data)

    similarity_score = answer_similarity.score(dataset)
    
    print(similarity_score)

similarity()