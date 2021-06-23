from IPython.core.display import display, HTML
import testpyColab.displayhtml as dhtml

class Student():
    def __init__(self, group=1, id='sin_id'):

        self.group = group
        self.id = id

    def check_info(self):    
        msg = f'¡Bienvenido estudiante {self.id}! El grupo ingresado ha sido el # {self.group}'
        display(HTML(dhtml.titleHTML(msg,level=2)))
