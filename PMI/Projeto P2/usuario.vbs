'Crie um script em vbscript que crie um diretório 
'c:\temp no computador e armazene em um arquivo CSV 
'o nome do usuário logado e o horário, 
'este arquivo devera ser atualizado a cada execução. (1,0)

'Criando um diretorio na pasta c.
Dim diretorio
Set diretorio = CreateObject("Scripting.FileSystemObject")

diretorio.CreateFolder "c:\temp"

'Criando variavel que guardara o arquivo em csv
dim filetxt 
Const ForReading = 1, ForWriting = 2, ForAppending = 8 

 
Set filetxt = diretorio.OpenTextFile("c:\temp\usuario.csv", ForAppending, True)
 
'Comando que ira identificar o usuario do sistema 
Dim usuario
Set usuario = WScript.CreateObject("WScript.Network")

'Função para definir a hora de acesso ao sistema
Function Fun_Hora()
    hora = hour(now)
    minutos = minute(now)
    segundos =second(now)
    if len(hora) = 1 or hora < 10 or hora = 0 then
  hora = "0" + CStr(hora)
    end if

    if len(minutos) = 1 or minutos < 10 then
  minutos = "0" + CStr(minutos)
    end if
    if len(segundos) = 1 or segundos < 10 then
  segundos = "0" + CStr(segundos)
    end if
    Fun_Hora = CStr(hora) + ":" + CStr(minutos) + ":" + CStr(segundos)
End Function

'Imprimindo no final no arquivo csv o usuario e o horario
filetxt.WriteLine("Usuário = " & usuario.UserName & VBCrLf) 
filetxt.WriteLine("Hora = " & Fun_Hora()) 

'Finalizando a criação do arquivo csv
filetxt.Close 
