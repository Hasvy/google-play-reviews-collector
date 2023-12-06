import os
import win32com.client

print("Создание Word документа")
Desktop = (os.environ['USERPROFILE']) + '\\Desktop\\'
wdFormatXMLDocumentMacroEnabled = 13
in_file = Desktop + 'Reviews\\result.txt'
out_file = Desktop + 'Reviews\\reviews-sorted.docm'
word = win32com.client.DispatchEx('Word.Application')

doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatXMLDocumentMacroEnabled)
doc.Application.Run ('CutAndPasteToTable')
doc.Close()
word.Quit()
os.remove(out_file)
print("Готово!")
exit()