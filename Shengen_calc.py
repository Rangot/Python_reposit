residence_limit = 90  # 45, 60
schengen_constraint = 180

# Мы тратим в день
cost_per_day = 15

first_of_january = 1  # первое января текущего года

visits = [[1, 11], [16, 27], [45, 46], [251, 260]]

for visit in visits:
    if not isinstance(visit, list):
        raise Exception('Ошибка в поездке', visit)
        
for visit in visits:
    if visit[0] > visit[1]:
        raise Exception('Ошибка ввода дат', visit)
       


# 11, 11 + 12, 11 + 12 + 2, 10

days_in_eu = []

total_time_in_es = 0

for visit in visits:
    past_days = 0
    for past_visit in visits:
        # совмещение 2 условий
        if visit[0] - schengen_constraint < past_visit[0] <= visit[0]:
            past_days += past_visit[1] - past_visit[0] + 1
    days_in_eu.append(past_days)
    total_time_in_es += visit[1] - visit[0] + 1



# assert total_time_in_es == 11 + 12 + 2 + 10

print(days_in_eu)
print(visits)
assert days_in_eu == [11, 11 + 12, 11 + 12 + 2, 10]

for visit, days in zip(visits, days_in_eu):
    if days > residence_limit:
        print('В течение поездки', visit, 'вы пребывали в ЕС слишком долго:', days)

if total_time_in_es > residence_limit:
    print('Вы не можете прибывать в ЕС так долго')

print('Вы пробудете в ЕС дней:', total_time_in_es)