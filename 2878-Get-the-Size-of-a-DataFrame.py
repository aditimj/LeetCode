import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    res = list(players.shape)
    return res    