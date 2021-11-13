def solution(balloons):
    answer = 0
    slopes1 = []
    slopes3 = []

    for i in range(len(balloons)):
        if (balloons[i][0] > 0 and balloons[i][1] > 0) or (balloons[i][0] < 0 and balloons[i][1] > 0) or (balloons[i][0] == 0 and balloons[i][1] > 0) or (balloons[i][0] < 0 and balloons[i][1] == 0):
            slope1 = balloons[i][1] / balloons[i][0]
            slopes1.append(slope1)
        else:
            slope3 = balloons[i][1] / balloons[i][0]
            slopes3.append(slope3)

    slopes1 = list(set(slopes1))
    slopes3 = list(set(slopes3))

    answer = len(slopes1) + len(slopes3)

    return answer