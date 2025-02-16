from cassandra.cluster import Cluster

# Подключение к Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Выбираем keyspace
session.set_keyspace('test_keyspace')

# Вставляем данные
session.execute("INSERT INTO users (id, name, age) VALUES (uuid(), 'Katerina', 30)")

# Проверяем, что данные добавились
rows = session.execute("SELECT * FROM users")
assert len(rows.current_rows) > 0, "Ошибка: Данные не добавились"

print("✅ Тест прошел успешно!")
