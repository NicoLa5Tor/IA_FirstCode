#la libreria json y la libreria os se usan solo para la lectura y extracción de path
# la libreria subprocess se usa solamente para ejecutar el comando bash encargado de mostrar un mesaje al usuario 
#
import os,json,subprocess

class System_op:
    def __init__(self) -> None:
        self.path = os.path.join(os.getcwd(),'')
    def create_and_write_document_json(self,dictionary,name = "historial.json"):
        with open(self.path+name,'w') as dc:
            dc.write(json.dumps(dictionary,indent=2))
    def create_txt(self,txtt,name ="Info.txt"):
        with open(self.path+name,'w') as txt:
            txt.write(txtt)
    def search_path(self,path):
        return os.path.join(os.getcwd(),path)
    def read_document(self,name):
        with open(name) as file:
            data = file.readlines()
        return data
    #esta funcion usa un comando en bash para poder mostrar un mensaje al usuario, los datos pedidos por la funcion
    #no son mas que el cuerpo del mensaje
    def mss_info(self,title,message,time=5,app_id="Entrenamiento perceptron",image_url = ""):
        powershell_command = f"""
            [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;
            $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastImageAndText02);
            $textNodes = $template.GetElementsByTagName("text");
            $textNodes.Item(0).AppendChild($template.CreateTextNode("{title}")) > $null;
            $textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;
            """

        powershell_command += f"""
            $imagePath = "{image_url}"
            $imageNodes = $template.GetElementsByTagName("image");
            $imageNodes.Item(0).Attributes.GetNamedItem("src").NodeValue = $imagePath;
            """
            
        powershell_command += f"""
            $toast = [Windows.UI.Notifications.ToastNotification]::new($template);
            $toast.ExpirationTime = [System.DateTimeOffset]::Now.AddSeconds({time});
            $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("{app_id}");
            $notifier.Show($toast);
            """
        subprocess.run(["powershell", "-Command", powershell_command])