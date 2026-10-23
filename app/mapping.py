from rapidfuzz import fuzz


def find_similar_parameters(
        old_keys,
        new_keys):

    mappings = []

    for old_key in old_keys:

        for new_key in new_keys:

            score = fuzz.ratio(
                old_key,
                new_key
            )

            if score > 80:

                mappings.append({
                    "old": old_key,
                    "new": new_key,
                    "score": score
                })

    return mappings
