import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._AeroportoPartenza = None
        self._AeroportoArrivo = None

    def handle_analisiAeroporti(self, e):
        self._view.txt_result.controls.clear()
        minimo = self._view.txtMinimo.value
        if minimo is None or minimo == "":
            self._view.create_alert("Inserire il nome")
            return
        self._model.buildGraph(minimo)
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente!"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi"))
        self.fillDD()
        self._view.update_page()

    def fillDD(self):
        nodiGrafo = self._model.getAllNodi()
        for n in nodiGrafo:
            self._view.dd_AeroportoP.options.append(ft.dropdown.Option(data= n,
                    on_click=self.readDDPartenza,
                    text=n.AIRPORT))
            self._view.dd_AeroportoA.options.append(ft.dropdown.Option(data= n,
                    on_click=self.readDDArrivo,
                    text=n.AIRPORT))

    def readDDPartenza(self, e):
        if e.control.data is None:
            self._AeroportoPartenza = None
        else:
            self._AeroportoPartenza = e.control.data

    def readDDArrivo(self, e):
        if e.control.data is None:
            self._AeroportoArrivo = None
        else:
            self._AeroportoArrivo = e.control.data

    def handle_testConnessione(self, e):
        percorso = self._model.cercaPercorso(self._AeroportoPartenza, self._AeroportoArrivo)
        for p in percorso:
            print(p)
        self._view.txt_result.controls.clear()
        if percorso is not None:
            self._view.txt_result.controls.append(ft.Text(f"E' stato trovato un percorso da {self._AeroportoPartenza} a {self._AeroportoArrivo}:"))
            for node in percorso:
                self._view.txt_result.controls.append(ft.Text(f"{node}"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Tra {self._AeroportoPartenza} e {self._AeroportoArrivo} non esiste nessun percorso."))
        self._view.update_page()



