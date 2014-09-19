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

        
        #configuration largeur colonnes tablewidget
        self.tableWidget.setColumnWidth(0,600)
        self.tableWidget.setColumnWidth(1,600)
        
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
        
        indicateurs_temperature = {}
        
        #nbr_etalonnage_temp:
        etalonnage = self.db.resencement_etalonnage_temp(date_debut, date_fin)
        nbr_etalonnage_temp = len(etalonnage)
        
        indicateurs_temperature["nombre etalonnages"] = nbr_etalonnage_temp
        
        #nbr reception
        reception = [ele for ele in self.db.recensement_intervention(date_debut, date_fin) if ele[3] == "Réception"]
        reception_temperature = [ele for ele in reception if ele[2] in identification_instruments_temperature]
        nbr_reception_temperature = len(reception_temperature)
        instruments_temp_receptionnes = [ele[2] for ele in reception_temperature]
        
        indicateurs_temperature["nbr d'instruments receptionnés"] = nbr_reception_temperature
        
        #nbr expedition
        expedition = [ele for ele in self.db.recensement_intervention(date_debut, date_fin) if ele[3] == "Expedition"]
        expedition_temperature = [ele for ele in expedition if ele[2] in identification_instruments_temperature]
        nbr_expedition_temperature = len(expedition_temperature)
        instruments_temp_expedies = [ele[2] for ele in expedition_temperature]
        
        indicateurs_temperature["nbr d'instruments expédiés"] = nbr_expedition_temperature
        
        #Delais de traitement:
        list_delais_intrum  = [(ele_ex[2], (ele_rec[4]-ele_ex[4])) for ele_ex in expedition_temperature for ele_rec in reception_temperature if ele_ex[2]in ele_rec[2]]
        list_delais = [(ele_rec[4]-ele_ex[4]).days for ele_ex in expedition_temperature for ele_rec in reception_temperature if ele_ex[2]in ele_rec[2]]

            #delais moyenne            
        delais_moyen = numpy.mean(numpy.array(list_delais), dtype =numpy.float)
        ecartype = numpy.std(numpy.array(list_delais), dtype =numpy.float, ddof = 1)
        
        indicateurs_temperature["delais moyen de traitement"] = delais_moyen
        indicateurs_temperature["ecart type delais moyen de traitement"] = ecartype
        
#        #Conformite :         
        recensement_conformite = self.db.recensement_conformite(date_debut, date_fin)
        nbr_declaration_conformite = len(recensement_conformite)
        
        indicateurs_temperature["nbr de CV"] = nbr_declaration_conformite
        
            #Conforme
        conforme = [ele for ele in recensement_conformite if ele[5] == "Conforme"]
        nbr_instrum_conforme = len(conforme)
        
        indicateurs_temperature["nbr d'instruments conforme"] = nbr_instrum_conforme
        
            #Non Conforme
        non_conforme = [ele for ele in recensement_conformite if ele[5] == "Non Conforme"]
        nbr_instrum_non_conforme = len(non_conforme)
        
        indicateurs_temperature["nbr d'instruments non conforme"] = nbr_instrum_non_conforme
#        
        
        #Presentation tableWidget final
        
        self.tableWidget.insertRow(0)                 
        self.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem(str("Nombre d'etalonnages")))
        self.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem(str(indicateurs_temperature["nombre etalonnages"])))
        
        self.tableWidget.insertRow(1)                 
        self.tableWidget.setItem(1, 0, QtGui.QTableWidgetItem(str("nbr d'instruments receptionnés")))
        self.tableWidget.setItem(1, 1, QtGui.QTableWidgetItem(str(indicateurs_temperature["nbr d'instruments receptionnés"])))
        
        self.tableWidget.insertRow(2)                 
        self.tableWidget.setItem(2, 0, QtGui.QTableWidgetItem(str("nbr d'instruments expédiés")))
        self.tableWidget.setItem(2, 1, QtGui.QTableWidgetItem(str(indicateurs_temperature["nbr d'instruments expédiés"])))
        
        self.tableWidget.insertRow(3)                 
        self.tableWidget.setItem(3, 0, QtGui.QTableWidgetItem(str("Delais moyen d'etalonnage")))
        self.tableWidget.setItem(3, 1, QtGui.QTableWidgetItem(str(indicateurs_temperature["delais moyen de traitement"])))
        
        self.tableWidget.insertRow(4)                 
        self.tableWidget.setItem(4, 0, QtGui.QTableWidgetItem(str("Ecart moyen entre les etalonnage (ecart type)")))
        self.tableWidget.setItem(4, 1, QtGui.QTableWidgetItem(str(indicateurs_temperature["ecart type delais moyen de traitement"])))
        
        self.tableWidget.insertRow(5)                 
        self.tableWidget.setItem(5, 0, QtGui.QTableWidgetItem(str("Nbr de declaration de conformite")))
        self.tableWidget.setItem(5, 1, QtGui.QTableWidgetItem(str(indicateurs_temperature["nbr de CV"])))
        
        self.tableWidget.insertRow(6)                 
        self.tableWidget.setItem(6, 0, QtGui.QTableWidgetItem(str("Nbr d'instruments conformes")))
        self.tableWidget.setItem(6, 1, QtGui.QTableWidgetItem(str(indicateurs_temperature["nbr d'instruments conforme"])))
        
        self.tableWidget.insertRow(7)                 
        self.tableWidget.setItem(7, 0, QtGui.QTableWidgetItem(str("Nbr d'instruments non conformes")))
        self.tableWidget.setItem(7, 1, QtGui.QTableWidgetItem(str(indicateurs_temperature["nbr d'instruments non conforme"])))
        
        
    def supprimer_lignes(self):
        '''Supprime l'ensemble des lignes du qtablewidget'''
        nbr_ligne = self.tableWidget.rowCount()
        
        if nbr_ligne != 0:
            for i in range(0, nbr_ligne):
                self.tableWidget.removeRow(0)
