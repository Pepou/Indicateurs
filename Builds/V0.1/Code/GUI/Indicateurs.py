# -*- coding: utf-8 -*-

"""
Module implementing Indicateur.
"""
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QMainWindow

from .Ui_Indicateurs import Ui_MainWindow
from Package.AccesBdd import AccesBdd

import numpy

class Indicateur(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, login, password, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.db = AccesBdd(login, password)
        self.instruments = self.db.resencement_instrument_utilises()
#        self.interventions = self.db.recensement_intervention()


    @pyqtSlot(str)
    def on_comboBox_activated(self, p0):
        """
        Slot documentation goes here.
        """
        
        self.supprimer_lignes()
        indicateur = self.comboBox.currentText()
        if indicateur == "Composition Parc":
            self.composition_parc_utilises()
        elif indicateur == "Temperature":
            self.indicateurs_temperature()
        
        
    
    def composition_parc_utilises(self):
        '''fct qui rappatrie et trie l'ensemble du parc de la base et renvoie un dictionnaire avec le nbr d'instrument pas designation
        '''
     
        #on trie le parc par domaine:
            #list des domaines de mesure:
        domaines_mesure = set([ele[1] for ele in self.instruments])
            #list des designations:
        designations = set([ele[2] for ele in self.instruments])
        
            #Indicateurs:
            
                #parc designations:       
        dict_instruments_par_designations = {}
        dict_nbr_instruments_par_designations = {}
        
        for ele in designations:
            list =  [x for x in self.instruments if x[2] == ele]
            dict_instruments_par_designations[ele] = list
            dict_nbr_instruments_par_designations[ele] = len(dict_instruments_par_designations[ele])
        
        
                #Presentation tableau de resultats  
        list_clef_dico = []
        
        for clef in dict_nbr_instruments_par_designations.keys(): #on recupere les clefs du dico en list pour trier par ordre alphabetique
            self.tableWidget.insertRow(0)
            list_clef_dico.append(clef)
            list_clef_dico.sort() 
        for ele in enumerate(list_clef_dico):            
            self.tableWidget.setItem((ele[0]), 0, QtGui.QTableWidgetItem(str(ele[1])))
            self.tableWidget.setItem((ele[0]), 1, QtGui.QTableWidgetItem(str(dict_nbr_instruments_par_designations[ele[1]])))
            
        
    def indicateurs_temperature(self):
        '''fct gerant les differents indicateurs dommaine temperature'''
        
        date_debut = self.dateEdit.date().toString('yyyy-MM-dd')
        date_fin = self.dateEdit_2.date().toString('yyyy-MM-dd')
        parc_temperature = [ele for ele in self.instruments if ele[1] == "Température"]
        identification_instruments_temperature = [ele[0] for ele in parc_temperature]
        
        
        #nbr_etalonnage_temp:
        etalonnage = self.db.resencement_etalonnage_temp(date_debut, date_fin)
        nbr_etalonnage_temp = len(etalonnage)
        
        #nbr reception
        reception = [ele for ele in self.db.recensement_intervention(date_debut, date_fin) if ele[3] == "Réception"]
        reception_temperature = [ele for ele in reception if ele[2] in identification_instruments_temperature]
        nbr_reception_temperature = len(reception_temperature)
        instruments_temp_receptionnes = [ele[2] for ele in reception_temperature]
        
        #nbr expedition
        expedition = [ele for ele in self.db.recensement_intervention(date_debut, date_fin) if ele[3] == "Expedition"]
        expedition_temperature = [ele for ele in expedition if ele[2] in identification_instruments_temperature]
        nbr_expedition_temperature = len(expedition_temperature)
        instruments_temp_expedies = [ele[2] for ele in expedition_temperature]
        
        #Delais de traitement:
        list_delais_intrum  = [(ele_ex[2], (ele_rec[4]-ele_ex[4])) for ele_ex in expedition_temperature for ele_rec in reception_temperature if ele_ex[2]in ele_rec[2]]
        list_delais = [(ele_rec[4]-ele_ex[4]).days for ele_ex in expedition_temperature for ele_rec in reception_temperature if ele_ex[2]in ele_rec[2]]
        print(list_delais)
            #delais moyenne            
        delais_moyen = numpy.mean(numpy.array(list_delais), dtype =numpy.float)
        ecartype = numpy.std(numpy.array(list_delais), dtype =numpy.float, ddof = 1)
#        reception_temperature.reverse()
        print(delais_moyen)
        print(ecartype)
#        print(delais_moyen)
        
    def supprimer_lignes(self):
        '''Supprime l'ensemble des lignes du qtablewidget'''
        nbr_ligne = self.tableWidget.rowCount()
        
        if nbr_ligne != 0:
            for i in range(0, nbr_ligne):
                self.tableWidget.removeRow(0)
