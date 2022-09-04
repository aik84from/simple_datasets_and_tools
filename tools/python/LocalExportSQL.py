import json
import psycopg2
from psycopg2.extras import RealDictCursor


class LocalExportSQL:
    def run(self, sql, filename, config):
        with psycopg2.connect(config) as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sql)
                with open(filename, 'w') as outfile:
                    json.dump(cursor.fetchall(), outfile, indent=4, sort_keys=True, default=str)

