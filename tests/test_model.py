
import pandas as pd
from recommender.model import recommend_outfit

def test_recommend_outfit():
    df = pd.DataFrame({'occasion': ['casual', 'formal'], 'outfit': ['jeans', 'suit']})
    result = recommend_outfit({'occasion': 'casual'}, df)
    assert result['outfit'] == 'jeans'
