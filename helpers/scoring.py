# -------------------------------------------------
# Scoring logic for phishing identification test
# -------------------------------------------------


from helpers.item_bank import ITEM_BANK
from helpers.item_service import get_item_responses


def compute_score():

    responses = get_item_responses()

    correct = 0
    total = 0

    for r in responses:

        item_id = r["item_id"]
        user_answer = r["value"]

        metadata = ITEM_BANK.get(item_id)

        if metadata is None:
            continue

        correct_answer = metadata["correct_answer"]

        if user_answer == correct_answer:
            correct += 1

        total += 1

    return correct, total



