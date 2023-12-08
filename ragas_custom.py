"""An implementation of the Ragas metric
"""
from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase
import warnings


class ContextualPrecisionMetric(BaseMetric):
    """This metric checks the contextual precision using Ragas"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        # sends to server
        try:
            from ragas import evaluate
            from ragas.metrics import context_precision

        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        # Create a dataset from the test case
        data = {
            "contexts": [test_case.retrieval_context],
            "question": [test_case.input],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)

        # Evaluate the dataset using Ragas
        scores = evaluate(dataset, metrics=[context_precision])

        # Ragas only does dataset-level comparisons
        context_precision_score = scores["context_precision"]
        self.success = context_precision_score >= self.minimum_score
        self.score = context_precision_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Contextual Precision"


class ContextualRelevancyMetric(BaseMetric):
    """This metric checks the contextual relevancy using Ragas"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        # sends to server
        try:
            from ragas import evaluate
            from ragas.metrics import context_relevancy

        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        # Create a dataset from the test case
        data = {
            "contexts": [test_case.retrieval_context],
            "question": [test_case.input],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)

        # Evaluate the dataset using Ragas
        scores = evaluate(dataset, metrics=[context_relevancy])

        # Ragas only does dataset-level comparisons
        context_relevancy_score = scores["context_relevancy"]
        self.success = context_relevancy_score >= self.minimum_score
        self.score = context_relevancy_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Contextual Relevancy"


class AnswerRelevancyMetric(BaseMetric):
    """This metric checks the answer relevancy using Ragas"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        # sends to server
        try:
            from ragas import evaluate
            from ragas.metrics import answer_relevancy

        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        data = {
            "question": [test_case.input],
            "answer": [test_case.actual_output],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)
        scores = evaluate(dataset, metrics=[answer_relevancy])
        answer_relevancy_score = scores["answer_relevancy"]
        self.success = answer_relevancy_score >= self.minimum_score
        self.score = answer_relevancy_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Answer Relevancy"


class FaithfulnessMetric(BaseMetric):
    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        # sends to server
        try:
            from ragas import evaluate
            from ragas.metrics import faithfulness

        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        data = {
            "contexts": [test_case.retrieval_context],
            "question": [test_case.input],
            "answer": [test_case.actual_output],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)
        scores = evaluate(dataset, metrics=[faithfulness])
        faithfulness_score = scores["faithfulness"]
        self.success = faithfulness_score >= self.minimum_score
        self.score = faithfulness_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Faithfulness"


class ContextRecallMetric(BaseMetric):
    """This metric checks the context recall using Ragas"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        # sends to server
        try:
            from ragas import evaluate
            from ragas.metrics import context_recall

        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        data = {
            "question": [test_case.input],
            "ground_truths": [[test_case.expected_output]],
            "contexts": [test_case.retrieval_context],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)
        scores = evaluate(dataset, [context_recall])
        context_recall_score = scores["context_recall"]
        self.success = context_recall_score >= self.minimum_score
        self.score = context_recall_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Context Recall"


class HarmfulnessMetric(BaseMetric):
    """This metric checks the harmfulness using Ragas"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        # sends to server
        try:
            from ragas import evaluate
            from ragas.metrics.critique import harmfulness

        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        data = {
            "ground_truths": [[test_case.expected_output]],
            "contexts": [test_case.context],
            "question": [test_case.input],
            "answer": [test_case.actual_output],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)
        scores = evaluate(dataset, [harmfulness])
        harmfulness_score = scores["harmfulness"]
        self.success = harmfulness_score >= self.minimum_score
        self.score = harmfulness_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Harmfulness"


class CoherenceMetric(BaseMetric):
    """This metric checks the coherence using Ragas"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        try:
            from ragas import evaluate
            from ragas.metrics.critique import coherence
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        data = {
            "ground_truths": [[test_case.expected_output]],
            "contexts": [test_case.context],
            "question": [test_case.input],
            "answer": [test_case.actual_output],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)
        scores = evaluate(dataset, [coherence])
        coherence_score = scores["coherence"]
        self.success = coherence_score >= self.minimum_score
        self.score = coherence_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Coherence"


class MaliciousnessMetric(BaseMetric):
    """This metric checks the maliciousness using Ragas"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        try:
            from ragas import evaluate
            from ragas.metrics.critique import maliciousness

        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        data = {
            "ground_truths": [[test_case.expected_output]],
            "contexts": [test_case.context],
            "question": [test_case.input],
            "answer": [test_case.actual_output],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)
        scores = evaluate(dataset, [maliciousness])
        maliciousness_score = scores["maliciousness"]
        self.success = maliciousness_score >= self.minimum_score
        self.score = maliciousness_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Maliciousness"


class CorrectnessMetric(BaseMetric):
    """This metric checks the correctness using Ragas"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        try:
            from ragas import evaluate
            from ragas.metrics.critique import correctness

        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        data = {
            "ground_truths": [[test_case.expected_output]],
            "contexts": [test_case.context],
            "question": [test_case.input],
            "answer": [test_case.actual_output],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)
        scores = evaluate(dataset, metrics=[correctness])
        correctness_score = scores["correctness"]
        self.success = correctness_score >= self.minimum_score
        self.score = correctness_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Correctness"


class ConcisenessMetric(BaseMetric):
    """This metric checks the conciseness using Ragas"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        try:
            from ragas import evaluate
            from ragas.metrics.critique import conciseness
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        data = {
            "ground_truths": [[test_case.expected_output]],
            "contexts": [test_case.context],
            "question": [test_case.input],
            "answer": [test_case.actual_output],
            "id": [[test_case.id]],
        }
        dataset = Dataset.from_dict(data)
        scores = evaluate(dataset, metrics=[conciseness])
        conciseness_score = scores["conciseness"]
        self.success = conciseness_score >= self.minimum_score
        self.score = conciseness_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "Conciseness"


class RagasMetric(BaseMetric):
    """This metric checks if the output is more than 3 letters"""

    def __init__(
        self,
        minimum_score: float = 0.3,
    ):
        self.minimum_score = minimum_score

    def measure(self, test_case: LLMTestCase):
        # sends to server
        try:
            from ragas import evaluate
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "Please install ragas to use this metric. `pip install ragas`."
            )

        try:
            # How do i make sure this isn't just huggingface dataset
            from datasets import Dataset
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Please install dataset")

        # Create a dataset from the test case
        # Convert the LLMTestCase to a format compatible with Dataset
        score_metadata = {}
        metrics = [
            ContextRecallMetric(),
            FaithfulnessMetric(),
            AnswerRelevancyMetric(),
        ]

        warnings_list = []

        for metric in metrics:
            score = metric.measure(test_case)
            score_metadata[metric.__name__] = score
            if score == 0:
                warnings_list.append(
                    f"The RAGAS score will be 0 since {metric.__name__} has a score of 0"
                )

        for warning in warnings_list:
            print(warning)

        if any(score == 0 for score in score_metadata.values()):
            ragas_score = 0
        else:
            ragas_score = len(score_metadata) / sum(
                1.0 / score for score in score_metadata.values()
            )

        self.success = ragas_score >= self.minimum_score
        self.score = ragas_score
        self.score_metadata = score_metadata
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "RAGAS"
