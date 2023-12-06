Attribute VB_Name = "CutAndPasteToTable"
Sub CutAndPasteToTable()
Dim count As String
Dim bold As Boolean
Set myDocument = Documents(Environ("userprofile") & _
    "\Desktop\Reviews\reviews-sorted.docm")

myDocument.Content.InsertAfter vbCr
LastPar = myDocument.Paragraphs.count - 1
myDocument.Paragraphs(LastPar).Range.Font.bold = True

Set myrange = myDocument.Content
myrange.Collapse Direction:=wdCollapseEnd
myDocument.Tables.Add Range:=myrange, NumRows:=1, NumColumns:=2
myDocument.Tables(1).Style = "Сетка таблицы"        'Table style name. Depends on language of the Word application. English version "Table Grid"'

i = 1
Do
    bold = myDocument.Paragraphs(1).Range.bold
    count = myDocument.Paragraphs(1).Range.Characters.count
    If count > 1 Then
        Set selected = myDocument.Paragraphs(1).Range
        myDocument.Tables(1).Cell(Row:=i, Column:=1).Range.InsertAfter selected
        selected.Delete
    Else
        myDocument.Tables(1).Range.Rows.Add
        myDocument.Paragraphs(1).Range.Delete
        i = i + 1
    End If
Loop While bold = False
myDocument.Range.Font.bold = 0
Documents("reviews-sorted.docm").SaveAs2 _
    FileName:=Environ("userprofile") & "\Desktop\Reviews\reviews-sorted " & _
    Format(Date, "dd.mm") & ".docx", FileFormat:=wdFormatDocumentDefault
End Sub


