# -*- coding: utf-8 -*-
# echo.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Dois - Brincando com o GIT.

.. codeauthor:: Carlo Oliveira

- Como criar um repositório no github
- Como clonar usando o comnando git
- Como comitar usando o comando git

Classes neste modulo
  :py:class: 'MAin' Exemplo de classe qualquer

Changelog
---------
.. versionadded::    20.07
        Documentação do tutorial.

"""

class Main:
    """Classe exemplo.

       :param versao: versão deste exemplo

    """
    def __init__(self, versao):
        print ("classe exemplo, versão {}".format(versao))

if __name__ == "__main__":
    Main(1)
