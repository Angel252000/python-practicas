from clase31 import Banco

def main():
  # Prueba la creación de una cuenta
  test_crear_cuenta()
  
  # Prueba la obtención de cuentas
  test_obtener_cuentas()
  
  # Prueba la búsqueda de una cuenta
  test_buscar_cuenta()
  
  # Prueba la registración de una transacción
  test_registrar_transaccion()
  
  # Prueba la visualización del libro diario
  test_ver_libro_diario()

def test_crear_cuenta():
  # Crea un objeto Banco
  banco = Banco()
  
  # Intenta crear una cuenta con el nombre "Colones"
  banco.crear_cuenta("Colones")
  
  # Verifica que la cuenta se haya creado correctamente
  assert len(banco.cuentas) == 1, "La cuenta no se creó correctamente"

def test_obtener_cuentas():
  # Crea un objeto Banco
  banco = Banco()
  
  # Crea dos cuentas con los nombres "Colones" y "Dolares"
  banco.crear_cuenta("Colones")
  banco.crear_cuenta("Dolares")
  
  # Verifica que la lista de cuentas devuelta tenga dos elementos
  assert len(banco.obtener_cuentas()) == 2, "La lista de cuentas no es correcta"

def test_buscar_cuenta():
  # Crea un objeto Banco
  banco = Banco()
  
  # Crea una cuenta con el nombre "Colones"
  banco.crear_cuenta("Colones")
  
  # Intenta buscar la cuenta con el ID 1
  cuenta = banco.buscar_cuenta(1)
  
  # Verifica que la cuenta encontrada sea del tipo correcto y tenga el ID 1
  assert isinstance(cuenta, cuenta), "La cuenta no es del tipo correcto"
  assert cuenta.id == 1, "La cuenta no tiene el ID correcto"

def test_registrar_transaccion():
  # Crea un objeto Banco
  banco = Banco()
  
  # Crea una cuenta con el nombre "Colones"
  banco.crear_cuenta("Colones")
  
  # Intenta registrar una transacción de depósito de 100 unidades en la cuenta 1
  banco.registrar_transaccion("deposito", 100, 1)
  
  # Verifica que la lista de transacciones tenga un elemento
  assert len(banco.transacciones) == 1, "La transacción no se registró correctamente"

def test_ver_libro_diario():
  # Crea un objeto Banco
  banco = Banco()
  
  # Crea una cuenta con el nombre "Colones"
  banco.crear_cuenta("Colones")
  
  # Intenta registrar una transacción de depósito de 100 unidades en la cuenta 1
  banco.registrar_transaccion("deposito", 100, 1)
  
  # Verifica que el libro diario se pueda ver correctamente
  banco.ver_libro_diario()

if __name__ == '__main__':
  main()