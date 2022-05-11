from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import os

caminho = os.getcwd()
caminho_completo = os.path.join(caminho, 'alunos.db')
engine = create_engine(f'sqlite:///{caminho_completo}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Aluno(Base):  
    __tablename__ = "Alunos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(895), nullable=False)
    email = Column(String(319), unique=True, nullable=False)
    cep = Column(String(9))
    endereco = Column(String(200))
    numero = Column(String(10))
    cidade = Column(String(200))
    estado = Column(String(2))
    complemento = Column(String(200))
    data_de_criacao = Column(DateTime, default=datetime.now)
    date_de_atualizacao = Column(DateTime, default=datetime.now, onupdate=datetime.now)

if not(os.path.exists(caminho_completo)):
    print(f'Criando banco de dados no arquivo "{caminho_completo}"')
    Base.metadata.create_all(engine)   

def cadastra_usuario(nome, email, cep, endereco, numero, cidade, estado, complemento):
    dados_do_aluno = Aluno(nome=nome, email=email, cep=cep, numero=numero, cidade=cidade, estado=estado, complemento=complemento)
    session.add(dados_do_aluno)
    try:
        session.commit()
        armazenado = True
    except IntegrityError:
        session.rollback()
        armazenado = False
    session.close()
    return armazenado

def consulta_registros():
    dados_dos_alunos = session.query(Aluno).all()
    for aluno in dados_dos_alunos:
        print(aluno)
    session.close()
    return dados_dos_alunos
