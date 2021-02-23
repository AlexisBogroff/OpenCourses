'''vba
Option Explicit

Sub s00_delete_all_info()
    ' ===========================
    ' Delete data from all tables
    ' ===========================
    
    ' YOUR CODE HERE
    
    Dim db As Database
    
    ' Open Database
    
    Set db = OpenDatabase("Database1.accdb")

    ' Delete records
    
    db.Execute "DELETE * FROM ratios;"
    
    'db.Execute "DELETE * FROM ratios_hist;"
    'Nous ne supprimons pas les donnÈes de la feuille ratio hist, car il s'agit de donnÈes historiques
    
    db.Execute "DELETE * FROM warning;"
    db.Execute "DELETE * FROM investors_metrics;"
    db.Execute "DELETE * FROM portfolios;"
    db.Execute "DELETE * FROM static_investors;"
    db.Execute "DELETE * FROM last_stock_value;"
    db.Execute "DELETE * FROM data;"


    db.Close


End Sub


Sub s01_create_table_data()
    ' =========================================
    ' Create a table named 'data'
    ' Fields :
    ' - id
    ' - date | format : yyyy/mm/dd
    ' - stock_name
    ' - stock_value
    ' =========================================
    
    ' YOUR CODE HERE
    Dim db As Database
    Set db = OpenDatabase("Database1.accdb")

    ' Creation de la table
    db.Execute "CREATE TABLE data (ID AUTOINCREMENT PRIMARY KEY, " _
        & "[date] DATE, " _
        & "stock_name TEXT, " _
        & "stock_value FLOAT);"
    

End Sub


Sub s02_feed_data()
    ' =============================
    ' Feed data table from csv file
    ' with the data from a company
    ' of your choice
    '
    ' 1. Change the path to match
    ' with your csv file location
    ' =============================
    
    ' Declarations
    Dim STR_PATH As String
    Dim STR_SHEET As Variant ' ‡ quoi sert cette variable ?
    
    ' Set constants
    STR_PATH = "C:\Users\henri\OneDrive\Bureau\FEM\Vba corp\Data_CAC40.xlsx"
    'modification du dossier si necessaire
    
    ' YOUR CODE HERE
    
    'verification de l'existance du fichier
    If Dir(STR_PATH) = "" Then
    MsgBox "Le classeur est introuvable.", vbExclamation
    Exit Sub
    End If
    
    
    'Recuperation des donnees depuis la feuille excel
    DoCmd.TransferSpreadsheet acImport, 10, "data", STR_PATH, True 'acSpreadsheetTypeExcel12Xml = 10

End Sub


Sub s03_get_data()
    ' ==============================================
    ' Get data from a specific table
    '
    ' 1. Change the name of STR_TABLE_NAME
    ' to match with one of your tables
    '
    ' 2. Complete the corresponding function
    ' f03_get_data()
    '
    ' 3. Debug.print the data obtained from
    ' the function f03_get_data()
    '
    ' 4. Export the data in a file (RTF, CSV or PDF)
    ' ==============================================
    
    ' YOUR CODE HERE
    Dim File As String
    Dim filepath As String
    Dim STR_TABLE_NAME As String

    'Choix de la table √† exporter
    
    STR_TABLE_NAME = InputBox("choisissez la table √† exporter")
    
    'Export en CSV

    File = STR_TABLE_NAME & ".csv"
    filepath = "C:\Users\bahahe15\Desktop" & "\" & File
    If Dir(filepath) <> "" Then Kill (filepath)
    
    DoCmd.OutputTo acOutputQuery, STR_TABLE_NAME, acFormatXLSX, filepath, False
    
    'Export en PDF
    
    File = STR_TABLE_NAME & ".pdf"
    filepath = "C:\Users\bahahe15\Desktop" & "\" & File
    If Dir(filepath) <> "" Then Kill (filepath)
    
    DoCmd.OutputTo acOutputQuery, STR_TABLE_NAME, acFormatPDF, filepath, False
    
    'Export en RTF
    
    File = STR_TABLE_NAME & ".rtf"
    filepath = "C:\Users\bahahe15\Desktop" & "\" & File
    If Dir(filepath) <> "" Then Kill (filepath)
    
    DoCmd.OutputTo acOutputQuery, STR_TABLE_NAME, acFormatRTF, filepath, False

End Sub


Function f03_get_data(STR_TABLE_NAME As String)
    ' =====================================
    ' 1. Get the data from a specific table
    ' passed as input in the function
    '
    ' 2. Return the data
    ' =====================================
    
    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")
    
    f03_get_data = db.OpenRecordset("SELECT * FROM " & STR_TABLE_NAME).GetRows

End Function


Sub s04_create_table_ratios()
    ' =========================================
    ' Create a table named 'ratios'
    '
    ' Fields :
    ' - id
    ' - ratio_name
    ' - ratio_value
    ' - stock_name
    ' =========================================
    
    ' YOUR CODE HERE
    
    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")

    ' Creation de la table
    db.Execute "CREATE TABLE ratios (ID AUTOINCREMENT PRIMARY KEY, " _
        & "ratio_name TEXT, " _
        & "ratio_value FLOAT, " _
        & "stock_name TEXT);"
    
    

End Sub


Sub s05_populate_table_ratios()
    ' =========================================
    ' Insert an entry for each pair of
    ' stock_name and ratio_name
    ' with the value NULL for the ratio_value
    '
    ' Measures to add (names only for now):
    ' - Average_rolling_10d
    ' - Average_rolling_30d
    ' - Average_rolling_1y
    ' - Max
    ' - Min
    ' - Volatility_rolling_10d
    ' - Volatility_rolling_1y
    '
    ' =========================================
    
    ' YOUR CODE HERE
    
    'initialisation
    Dim db As Database
    Dim Mesures_names As Variant 'liste de toutes les mesures et de toutes les entreprises
    Dim p_Mesure, p_Company As String 'pointeur sur chaque noms d'entreprises et chaque mesures
    Dim i As Long
    Dim rs As Recordset 'stockage des noms d'entreprises
    
    Set db = OpenDatabase("Database1.accdb")
    
    'rÈcuperation de la liste des ratios
    
    Mesures_names = Array("Average_rolling_10d", "Average_rolling_30d", "Average_rolling_1y", "Max", "Min", "Volatility_rolling_10d", "Volatility_rolling_1y")
    
    
    Set rs = db.OpenRecordset("SELECT distinct stock_name FROM data")
    
    'remplissage de la feuille ratio avec pour chaque entreprises les diffÈrents ratios
    
    While Not rs.EOF
        p_Company = rs.Fields("stock_name")
        For Each p_Mesure In Mesures_names
            i = i + 1
            db.Execute "INSERT INTO ratios(id,ratio_name,ratio_value,stock_name) VALUES (" & i & ",'" & p_Mesure & "',Null,'" & p_Company & "')"
        Next p_Mesure
        rs.MoveNext
    Wend
    
    db.Close
    
End Sub


Sub s06_update_ratios()
    ' =========================================
    ' Update the table ratios based on the
    ' values of the table 'data'
    ' =========================================
    
    ' YOUR CODE HERE
    
    'initialisation
    Dim db As Database
    Dim Company_all_names As String
    Dim Mesures_all As Variant
    Dim Company_all As String
    Dim Mesures_names As Variant
    Dim Company_names As String
    Dim Mesures_output As Variant
    
    Dim j As Long
    Dim rs As Recordset, Mesures_names_all
    
    Set db = OpenDatabase("Database1.accdb")
    
    'rÈcuperation de la liste des ratios
    
    Mesures_names_all = Array("Average_rolling_10d", _
        "Average_rolling_30d", _
        "Average_rolling_1y", _
        "Max", _
        "Min", _
        "Volatility_rolling_10d", _
        "Volatility_rolling_1y")
    
    'rÈcuperation des noms des entreprises
    
    Company_all_names = "SELECT DISTINCT stock_name FROM data"
    
    Set rs = db.OpenRecordset(Company_all_names)
    
    'calcul des ratio pour chaque entreprise
    While Not rs.EOF
        Company_names = rs.Fields("stock_name")
        j = 0
        Mesures_all = Array(f061_compute_average_rolling(Company_names, 10), _
            f061_compute_average_rolling(Company_names, 30), _
            f061_compute_average_rolling(Company_names, 365), _
            f063_Max(Company_names), _
            f064_Min(Company_names), _
            f062_compute_volatility_rolling(Company_names, 10), _
            f062_compute_volatility_rolling(Company_names, 365))

        'remplissage des ratios pour chaque entreprise
        
        For Each Mesures_names In Mesures_all
            
            Mesures_output = "UPDATE ratios SET ratio_value = " & Str(Mesures_names) & _
                " WHERE stock_name = '" & Company_names & _
                "' AND ratio_name = '" & Mesures_names_all(j) & "'"
              db.Execute Mesures_output
              j = j + 1
        Next Mesures_names
        rs.MoveNext
    Wend
    
    
    db.Close
End Sub


Function f061_compute_average_rolling(str_stock_name As String, int_period As Integer)
    ' =========================================
    ' Compute and return the average value of a
    ' stock based on the N last days/years
    ' depending on the value of input 'period'
    ' =========================================
    
    ' YOUR CODE HERE
    
    'initialisation
    Dim db As Database
    Dim rs As Recordset
    Dim calcul As String
    Dim date_calcul As Date
    Dim last_date As Date
    Dim mesure_output As Variant
    Dim jour As Long
    Dim jour_fin As Long
    Dim mois As Long
    Dim annee As Long
    
    
    'derniere date
    
    last_date = "2020 - 10 - 20"

    
    'calcul date de dÈbut pour la moyenne glissante
    
    Set db = OpenDatabase("Database1.accdb")
    
    date_calcul = last_date - int_period
    jour = Day(date_calcul)
    jour_fin = Day(last_date)
    mois = Month(date_calcul)
    annee = Year(date_calcul)
    
    'calcul de la moyenne glissante
    
    calcul = "SELECT Sum(stock_value)/ " & int_period & " FROM data WHERE stock_name='" & str_stock_name & "' AND date >= " & annee & "-" & mois & "-" & jour & ";"
    
    mesure_output = db.OpenRecordset(calcul).GetRows(1)
    f061_compute_average_rolling = mesure_output(0, 0)
    
    db.Close
End Function


Function f062_compute_volatility_rolling(str_stock_name As String, int_period As Integer)
    ' =========================================
    ' Compute and return the volatility of a
    ' stock based on the N last days/years
    ' depending on the value of input 'period'
    ' =========================================
    
    ' YOUR CODE HERE
    
    'initialisation
    
    Dim db As Database
    Dim rs As Recordset
    Dim calcul As String
    Dim date_close As Date
    Dim last_date As Date
    Dim mesure_output As Variant
    
    'derniere date
    
    last_date = "2020 - 10 - 20"
    
    Set db = CurrentDb
    
    'calcul date de dÈbut pour la volatilitÈ glissante
    
    date_close = last_date - int_period
    
    'calcul de la volatilitÈ glissante
    
    calcul = "SELECT STDEV(stock_value) FROM data WHERE [stock_name]='" & str_stock_name & "' AND date >= " & date_close
    mesure_output = db.OpenRecordset(calcul).GetRows(1)
    f062_compute_volatility_rolling = mesure_output(0, 0)
    
    db.Close
    

End Function

Function f063_Max(ByVal str_stock_name As String)
    ' =========================================
    ' Compute and return the maximum
    ' =========================================
    
    ' YOUR CODE HERE
    'initialisation
    
    Dim mesure_output As Variant
    Dim mesure_calcul As String
    
    'calcul max
    
    mesure_calcul = "SELECT Max(stock_value) FROM data WHERE stock_name='" & str_stock_name & "'"
    mesure_output = CurrentDb.OpenRecordset(mesure_calcul).GetRows(1)
    f063_Max = mesure_output(0, 0)
    
End Function


Function f064_Min(ByVal str_stock_name As String)
    ' =========================================
    ' Compute and return the minimum
    ' =========================================
    
    ' YOUR CODE HERE
    
    'initialisation
    
    Dim mesure_output As Variant
    Dim mesure_calcul As String
    
    'calcul min
    
    mesure_calcul = "SELECT Min(stock_value) FROM data WHERE[stock_name]='" & str_stock_name & "'"
    mesure_output = CurrentDb.OpenRecordset(mesure_calcul).GetRows(1)
    f064_Min = mesure_output(0, 0)
    
End Function


Sub s07_create_table_ratios_hist()
    ' =========================================
    ' Create a table named 'ratios_hist'
    ' Fields :
    ' - id
    ' - datetime | format : yyyy/mm/dd hh:nn:ss
    ' - ratio_name
    ' - ratio_value
    ' - stock_name
    ' =========================================
    
    ' YOUR CODE HERE
    
    ' YOUR CODE HERE
    
    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")

    ' Creation de la table
    db.Execute "CREATE TABLE ratios_hist (ID AUTOINCREMENT PRIMARY KEY, " _
        & "[date] DATE, " _
        & "ratio_name TEXT, " _
        & "ratio_value FLOAT, " _
        & "stock_name TEXT);"

End Sub


Sub s08_create_table_warning()
    ' =========================================
    ' Create a table named 'warnings'
    ' Fields :
    ' - id
    ' - ratio_name
    ' - ratio_value
    ' - warning_type
    ' - stock_name
    ' =========================================
    
    ' YOUR CODE HERE
    
    'initialisation
    
    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")

    ' Creation de la table
    db.Execute "CREATE TABLE warning (ID AUTOINCREMENT PRIMARY KEY, " _
        & "ratio_name TEXT, " _
        & "ratio_value FLOAT, " _
        & "warning_type TEXT, " _
        & "stock_name TEXT);"


End Sub


Sub s09_populate_table_warning()
    ' ============================================
    ' Add an entry to the table 'warning' for each
    ' pair of : ratio_name and stock_name
    ' Set the ratio_value and warning_type to NULL
    ' ============================================
    
    ' YOUR CODE HERE
    
    'initialisation
    Dim db As Database
    Dim Mesures_all As Variant
    Dim Company_all As Variant
    Dim Mesure_name As Variant
    Dim Company_name As Variant
    Dim output As String
    Dim j As Long
    Dim rs As Recordset
    Dim Company_all_names As String
    
    Set db = OpenDatabase("Database1.accdb")

    
    'rÈcuperation de la liste des ratios
    Mesures_all = Array("Average_rolling_10d", _
        "Average_rolling_30d", _
        "Average_rolling_1y", _
        "Max", _
        "Min", _
        "Volatility_rolling_10d", _
        "Volatility_rolling_1y")
    
    'rÈcupÈration des noms des entreprises
    Company_all_names = "SELECT distinct stock_name FROM data"
    
    Set rs = db.OpenRecordset(Company_all_names)
    
    'remplissage de la feuille warning avec pour chaque entreprises les diffÈrents ratios
    While Not rs.EOF
        Company_name = rs.Fields("stock_name")
        For Each Mesure_name In Mesures_all
            j = j + 1
            output = "INSERT INTO warning(id,ratio_name,ratio_value,warning_type,stock_name) VALUES (" & j & ",'" & Mesure_name & "',Null,Null,'" & Company_name & "')"
              db.Execute output
        Next Mesure_name
        rs.MoveNext
    Wend
    
    
    db.Close

End Sub


Sub s10_update_ratios_if_limit_breached()
    ' ============================================
    ' Update the warning table only if one
    ' of the following limit is breached for the
    ' data of the current day
    '
    ' Warning types:
    ' - limit_max : ratio value above a threshold
    ' - limit_min : ratio value below a threshold
    ' - NULL : otherwise
    ' ============================================
    
    ' YOUR CODE HERE
    
    'initialisation
    Dim db As Database
    Dim Company_all_names As String
    Dim Mesures_all As Variant
    Dim Company_all As String
    Dim Mesures_names As Variant
    Dim Company_names As String
    Dim Mesures_output As Variant
    Dim limit_max As Long
    Dim limit_min As Long
    Dim type_limit As Variant
    
    Dim j As Long
    Dim rs As Recordset, Mesures_names_all
    
    Set db = OpenDatabase("Database1.accdb")
    
    'recuperation des ratios
    Mesures_names_all = Array("Average_rolling_10d", _
        "Average_rolling_30d", _
        "Average_rolling_1y", _
        "Max", _
        "Min", _
        "Volatility_rolling_10d", _
        "Volatility_rolling_1y")
    
    'recuperation des noms de chaque entreprise
    Company_all_names = "SELECT DISTINCT stock_name FROM data"
    
    Set rs = db.OpenRecordset(Company_all_names)
    
    'choix des limite supÈrieur et infÈrieur
    limit_max = 500
    limit_min = 25

    'calcul des ratios pour chaque entreprise
    While Not rs.EOF
        Company_names = rs.Fields("stock_name")
        j = 0
        Mesures_all = Array(f061_compute_average_rolling(Company_names, 10), _
            f061_compute_average_rolling(Company_names, 30), _
            f061_compute_average_rolling(Company_names, 365), _
            f063_Max(Company_names), _
            f064_Min(Company_names), _
            f062_compute_volatility_rolling(Company_names, 10), _
            f062_compute_volatility_rolling(Company_names, 365))
        
        
        'modification des ratios si les seuils Ètablit sont dÈpassÈs (borne infÈrieur et supÈrieur)
        For Each Mesures_names In Mesures_all
            If Mesures_names > limit_max Then
                type_limit = "Limit Max"
                Mesures_output = "UPDATE warning SET ratio_value = " & Str(Mesures_names) & _
                ",warning_type = '" & type_limit & "' WHERE stock_name = '" & _
                Company_names & "' AND ratio_name = '" & Mesures_names_all(j) & "'"

                db.Execute Mesures_output
            
            ElseIf Mesures_names < limit_min Then
                type_limit = "Limit Min"
                Mesures_output = "UPDATE warning SET ratio_value = " & Str(Mesures_names) & _
                ",warning_type = '" & type_limit & "' WHERE stock_name = '" & _
                Company_names & "' AND ratio_name = '" & Mesures_names_all(j) & "'"

                db.Execute Mesures_output
            End If
            
    
              j = j + 1
        Next Mesures_names
        rs.MoveNext
    Wend
    
    
  
End Sub


Sub s11_log_ratios_hist()
    ' =========================================
    ' Insert the ratio values for each pair of
    ' stock_name and ratio_name in the table
    ' 'ratios_hist' along with the current
    ' datetime
    ' =========================================

    ' YOUR CODE HERE
    Dim db As Database
    Dim table_ratios As String
    Dim rs As Recordset
    Dim last_date As Date
    
    Set db = OpenDatabase("Database1.accdb")
    
    'rÈcuperation du nom de tous les ratios
    table_ratios = "SELECT * FROM ratios"
    
    Set rs = db.OpenRecordset(table_ratios)
    
    ' Insertion des donnÈes calculÈ dans la feuille ratio historique
    While Not rs.EOF
        last_date = 20 / 10 / 2020
        SQL = "INSERT INTO ratios_hist(id,datet,ratio_name,ratio_value,stock_name) VALUES (" & rs.Fields("id") & ",'" & last_date & "','" & rs.Fields("ratio_name") & "','" _
        & rs.Fields("ratio_value") & "','" & rs.Fields("stock_name") & "')"
        db.Execute SQL
        rs.MoveNext
    Wend
    
    
    db.Close

End Sub

    
End Sub


Sub s12_create_table_static_investors()
    ' =========================================
    ' Create a table named 'static_investors'
    '
    ' Fields :
    ' - id
    ' - name
    ' - birth
    ' =========================================
    
    ' YOUR CODE HERE
    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")

    ' Creation de la table
    db.Execute "CREATE TABLE static_investors (ID AUTOINCREMENT PRIMARY KEY, " _
        & "name TEXT, " _
        & "birth DATE);"
    

End Sub


Sub s13_create_table_portfolios()
    ' =========================================
    ' Create a table named 'portfolios'
    '
    ' Fields :
    ' - id
    ' - investor_id
    ' - stock_name
    ' - quantity
    ' =========================================
    
    ' YOUR CODE HERE
    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")

    ' Creation de la table
    db.Execute "CREATE TABLE portfolios (ID AUTOINCREMENT PRIMARY KEY, " _
        & "investor_id INT, " _
        & "stock_name TEXT, " _
        & "quantity FLOAT);"
    

End Sub


Sub s14_feed_static_investors()
    ' ===========================================
    ' Feed table static_investors from a csv file
    ' with arbitrary data
    ' ===========================================
    
    ' Declarations
    Dim STR_PATH As String
    
    ' Set constants
    STR_PATH = "C:\Users\henri\OneDrive\Bureau\FEM\Vba corp\Investors.xlsx"
    
    'verification de l'existance du fichier
    If Dir(STR_PATH) = "" Then
    MsgBox "Le classeur est introuvable.", vbExclamation
    Exit Sub
    End If
    
    
    'Recuperation des donnees depuis la feuille excel
    DoCmd.TransferSpreadsheet acImport, 10, "static_investors", STR_PATH, True

    
    

End Sub


Sub s15_feed_portfolios()
    ' ===========================================
    ' Feed table portfolios from a csv file
    ' with arbitrary data
    ' ===========================================
    
     ' Declarations
    Dim STR_PATH As String
    
    ' Set constants
    STR_PATH = "C:\Users\henri\OneDrive\Bureau\FEM\Vba corp\Portfolios.xlsx"
    
    'verification de l'existance du fichier
    If Dir(STR_PATH) = "" Then
    MsgBox "Le classeur est introuvable.", vbExclamation
    Exit Sub
    End If
    
    
    'Recuperation des donnees depuis la feuille excel
    DoCmd.TransferSpreadsheet acImport, 10, "portfolios", STR_PATH, True
    
    

End Sub

Sub Create_table_last_stock_value()

    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")

    ' Creation de la table
    db.Execute "CREATE TABLE last_stock_value (ID AUTOINCREMENT PRIMARY KEY, " _
        & "stock_name TEXT, " _
        & "last_value FLOAT); "
        
End Sub

Sub Populate_table_last_stock_value()

    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")


    db.Execute "INSERT INTO last_stock_value ( stock_name, last_value )" _
        & "SELECT stock_name, stock_value FROM Data WHERE MONTH(date)=10 AND DAY(date)=20 AND YEAR(date)=2020;"

    
End Sub

Sub s16_create_table_investors_metrics()
    ' =========================================
    ' Create a table named 'investors_metrics'
    '
    ' Fields :
    ' - investor_id
    ' - stocks_number_of
    ' - stocks_total_value
    ' - stocks_average_value
    ' =========================================
    
    ' YOUR CODE HERE

    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")

    ' Creation de la table
    db.Execute "CREATE TABLE investors_metrics (investor_id INT, " _
        & "stock_number_of INT, " _
        & "stock_total_value FLOAT, " _
        & "stock_average_value FLOAT);"
    
    

End Sub


Sub s17_populate_table_investors_metrics()
    ' =========================================
    ' Insert an entry for each investor
    ' with a NULL value for the metrics
    '
    ' =========================================
    
    ' YOUR CODE HERE

    ' Nous n'utilisons pas cette sub, nous remplissons directement la table investors_metrics ‡ l'aide de la sub 18 ci-dessous
    
End Sub


Sub s18_update_investors_metrics()
    ' ============================================
    ' Update the table investors_metrics based on
    ' the stocks they owe, their quantity, and
    ' the stocks' value
    '
    ' This question requires the use of a JOIN
    ' ============================================
    
    ' YOUR CODE HERE
    
    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")

    db.Execute "INSERT INTO investors_metrics ( investor_id, stock_number_of, stock_total_value, stock_average_value )" _
                & " SELECT portfolios.investor_id," _
                & " SUM(portfolios.quantity)," _
                & " ROUND(SUM(portfolios.quantity*last_stock_value.last_value),0)," _
                & " ROUND(SUM(portfolios.quantity*last_stock_value.last_value)/SUM(portfolios.quantity),0)" _
                & " FROM portfolios" _
                & " INNER JOIN last_stock_value ON portfolios.stock_name = last_stock_value.stock_name" _
                & "GROUP BY portfolios.investor_id;"
  
End Sub


Sub s19_drop_tables_all()
    ' ==========================================
    ' Drop all tables to reinitiate the database
    ' ==========================================
    
    ' YOUR CODE HERE
    
    Dim db As Database
    
    Set db = OpenDatabase("Database1.accdb")
    
    db.Execute "DROP TABLE ratios;"
    db.Execute "DROP TABLE ratios_hist;"
    db.Execute "DROP TABLE warning;"
    db.Execute "DROP TABLE investors_metrics;"
    db.Execute "DROP TABLE portfolios;"
    db.Execute "DROP TABLE static_investors;"
    db.Execute "DROP TABLE last_stock_value;"
    db.Execute "DROP TABLE data;"

End Sub
'''
