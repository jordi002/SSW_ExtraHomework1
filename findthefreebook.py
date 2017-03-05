#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
"""
Simple client web per descarregar el llibre gratuit/dia de https://www.packtpub.com/packt/offers/free-learning/
@author: jordigm@jordigm.com
"""

import urllib2
import bs4

class Client(object):

    def get_webpage(self,page):
        """ obtenir la pagina web """
        f = urllib2.urlopen(page)
        htmlpage = f.read()
        f.close()
        return htmlpage

    def search_data(self,html):
        """ buscar dades """
        bs = bs4.BeautifulSoup(html,"lxml")
        caixa = bs.find("div", "dotd-main-book-summary float-left")
        items = caixa.find("div","dotd-title").find("h2").text.strip()

        results = []

        results.append(items)

        return results

    def main(self):
        #obtenir plana web
        webpag = self.get_webpage('https://www.packtpub.com/packt/offers/free-learning/')
        #buscar dades
        results = self.search_data(webpag)
        #imprimir resultats

        print "Today free book: " + str(results)


if __name__ == "__main__":
    cw = Client()
    cw.main()
