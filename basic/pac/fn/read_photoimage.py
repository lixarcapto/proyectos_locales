


import PIL.ImageTk as ImageTk
import PIL.Image as Image

"""
    Funcion que lee una imagen en la direccion indicada
    y la carga como un objeto PhotoImage de PIL
"""
# return PhotoImage
def read_photoimage(route:str, 
               range_size = None):
        imagen = Image.open(route)  
        if(not range_size == None):
          imagen = imagen.resize((
              range_size[0], range_size[1]
         )) 
        # Ajustar ancho y mantener relación de aspecto
        imagen = ImageTk.PhotoImage(imagen)
        return imagen