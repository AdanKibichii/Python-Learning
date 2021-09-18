import random
def coin_flip():
    if random.randint(0,1)==0:
        return "heads"
    else:
        return "tails"

flips=0
num_trial=10_000
for trial in range (num_trial):
    first_trial=coin_flip()
    flips=flips+1
    if coin_flip()==first_trial:
        flips=flips+1
    flips=flips+1

avg_flips_per_trial=flips/num_trial
print(avg_flips_per_trial)



import random
def roll():
    for roll in range (random.randint(1,6)):
        return random.randint(1,6)

tally1=0
tally2=0
tally3=0
tally4=0
tally5=0
tally6=0
for trials in range (10_000):
    if roll()==1:
        tally1=tally1+1
    elif roll()==2:
        tally2=tally2+1
    elif roll()==3:
        tally3=tally3+1
    elif roll()==4:
        tally4=tally4+1
    elif roll()==5:
        tally5=tally5+1
    elif roll()==6:
        tally6=tally6+1

print(f"one={tally1}, two={tally2}, three={tally3}, four={tally4}, five={tally5}, six={tally6}")