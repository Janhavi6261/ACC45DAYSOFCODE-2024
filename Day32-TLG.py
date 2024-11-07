
N = int(input().strip())


cumulative_score_1 = 0
cumulative_score_2 = 0
max_lead = 0
winner = 0

 
for _ in range(N):
    S, T = map(int, input().strip().split())
    
   
    cumulative_score_1 += S
    cumulative_score_2 += T
    
  
    if cumulative_score_1 > cumulative_score_2:
        current_lead = cumulative_score_1 - cumulative_score_2
        current_leader = 1
    else:
        current_lead = cumulative_score_2 - cumulative_score_1
        current_leader = 2
    
  
    if current_lead > max_lead:
        max_lead = current_lead
        winner = current_leader


print(winner, max_lead)
