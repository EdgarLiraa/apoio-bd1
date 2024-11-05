from datetime import datetime
from servicos.database.conector import DatabaseManager


class ExampleDatabase:
    def __init__(self, db_provider=DatabaseManager()) -> None:
        self.db = db_provider

    def get_generico_com_algum_parametro(self):
        """select genérico com algum filtro padrão"""
        data = datetime.now().date().isoformat()  # Data atual
        query = f"SELECT * FROM imprime WHERE data_entrega < '{data}';"
        return self.db.execute_select_all(query)

    def insercao_generica(
        self, lisbn: str, grafica_id: str, nto_copias: str, data_entrega: str
    ) -> bool:
        """Exemplo de Insert no database, deletes seguem a mesma ideia"""
        statement = f"INSERT INTO imprime (lisbn, grafica_id, nto_copias, data_entrega) VALUES ('{lisbn}', {grafica_id}, {nto_copias}, '{data_entrega}');"
        return self.db.execute_statement(statement)

    def get_com_filtro(self, rg: str, editora: str, livro: str):
        """Exemplo de como fazer um filtro, não é uma maneira excelente, mas funciona"""
        query = """
                SELECT * FROM livros l
                LEFT JOIN editora e ON e.id = l.editora_id 
                LEFT JOIN escreve es ON es.isbn = l.isbn
                LEFT JOIN autor a ON a.rg = es.rg
                """

        if rg:
            query += f"WHERE a.rg = '{rg}'\n"

        if editora:
            if "WHERE" in query:
                query += f"AND e.id = {editora}\n"
            else:
                query += f"WHERE e.id = {editora}\n"

        if livro:
            if "WHERE" in query:
                query += f"AND l.isbn = '{livro}'\n"
            else:
                query += f"WHERE es.isbn = '{livro}'\n"

        return self.db.execute_select_all(query)
