import sqlite3
import sys

def main():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    try:
        cur.execute('SELECT app, name FROM django_migrations ORDER BY id DESC LIMIT 100')
        migrations = cur.fetchall()
    except Exception as e:
        print('ERROR reading django_migrations:', e)
        migrations = None

    cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = cur.fetchall()
    print('django_migrations:', migrations)
    print('tables:', tables)
    conn.close()

if __name__ == '__main__':
    main()
