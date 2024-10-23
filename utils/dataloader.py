import json
import dspy


def load_temusnews_data():
    # Make the temus dataset
    data_path = "data/data.json"

    # Load json
    raw = json.load(open(data_path))

    processed = []
    for d in raw:
        processed.append(
            dspy.Example(question=d["full_text"], answer=d["short_text"]).with_inputs(
                "question"
            )
        )

    return processed


def load_temusnews_data_raw():
    # Make the temus dataset
    data_path = "data/data.json"

    # Load json
    raw = json.load(open(data_path))

    return raw
