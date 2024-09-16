def calcular_arepas(harina, agua, sal):
  """Calcula la cantidad de arepas que se pueden hacer.

  Args:
    harina: Cantidad de harina en gramos.
    agua: Cantidad de agua en mililitros.
    sal: Cantidad de sal en gramos.

  Returns:
    La cantidad estimada de arepas.
  """

  # Ajusta estos valores según tu receta específica
  harina_por_arepa = 100  # Gramos de harina por arepa
  agua_por_arepa = 50   # Mililitros de agua por arepa

  # Calcula la cantidad máxima de arepas que se pueden hacer
  # basándose en la harina, ya que suele ser el ingrediente limitante
  arepas_por_harina = harina // harina_por_arepa

  # Verifica si el agua es suficiente
  agua_necesaria = arepas_por_harina * agua_por_arepa
  if agua < agua_necesaria:
    print("No tienes suficiente agua.")
    arepas_por_harina = agua // agua_por_arepa

  return arepas_por_harina

# Solicitar los ingredientes al usuario
harina_str = input("Ingrese la cantidad de harina en gramos: ")
agua_str = input("Ingrese la cantidad de agua en mililitros: ")
sal_str = input("Ingrese la cantidad de sal en gramos: ")

# Convertir los valores a números
harina = int(harina_str)
agua = int(agua_str)
sal = int(sal_str)

# Calcular y mostrar el resultado
cantidad_arepas = calcular_arepas(harina, agua, sal)
print(f"Con los ingredientes ingresados, puedes hacer aproximadamente {cantidad_arepas} arepas.")