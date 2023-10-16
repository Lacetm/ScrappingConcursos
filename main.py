from bs4 import BeautifulSoup
import requests
from django.db import models

link = "https://www.estrategiaconcursos.com.br/blog/concursos-nordeste/#paraiba"
req = requests.get(link)

site = BeautifulSoup(req.text, "html.parser")

PB = site.find_all("p", class_="has-very-light-gray-background-color has-background has-medium-font-size")


def get_status():
    status = PB[0].find_next_sibling()
    return status


def get_perspectivas(status):
    perspectivas = status.find_next_sibling()
    return perspectivas


def get_cargos_vagas(perspectivas):
    li_tags = perspectivas.find_next_sibling().find_next_sibling()

    cargos = None
    vagas = None
    for li in li_tags:
        txt = li.text
        trecho = txt.split(": ")
        print(trecho)
        if trecho[0] == "Cargos":
            cargos = trecho[1]

        if trecho[0].__contains__("Vagas"):
            vagas = trecho[0]


def get_link_concurso():
    tag = PB[0].find_next("a")
    link = tag.attrs.get("href")
    return link

def get_situacao(link):
    req = requests.get(link)
    site = BeautifulSoup(req.text, "html.parser")

    div = site.find_all("ul", class_="has-very-light-gray-to-cyan-bluish-gray-gradient-background has-background")

    for li in div:
        txt = li.text
        trecho = txt.split("\n")
        print(trecho)
        for i in range(len(trecho)):
            if trecho[i].__contains__("Situação"):
                situacao = trecho[i]
                return situacao



