import pandas as pd

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_3_(1991%E2%80%9392)')

print(len(simpsons))
