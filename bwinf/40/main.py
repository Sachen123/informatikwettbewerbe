import itertools
from operator import itemgetter

inout = open("hotels5.txt").read().splitlines()

hotels_counts = 0
hotels = []
hotel = []
time_given = 0
time = 0
last_time = 0

for j in range(2):
    if j == 0:
        hotels_counts = int(inout[j])
    else:
        time_given = int(inout[j])

time_between = 60 * 4

for lines in range(len(inout)):
    hotel = []
    line = inout[lines].split(" ")
    if lines <= 1:
        continue

    hotel.append(int(line[0]))
    hotel.append(float(line[1]))
    hotels.append(hotel)

diff = 1800 - time_given

hotels_taken = []
combos = []
for a in range(len(hotels)):
    if hotels[a][0] < 360:
        for b in range(a + 1, len(hotels)):
            if hotels[b][0] < 360 + hotels[a][0]:
                for c in range(b + 1, len(hotels)):
                    if hotels[c][0] < 360 + hotels[b][0]:
                        for d in range(c + 1, len(hotels)):
                            if hotels[d][0] < 360 + hotels[c][0]:
                                if hotels[d][0] + 360 >= time_given:
                                    combo = [hotels[a], hotels[b], hotels[c], hotels[d]]
                                    combos.append(combo)
                    else:
                        continue
            else:
                continue
    else:
        continue


def sort_rating(rat1, rat2, rat3, rat4):
    rating_list = [rat1, rat2, rat3, rat4]
    rating_list.sort()
    return rating_list[0]


for comb in combos:
    rating = sort_rating(comb[0][1], comb[1][1], comb[2][1], comb[3][1])
    combr = [comb, rating]
    hotels_taken.append(combr)
hotels_taken.sort(key=itemgetter(1), reverse=True)
print(hotels_taken[0])

"""
Beispiel1: [347, 2.7], [687, 4.4], [1007, 2.8], [1360, 2.8]
Beispiel2: [341, 2.3], [700, 3.0], [1051, 2.3], [1380, 5.0]
Beispiel3: [358, 2.5], [717, 0.3], [1075, 0.8], [1433, 1.7]
Beispiel4: [340, 4.6], [658, 4.6], [979, 4.7], [1301, 5.0]
Beispiel5: [280, 5.0], [636, 5.0], [987, 5.0], [1271, 5.0]
"""