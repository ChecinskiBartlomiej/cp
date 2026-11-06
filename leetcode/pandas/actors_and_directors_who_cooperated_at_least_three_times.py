#https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/

import pandas as pd

data={
    "actor_id": [1,1,1,1,1,2,2],
    "director_id": [1,1,1,2,2,1,1],
    "timestep": [0,1,2,3,4,5,6]
}
df = pd.DataFrame(data)

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    out=actor_director.groupby(["actor_id","director_id"],as_index=False).size()
    out=out[out["size"]>=3].loc[:,["actor_id","director_id"]]
    return out