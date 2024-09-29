import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pandas.DataFrame(student_data,columns = ['student_id','age'])
    return df
    