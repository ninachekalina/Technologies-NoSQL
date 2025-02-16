import uuid
from cassandra.cluster import Cluster

def test_insert_and_read():
    cluster = Cluster(['localhost'])
    session = cluster.connect('test_keyspace')

    # Вставляем данные
    session.execute("INSERT INTO users (id, name) VALUES (1, 'Ekaterina')")

    # Проверяем, что запись вставлена
    rows = session.execute("SELECT id, name FROM users WHERE id = 1")

    for row in rows:
        print(f"Inserted row: id={row.id}, name={row.name}")  # Этот вывод появится в логах GitHub Actions

    assert any(row.name == 'Ekaterina' for row in rows), "Data was not inserted!"

