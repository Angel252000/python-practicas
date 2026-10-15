class consulta:
    def __init__(self, paciente, peso, sintomatologia, notas_evaluacion_fisica, diagnostico, requiere_control, examenes, prescripciones, fecha_consulta):
        self.paciente = paciente
        self.peso = peso
        self.sintomatologia = sintomatologia
        self.notas_evaluacion_fisica = notas_evaluacion_fisica
        self.diagnostico = diagnostico
        self.requiere_control = requiere_control
        self.examenes = examenes
        self.prescripciones = prescripciones
        self.fecha_consulta = fecha_consulta
        paciente.consultas.append(self)