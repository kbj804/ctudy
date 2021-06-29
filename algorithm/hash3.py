def solution(genres, plays):
    music ={}
    key = {}
    for i in range(0, len(genres)):
        if genres[i] in music:
            key[genres[i]] += plays[i]
            music[genres[i]][i] = plays[i]

        else:
            music[genres[i]] = {}
            key[genres[i]] = 0
            key[genres[i]] += plays[i]
            music[genres[i]][i] = plays[i]

    answer = []
    
    key_sort = sorted(key.items(), key=lambda x:x[1] ,reverse=True)

    for key, _ in key_sort:
        mm = sorted(music[key].items(), key=lambda x:x[1], reverse=True)
        if len(mm) > 1:
            answer.append(mm[0][0])
            answer.append(mm[1][0])
        else:
            answer.append(mm[0][0])

    return answer

a = solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])
print(a)