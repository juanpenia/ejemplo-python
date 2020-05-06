import hangman
import reversegam
import tictactoeModificado
import json
import PySimpleGUI as sg
from os.path import isfile

def FileName():
	return "historial.json"

def GuardarAJSON(nombre, juego):
	dato_nuevo = "Nombre: {}. Juego: {}".format(nombre, juego)
	if(isfile(FileName())):
		with open(FileName()) as arc:
			datos = json.load(arc)
			datos.append(dato_nuevo)
	
	else:
		datos = [dato_nuevo]

	with open(FileName(), "w") as arc:
		json.dump(datos, arc, indent=4)

def interfaz():

	sg.theme("DarkAmber")

	layout =[
			[sg.Text('Ingrese nombre del jugador: '), sg.InputText(size=(8, 0))],
			[sg.Text('Selecciona el juego:'), sg.Combo(values=('Ahorcado', 'TA-TE-TI', 'Otello'), size=(10, 10), key='lista_juegos')],
			[sg.Submit(), sg.Cancel()] ]
         

	window = sg.Window('Juegos', layout, size=(300, 120))

	while True:
		event, values = window.read()
		if event in (None, 'Submit'):

			juego = values['lista_juegos'] # valor seleccionado del combo
			GuardarAJSON(values[0], juego)
			if juego == 'Ahorcado':
				hangman.main()
			elif juego == 'TA-TE-TI':
				tictactoeModificado.main()
			elif juego == 'Otello':
				reversegam.main()

		if event in (None, 'Cancel'):
			break
	window.close()



def main(args):
	interfaz()
	
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))