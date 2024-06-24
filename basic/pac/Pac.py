

from .fn.clear_txt import*
from .fn.execute import*
from .fn.read_txt import*
from .fn.write_txt import*
from .fn.create_txt import*
from .fn.delete_txt import*
from .fn.read_photoimage import*
from .fn.read_excel_dict import*
from .fn.read_xlsx_nested import*

class Pac:

    def __init__(self) -> None:
        pass

    def clear_txt(file_path:str)->None:
        clear_txt(file_path)

    def execute(script_path:str)->None:
        execute(script_path)
    
    def read_txt(file_path:str)->str:
        return read_txt(file_path)

    def write_txt(file_path:str, text:str)\
        ->None:
        write_txt(file_path, text)

    def create_txt(filename:str, 
        content:str="")->None:
        return create_txt(filename, content)
    
    def delete_txt(filename:str)->None:
        delete_txt(filename)

    # return PhotoImage
    def read_photoimage(ruta_imagen:str):
        return read_photoimage(ruta_imagen)
    
    def read_excel_dict(filename:str)\
            ->dict[list]:
        return read_excel_dict(filename)
    
    def read_xlsx_nested(filename:str)\
            ->dict[dict]:
        return read_xlsx_nested(filename)
    


    