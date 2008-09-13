# -*- coding: latin-1 -*-
"""
Clase hospital que corresponde a la entidad hospital.
$Id: turno.py,v 1.3.2.1 2004/11/26 13:24:27 jmschillaci Exp $
"""
from sisalud.entidades.entidad import Entidad
from sisalud.entidades.turnos.pacienteturnos import PacienteTurnos
from sisalud.entidades.obrasocialmgr import ObraSocialMgr
from sisalud.constantes.constantes import *
from sisalud.turnos.agenda import agenda
from sisalud.fechas import *
from string import *
from mx.DateTime import *
from sisalud.util.config import config



import sisalud.wslib as wslib2

#Importo los comprobantes
from sisalud.comprobantes.ComprobanteTur import ComprobanteTur


class Turno(Entidad):
    def __init__(self):
        Entidad.__init__(self)
        self.id=None
        self.agenda=None
        self.paciente=None
        self.idhorario=None
        self.sobreturno=None
        self.operador=None
        self.terminal=None
        self.obrasocial=None
        self.primeravez=0
        self.consultorio=None
        self.obrasocial=None
        self.especialidad=None
        self.medico=None
        self.fechaturno=None
        self.hostaddress=None
        self.fechaotorg=None

    # *** funciones get ***
    
    def getId(self): return self.id

    def getAgenda(self):
        if self.agenda!=None:
            return self.agenda
        else:
            self.agenda=self.__getAgendaByIdTurno__()
            return self.agenda

        
    def getPaciente(self): 
        if self.paciente==None:
            """
            Si el paciente no esta seteado trata de buscarlo por el id del turno
            """
            try:
                #Todavia no esta hecho esto
                self.paciente.getPacienteByIdTurno() 
            except:
                return self.paciente
        else:
            return self.paciente

    
    def getHorario(self): return self.horario
    def getObraSocial(self): return self.obrasocial
    def getTerminal(self): return self.terminal
    def getOperador(self):  return self.operador
    def getIdHorario(self): return self.idhorario

    def getEspecialidades(self):
        if self.especialidad==None:
            if self.id == None:
                return self.__getEspecialidadesByAge__()
            else:
                print "hola"
                return self.__getEspecialidadesByIdTurno__()
        else:
            return self.especialidad
    
    def __getAgendaByIdTurno__(self):
        bi=wslib2.conectar()      
        agenda=wslib2.unserializar(bi.getAgendByIdTurno(self.getId())[0])
        return agenda
    
    def getMedicos(self):
        if self.medico==None:
            if self.id == None:
                print "sacando el medico por el id de agenda"
                return self.__getMedicosByAge__()
            else:
                print "sacando el medico por el id de turno"
                return self.__getMedicosByIdTurno__()
        else:
            return self.medico

    def __getMedicosByAge__(self):
        bi=wslib2.conectar()      
        medic=wslib2.unserializar(bi.get_agendamedico(self.agenda.id_agenda)[0])
        print "Imprimo las entradas que me devuelve"
        print medic
        
        nommed=""
        for elem in medic:
            Nombre=elem["Apellido"] + ", " +elem["Nombres"]
            if nommed == "":
                nommed = Nombre 
            else:
                nommed+=" | %s" % Nombre
        return nommed

    def __getEspecialidadesByAge__(self):
        bi=wslib2.conectar()      
        espec=wslib2.unserializar(bi.get_agendaespec(self.agenda.id_agenda)[0])
        nomesp=""
        for elem in espec:
            if nomesp == "":
                nomesp = elem["nomespec"]
        else:
            nomesp+=" | %s" % elem["nomespec"]
        
        return nomesp
 

    def __getMedicosByIdTurno__(self):
        bi=wslib2.conectar()      
        medic=wslib2.unserializar(bi.get_medicosByIdTurno(self.id)[0])
        
        nommed=""
        for elem in medic:
            Nombre=elem["Apellido"] + ", " +elem["Nombres"]
            if nommed == "":
                nommed = Nombre 
            else:
                nommed+=" | %s" % Nombre
        return nommed

    def __getEspecialidadesByIdTurno__(self):
        bi=wslib2.conectar()      
        espec=wslib2.unserializar(bi.get_especialidadesByIdTurno(self.id)[0])
        nomesp=""
        print espec 
        for elem in espec:
            if nomesp == "":
                nomesp = elem["nomespec"]
            else:
                nomesp+=" | %s" % elem["nomespec"]
        
        return nomesp
 
    def getConsultorio(self):
        if self.agenda != None:
            return self.__getConsultorioByAgenda__()
        else:
            return self.__getConsultorioByIdTurno__()

            
    def __getConsultorioByAgenda__(self):
         for elem in self.agenda.horarios:
            if elem["idhorario"]==self.idhorario:
                return elem["consultorio"]
        
    def __getConsultorioByIdTurno__(self):
        bi = wslib2.conectar()
        consult=wslib2.unserializar(bi.getConsultorioByIdTurno(self.getId())[0])
        return consult[0]["consultorio"]
 


    def esEspontaneo(self):
         for elem in self.agenda.horarios:
            if elem["idhorario"]==self.idhorario:
                return elem["espontaneo"]
                pass
    
    def esPrimeraVez(self): return self.primeravez
        

    def getHostAddress(self):
        return self.hostaddress
    

    def getFechaOtorg(self, formato=0):
        """
        Esta funcion se ocupa de devolver la fecha y hora de otorgamiento segun  el formato pasado
        @param formato: formato en el que se devolvera la fechahora, 1=mxDateTime, 2=dd/mm/yyyy, 3=HH:MM:SS
        """
        if self.fechaotorg!=None:
            if formato==0:
                return self.fechaotorg
            elif formato==1:
                return mysql2dmy(str(self.fechaotorg).split(" ")[0])
            elif formato==2:
                return str(self.fechaotorg).split(" ")[1].rstrip()
            elif formato==3:
                return (self.fechaotorg).strftime("%H")+":00"
        else:
            return self.fechaotorg



    def getFechaTurno(self, formato=0):
        """
        Esta funcion se ocupa de devolver la fecha y hora del turno segun  el formato pasado
        @param formato: formato en el que se devolvera la fechahora, 0=mxDateTime, 1=dd/mm/yyyy, 2=HH:MM:SS
        formato=3 pasa la banda horaria
        """
        if self.fechaturno!=None:
            if formato==0:
                return self.fechaturno
            elif formato==1:
                return mysql2dmy(str(self.fechaturno).split(" ")[0])
            elif formato==2:
                return self.fechaturno.strftime("%H:%M")
            elif formato==3:
                print "Aun no implementado, devolviendo el horario comun"
                return str(self.fechaturno).split(" ")[1].rstrip()
            elif formato==4:
                print "Devolviendo en formato redondeado de hora"
                return (self.fechaotorg).strftime("%H")+":00"
               
        else:
            return self.fechaturno

       
    def confirmar(self):
        bi = wslib2.conectar()
        #solo confirma si no tiene obra social
        if self.getOS().getId()==OS_SC_ID:
            bi.operar_turno(self.getId(), 2)
        else:
            print "debe pasar al circuito de confirmacion"

    def getTurnoById(self, id):
        """
        Trae todo la informacion del turno y setea todos los campos
        """
        if 1:
        #try:
            bi = wslib2.conectar()
            turno=wslib2.unserializar(bi.getTurnoById(id)[0])
            self.setId(id)
            if turno!=None: 
                self.getAgenda()
                self.__setFechaTurno__(turno[0]["horario"])
                self.setIdHorario(turno[0]["idhorario"])
                self.setOperador(turno[0]["operador"])
                #self.__setFechaOtorg__( ((turno[0]["ultmod"]).split("."))[0] )
                self.__setFechaOtorg__( turno[0]["ultmod"] )

                """
                self.setFechaOtor(mysql2dmy(str(turno[0]["ultmod"]).split(" ")[0]))
                self.setHoraOtor(str(turno[0]["ultmod"]).split(" ")[1])
                """
            else:
                return None

        #except:
        #    print "Fallo al traer el turno"
 
    def guardar(self):
        """
        Inserta el turno correspondiente
        """
        bi=wslib2.conectar()
        #poshoy+posini ya no va aca, porque el turno se actualiza al bloquearlo ya
        idturno=bi.insertar_turnoSB(self.getFechaTurno(),  self.getAgenda().headers["idagenda"], \
            self.getPaciente().getId(), 0, self.getOperador(),  "s", "s" , self.getHostAddress(),  \
            self.getOS().getId(), self.getOS().sigla, self.getIdHorario() , self.esPrimeraVez())
        
        self.setId(idturno[0]) 
        self.__setFechaOtorg__()
   
    # *** funciones set ***
    
    def setId(self, id): 
        self.id = id
        
    def setAgenda(self, agenda): 
        self.agenda = agenda
        
    def setPaciente(self, paciente): 
        self.paciente = paciente
        
    def setIdHorario(self, idhorario): 
        self.idhorario=idhorario
        
    def setConsultorio(self, consultorio): 
        self.consultorio=consultorio
        
    def setOS(self, obrasocial): 
        self.obrasocial=obrasocial
        
    def setTerminal(self, terminal): 
        self.terminal=terminal

        
    def setOperador(self, operador):
        self.operador=operador

    def setPrimeraVez(self, primeravez):
        self.primeravez=primeravez
    
    def getOS(self):
        return self.obrasocial                   

    def setHostAddress(self, address):
        self.hostaddress = address

    def setMedico(self, medico):
        self.medico = medico

    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad
 
    def __setFechaTurno__(self, mxfechahora=now()):
        self.fechaturno=mxfechahora;

    def __setFechaOtorg__(self, mxfechahora=now()):
        self.fechaotorg=mxfechahora;
        
    def generarComprobantes(self, tipo=2):
        """
        genera un comprobante para un turno
        si no se especifica cual trata de averiguarlo automaticamente (tipo=2)
        """
        if tipo==2:
            if self.esEspontaneo()==0:
                """
                Si el turno no es espontaneo
                """

                if config["turnos"]["impresion_programados"]:
                    ComprobanteTur(self, 0)
                pass
            else:
                """
                Si es espontaneo
                """
                #Lo confirmo automaticamente
                if self.obrasocial.getId()!=OS_SC_ID:
                    print "Llamar a confirmacion"
                else:
                    if config["turnos"]["impresion_espontaneos"]:
                        ComprobanteTur(self, 1)
        else:
            ComprobanteTur(self, tipo)    
    
        
    def __repr__(self):
        return 

if __name__ == "__main__":
    a=Turno()
    a.getTurnoById(1540)

