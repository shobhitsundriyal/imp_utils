import os

i = 0
for filename in os.listdir("Infection"): 
    dst ="incision_infected(" + str(i) + ").jpg"
    src ='Infection/'+ filename 
    dst ='Infection/'+ dst 
    os.rename(src, dst) 
    i += 1