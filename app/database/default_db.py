import pandas as pd
from mysql import connector
from datetime import date, datetime, timedelta
import bcrypt
class DefaultDB(object):

    l_cursos = []
    l_campus = []
    l_docentes = []
    l_tecnicos = []
    l_usuarios = []

    def __init__(self, database = None, user = "dev", password = "Ufop4&2021", path_sql_db = "schema/mydbpaem_create.sql"):
        self.database = database
        self.user = user
        self.password = password
        self.path_sql_db = path_sql_db
        # if(database == None):
        #     self.conn = connector.connect(user=self.user, password=self.password, host='127.0.0.1')
        # else:
        #     self.conn = connector.connect(user=self.user, password=self.password, host='127.0.0.1', database = database)

        self.create_database_from_sql()

    def insert_campus(self):
        cursor = self.conn.cursor()
        add_campus = ("INSERT INTO campus (ano_fundacao, nome) VALUES (%s, %s)")
        df = pd.read_csv ('inputs/campus.csv', sep=';',encoding = "ISO-8859-1")
        print("Inserindo registros de Campus ...")
        for index, row in df.iterrows():
            print(row.values)
            data_campus = (row[0], row[1])
            cursor.execute(add_campus, data_campus)
            self.l_campus.append([row[0], row[1]])
        self.conn.commit()
        cursor.close()


    def insert_curso(self):
        cursor = self.conn.cursor()
        add_curso = ("INSERT INTO curso (nome, data_fundacao, campus_id_campus) VALUES (%s, %s, %s)")
        df = pd.read_csv ('inputs/curso.csv', encoding = "utf-8", sep=';')
        print("Inserindo registros dos Cursos ...")
        for index, row in df.iterrows():
            print(row.values)
            data_curso = (row[0], row[1], row[2])
            self.l_cursos.append([row[0], row[1], row[2]])
            cursor.execute(add_curso, data_curso)

        self.conn.commit()
        cursor.close()

    def insert_discente(self):
        cursor = self.conn.cursor()
        add_discente = ("INSERT INTO discente (matricula, nome, entrada, status_covid, status_permissao, curso_id_curso) VALUES (%s, %s, %s, %s, %s, %s)")
        df = pd.read_csv ('inputs/discente.csv', encoding = "ISO-8859-1", sep=';')
        print("Inserindo registros dos Discentes ...")
        for index, row in df.iterrows():
            matricula = str(row[0]); nome = row[1]; curso = row[2]
            entrada = matricula[:4]

            for i in range(len(self.l_cursos)):
                if(curso == self.l_cursos[i][0]):
                    id_curso = i + 1
            data_discente = (matricula, nome, entrada, -1, 1, id_curso)
            print(data_discente)
            cursor.execute(add_discente, data_discente)

        self.conn.commit()
        cursor.close()

    def insert_docente(self):
        cursor = self.conn.cursor()
        add_docente = ("INSERT INTO docente (siape, nome, data_nascimento, escolaridade, situacao, status_covid, status_afastamento, curso_id_curso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        df = pd.read_csv ('inputs/docentes.csv', encoding = "ISO-8859-1", sep=';')
        print("Inserindo registros dos Docentes ...")
        for index, row in df.iterrows():
            siape = str(row[0]); nome = row[1]; escolaridade = row[3]; situacao = row[4]; curso = row[5]
            data_nascimento = row[2].split("/")[2] + "-"+ row[2].split("/")[1] + "-" + row[2].split("/")[0]

            for i in range(len(self.l_cursos)):
                if(curso == self.l_cursos[i][0]):
                    id_curso = i + 1
            data_docente = (siape, nome, data_nascimento, escolaridade, situacao, -1, 0, id_curso)
            self.l_docentes.append([siape, nome, data_nascimento, escolaridade, situacao, -1, 0, id_curso])
            print(data_docente)
            cursor.execute(add_docente, data_docente)

        self.conn.commit()
        cursor.close()

    def insert_tecnico(self):
        cursor = self.conn.cursor()
        add_tecnico = ("INSERT INTO tecnico (siape, nome, data_nascimento, cargo, status_covid, status_afastamento, campus_id_campus) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        df = pd.read_csv ('inputs/tecnico.csv', encoding = "ISO-8859-1", sep=';')
        print("Inserindo registros dos Técnicos ...")
        for index, row in df.iterrows():
            siape = str(row[0]); nome = row[1]; cargo = row[3];
            data_nascimento = row[2].split("/")[2] + "-"+ row[2].split("/")[1] + "-" + row[2].split("/")[0]

            data_tecnico = (siape, nome, data_nascimento, cargo,  -1, 0, 1)
            self.l_tecnicos.append([siape, nome, data_nascimento, cargo,  -1, 0, 1])
            print(data_tecnico)
            cursor.execute(add_tecnico, data_tecnico)

        self.conn.commit()
        cursor.close()

    def insert_recurs_campus(self):
        cursor = self.conn.cursor()
        add_recurso = ("INSERT INTO recurso_campus (nome, capacidade, descricao, inicio_horario_funcionamento, fim_horario_funcionamento, campus_id_campus) VALUES (%s, %s, %s, %s, %s, %s)")
        df = pd.read_csv ('inputs/recurso_campus.csv', encoding = "ISO-8859-1", sep=';')
        print("Inserindo registros dos Recursos Presentes no Campus ...")
        for index, row in df.iterrows():
            nome = str(row[0]);  descricao = row[2];
            try:
                capacidade = int(row[1]);
            except:
                capacidade = -1
            inicio_horario_funcionamento = row[3]; fim_horario_funcionamento = row[4]
            campus = row[5]
            id_campus = 0
            for i in range(len(self.l_campus)):
                if(campus == self.l_campus[i][1]):
                    id_campus = i + 1
            data_recurso = (nome, capacidade, descricao, inicio_horario_funcionamento, fim_horario_funcionamento, id_campus)
            print(data_recurso)
            cursor.execute(add_recurso, data_recurso)

        self.conn.commit()
        cursor.close()

    def insert_usuarios(self):
        cursor = self.conn.cursor()
        add_usuario = ("INSERT INTO usuario (login, senha, email, tipo) VALUES (%s, %s, %s, %s)")
        df = pd.read_csv ('inputs/usuario.csv', encoding = "ISO-8859-1", sep=';')
        print("Inserindo registros Usuarios de Teste ...")
        for index, row in df.iterrows():
            print(index + 1)
            login = str(row[0]);  email = row[2]; tipo = row[3].upper(); siape = row[4]
            print(row[1])
            senha = row[1];
            hash_senha = Seguranca().criptografa_senha(senha)
            print(hash_senha)
            id_tipo = -1

            if(tipo == "ADMIN"):
                id_tipo = 0
            if (tipo == "TÉCNICO"):
                id_tipo = 1
            if (tipo == "DOCENTE"):
                id_tipo = 2
            if (tipo == "DISCENTE"):
                id_tipo = 3
            if (tipo == "PORTARIA"):
                id_tipo = 4

            self.l_usuarios.append([login, senha, email, id_tipo, siape])
            data_usuario = (login, str(hash_senha), email, id_tipo)
            print(data_usuario)
            cursor.execute(add_usuario, data_usuario)

        self.conn.commit()
        cursor.close()

    def update_usuarios_tecnicos_docentes(self):
        cursor = self.conn.cursor()
        for i in range(len(self.l_usuarios)):

            if(self.l_usuarios[i][3] == 1) or (self.l_usuarios[i][3] == 0):
                alter_tecnico = ("UPDATE tecnico SET usuario_id_usuario = %s WHERE siape = %s")
                try:
                    siape = int(self.l_usuarios[i][4])
                    data_tecnico = (i + 1, siape)
                except:
                    print("Sem SIAPE vinculado ao usuário...")
                print(data_tecnico)
                cursor.execute(alter_tecnico, data_tecnico)

            if (self.l_usuarios[i][3] == 2):
                alter_docente = ("UPDATE docente SET usuario_id_usuario = %s WHERE siape = %s")
                try:
                    siape = int(self.l_usuarios[i][4])
                    data_tecnico = (i + 1, siape)
                except:
                    print("Sem SIAPE vinculado ao usuário...")
                print(data_tecnico)
                cursor.execute(alter_docente, data_tecnico)



        self.conn.commit()
        cursor.close()

    def create_database_from_sql(self):
        print("Iniciando a Criação do ")
        cursor = self.conn.cursor(buffered=True)
        cursor.execute("DROP DATABASE IF EXISTS "+self.database)
        cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.database)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        self.conn = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1',
                                            database=self.database)
        cursor = self.conn.cursor(buffered=True)
        file = open(self.path_sql_db)
        sql = file.read()
        for result in cursor.execute(sql, multi=True):
            if result.with_rows:
                print("Rows produced by statement '{}':".format(
                    result.statement))
                print(result.fetchall())
            else:
                print("Number of rows affected by statement '{}': {}".format(
                    result.statement, result.rowcount))

        self.conn.commit()


    def run(self):
        self.create_database_from_sql()
        self.insert_campus()
        self.insert_curso()
        self.insert_discente()
        self.insert_docente()
        self.insert_tecnico()
        self.insert_recurs_campus()
        self.insert_usuarios()
        self.update_usuarios_tecnicos_docentes()

if __name__ == '__main__':
    DefaultDB("mydbpaem","dev", "Ufop4&2021").run()
