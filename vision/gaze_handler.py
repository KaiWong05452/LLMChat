# Calculate the tuple [float, float]
# if the float is close to -1, 0, 1,
# the weight of the float will be large to the closest value.
# then calculate the ratio of 0 weighted counts / total weighted counts
# the ratio will be the eye contact ratio ranged from 0~1
# 0 means no eye contact, 1 means very eye contact.


def calculate_eye_contact_ratio(directions):
    weights = {-1: 0, 0: 0, 1: 0}

    for direction in directions:
        for value in direction:
            closest = min(weights.keys(), key=lambda k: abs(k-value))
            weights[closest] += 1 - abs(closest - value)

    total = sum(weights.values())
    eye_contact_ratio = weights[0] / total * 100 if total != 0 else 0

    return eye_contact_ratio
