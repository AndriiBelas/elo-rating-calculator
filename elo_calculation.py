def get_expected_score(rating_difference):
    return 1/(1+10**(rating_difference/400))

def calculate_new_elo(first_rating, second_rating, result, k):
    rating_difference = second_rating-first_rating
    expected_score_1 = get_expected_score(rating_difference)
    expected_score_2 = get_expected_score(-rating_difference)
    new_first_rating = round(first_rating + k*(result-expected_score_1))
    new_second_rating = round(second_rating + k*(1-result-expected_score_2))
    return new_first_rating, new_second_rating

