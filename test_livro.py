import os
import pytest
from livro import Livro, Livraria

@pytest.fixture
def banco_teste():
    livraria = Livraria("test_livros.db")
    yield livraria
    livraria.fechar()
    os.remove("test_livros.db")

def test_adicionar_e_listar_livro(banco_teste):
    livro = Livro("Teste", "Autor Teste", "Editora X", 123, "Descrição", "2024-01-01")
    banco_teste.adicionar(livro)
    
    livros = banco_teste.listar()
    assert len(livros) == 1
    assert livros[0][1] == "Teste"
    assert livros[0][2] == "Autor Teste"

def test_buscar_por_id(banco_teste):
    livro = Livro("ID Teste", "Autor A", "", 100, "", "2023-12-12")
    banco_teste.adicionar(livro)

    livro_inserido = banco_teste.listar()[0]
    livro_id = livro_inserido[0]

    buscado = banco_teste.buscar_por_id(livro_id)
    assert buscado is not None
    assert buscado[1] == "ID Teste"

def test_atualizar_livro(banco_teste):
    original = Livro("Original", "Autor", "", 100, "", "2022-10-10")
    banco_teste.adicionar(original)
    livro_id = banco_teste.listar()[0][0]

    novo = Livro("Atualizado", "Autor Novo", "", 200, "Nova descrição", "2024-02-02")
    banco_teste.atualizar(livro_id, novo)

    atualizado = banco_teste.buscar_por_id(livro_id)
    assert atualizado[1] == "Atualizado"
    assert atualizado[2] == "Autor Novo"
    assert atualizado[4] == 200

def test_deletar_livro(banco_teste):
    livro = Livro("Para Deletar", "Autor X", "", 90, "", "2021-01-01")
    banco_teste.adicionar(livro)

    livro_id = banco_teste.listar()[0][0]
    banco_teste.deletar(livro_id)

    assert banco_teste.buscar_por_id(livro_id) is None

def test_adicionar_paginas_invalidas(banco_teste):
    with pytest.raises(ValueError):  
        livro = Livro("Erro Páginas", "Autor", "", "cem", "", "2023-01-01")  
        banco_teste.adicionar(livro)

def test_adicionar_data_mal_formatada(banco_teste):
    livro = Livro("Erro Data", "Autor", "", 100, "", "31-12-2023")  

    with pytest.raises(ValueError):
     banco_teste.adicionar(livro)
     resultado = banco_teste.buscar_por_id(1)
     assert resultado is None  

def test_buscar_id_inexistente(banco_teste):
    resultado = banco_teste.buscar_por_id(999)
    assert resultado is None

def test_deletar_id_inexistente(banco_teste):
    banco_teste.deletar(999)   