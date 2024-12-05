import pandas as pd

# Завантаження даних
data = pd.read_csv("DataAnalyst.csv")

# Припускаємо, що в датасеті є колонки "Founded" (рік заснування) і "Rating" (рейтинг компанії)
current_year = 2024

# Гіпотеза 1: Рейтинг компаній до 2000 року vs після 2000 року
data['before_2000'] = data['Founded'] < 2000

# Обчислення середнього рейтингу для кожної групи
avg_Rating_before_2000 = data[data['before_2000']]['Rating'].mean()
avg_Rating_after_2000 = data[~data['before_2000']]['Rating'].mean()

print("Гіпотеза 1:")
print(f"Середній рейтинг компаній, створених до 2000 року: {avg_Rating_before_2000:.2f}")
print(f"Середній рейтинг компаній, створених після 2000 року: {avg_Rating_after_2000:.2f}")
if avg_Rating_before_2000 > avg_Rating_after_2000:
    print("Гіпотеза підтверджена: старі компанії мають вищий рейтинг.")
else:
    print("Гіпотеза спростована: новіші компанії мають вищий рейтинг.")

# Гіпотеза 2: Рейтинг компаній залежить від їх віку
data['company_age'] = current_year - data['Founded']

# Групування за віком компанії (наприклад, кожні 10 років)
data['age_group'] = (data['company_age'] // 10) * 10

# Обчислення середнього рейтингу для кожної групи
age_group_Rating = data.groupby('age_group')['Rating'].mean()

print("\nГіпотеза 2:")
print("Середній рейтинг за віковими групами:")
print(age_group_Rating)

# Перевірка тренду (якщо рейтинг зменшується з віком)
if age_group_Rating.is_monotonic_decreasing:
    print("Гіпотеза підтверджена: рейтинг компаній знижується з віком.")
else:
    print("Гіпотеза спростована: рейтинг компаній не має чіткої залежності від віку.")