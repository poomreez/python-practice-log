from typing import Union

def score_cal(a: int, b: int) -> Union[int, float]:
    return a / b

score1 = score_cal(20, 10)

print(score1)