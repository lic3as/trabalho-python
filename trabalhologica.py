placa = input("INFORME A PLACA DO VEICULO:\n")

from datetime import datetime

entrada = input("HORA DA ENTRADA:\n")
saida = input("HORA DA SAIDA:\n")

formato = '%H:%M'
entradac = datetime.strptime(entrada, formato)
saidac = datetime.strptime(saida, formato)

tempo = (saidac - entradac).total_seconds()/3600
print(tempo)

seuveiculo = input("MOTO OU CARRO?\n")

veiculos = ["carro", "moto"]

if seuveiculo == "moto":
    total = int(tempo)*8

elif seuveiculo == "carro":
    total = int(tempo)*12

print("O VEICULO DE PLACA", placa, "PASSOU", tempo, "NO ESTACIONAMENTO E TERA QUE PAGAR", total)