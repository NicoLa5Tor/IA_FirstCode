#la libreria json y la libreria os se usan solo para la lectura y extracción de paths y para la 
#
import os,json

class System_op:
    def __init__(self) -> None:
        self.path = os.path.join(os.getcwd(),'')
    def create_and_write_document_json(self,dictionary):
        with open(self.path+"historial.json",'w') as dc:
            dc.write(json.dumps(dictionary,indent=2))
    def create_txt(self,txtt):
        with open(self.path+"Readme.txt",'w') as txt:
            txt.write(txtt)