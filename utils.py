from bs4 import BeautifulSoup
import requests
from django.db import models

link = "https://www.estrategiaconcursos.com.br/blog/concursos-nordeste/#paraiba"
req = requests.get(link)

site = BeautifulSoup(req.text, "html.parser")

PB = site.find_all("p", class_="has-very-light-gray-background-color has-background has-medium-font-size")


def get_status(indice):
    status = PB[indice].find_next_sibling()
    return status

def get_nome(indice):
    nome = PB[indice].text
    return nome


def get_perspectivas(indice):
    status = get_status(indice)
    perspectivas = status.find_next_sibling()
    return perspectivas


def get_cargos(indice):
    perspectivas = get_perspectivas(indice)
    li_tags = perspectivas.find_next_sibling().find_next_sibling()

    cargos = None
    for li in li_tags:
        txt = li.text
        trecho = txt.split(": ")
        if trecho[0] == "Cargos":
            cargos = trecho[1]

    return cargos

def get_vagas(indice):
    perspectivas = get_perspectivas(indice)
    li_tags = perspectivas.find_next_sibling().find_next_sibling()

    vagas = None
    for li in li_tags:
        txt = li.text
        trecho = txt.split(": ")

        if trecho[0].__contains__("Vagas"):
            vagas = trecho[0]

    return vagas


def get_link_concurso(indice):
    tag = PB[indice].find_next("a")
    link = tag.attrs.get("href")
    return link

def get_situacao(indice):
    link = get_link_concurso(indice)
    req = requests.get(link)
    site = BeautifulSoup(req.text, "html.parser")

    div = site.find("ul", class_="has-very-light-gray-to-cyan-bluish-gray-gradient-background has-background")

    for li in div:
        txt = li.text
        trecho = txt.split("\n")
        for i in range(len(trecho)):
            if trecho[i].__contains__("Situação:"):
                situacao = trecho[i]
                return situacao
            else:
                situacao = "Não há análise da situaçao atual"
                return situacao



