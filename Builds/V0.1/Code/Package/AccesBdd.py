#-*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.engine import create_engine


class AccesBdd():
    '''class gerant la bdd'''
    
    def __init__(self, login, password):
        self.namebdd = "Labo_Metro_Test"#"Labo_Metro_Prod"
        self.adressebdd = "localhost" #"10.42.1.74"    #"localhost"            
        self.portbdd = "5432"
        self.login = login
        self.password = password
           
            #création de l'"engine"
        self.engine = create_engine("postgresql+psycopg2://{}:{}@{}:{}/{}".format(self.login, self.password, self.adressebdd, self.portbdd, self.namebdd)) 
        self.meta = MetaData()        
        self.meta.reflect(bind=self.engine)
#        self.table_instruments = Table('INSTRUMENTS', self.meta)
        self.connection = self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session.configure(bind=self.engine)
        
        
    def __del__(self):
        self.connection.close()
    

    def resencement_instrument(self):
        '''retourne tous les identifications des instruments dans une list'''

        result = self.connection.execute('SELECT "IDENTIFICATION", "DOMAINE_MESURE", "DESIGNATION" FROM "INSTRUMENTS"')
        
        instruments = []        
        for ele in result:            
            
            instruments.append(ele) #mise en forme

        return instruments
    def resencement_instrument_utilises(self):
        '''retourne tous les identifications des instruments utilisés dans une list'''

        result = self.connection.execute('''SELECT "IDENTIFICATION", "DOMAINE_MESURE", "DESIGNATION" FROM "INSTRUMENTS" WHERE "ETAT_UTILISATION" != 'Sommeil' AND "ETAT_UTILISATION" != 'Réformé' ''')
        
        instruments = []        
        for ele in result:            
            
            instruments.append(ele) #mise en forme

        return instruments
    
    def resencement_etalonnage_temp(self, date_debut, date_fin):
        '''retourne les etalonnages effectues entre deux dates dans une list'''

        result = self.connection.execute("""SELECT * FROM "ETALONNAGE_TEMP_ADMINISTRATION" WHERE "DATE_ETAL" >= '{}' AND "DATE_ETAL" <= '{}' ORDER BY "ID_ETAL" """.format(date_debut, date_fin))
        
        etalonnage_temp = []        
        for ele in result:            
            
            etalonnage_temp.append(ele) #mise en forme

        return etalonnage_temp
    
    def recensement_intervention(self, date_debut, date_fin):
        '''retourne sous forme de list l'ensemble de la table intervention'''
        result = self.connection.execute("""SELECT * FROM "INTERVENTIONS" WHERE "DATE_INTERVENTION" >= '{}' AND "DATE_INTERVENTION" <= '{}' ORDER BY "ID_INTERVENTION" """.format(date_debut, date_fin))
        
        intervention = []        
        for ele in result:            
            
            intervention.append(ele) #mise en forme

        return intervention
        
        
    def recensement_conformite(self, date_debut, date_fin):
        '''fct permettant de connaitre le nbr de non conforme'''
        
        result = self.connection.execute("""SELECT * FROM "CONFORMITE_TEMP_RESULTAT" WHERE "DATE_ETAL" >= '{}' AND "DATE_ETAL" <= '{}' ORDER BY "ID_CONFORMITE" """.format(date_debut, date_fin))
        
        conformite = []        
        for ele in result:            
            
            conformite.append(ele) #mise en forme

        return conformite
        
        
        
        
    def return_code_intrument(self, identification_instrument):
        '''retourne le code instrument'''
        result = self.connection.execute("""SELECT "CODE" FROM "INSTRUMENTS" WHERE "IDENTIFICATION" ='{}'""".format(identification_instrument))
        
        for ele in result:
            code = ele[0]
        return code
        
        
        

