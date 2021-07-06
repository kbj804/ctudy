def solution(genres, plays):
    music ={}
    total = {}
    for i in range(0, len(genres)):
        if genres[i] in music:
            total[genres[i]] += plays[i]
            music[genres[i]][i] = plays[i]

        else:
            music[genres[i]] = {}
            total[genres[i]] = 0
            total[genres[i]] += plays[i]
            music[genres[i]][i] = plays[i]

    answer = []
    
    total_sort = sorted(total.items(), key=lambda x:x[1] ,reverse=True)

    for key, _ in total_sort:
        rank = sorted(music[key].items(), key=lambda x:x[1], reverse=True)
        if len(rank) > 1:
            answer.append(rank[0][0])
            answer.append(rank[1][0])
        else:
            answer.append(rank[0][0])

    return answer

a = solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])
print(a)