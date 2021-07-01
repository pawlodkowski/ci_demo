from funcs import add_one, recommend_movie
import pytest


# parametrized test
EXAMPLES = [(5, 6), (100, 101), (5.3, 6.3), (-100, -99)]
MOVIES = ["Harry Potter and the Colime Similarity", "Star Wars: The colimes awaken", "Lord of the colimes"]

@pytest.mark.parametrize(['inp', 'exp_out'], EXAMPLES)    #variable names as string
def test_no1(inp, exp_out):
    assert add_one(inp) == exp_out

def test_recommender():
    result = recommend_movie(MOVIES)
    assert isinstance(result, str)
    assert result.isupper()

def test_recommender2():
    assert len(recommend_movie(MOVIES)) > 0 

def test_wrong_input():
    with pytest.raises(TypeError):
        recommend_movie('Hello')  # we test if the test is raised with wrong input