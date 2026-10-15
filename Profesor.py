from Persona import Persona 

class Profesor(Persona):
  def __init__(self, nombre, edad):
    super().__init__(nombre, edad, 'Profesor')
    
