# google-play-reviews-collector
How to use
1. Change "myDocument.Tables(1).Style = ", table style name. Depends on language of the Word application. English version "Table Grid"
2. Import CutAndPasteToTable.bas script into your Word application with name "CutAndPasteToTable".
3. Run the script, it will generate a folder "Reviews" on your Desktop
4. Get .html file from your application administrator account on Google Play.
5. Put .html file with reviews into Reviews/html files.
6. Run the script and it will parse reviews from .html file to table in Reviews/reviews-sorted dd.mm.docx
