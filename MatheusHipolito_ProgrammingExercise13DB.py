import sqlite3
import matplotlib.pyplot as plt

# Database setup
def create_database():
    db_name = "population_MH.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    return db_name

# Insert initial data for 10 cities in Florida
def insert_initial_data(db_name):
    initial_data = [
        ('Miami', 2023, 442241),
        ('Tampa', 2023, 387050),
        ('Orlando', 2023, 307573),
        ('Jacksonville', 2023, 971319),
        ('Tallahassee', 2023, 199705),
        ('St. Petersburg', 2023, 261338),
        ('Hialeah', 2023, 233339),
        ('Fort Lauderdale', 2023, 184765),
        ('Gainesville', 2023, 141085),
        ('Pensacola', 2023, 54302)
    ]
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO population (city, year, population)
        VALUES (?, ?, ?)
    ''', initial_data)
    conn.commit()
    conn.close()

# Simulate population growth for the 20 years
def simulate_population_growth(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT city FROM population WHERE year = 2023")
    cities = [row[0] for row in cursor.fetchall()]

    for city in cities:
        cursor.execute("SELECT population FROM population WHERE city = ? AND year = 2023", (city,))
        population = cursor.fetchone()[0]
        for year in range(2024, 2044):
            population = int(population * 1.02)
            cursor.execute('''
                INSERT INTO population (city, year, population)
                VALUES (?, ?, ?)
            ''', (city, year, population))
    conn.commit()
    conn.close()

# Display the population growth using the funtction matplotlib
def display_population_growth(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cities = [row[0] for row in cursor.execute("SELECT DISTINCT city FROM population")]
    print("Cities available:", ", ".join(cities))

    while True:
        city = input("Enter a city from the list above (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            break
        if city not in cities:
            print("Invalid city. Please choose from the list.")
            continue

        cursor.execute("SELECT year, population FROM population WHERE city = ?", (city,))
        data = cursor.fetchall()
        years, populations = zip(*data)

        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker='o')
        plt.title(f"Population Growth of {city}")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.grid(True)
        plt.show()

    conn.close()

# Main execution
if __name__ == "__main__":
    database_name = create_database()
    insert_initial_data(database_name)
    simulate_population_growth(database_name)
    display_population_growth(database_name)

