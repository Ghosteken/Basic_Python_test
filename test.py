from collections import Counter
import psycopg2
from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")


color_data = []
table_rows = soup.find_all("tr")
for row in table_rows[1:]: 
    cells = row.find_all("td")
    color_data.extend(cells[1].text.split(", "))

mean_color = Counter(color_data).most_common(1)[0][0]

mode_color = Counter(color_data).most_common(1)[0][0]

sorted_colors = sorted(color_data)
median_index = len(sorted_colors) // 2
median_color = sorted_colors[median_index]

color_counts = Counter(color_data)
total_colors = sum(color_counts.values())
mean_frequency = sum(count / total_colors for color, count in color_counts.items())

variance = sum((count / total_colors - mean_frequency) ** 2 for color, count in color_counts.items())

red_probability = color_counts.get('RED', 0) / total_colors

# PostgreSQL database
conn = psycopg2.connect(database="db.sql", user="nicholas", password="nicholas", host="localhost", port="5000")
cursor = conn.cursor()

for color, count in color_counts.items():
    cursor.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, count))

conn.commit()
conn.close()

print("Mean color:", mean_color)
print("Mode (most frequently worn) color:", mode_color)
print("Median color:", median_color)
print("Variance:", variance)
print("Probability of choosing red:", red_probability)
