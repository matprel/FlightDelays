import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txtMinimo = None
        self.dd_AeroportoP= None
        self.dd_AeroportoA= None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("FlightDelays", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name

        self.txtMinimo = ft.TextField(
            label="numero minimo",
            width=200,
            hint_text="Inserisci un numero minimo"
        )

        # button for the "hello" reply
        self.btn_AnalizzaAeroporti = ft.ElevatedButton(text="Analizza Aeroporti", on_click=self._controller.handle_analisiAeroporti)
        row1 = ft.Row([self.txtMinimo, self.btn_AnalizzaAeroporti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.dd_AeroportoP = ft.Dropdown(label="Aeroporto di Partenza", width=500)
        self.dd_AeroportoA = ft.Dropdown(label="Aeroporto di Arrivo", width=500)

        self.btn_testConnessione = ft.ElevatedButton(text="Test Connessione",
                                                       on_click=self._controller.handle_testConnessione)
        row2 = ft.Row([self.dd_AeroportoP],
                      alignment=ft.MainAxisAlignment.CENTER)
        row3 = ft.Row([self.dd_AeroportoA],alignment=ft.MainAxisAlignment.CENTER)
        row4 = ft.Row([self.btn_testConnessione],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self._page.controls.append(row3)
        self._page.controls.append(row4)


        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
