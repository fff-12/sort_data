import pandas as pd

data = pd.read_csv("DataAnalyst.csv")

current_year = 2024

# Гіпотеза 1: Рейтинг компаній до 2000 року vs після 2000 року
data['before_2000'] = data['Founded'] < 2000
data['after_2000'] = data['Founded'] > 2000

avg_Rating_before_2000 = data[data['before_2000']]['Rating'].mean()
avg_Rating_after_2000 = data[data['after_2000']]['Rating'].mean()

print("Гіпотеза 1:")
print(f"Середній рейтинг компаній, створених до 2000 року: {avg_Rating_before_2000:.2f}")
print(f"Середній рейтинг компаній, створених після 2000 року: {avg_Rating_after_2000:.2f}")
if avg_Rating_before_2000 > avg_Rating_after_2000:
    print("Гіпотеза підтверджена: старі компанії мають вищий рейтинг.")
else:
    print("Гіпотеза спростована: новіші компанії мають вищий рейтинг.")

# Гіпотеза 2: Рейтинг компаній зменшується з віком
data['company_age'] = current_year - data['Founded']

data['age_group'] = (data['company_age'] // 10) * 10

age_group_Rating = data.groupby('age_group')['Rating'].mean()

print("Гіпотеза 2:")
print("Середній рейтинг за віковими групами:")
print(age_group_Rating)

if age_group_Rating.is_monotonic_decreasing:
    print("Гіпотеза підтверджена: рейтинг компаній знижується з віком.")
else:
    print("Гіпотеза спростована: рейтинг компаній не має чіткої залежності від віку.")
