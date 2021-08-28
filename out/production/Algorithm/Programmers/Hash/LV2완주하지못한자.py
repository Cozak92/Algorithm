def solution(participants, completions):
    answer = {participant : 0 for participant in participants}
    for completion in completions:
            answer[completion] += 1

    for participant in participants:
        if answer[participant] == 0 :
            return participant
        else:
            answer[participant] -= 1

# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
        

participants = ["marina", "josipa", "nikola", "vinko", "filipa"]
completions = ["josipa", "filipa", "marina", "nikola"]

solution(participants,completions)

# for a in zip(participants,completions):
#     print(a)