Option Explicit

' *********************************************
' 定数定義
' *********************************************

Const HEADER_MEMORY = "MEMORY {"
Const HEADER_DEFAULT = "DEFAULTS {"
Const HEADER_SECTION = "SECTIONS {"
Const FOOTER_COMMON = "}"
Const HEADER_COMMENT_SECTION_0 = "/*************************************************************************************************/"
Const HEADER_COMMENT_SECTION_1 = "/* セクション定義                                                                                */"
Const HEADER_COMMENT_SECTION_2 = "/*************************************************************************************************/"
Const ORIGIN = ": ORIGIN = "
Const LENGTH = ", LENGTH = "
Const EQUAL = " = "
Const SHEETNAME_SETTING = "設定"
Const SHEETNAME_MEMORYMAP = "メモリマップ定義"
Const SHEETNAME_OUTSETTING = "ユーザー定義シンボル"
Const SHEETNAME_MEMORYPLACEMENT = "メモリ配置図"
Const SHEETNAME_RIVISION = "改訂履歴"
Const SYMBOL_for_MICROSAR_OS_1 = "    /* ------ SYMBOL for MICROSAR OS ------ */"              'MICROSAR OSのためのシンボル
Const SYMBOL_for_MICROSAR_OS_2 = "    __OS_CODE_START = ADDR(.OS_CODE);"         'MICROSAR OSのためのシンボル
Const SYMBOL_for_MICROSAR_OS_3 = "    __OS_CODE_END = ENDADDR(.OS_CODE) - 1;"    'MICROSAR OSのためのシンボル
Const AREA_TOP = "    /* ------"
Const AREA_END = "------ */"
Const SECTION_SPACE = "    "
Const MEMORY_CATEGORY_PREFIX = " /* "
Const MEMORY_CATEGORY_POSTFIX = " */"
Const SECTION_CATEGORY_PREFIX = " /*------ FUNCTYPE:"
Const SECTION_CATEGORY_POSTFIX = " ------*/"

Const INDENTS_MEMORY2ORIGIN = 20        'LDファイルの視認性を向上させるために、各ブロックにインデントをつけている
Const INDENTS_CONST2VALUE = 15          '現在の実装ではインデント数＝文字数の制約になっている
Const INDENTS_SECTION2ELEMENT1 = 30     'もし、出力された文字列の一部が上書きされているなどがあれば、
Const INDENTS_ELEMENT32MEMORY = 41      'これらのインデントの値を修正することで問題が解消されるかもしれない
Const INDENTS_MEMORY2COMMENT = 15       'ブラッシュアップ：定数に依存しないインデントの付け方
Const INDENTS_FORMULA2LEFT = 12
Const INDENTS_FORMULA2RIGHT = 18
Const INDENTS_FORMULA2FULL = 34

Const INDEX_START_ARRAY = 1

Const HEADER_COMENT_TOP = "/*""""FILE COMMENT""""*******************************************************************************************************/"
Const HEADER_COMENT_FILENAME = "/* File Name   : aipf_startup_HOST.ld                                                                                   */"
Const HEADER_COMENT_FILENAME_TOP = "/* File Name   : "
Const HEADER_COMENT_FILENAME_END = "*/"
Const HEADER_COMENT_CONTENTS = "/* Contents    : スタートアップ機能 - HOST - リンカディレクティブ                                                       */"
Const HEADER_COMENT_COMPILER = "/* Compiler    : Green Hills コンパイラ                                                                                 */"
Const HEADER_COMENT_CPU = "/* CPU         : RH850/F1KM-S1/S4                                                                                       */"
Const HEADER_COMENT_NOTE = "/* Note        : 編集許可                                                                                               */"
Const HEADER_COMENT_DOTLINE = "/*----------------------------------------------------------------------------------------------------------------------*/"
Const HEADER_COMENT_HISTORY_TOP = "/* History     : "
Const HEADER_COMENT_SUBHISTORY_TOP = "/*             : "
Const HEADER_COMENT_HISTORY_END = "*/"
Const HEADER_COMENT_HISTORY = "/* History     :                                                                                                        */"
Const HEADER_COMENT_SUBHISTORY = "/*             :                                                                                                        */"
Const HEADER_COMENT_LINE = "/************************************************************************************************************************/"
Const HEADER_COMENT_COPYRIGHT = "/*                                                                                    Copyright(c)  AISIN SEIKI CO.,LTD */"
Const HEADER_COMENT_END = "/*""""FILE COMMENT END""""***************************************************************************************************/"

Const HEADER_COMENT_BYTE = 120
Const TABLE_FILEID_TITLE = "LDファイルID"
Const TABLE_DEFINE_SYMBOL = "[DEFINE_SYMBOL_TOP]"
Const TABLE_DEFAULT_SECTION_CHECK_SETTING_TOP = "[DEFAULT_SECTION_CHECK_SETTING_TOP]"
Const TABLE_DEFAULT_SECTION_CHECK_SETTING_END = "[DEFAULT_SECTION_CHECK_SETTING_END]"
Const TABLE_COMPILER_AUTO_GENERATE_SECTION_TOP = "[COMPILER_AUTO_GENERATE_SECTION_TOP]"
Const TABLE_COMPILER_AUTO_GENERATE_SECTION_END = "[COMPILER_AUTO_GENERATE_SECTION_END]"
Const TABLE_MEMORY_ROMRAM_CALC_FORMULA_TOP = "[MEMORY_CATEGORY_TOP]"
Const TABLE_MEMORY_ROMRAM_CALC_FORMULA_END = "[MEMORY_CATEGORY_END]"
Const TABLE_MEMORY_FUNCTION_CALC_FORMULA_TOP = "[APPLICATION_CATEGORY_TOP]"
Const TABLE_MEMORY_FUNCTION_CALC_FORMULA_END = "[APPLICATION_CATEGORY_END]"

Const COLUMN_DELETE_RANGE = "D:Z"

' エラーメッセージのタイトル
Const ERROR_TITLE = "エラー"

' エラーメッセージ
'項目未記入のエラーメッセージ
Const MEMORY_NAME_BLANK = "メモリ名が未記入です。"
Const SIZE_BLANK = "サイズが未記入です。"
Const START_ADDRESS_BLANK = "開始アドレスが未記入です。"
Const MEMORY_CATEGORY_BLANK = "メモリカテゴリが未記入です。"
Const LD_FILE_ID_BLANK = "LDファイルIDが未記入です。"

'確認メッセージのタイトル
Const QUESTION_TITLE = "確認"

'表削除の確認メッセージ
Const QUESTION_DELETE_TABLE = "編集中の表が削除されます、よろしいですか?"

'リストボックスの位置参照用の定数
Const ROW_LISTBOX_LOCATION = 2
Const COLUMN_LISTBOX_LOCATION = 2

'最終行の取得後の、最終行を示す文字の説明を含むための定数
Const LASTROW_DESCRIPTION = 2

' *********************************************
' 型定義
' *********************************************
Private Type LDFile_STR
    LDFileID         As String          'ldファイルID
    LDFileName       As String          'ldファイル名
    Output_Memory    As String          '出力データ（メモリ）メモリ部分に出力する文字列
    Output_Const     As String          '出力データ（定数）定数部分に出力する文字列
    Output_Section   As String          '出力データ（セクション）セクション部分に出力する文字列
End Type

Private Type Section_STR
    LDFileID                    As String
    Memory                      As String
    Section_Name                As String
    Start_Expression            As String
    Attributes                  As String
    Contents                    As String
    Section_Category            As String
    Section_ExMemoryCalcSetting As String
    Comment                     As String
End Type

' *********************************************
' プロシージャレベル変数
' *********************************************
Private Sheet_Setting      As Worksheet '設定シートのオブジェクト
Private Sheet_MemoryMap    As Worksheet 'メモリマップ定義シートのオブジェクト
Private Sheet_OutSetting   As Worksheet '任意出力設定シートのオブジェクト
Private Sheet_Addr_Spese   As Worksheet 'アドレス空間シートのオブジェクト
Private Sheet_MemoryPlace  As Worksheet 'メモリ配置シートのオブジェクト
Private Sheet_Revision     As Worksheet '改訂履歴シートのオブジェクト

Dim Rowindex_TopLDFileID                '設定シートのldファイル入力エリア開始行インデックス
Dim RowIndex_TopConst                   '設定シートの固定領域入力エリア開始行インデックス

Dim RowIndex_TopMemoryMap               'メモリマップ定義シート入力エリア開始行インデックス
Dim Rowindex_EndRow                     'メモリマップ定義シートの最終行
Dim ColIndex_Area                       'Area名列インデックス
Dim ColIndex_MemoryLDFileID             'メモリシートのldファイルID列インデックス
Dim ColIndex_MemoryName                 'メモリブロック名列インデックス
Dim ColIndex_MemoryAddr_Start           'メモリ開始アドレス列インデックス
Dim ColIndex_MemorySize                 'メモリサイズ列インデックス
Dim ColIndex_MemoryCategory             'メモリ種別列インデックス
Dim ColIndex_SectionName                'セクション名列インデックス
Dim ColIndex_SectionStartExpression     'セクション開始アドレス（start_expression）列インデックス
Dim ColIndex_SectionAttributes          'セクション属性（Attributes）列インデックス
Dim ColIndex_SectionContents            'セクションオブジェクト配置（Contents）列インデックス
Dim ColIndex_SectionCategory            'セクション種別列インデックス
Dim ColIndex_Comment                    'コメント列インデックス

Dim Error_Message_Text As String        'エラーメッセージに表示するテキスト

Private Is_Fraud As Boolean             'フォーマット不正判定の変数(Trueの場合、不正とする)

Private SectionList() As Section_STR    'セクションリスト　セクション名のリスト
                                        '一つの関数内でしか使用していないため、オート変数で宣言することも可能だが、
                                        'デバッグをやり易くするために、プロシージャレベルで宣言する

Private Output_Memory   As String       '出力データ（メモリ）　メモリ部分に出力する文字列
Private Output_Const    As String       '出力データ（固定領域）　固定領域部分に出力する文字列
Private Output_Section  As String       '出力データ（セクション）　セクション部分に出力する文字列

Private LDList(5) As LDFile_STR         'ldリスト　各ldファイルで作成するldファイルの情報のリスト
                                        '動的に配列を定義する方法を忘れたため、エイヤで要素を5としている(5に意図はない)
                                        'ブラッシュアップ：動的に宣言できる方法があれば修正してほしい

Private NumberLD As Variant             'ldファイルの個数

Private Before_Item_Name As String      '前回選択した、アドレス空間リストボックスのアイテム名

Private History_List() As String        '改訂履歴のリスト

Private Output_Setting_List() As String '任意出力

' *********************************************
' 処理
' *********************************************

'/**************************************************************************************
'/* 概要   | ldファイル生成のメイン関数
'/*        | エクセル内の「LDファイル生成」ボタンをクリックするとこの関数が呼び出される
'/**************************************************************************************
Public Sub Main()
    Call Init_Data              'フォーマット（見出し列）を設定する
    Call Get_LDName             'ldファイルリストの情報を読み込む
    Call Get_MemoryName         'メモリマップ定義シート：メモリ情報を読み込む
    
    If (Is_Fraud = False) Then  'フォーマットが不正の場合エラーメッセージを表示し、以降の処理は行わない
        Call Get_SectionData    'メモリマップ定義シート：セクション情報を読み込む
        Call Create_LD          'ldファイルを生成する
    Else
        Call Show_Error_Messsage(Error_Message_Text)
    End If
End Sub

'/**************************************************************************************
'/* 概要   | ldファイル作成で使用するグローバル変数の初期値を設定する
'/*        | シートや見出しを変更した際には、この関数内の処理や値を変える
'/*        | ☆★☆で囲んだ部分がシートや見出しを変更した際に変更する箇所である
'/**************************************************************************************
Public Sub Init_Data()
    '出力文字列の初期化
    '初期化しないと前の情報を保持し意図しないデータも出力してしまうため、削除には注意すること
    Erase SectionList
    Erase LDList
    
    'シートオブジェクトを別のオブジェクトに格納する
    'ワークシート名をいちいち打たずに(開発時に)見やすくするために実施
    Set Sheet_Setting = ActiveWorkbook.Worksheets(SHEETNAME_SETTING)
    Set Sheet_MemoryMap = ActiveWorkbook.Worksheets(SHEETNAME_MEMORYMAP)
    Set Sheet_Revision = ActiveWorkbook.Worksheets(SHEETNAME_RIVISION)
    Set Sheet_OutSetting = ActiveWorkbook.Worksheets(SHEETNAME_OUTSETTING)
    
    'メモリマップ設定シートの終端の行数を取得する
    Rowindex_EndRow = 1                                                            'メモリマップシートの最終行を初期化する'
    Do Until InStr(Sheet_MemoryMap.Cells(Rowindex_EndRow, COLUM_A).Text, "■") > 0  'A列の最終行を示す「■」を見つけるまで、A列の各セルのデータを比較している(ループ)'
        Rowindex_EndRow = Rowindex_EndRow + 1                                      'ループの値には内部変数を使って、最終行が決まったらデータ更新したいが、'
    Loop                                                                           'CPUのメモリを節約するために直接データを更新している'
    
    '☆★☆☆★☆☆★☆☆★☆☆★☆☆★☆
    
    '見出しのセルの行や列を設定する。
    '初期化関数内で実施している理由は、メンテナンス性向上のためである。
    'いずれテンプレートなどが固まったり、見出しの位置を変更した場合に、列や行の値を変更する必要がある。
    '変更すべきデータをある程度まとめておくことで、列や行の変更に対応しやすくする。
    'テンプレートを決定した後は、見出しの列や行を設定する位置を変更しても問題ない。
    'また、今は暫定的に直値を入れているが、セルの探索などを使用して賢い方法をとってもいいと思う
    'ブラッシュアップ： 「メモリ名」というセルを探索しその行を検索するようにしたいが、ベストな案が思いつかないため決め打ちでセルの位置を取得する

    'メモリマップ設計シート内の見出し行・列設定
    RowIndex_TopMemoryMap = 6                               'メモリマップ設計シートの入力エリアの行番号を設定する(6行)
                                                            
    ColIndex_Area = COLUM_A                                 '「Area列」の列番号を設定する(B列)
    ColIndex_MemoryName = COLUM_B                           '「メモリ名」列の列番号を設定する(B列)
    ColIndex_MemoryAddr_Start = COLUM_C                     '「開始アドレス」列の列番号を設定する(C列)
    ColIndex_MemorySize = COLUM_D                           '「サイズ」列の列番号を設定する(D列)
    ColIndex_MemoryCategory = COLUM_E                       '「メモリカテゴリ」列の列番号を設定する(E列)
    ColIndex_SectionName = COLUM_F                          '「セクション名」列の列番号を設定する(F列)
    ColIndex_SectionStartExpression = COLUM_G               '「開始アドレス（start_expression）」列の列番号を設定する(G列)
    ColIndex_SectionAttributes = COLUM_H                    '「属性（attributes）」列の列番号を設定する(H列)
    ColIndex_SectionContents = COLUM_I                      '「オブジェクト配置（contents）」列の列番号を設定する(I列)
    ColIndex_SectionCategory = COLUM_J                      '「セクションカテゴリ」列の列番号を設定する(J列)
    ColIndex_Comment = COLUM_K                              '「コメント」列の列番号を設定する(K列)
    
    '☆★☆☆★☆☆★☆☆★☆☆★☆☆★☆
    
    'フォーマット不正判定を初期状態にする。
    Is_Fraud = False
    Error_Message_Text = ""
End Sub

'/**************************************************************************************
'/* 概要   | ldファイル名を取得する関数
'/*        | 「設定」シートからldファイルIDとldファイル名を取得する
'/**************************************************************************************
Sub Get_LDName()
    Dim tmp_ldfile_num
    Dim tmp_RowIndex_LDFileID
    Dim i
    Dim find_Range As Range

    'Eraseでどこまで初期化してくれるのかわからなかったため、念のためで初期化している。
    '不要と分かれば削除してほしい
    For i = INDEX_START_ARRAY To 5
        LDList(i).LDFileName = ""
    Next
    
    'Excel上、LDファイルIDは廃止するが、VBA処理内部では0固定とする
    LDList(INDEX_START_ARRAY).LDFileID = 0
    
    '内部変数の初期化
    tmp_ldfile_num = 0  'ldファイル数を0で初期化 Do Whileで先頭でインクリメントすることで正しく個数を認識させたい。そのため、0で初期化し、ループ文の先頭でインクリメントして1としたいため0で初期化する
        
    '行インデックスをInit_Dataで初期化した変数から取得する
    Set find_Range = Sheet_Setting.Cells.Find(What:="[LDFILE_TOP]", LookIn:=xlValues, LookAt:=xlWhole)
    tmp_RowIndex_LDFileID = find_Range.Row + 2
    
    Do Until InStr(Sheet_Setting.Cells(tmp_RowIndex_LDFileID, COLUM_B).Text, "[LDFILE_END]") > 0    'B列の最終行を示す「[LDFILE_END]」を見つけるまで、D列の各セルのデータを比較する(ループ)'
        'ldファイル数をインクリメントする このループ内に入るたびにインクリメントするため、インクリメントしすぎを防ぐために初期値は0にし、ここでインクリメントしている
        tmp_ldfile_num = tmp_ldfile_num + 1
        
        'ldファイル名とファイル名をエクセルから取得する
        LDList(tmp_ldfile_num).LDFileName = Sheet_Setting.Cells(tmp_RowIndex_LDFileID, COLUM_B).Text
        
        '参照する行インデックスをインクリメントし、次の行を参照するようにする
        tmp_RowIndex_LDFileID = tmp_RowIndex_LDFileID + 1
    Loop
    'LDファイル数をグローバル変数に格納し、他のプロシージャ上で使用できるように公開する
    NumberLD = tmp_ldfile_num
End Sub

'/**************************************************************************************************************
'/* 概要   | MEMORY{}内に定義するメモリ領域のデータをエクセルファイルから取得する
'/*        | Output_Memoryに出力するデータを格納するので、デバッグ時はOutput_Memoryに着目すると良いかもしれない
'/**************************************************************************************************************
Public Sub Get_MemoryName()
    '内部変数の宣言
    Dim tmp_RowIndex_MemoryName  'メモリブロック名行インデックス
    Dim tmp_Memoryindex          'メモリインデックス
    Dim tmp_MemoryAddr_Start     '開始アドレスデータ
    Dim tmp_MemorySize           'サイズデータ
    Dim tmp_Target_Area          'Area
    Dim tmp_Target_Area_old      'Areaの前回値
    Dim tmp_OutputArea           'Areaの出力データ
    Dim tmp_TargetLDFileID       'メモリを配置するldファイル
    Dim tmp_MemoryName           'メモリブロック名
    Dim tmp_MemoryCategory       'メモリ種別
    Dim tmp_LDFileID_old         'ldファイルIDの前回値
    Dim i
    
    '内部変数を初期化する
    tmp_Memoryindex = 1                                 'メモリインデックスを初期化する(メモリは1つ以上必ず記載されていると想定し、1で初期化する)
    tmp_RowIndex_MemoryName = RowIndex_TopMemoryMap     'メモリブロック名行インデックスに入力エリア開始行インデックスを代入する
    tmp_Target_Area_old = ""                            'Area前回値をブランクで初期化する
    tmp_LDFileID_old = ""
    
    'Eraseでどこまで初期化してくれるのかわからなかったため、念のためで初期化している。
    '不要と分かれば削除してほしい
    For i = INDEX_START_ARRAY To NumberLD
        LDList(i).Output_Memory = ""
    Next
    
    'メモリブロック名列（記入領域）の先頭行からメモリマップ定義シートの最終行までメモリブロック名が記載されているセルを全て探索する
    Do Until tmp_RowIndex_MemoryName > Rowindex_EndRow
        '処理対象の行のフォーマットを確認し、フォーマット不正と判断した場合ループを中断する
        If (Row_Format_Checker(tmp_RowIndex_MemoryName) = True) Then
            'フォーマット不正フラグをTrueに変更する
            Is_Fraud = True
            Exit Do
        End If
    
        'セル結合しているため空白セルを無視し何か記載しているセルにはメモリブロック名が記載されていると判断する
        If Sheet_MemoryMap.Cells(tmp_RowIndex_MemoryName, ColIndex_MemoryName).Text <> "" Then
            '参照したメモリを配置するAreaを取得する
            tmp_Target_Area = Target_Area(tmp_RowIndex_MemoryName)
            
            '参照したメモリを配置するldファイルIDを取得する
            'Excel上、LDファイルIDは廃止するが、VBA処理内部では0固定とする
            tmp_TargetLDFileID = 0
            
            'Areaをコメントに記載する
            '現在参照しているメモリのAreaと前回値を比較し､異なる場合はAreaをldファイルにコメントとして出力し、異なる場合は何もしない
            'または　ldファイルIDが前回値と異なる場合にはAreaをldファイルにコメントとして出力し、ldファイルIDが同じ場合はAreaの前回値の判定に従う
            'Areaの判定のみだと、1つのAreaに複数のldファイルIDが記載されている場合に、先に記載されたldファイルにしかコメントが挿入されない
            If (tmp_Target_Area <> tmp_Target_Area_old) Or (tmp_LDFileID_old <> tmp_TargetLDFileID) Then
                tmp_OutputArea = vbCrLf & COMMENT_PREFIX_COMMON & tmp_Target_Area & COMMENT_POSFIX_COMMON & vbCrLf
                tmp_Target_Area_old = tmp_Target_Area
            Else
                tmp_OutputArea = ""
            End If
            
            'メモリブロック名列のテキストデータをメモリブロック名データに格納する
            tmp_MemoryName = Sheet_MemoryMap.Cells(tmp_RowIndex_MemoryName, ColIndex_MemoryName).Text

            '開始アドレス列のテキストデータを開始アドレスデータに格納する
            tmp_MemoryAddr_Start = Sheet_MemoryMap.Cells(tmp_RowIndex_MemoryName, ColIndex_MemoryAddr_Start).Text

            'サイズ列のテキストデータをサイズデータに格納する
            tmp_MemorySize = Sheet_MemoryMap.Cells(tmp_RowIndex_MemoryName, ColIndex_MemorySize).Text
            tmp_MemorySize = Convert_Memory_Size(tmp_MemorySize)

            'メモリ種別列のテキストデータをメモリ種別データに格納する
            tmp_MemoryCategory = Sheet_MemoryMap.Cells(tmp_RowIndex_MemoryName, ColIndex_MemoryCategory).Text

            'メモリブロック名～ORIGINとの間にインデントをつけて見やすく調整する
            'ここでエラーが出たら、第2引数を第1引数の値より大きくなるように変更すると直ると思う
            tmp_MemoryName = Adjust_Indents(tmp_MemoryName, INDENTS_MEMORY2ORIGIN)
            
            '出力データ(メモリ)に「メモリブロック名」「開始アドレス」「サイズ」「メモリ種別」を整形して格納する
            '現在参照しているメモリのldファイルIDを、ldファイルリストから探索し、ID毎に出力データを振り分ける
            For i = INDEX_START_ARRAY To NumberLD
                If LDList(i).LDFileID = tmp_TargetLDFileID Then
                    'ldファイルへの出力データ（メモリ）にメモリ定義を格納する
                    LDList(i).Output_Memory = LDList(i).Output_Memory & tmp_OutputArea & INDENT & tmp_MemoryName & ORIGIN & tmp_MemoryAddr_Start & LENGTH & tmp_MemorySize & MEMORY_CATEGORY_PREFIX & tmp_MemoryCategory & MEMORY_CATEGORY_POSTFIX & vbCrLf
                    
                    'ldファイルIDの前回値を更新する
                    tmp_LDFileID_old = tmp_TargetLDFileID
                End If
            Next
            
            'メモリインデックスをインクリメントし、次のループでメモリリストの配列のインデックス番目の要素を入れる
            tmp_Memoryindex = tmp_Memoryindex + 1
        End If
        
        'メモリブロック名行をインクリメントし次のセルを参照する
        tmp_RowIndex_MemoryName = tmp_RowIndex_MemoryName + 1
    Loop
End Sub

'/****************************************************************************************************
'/* 概要   | 引数で渡された行位置のフォーマットを確認し、
'/*        | 確認結果を戻り値として返す、フォーマット不正の場合はTrueを返す
'/****************************************************************************************************
Public Function Row_Format_Checker(rowIndex) As Boolean
    '既定値はFalse
    Row_Format_Checker = False
    
    'メモリブロック名の記載状態で処理を分岐する
    'メモリブロック名に記載がある場合
    If Get_MergeCells_Text(rowIndex, ColIndex_MemoryName) <> "" Then
        '開始アドレスを確認し記載がない場合、フォーマット不正と判断し
        '開始アドレスの記載がないことを示すエラーメッセージを設定する
        If (Get_MergeCells_Text(rowIndex, ColIndex_MemoryAddr_Start) = "") Then
            Row_Format_Checker = True
            Error_Message_Text = START_ADDRESS_BLANK
            Exit Function
        End If

        'サイズを確認し記載がない場合、フォーマット不正と判断し
        'サイズの記載がないことを示すエラーメッセージを設定する
        If (Get_MergeCells_Text(rowIndex, ColIndex_MemorySize) = "") Then
            Row_Format_Checker = True
            Error_Message_Text = SIZE_BLANK
            Exit Function
        End If
        
        'メモリ種別を確認し記載がない場合、フォーマット不正と判断し
        'メモリ種別の記載がないことを示すエラーメッセージを設定する
        If (Get_MergeCells_Text(rowIndex, ColIndex_MemoryCategory) = "") Then
            Row_Format_Checker = True
            Error_Message_Text = MEMORY_CATEGORY_BLANK
            Exit Function
        End If

    'メモリブロック名に記載がない場合
    Else
        '開始アドレス/サイズ/メモリ種別のいずれかに記載がある場合
        'メモリブロック名の記載がないことを示すエラーメッセージを設定する
        If (Get_MergeCells_Text(rowIndex, ColIndex_MemoryAddr_Start) <> "") Or (Get_MergeCells_Text(rowIndex, ColIndex_MemorySize) <> "") Or (Get_MergeCells_Text(rowIndex, ColIndex_MemoryCategory) <> "") Then
            Row_Format_Checker = True
            Error_Message_Text = MEMORY_NAME_BLANK
        End If
    End If
End Function

'/**************************************************************************************************************
'/* 概要   | 結合セルのテキストを取得する
'/*        | 第1引数の行位置、第2引数の列位置の位置に存在するセルが結合セルかをチェックし
'/*        | 結合セルであればその結合セルのテキストを取得し、結合セルでない場合
'/*        | そのセルのテキストを取得し返す
'/**************************************************************************************************************
Public Function Get_MergeCells_Text(row_Index, col_Index) As String
    If Sheet_MemoryMap.Cells(row_Index, col_Index).MergeCells Then
        Get_MergeCells_Text = Sheet_MemoryMap.Cells(row_Index, col_Index).MergeArea(1, 1).Text
    Else
        Get_MergeCells_Text = Sheet_MemoryMap.Cells(row_Index, col_Index).Text
    End If
End Function

'/**************************************************************************************************************
'/* 概要   | DEFAULTS{}内に定義する固定領域のデータをエクセルファイルから取得する
'/*        | Output_Constに出力するデータを格納するので、デバッグ時はOutput_Constに着目すると良いかもしれない
'/**************************************************************************************************************
Public Sub Get_ConstData()
    '内部変数の宣言
    Dim tmp_ConstName
    Dim tmp_ConstData
    Dim tmp_RowIndex_Const
    Dim tmp_TargetLDFileID          '固定領域を定義するldファイルID
    Dim i
    
    For i = INDEX_START_ARRAY To NumberLD
        LDList(i).Output_Const = ""
    Next
    
    '内部変数を初期化する
    tmp_RowIndex_Const = RowIndex_TopConst 'メモリブロック名行インデックスに入力エリア開始行インデックスを代入する
    
    '設定シートから固定領域のラベルとサイズを取得する
    Do Until InStr(Sheet_Setting.Cells(tmp_RowIndex_Const, COLUM_B).Text, "[STATIC_FIXED_AREA_END]") > 0    'B列の最終行を示す[STATIC_FIXED_AREA_END]を見つけるまで、B列の各セルのデータを比較する(ループ)'
        '参照したメモリを配置するldファイルIDを取得する
        tmp_TargetLDFileID = Target_LDFile_Const(tmp_RowIndex_Const)
        
        'セルの内容を取得する
        tmp_ConstName = Sheet_Setting.Cells(tmp_RowIndex_Const, ColIndex_ConstName).Text 'Label列の情報を取得する
        tmp_ConstData = Sheet_Setting.Cells(tmp_RowIndex_Const, ColIndex_ConstData).Text 'サイズ列の情報を取得する
        
        'Label名～"="との間にインデントをつけて見やすく調整する
        'ここでエラーが出たら、第2引数を第1引数の値より大きくなるように変更すると直ると思う
        tmp_ConstName = Adjust_Indents(tmp_ConstName, INDENTS_CONST2VALUE)
        
        '固定領域データをldファイル出力形式に整形し、出力文字列に格納する
        For i = INDEX_START_ARRAY To NumberLD
            If LDList(i).LDFileID = tmp_TargetLDFileID Then
                LDList(i).Output_Const = LDList(i).Output_Const & INDENT & tmp_ConstName & EQUAL & tmp_ConstData & vbCrLf
            End If
        Next
        
        '固定領域設定の次の行を参照させる
        tmp_RowIndex_Const = tmp_RowIndex_Const + 1
    Loop
End Sub

'/**************************************************************************************************************
'/* 概要   | SECTIONS{}内に定義するメモリ領域のデータをエクセルファイルから取得する
'/*        | Output_Sectionに出力するデータを格納するので、デバッグ時はOutput_Constに着目すると良いかもしれない
'/**************************************************************************************************************
Public Sub Get_SectionData()
    Dim tmp_SectionIndex As Integer                     'セクションインデックス
    Dim tmp_RowIndex_SectionName As Integer             'セクション名の行インデックス
    Dim tmp_OutputMemoryName                            '出力データに書き込むメモリ名
    Dim tmp_OutputSection As String
    Dim tmp_OutputElement As String
    Dim tmp_OutputSectionCategory As String
    Dim tmp_OutputComment As String
    Dim tmp_Target_Area                                 'Area
    Dim tmp_Target_Area_old                             'Areaの前回値
    Dim tmp_OutputArea                                  'Areaの出力データ
    Dim tmp_Breakline                                   'セクションの定義先のメモリが異なる場合、見やすくするために改行したいので、そのための出力データ
    Dim tmp_LDFileID_old                                'ldファイルIDの前回値
    Dim tmp_OutputString As String                      '出力文字列
    Dim i
    
    'Eraseでどこまで初期化してくれるのかわからなかったため、念のためで初期化している。
    '不要と分かれば削除してほしい
    For i = INDEX_START_ARRAY To NumberLD
        LDList(i).Output_Section = ""
    Next
    
    '内部変数を初期化する(Write前にReadするものを初期化する)
    tmp_SectionIndex = 1                                    'セクションインデックスを初期化する(セクションは1つ以上必ず記載されていると想定し、1で初期化する)
    tmp_RowIndex_SectionName = RowIndex_TopMemoryMap        'セクション名行インデックスに入力エリア開始行インデックスを代入する
    tmp_Target_Area_old = ""                            'Areaの前回値をブランクで初期化する
    tmp_LDFileID_old = ""                                   'ldファイルIDの前回値をブランクで初期化する
    
    'セクション名列（記入領域）の先頭行からメモリマップ定義シートの最終行までセクション名が記載されているセルを全て探索する
    Do Until tmp_RowIndex_SectionName > Rowindex_EndRow
        'セル結合しているため空白セルを無視し何か記載しているセルにはセクション名が記載されていると判断する
        If Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_SectionName).Text <> "" Then
            'Area、、ldファイルID、メモリ名、セクション名、属性、セクション種別、メモリ容量算出除外設定、コメントを取得する
            tmp_Target_Area = Target_Area(tmp_RowIndex_SectionName)
            '要素数の変更
            ReDim Preserve SectionList(tmp_SectionIndex)
            'Excel上、LDファイルIDは廃止するが、VBA処理内部では0固定とする
            'SectionList(tmp_SectionIndex).LDFileID = Target_LDFile(tmp_RowIndex_SectionName)
            SectionList(tmp_SectionIndex).LDFileID = 0
            SectionList(tmp_SectionIndex).Memory = Target_Memory(tmp_RowIndex_SectionName)
            SectionList(tmp_SectionIndex).Section_Name = Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_SectionName).Text
            SectionList(tmp_SectionIndex).Start_Expression = Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_SectionStartExpression).Text
            SectionList(tmp_SectionIndex).Attributes = Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_SectionAttributes).Text
            SectionList(tmp_SectionIndex).Contents = Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_SectionContents).Text
            SectionList(tmp_SectionIndex).Section_Category = Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_SectionCategory).Text
            SectionList(tmp_SectionIndex).Comment = Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_Comment).Text
            
            'Areaをコメントに記載する
            '現在参照しているメモリのAreaと前回値を比較し､異なる場合はAreaをldファイルにコメントとして出力し、異なる場合は何もしない
            'または　ldファイルIDが前回値と異なる場合にはAreaをldファイルにコメントとして出力し、ldファイルIDが同じ場合はAreaの前回値の判定に従う
            'Areaの判定のみだと、1つのAreaに複数のldファイルIDが記載されている場合に、先に記載されたldファイルにしかコメントが挿入されない
            If (tmp_Target_Area <> tmp_Target_Area_old) Or (tmp_LDFileID_old <> SectionList(tmp_SectionIndex).LDFileID) Then
                tmp_OutputArea = COMMENT_PREFIX_COMMON & tmp_Target_Area & COMMENT_POSFIX_COMMON & vbCrLf
                tmp_Target_Area_old = tmp_Target_Area
            Else
                tmp_OutputArea = ""
            End If
            
            tmp_OutputSection = SectionList(tmp_SectionIndex).Section_Name
            
            tmp_OutputElement = "" '初期化
            If SectionList(tmp_SectionIndex).Start_Expression <> "" Then
                tmp_OutputElement = SectionList(tmp_SectionIndex).Start_Expression & " "
            End If
            If SectionList(tmp_SectionIndex).Attributes <> "" Then
                tmp_OutputElement = tmp_OutputElement & SectionList(tmp_SectionIndex).Attributes & " "
            End If
            If SectionList(tmp_SectionIndex).Contents <> "" Then
               tmp_OutputElement = Adjust_Indents(tmp_OutputElement, INDENTS_ELEMENT32MEMORY) & " : " & SectionList(tmp_SectionIndex).Contents
            Else
               tmp_OutputElement = Adjust_Indents(tmp_OutputElement, INDENTS_ELEMENT32MEMORY) & " :"
            End If

            'セクションカテゴリが入力されている場合、コメント修飾「 /*------ FUNCTYPE:xxxx ------*/」を追加する
            'セクションカテゴリが入力されていない場合はブランクで初期化する(出力部を条件分岐させたくないため)
            If SectionList(tmp_SectionIndex).Section_Category <> "" Then
                tmp_OutputSectionCategory = SECTION_CATEGORY_PREFIX & SectionList(tmp_SectionIndex).Section_Category & SECTION_CATEGORY_POSTFIX
            Else
                tmp_OutputSectionCategory = ""
            End If

            'コメント部分が入力されている場合には、メモリブロック名とコメント出力部を整形する
            'メモリブロック名にはインデントを追加する。コメント部には「/*------  ------*/」を追加する
            'コメントが入力されていない場合はブランクで初期化する(出力部を条件分岐させたくないため)
            If SectionList(tmp_SectionIndex).Comment <> "" Then
                tmp_OutputMemoryName = tmp_OutputMemoryName
                tmp_OutputComment = COMMENT_PREFIX_COMMON & SectionList(tmp_SectionIndex).Comment & COMMENT_POSFIX_COMMON
            Else
                tmp_OutputComment = ""
            End If

            'セクションを配置するメモリブロックを取得する
            'メモリブロック名列から探索し、探索結果に応じて、内部データに保持する
            '内部保持データは、前回値と同じ場合は「.」を保持し、異なる場合はメモリブロック名列に記載されたメモリブロック名を保持する
            'また、前回値と同じ場合はldファイル内の出力データを続きの行で出力するが、異なる場合は改行する（見やすくするために）。
            If ((tmp_SectionIndex > 1) And (SectionList(tmp_SectionIndex).Memory = SectionList(tmp_SectionIndex - 1).Memory)) And (tmp_LDFileID_old = SectionList(tmp_SectionIndex).LDFileID) Then
                tmp_OutputMemoryName = "."
                tmp_Breakline = ""
            Else
                tmp_OutputMemoryName = SectionList(tmp_SectionIndex).Memory
                tmp_Breakline = vbCrLf
            End If

            '出力データ(セクション)にArea、メモリブロック名、セクション名、属性、セクション種別、コメントを整形して格納する
            '現在参照しているメモリのldファイルIDを、ldファイルリストから探索し、ID毎に出力データを振り分ける
            For i = INDEX_START_ARRAY To NumberLD
                If (LDList(i).LDFileID = SectionList(tmp_SectionIndex).LDFileID) Then
                    If (InStr(tmp_OutputSection, "#define") Or InStr(tmp_OutputSection, "#include")) Then 'セクション名に#define又は#includeが含まれる場合
                        '#define又は#includeの記述をそのまま出力する
                        tmp_OutputString = AddIndentSpace & tmp_OutputSection
                        If StrComp(tmp_OutputComment, "") <> 0 Then                                       'コメントが空白以外の場合
                            tmp_OutputString = tmp_OutputString & AddCommentSpace(tmp_OutputString) & tmp_OutputComment & vbCrLf
                        Else
                            tmp_OutputString = tmp_OutputString & vbCrLf
                        End If
                    Else                                                                                  'セクション名に#define又は#includeが含まれない場合
                        tmp_OutputString = AddIndentSpace & tmp_OutputSection
                        If StrComp(tmp_OutputElement, "") <> 0 Then                                       '属性が空白以外の場合
                            tmp_OutputString = tmp_OutputString & AddElementSpace(tmp_OutputString) & tmp_OutputElement
                        End If
                        tmp_OutputString = tmp_OutputString & AddFixAddressSpace(tmp_OutputString) & "> " & tmp_OutputMemoryName
                        If StrComp(tmp_OutputSectionCategory, "") <> 0 Then                               'セクション種別が空白以外の場合
                            tmp_OutputString = tmp_OutputString & AddCommentSpace(tmp_OutputString) & tmp_OutputSectionCategory
                        End If
                        If StrComp(tmp_OutputComment, "") <> 0 Then                                       'コメントが空白以外の場合
                            tmp_OutputString = tmp_OutputString & AddCommentSpace(tmp_OutputString) & tmp_OutputComment & vbCrLf
                        Else
                            tmp_OutputString = tmp_OutputString & vbCrLf
                        End If
                        tmp_OutputString = tmp_OutputArea & tmp_OutputString
                    End If
                    'ldファイルへの出力データ（セクション）にメモリ定義を格納する
                    LDList(i).Output_Section = LDList(i).Output_Section & tmp_Breakline & tmp_OutputString

                    'ldファイルIDの前回値を更新する
                    tmp_LDFileID_old = LDList(i).LDFileID
                End If
            Next
            
            'メモリインデックスをインクリメントし、次のループでメモリリストの配列のインデックス番目の要素を入れる
            tmp_SectionIndex = tmp_SectionIndex + 1
        End If
        'メモリブロック名行をインクリメントし、次のセルを参照する
        tmp_RowIndex_SectionName = tmp_RowIndex_SectionName + 1
    Loop
End Sub

'/**************************************************************************************************************
'/* 概要   | セクション定義の記述開始列を合わせるためのスペース量を算出し、文字列として出力する
'/**************************************************************************************************************
Private Function AddIndentSpace() As String
    AddIndentSpace = Space(4)
End Function

Private Function AddElementSpace(ByVal strPreString) As String
    If (35 - LenB(StrConv(strPreString, vbFromUnicode))) > 0 Then                   '35文字未満の場合
        AddElementSpace = Space(35 - LenB(StrConv(strPreString, vbFromUnicode)))
    Else                                                    '35文字以上の場合
        AddElementSpace = Space(1)
    End If
End Function

Private Function AddFixAddressSpace(ByVal strPreString) As String
    If (76 - LenB(StrConv(strPreString, vbFromUnicode))) > 0 Then                   '76文字未満の場合
        AddFixAddressSpace = Space(76 - LenB(StrConv(strPreString, vbFromUnicode)))
    Else                                                    '76文字以上の場合
        AddFixAddressSpace = Space(1)
    End If
End Function

Private Function AddCommentSpace(ByVal strPreString) As String
    If (98 - LenB(StrConv(strPreString, vbFromUnicode))) > 0 Then                  '98文字未満の場合
        AddCommentSpace = Space(98 - LenB(StrConv(strPreString, vbFromUnicode)))
    Else                                                    '98文字以上の場合
        AddCommentSpace = Space(1)
    End If
End Function

'/**************************************************************************************************************
'/* 概要   | 引数で渡された行のArea名を取得し、戻り値として返す
'/*        | 引数で渡された行のArea列を参照する、空白なら上の行を参照し空白セル以外を探索する、
'/*        | 空白セル以外ならArea名と判断し、戻り値でArea名を返す
'/**************************************************************************************************************
Function Target_Area(ByVal arg_RowIndex_MemoryName As Integer) As String
    Dim tmp_RowIndex_MemoryName As Integer
    
    tmp_RowIndex_MemoryName = arg_RowIndex_MemoryName
    
    Do Until Sheet_MemoryMap.Cells(tmp_RowIndex_MemoryName, ColIndex_Area).Text <> ""
        tmp_RowIndex_MemoryName = tmp_RowIndex_MemoryName - 1
    Loop
    
    Target_Area = Sheet_MemoryMap.Cells(tmp_RowIndex_MemoryName, ColIndex_Area).Text
End Function

'/**************************************************************************************************************
'/* 概要   | 引数で渡された行のメモリブロック名を取得し、戻り値として返す
'/*        | 引数で渡された行のメモリブロック列を参照する、空白なら上の行を参照し空白セル以外を探索する、
'/*        | 空白セル以外ならメモリブロック名と判断し、戻り値でメモリブロック名を返す
'/**************************************************************************************************************
Function Target_Memory(ByVal arg_RowIndex_SectionName As Integer) As String
    Dim tmp_RowIndex_SectionName As Integer
    
    tmp_RowIndex_SectionName = arg_RowIndex_SectionName
    
    Do Until Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_MemoryName).Text <> ""
        tmp_RowIndex_SectionName = tmp_RowIndex_SectionName - 1
    Loop
    
    Target_Memory = Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_MemoryName).Text
End Function

'/**************************************************************************************************************
'/* 概要   | 引数で渡された行のldファイル名を取得し、戻り値として返す
'/*        | 引数で渡された行のldファイルID列を参照する、空白なら上の行を参照し空白セル以外を探索する、
'/*        | 空白セル以外ならldファイル名と判断し、戻り値でldファイル名を返す
'/**************************************************************************************************************
Function Target_LDFile(ByVal arg_RowIndex_SectionName As Integer) As String
    Dim tmp_RowIndex_SectionName As Integer
    
    tmp_RowIndex_SectionName = arg_RowIndex_SectionName
    
    Do Until Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_MemoryLDFileID).Text <> ""
        tmp_RowIndex_SectionName = tmp_RowIndex_SectionName - 1
    Loop
    
    Target_LDFile = Sheet_MemoryMap.Cells(tmp_RowIndex_SectionName, ColIndex_MemoryLDFileID).Text
End Function

'/**************************************************************************************************************
'/* 概要   | 引数で渡された行のldファイルIDを取得し、戻り値として返す
'/*        | 引数で渡された行のldファイルID列を参照する、空白なら上の行を参照し空白セル以外を探索する、
'/*        | 空白セル以外ならldファイルIDと判断し、戻り値でldファイルIDを返す
'/**************************************************************************************************************
Function Target_LDFile_Const(ByVal arg_RowIndex_SectionName As Integer) As String
    Dim tmp_RowIndex_SectionName As Integer
    
    tmp_RowIndex_SectionName = arg_RowIndex_SectionName
    
    Do Until Sheet_Setting.Cells(tmp_RowIndex_SectionName, ColIndex_SettingLDFileID).Text <> ""
        tmp_RowIndex_SectionName = tmp_RowIndex_SectionName - 1
    Loop
    
    Target_LDFile_Const = Sheet_Setting.Cells(tmp_RowIndex_SectionName, ColIndex_SettingLDFileID).Text
End Function

'/**************************************************************************************************************
'/* 概要   | 第1引数の文字列に、第2引数のインデント数になるようにスペースを加える
'/*        | 第2引数で渡された値＞第1引数の文字数　の場合エラーとなるので、引数の値に十分な値を設定すること
'/**************************************************************************************************************
Function Adjust_Indents(ByVal arg_String As String, arg_NumberIndent As Integer) As String
    Dim tmp_NeededNumberIndents       '必要なインデント数
    Dim tmp_loopcnt_len_string        'インデントを加える際に使用したループのインデックス
    Dim tmp_len_string
    
    '引数でインデント数を渡され､そのインデント数から調整する対象の文字数を引く｡
    'そうすると、必要なインデント数が求められる
    tmp_len_string = arg_NumberIndent - Len(arg_String)
        
    'ループ文で、必要なインデント数ループし、ループごとにスペースを足していく
    'ブラッシュアップ：愚直な処理になっているので、スマートなやり方があれば変更してほしい
    For tmp_loopcnt_len_string = 0 To tmp_len_string
        arg_String = arg_String & " "
    Next
    
    '戻り値にインデントが追加された文字列を格納する
    Adjust_Indents = arg_String
End Function

'/****************************************************************************************************
'/* 概要   | エクセルから取得したデータをldファイルに書き込む
'/*        | ldファイルはこのツールと同じ階層に出力する
'/*        | 階層を変えたい場合は ThisWorkbook.Path を別のパスに書き換えればよい
'/*        | 書き込めませんとエラーが出たときは、たぶんファイルをエディタで開いているか階層が深すぎる
'/****************************************************************************************************
'取得したデータをld出力する
Public Sub Create_LD()
    Dim tmp_File_Path
    Dim tmp_FSO
    Dim tmp_oLog
    Dim i
    
    'ファイルダイアログから保存先のフォルダを選択し、選択したフォルダのパスを取得する
    '保存先のフォルダのパスが取得できなかった場合、処理を行わない
    If (Application.FileDialog(msoFileDialogFolderPicker).Show <> 0) Then
    
        tmp_File_Path = Application.FileDialog(msoFileDialogFolderPicker).SelectedItems(1)
    
        For i = INDEX_START_ARRAY To NumberLD
            'ldファイルを生成する
            Set tmp_FSO = CreateObject("Scripting.FileSystemObject")                                        'ファイルを生成するためのおまじない
            Set tmp_oLog = tmp_FSO.CreateTextFile(tmp_File_Path & "\" & LDList(i).LDFileName & ".ld")      'エクセルのディレクトリにldファイルを生成する
            
            'ヘッダテキストの出力
            tmp_oLog.WriteLine (HEADER_COMENT_TOP)                               ' ファイルコメントヘッダを出力する
            tmp_oLog.WriteLine (Output_FileName((LDList(i).LDFileName) & ".ld")) ' ファイル名情報を出力する
            tmp_oLog.WriteLine (HEADER_COMENT_CONTENTS)                          ' コンテンツ情報を出力する
            tmp_oLog.WriteLine (HEADER_COMENT_COMPILER)                          ' コンパイラ情報を出力する
            tmp_oLog.WriteLine (HEADER_COMENT_CPU)                               ' CPU情報を出力する
            tmp_oLog.WriteLine (HEADER_COMENT_NOTE)                              ' Note情報を出力する
            tmp_oLog.WriteLine (HEADER_COMENT_DOTLINE)                           ' 点線を出力する
            Call Output_History(LDList(i).LDFileID, tmp_oLog)                    ' History行を成形出力する
            tmp_oLog.WriteLine (HEADER_COMENT_LINE)                              ' 分割線を出力する
            tmp_oLog.WriteLine (HEADER_COMENT_COPYRIGHT)                         ' コピーライト情報を出力する
            tmp_oLog.WriteLine (HEADER_COMENT_LINE)                              ' 分割線を出力する
            tmp_oLog.WriteLine (HEADER_COMENT_END)                               ' ヘッダコメント終了情報を出力する

            '計算式の出力
            tmp_oLog.WriteLine (vbCrLf & "/* *** MEMORY CATEGORY TOP *** */")
            Call Output_CalculationFormula(TABLE_MEMORY_ROMRAM_CALC_FORMULA_TOP, TABLE_MEMORY_ROMRAM_CALC_FORMULA_END, tmp_oLog)
            tmp_oLog.WriteLine ("/* *** MEMORY CATEGORY END *** */" & vbCrLf)
            
            tmp_oLog.WriteLine ("/* *** APPLICATION CATEGORY TOP *** */")
            Call Output_CalculationFormula(TABLE_MEMORY_FUNCTION_CALC_FORMULA_TOP, TABLE_MEMORY_FUNCTION_CALC_FORMULA_END, tmp_oLog)
            tmp_oLog.WriteLine ("/* *** APPLICATION CATEGORY END *** */" & vbCrLf)
            
            'メモリ領域の出力
            tmp_oLog.WriteLine (HEADER_MEMORY)                                   ' "MEMORY {"を出力する
            tmp_oLog.WriteLine (LDList(i).Output_Memory)                         ' MEMORY領域に記載する要素を出力する
            tmp_oLog.WriteLine (FOOTER_COMMON & vbCrLf)                          ' "}"を出力する
            
            'セクション領域の出力
            tmp_oLog.WriteLine (HEADER_COMMENT_SECTION_0)                        ' セクション定義開始を示すコメントを出力する
            tmp_oLog.WriteLine (HEADER_COMMENT_SECTION_1)                        ' セクション定義開始を示すコメントを出力する
            tmp_oLog.WriteLine (HEADER_COMMENT_SECTION_2)                        ' セクション定義開始を示すコメントを出力する
    
            tmp_oLog.WriteLine (HEADER_SECTION)                                  ' "SECTIONS {"を出力する
            tmp_oLog.WriteLine (LDList(i).Output_Section)                        ' SECTIONS部分に記載する要素を出力する
            
            'MICROSAR OSのためのシンボルを暫定的に強制的に出力する
            'ボタンとかあったほうがいいか、など検討したいが、全体的な設計を検討する余裕がないため強制的に出力させている
            'ブラッシュアップ：BSW固有で文字列を出力する仕組み
            Call Output_OutSetting_Manager(LDList(i).LDFileID, tmp_oLog)
            
            tmp_oLog.WriteLine (FOOTER_COMMON & vbCrLf)     ' "}"を出力する
        
            'ldファイルをクローズし、オブジェクトとして使用したデータを開放する
            Call tmp_oLog.Close
            Set tmp_oLog = Nothing
            Set tmp_FSO = Nothing
        Next
    End If
End Sub

'/****************************************************************************************************
'/* 概要   | 第1引数で渡されたファイル名ヘッダコメントのフォーマットにあった文に成形し返す
'/****************************************************************************************************
Public Function Output_FileName(fileName As String) As String
    Dim fileName_Byte As Integer                                                    '成形したファイル名のバイト数
    
    Output_FileName = HEADER_COMENT_FILENAME_TOP & fileName
     
    fileName_Byte = LenB(StrConv(Output_FileName, vbFromUnicode))                   '成形した文のバイト数を取得する
        
    If (fileName_Byte < HEADER_COMENT_BYTE) Then                                    '成形した文が規定のバイト数を超えていないか確認する
        Do Until fileName_Byte = HEADER_COMENT_BYTE
            Output_FileName = Output_FileName & " "
            fileName_Byte = LenB(StrConv(Output_FileName, vbFromUnicode))
        Loop
            Output_FileName = Output_FileName & HEADER_COMENT_FILENAME_END
    Else
        Output_FileName = Output_FileName & HEADER_COMENT_FILENAME_END
    End If
End Function

'/****************************************************************************************************
'/* 概要   | 第1引数で渡されたファイル名の改訂履歴を第2引数のファイルに出力する
'/****************************************************************************************************
Public Sub Output_History(fileID As String, tmp_oLog)
    Dim find_Range As Range
    Dim num
    
    Set find_Range = Sheet_Revision.Columns(COLUM_D).Find(What:="日付", LookIn:=xlValues, LookAt:=xlWhole)
    
    If Not find_Range Is Nothing Then
        Call SetDefault_History_List(fileID, find_Range.Row)  '改訂履歴のリストを初期化する
        Call SetValue_History_List(fileID, find_Range.Row)    '改訂履歴のリストに要素を追加する
            
        If (0 < UBound(History_List)) Then                    '改訂履歴のリストにアイテムがある場合のみ処理を続行する
            For num = 1 To UBound(History_List)               '改訂履歴のリストのアイテムすべてを対象ファイルに出力する
                tmp_oLog.WriteLine (History_List(num))
            Next
        Else
            tmp_oLog.WriteLine (HEADER_COMENT_HISTORY)
        End If
    End If
End Sub

'/****************************************************************************************************
'/* 概要   | 改訂履歴のリストを初期化し、改訂履歴シートの表から第1引数のファイル名と同じファイル名
'/*        | の項目の数までリストの配列数を変更する
'/*        | 第2引数は行の参照開始位置
'/****************************************************************************************************
Public Sub SetDefault_History_List(fileID As String, rowIndex As Integer)
    Dim macth_Conter As Integer                                                             'ファイル名一致のカウンタ
    Dim cell_fileID As String                                                               'ファイル名一致のカウンタ
    
    ReDim History_List(0)                                                                   '改訂履歴リストを初期化する
    
    macth_Conter = 0                                                                        'カウンタを初期値の0にする
    rowIndex = rowIndex + 1                                                                 '参照開始位置が列タイトルのためインクリメントする
    
    Do Until InStr(Sheet_Revision.Cells(rowIndex, COLUM_D).Text, "■") > 0                   'D列の最終行を示す「■」を見つけるまで、D列の各セルのデータを比較する(ループ)'
        If Sheet_Revision.Cells(rowIndex, COLUM_D).MergeCells Then                          '比較対象セルが結合セルの場合、ファイル名の読み込みができない場合があるため
            cell_fileID = Sheet_Revision.Cells(rowIndex, COLUM_D).MergeArea(1, 1).Text      '結合セルの場合はMergeAreaからファイル名を取得する
        Else
            cell_fileID = Sheet_Revision.Cells(rowIndex, COLUM_D).Text                      '結合セルでない場合はCellsからファイル名を取得する
        End If
          
        'Excel上、LDファイルIDは廃止するが、VBA処理内部では0固定とする
        If cell_fileID <> "" Then
            cell_fileID = 0
        End If
          
        If fileID = cell_fileID Then                                                        '引数のファイル名と比較対象のセルのファイル名が一致する場合
            macth_Conter = macth_Conter + 1                                                 'カウンタをインクリメントする
        End If
        
        rowIndex = rowIndex + 1                                                             '行参照位置をインクリメントする
    Loop
    
    ReDim History_List(macth_Conter)                                                        '改訂履歴のリストの配列数をカウンタの数まで用意する
End Sub

'/****************************************************************************************************
'/* 概要   | 改訂履歴のリストに第1引数と同じファイル名の改訂履歴を
'/*        | ヘッダテキストのフォーマットに成形した状態で格納する
'/*        | 第2引数は行の参照開始位置
'/****************************************************************************************************
Public Sub SetValue_History_List(fileID As String, rowIndex As Integer)
    Dim history_Byte As Integer                                                             '成形した改訂履歴のバイト数
    Dim macth_Conter As Integer                                                             'ファイル名一致のカウンタ
    Dim cell_fileID As String                                                               'ファイル名一致のカウンタ
    Dim history_value As String                                                             '成形した改訂履歴の文章
    
    macth_Conter = 0                                                                        'カウンタを初期値の0にする
    rowIndex = rowIndex + 1                                                                 '参照開始位置が列タイトルのためインクリメントする

    '改訂履歴の対象の行から必要なデータを取得しヘッダテキストのフォーマットにあった文章に成形する
    Do Until InStr(Sheet_Revision.Cells(rowIndex, COLUM_D).Text, "■") > 0                   'D列の最終行を示す「■」を見つけるまで、D列の各セルのデータを比較する(ループ)'
        If Sheet_Revision.Cells(rowIndex, COLUM_D).MergeCells Then                          '比較対象セルが結合セルの場合、ファイル名の読み込みができない場合があるため
            cell_fileID = Sheet_Revision.Cells(rowIndex, COLUM_D).MergeArea(1, 1).Text      '結合セルの場合はMergeAreaからファイル名を取得する
        Else
            cell_fileID = Sheet_Revision.Cells(rowIndex, COLUM_D).Text                      '結合セルでない場合はCellsからファイル名を取得する
        End If
    
        'Excel上、LDファイルIDは廃止するが、VBA処理内部では0固定とする
        If cell_fileID <> "" Then
            cell_fileID = 0
        End If
        
        If fileID = cell_fileID Then                                                        '引数のファイル名と比較対象のセルのファイル名が一致する場合
            macth_Conter = macth_Conter + 1                                                 'カウンタをインクリメントする
            With Sheet_Revision                                                             '改訂履歴の表から必要なデータを取得する
                history_value = .Cells(rowIndex, COLUM_D) & " " & .Cells(rowIndex, COLUM_E) & " " & .Cells(rowIndex, COLUM_F)
            End With
            
            If macth_Conter = 1 Then                                                        '対象ファイルの改訂履歴が複数ある場合最初のHistory行のみ行タイトルを設定する
                history_value = HEADER_COMENT_HISTORY_TOP & history_value
            Else
                history_value = HEADER_COMENT_SUBHISTORY_TOP & history_value
            End If
                    
            history_Byte = LenB(StrConv(history_value, vbFromUnicode))                      '生成した文のバイト数を取得する
        
            If (history_Byte < HEADER_COMENT_BYTE) Then                                     '成形した文が規定のバイト数を超えていないか確認する
                Do Until history_Byte = HEADER_COMENT_BYTE                                  '超えていない場合は、既定のバイト数になるまで空白文字を挿入する
                    history_value = history_value & " "
                    history_Byte = LenB(StrConv(history_value, vbFromUnicode))
                Loop
                
                history_value = history_value & HEADER_COMENT_HISTORY_END
            Else
                history_value = history_value & HEADER_COMENT_HISTORY_END
            End If
            
            History_List(macth_Conter) = history_value
        End If
        
        rowIndex = rowIndex + 1                                                             '行参照位置をインクリメントする
    Loop
End Sub

'/****************************************************************************************************
'/* 概要   | 設定シートのシンボル定義表から第1引数で渡されたldファイルID
'/*        | と同じldファイルIDを持つ行のデータを第2引数のファイルへの
'/*        | 出力を操作する関数
'/****************************************************************************************************
Public Sub Output_OutSetting_Manager(fileID As String, tmp_oLog)

    Dim find_Range As Range                                                                           '設定シートのldファイルID列のタイトルセル位置
    Dim rowIndex As Integer                                                                           '読み込み行位置
    Dim fileID_Range As Integer                                                                       '読み込んだldファイルの範囲
    
    Set find_Range = Sheet_OutSetting.Cells.Find(What:="[DEFINE_SYMBOL_TOP]", LookIn:=xlValues, LookAt:=xlWhole)
    
    If Not find_Range Is Nothing Then                                                                 'B列からldファイルIDタイトル位置を検索し見つかる場合のみ処理を続行する
        rowIndex = find_Range.Row + 2                                                                 '[DEFINE_SYMBOL_TOP]の2行下から読み込みを行う
    
        Do Until InStr(Sheet_OutSetting.Cells(rowIndex, COLUM_B).Text, "[DEFINE_SYMBOL_END]") > 0        'B列の最終行を示す[DEFINE_SYMBOL_END]を見つけるまで、B列の各セルのデータを比較する(ループ)
            If ("" <> Sheet_OutSetting.Cells(rowIndex, COLUM_B).Text) Then                            '第1引数で渡されたldファイルIDと同じldファイルIDの場合、行データの読み込みを行う
               If Sheet_OutSetting.Cells(rowIndex, COLUM_B).MergeCells Then                              '読み込み対象のldファイルIDの範囲を取得する
                    fileID_Range = Sheet_OutSetting.Cells(rowIndex, COLUM_B).MergeArea.Rows.count
               Else
                    fileID_Range = 1
               End If
               
               Call Output_Area(rowIndex, fileID_Range, tmp_oLog)                                     'BLOCK名の読み込みを行う
            Else
               rowIndex = rowIndex + 1
            End If
        Loop
    End If
End Sub

'/****************************************************************************************************
'/* 概要   | 設定シートのシンボル定義表から第1引数で渡された行位置から
'/*        | 第2引数で渡された行範囲までのBLOCK名を第3引数のファイルに出力し
'/*        | 出力したBLOCK名に属するサイズの出力を操作する関数
'/****************************************************************************************************
Public Sub Output_Area(rowIndex As Integer, fileID_Range As Integer, tmp_oLog)
    Dim lastRow As Integer                                              '読み込み終了行
    Dim area As String                                                  'BLOCK名
    Dim area_Range As Integer                                           '読み込んだBLOCK名の範囲
    
    lastRow = rowIndex + fileID_Range                                   '第1引数で渡された行位置から第2引数で渡された範囲を加算した位置を読み込み終了行とする

    Do Until rowIndex >= lastRow                                        '読み込み行位置が読み込み終了行以上になるまでBLOCK名を読み込み対象のファイルに出力する
        area = AREA_TOP & Sheet_OutSetting.Cells(rowIndex, COLUM_B).Text & AREA_END
        tmp_oLog.WriteLine (area)
        If Sheet_OutSetting.Cells(rowIndex, COLUM_B).MergeCells Then       'BLOCK名の範囲を取得する
             area_Range = Sheet_OutSetting.Cells(rowIndex, COLUM_B).MergeArea.Rows.count
        Else
             area_Range = 1
        End If
        
        Call Output_SettingValue(rowIndex, area_Range, tmp_oLog)        '取得したBLOCK名の範囲内の設定値の出力を行う
    Loop
End Sub

'/****************************************************************************************************
'/* 概要   | 設定シートのシンボル定義表から第1引数で渡された行位置から
'/*        | 第2引数で渡された行範囲までの設定値を第3引数のファイルに出力する関数
'/****************************************************************************************************
Public Sub Output_SettingValue(rowIndex As Integer, area_Range, tmp_oLog)
    Dim lastRow As Integer                      '読み込み終了位置
    Dim settingValue As String                  '設定値
    Dim area
    
    lastRow = rowIndex + area_Range             '第1引数で渡された行位置から第2引数で渡された範囲を加算した位置を読み込み終了行とする
    
    Do Until rowIndex >= lastRow                '読み込み行位置が読み込み終了行以上になるまで設定値の読み込み対象のファイルに出力する
        If Sheet_OutSetting.Cells(rowIndex, COLUM_D).Text <> "" Then
            area = SECTION_SPACE & Adjust_Indents(Sheet_OutSetting.Cells(rowIndex, COLUM_C).Text, 80) & Sheet_OutSetting.Cells(rowIndex, COLUM_D).Text
        Else
            area = SECTION_SPACE & Sheet_OutSetting.Cells(rowIndex, COLUM_C).Text
        End If
        tmp_oLog.WriteLine (area)
        rowIndex = rowIndex + 1
    Loop
    
    tmp_oLog.WriteLine ("")
End Sub

'/****************************************************************************************************
'/* 概要   | フォーマットが不正の場合に
'/*        | 引数で渡されたメッセージを
'/*        | エラーメッセージに表示する
'/****************************************************************************************************
' エラーメッセージを表示する。
Public Sub Show_Error_Messsage(message As String)
    'エラーメッセージを表示する
    MsgBox message, vbOKOnly, ERROR_TITLE
    
End Sub

'/****************************************************************************************************
'/* 概要   | メモリサイズ（length）を16進数4byte表記（0xXXXXXXXX）に変換する
'/****************************************************************************************************
Function Convert_Memory_Size(inputString) As String
    Dim regEx As Object, Matches  As Object, Match As Object
    Dim tmpString As String
    Dim tmpHexString As String
    Dim arrayIndex As Integer
    Dim tmpList() As String
    Dim HexConversion As String

    ReDim tmpList(Len(inputString))
    arrayIndex = 0

    Set regEx = CreateObject("VBScript.RegExp")
    With regEx
        .Pattern = "([0-9a-fA-FxX]+|[\K\M\+\-\*\/\(\)]+)"   'パターンを設定
        .IgnoreCase = False                                 '大文字と小文字を区別しないように設定
        .Global = True                                      '文字列全体を検索
    End With
    
    Set Matches = regEx.Execute(inputString)
    
    For Each Match In Matches
        If Mid(Match.Value, 1, 2) = "0x" Or Mid(Match.Value, 1, 2) = "0X" Then
            tmpList(arrayIndex) = Val("&H" & Mid(Match.Value, 3) & "&")
        Else
            tmpList(arrayIndex) = Match.Value
        End If
        arrayIndex = arrayIndex + 1
    Next Match
    
    For arrayIndex = LBound(tmpList) To UBound(tmpList)
        tmpString = tmpString & tmpList(arrayIndex)
    Next arrayIndex
    
    tmpString = Replace(tmpString, "K", "*1024")
    tmpString = Replace(tmpString, "M", "*1024*1024")
    
    tmpString = Evaluate(tmpString)
    tmpString = "0x" & Right("00000000" & Hex(tmpString), 8)
    
    Convert_Memory_Size = tmpString
End Function

'/****************************************************************************************************
'/* 概要   | メモリ計算式を作成する
'/****************************************************************************************************
Public Sub Output_CalculationFormula(keyItemTop As String, keyItemEnd As String, tmp_oLog)
    Dim cntRowIndex As Integer
    Dim cntColumnIndex As Integer
    Dim cntArrayIndex As Integer
    Dim i As Integer
    Dim find_Range As Range
    Dim tmpCalculation_Formula As String
    Dim tmpCalcBlock As String
    Dim tmpCalcBlockName As String
    Dim tmpCalcList() As String
    
    Set find_Range = Sheet_Setting.Cells.Find(What:=keyItemTop, LookIn:=xlValues, LookAt:=xlWhole)
    
    If Not find_Range Is Nothing Then
        '初期化
        cntRowIndex = find_Range.Row + 2
        cntArrayIndex = 0

        '配列の要素数を求める
        Do Until InStr(Sheet_Setting.Cells(cntRowIndex, find_Range.Column).Text, keyItemEnd) > 0
            cntRowIndex = cntRowIndex + 1
        Loop

        '配列の要素数確定
        ReDim tmpCalcList(cntRowIndex - find_Range.Row - 1)
        cntRowIndex = find_Range.Row + 2

        Do Until InStr(Sheet_Setting.Cells(cntRowIndex, find_Range.Column).Text, keyItemEnd) > 0
            cntColumnIndex = find_Range.Column
            tmpCalcBlockName = ""
            tmpCalculation_Formula = Sheet_Setting.Cells(cntRowIndex, cntColumnIndex).Text
            cntColumnIndex = cntColumnIndex + 1
            
            '行単位の計算式を作成
            Do Until InStr(Sheet_Setting.Cells(cntRowIndex, cntColumnIndex).Text, "") = 0
                If Sheet_Setting.Cells(cntRowIndex, cntColumnIndex).Text <> "" Then
                    If tmpCalcBlockName = "" Then
                        tmpCalcBlockName = Sheet_Setting.Cells(cntRowIndex, cntColumnIndex).Text
                    Else
                        tmpCalcBlockName = tmpCalcBlockName & " + " & Sheet_Setting.Cells(cntRowIndex, cntColumnIndex).Text
                    End If
                End If
                cntColumnIndex = cntColumnIndex + 1
            Loop
            
            '計算式がない場合、配列に空情報を格納
            If tmpCalculation_Formula = "" Then
                tmpCalcList(cntArrayIndex) = ""
            Else
                '配列に計算式を格納
                If tmpCalcBlockName = "" Then
                    If tmpCalculation_Formula <> "NA" Then
                        tmpCalculation_Formula = Adjust_Indents(tmpCalculation_Formula, INDENTS_FORMULA2FULL)
                        tmpCalcList(cntArrayIndex) = "/* " & tmpCalculation_Formula & " */"
                    End If
                Else
                    tmpCalculation_Formula = Adjust_Indents(tmpCalculation_Formula, INDENTS_FORMULA2LEFT)
                    tmpCalcBlockName = Adjust_Indents(tmpCalcBlockName, INDENTS_FORMULA2RIGHT)
                    tmpCalcList(cntArrayIndex) = "/* " & tmpCalculation_Formula & " = " & tmpCalcBlockName & " */"
                End If
            End If
            
            cntRowIndex = cntRowIndex + 1
            cntArrayIndex = cntArrayIndex + 1
        Loop
        
        'ldファイルに出力
        For i = LBound(tmpCalcList) To UBound(tmpCalcList)
            If "" <> tmpCalcList(i) Then
                tmp_oLog.WriteLine (tmpCalcList(i))
            End If
        Next i
    End If
End Sub
