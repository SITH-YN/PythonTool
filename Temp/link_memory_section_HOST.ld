/*""FILE COMMENT""*******************************************************************************************************/
/* File Name   : link_memory_section_HOST.ld                                                                            */
/* Contents    : スタートアップ機能 - HOST - リンカディレクティブ                                                       */
/* Compiler    : Green Hills コンパイラ                                                                                 */
/* CPU         : RH850/F1KM-S1/S4                                                                                       */
/* Note        : 編集許可                                                                                               */
/*----------------------------------------------------------------------------------------------------------------------*/
/* History     : 2023/08/07 PAD 木寺 新規作成                                                                           */
/*             : 2023/12/19 HISOL日比野 MIRM、PWSW用セクション追加                                                      */
/*             : 2023/12/21 HISOL橋倉 SPI 64bit版対応によるMEMBLOCK_CONST_DATA拡張暫定対応 不要コード削除時に見直し     */
/*             : 2023/12/22 PAD 木寺 MR,FH,WR,DL,APLOS用のセクションを追加                                              */
/*             : 2023/12/26 HISOL日比野 PWMDRV、LED用セクション追加                                                     */
/*             : 2024/01/09 PAD 木寺 ldファイルをS4マイコン向けに適切に再設計                                           */
/*             : 2024/01/17 HISOL小島 DBGS用セクション追加                                                              */
/*             : 2024/01/17 HISOL日比野 不要セクション削除(BTS7008,TLE92108,HEATER,SVS,THERMISTOR,VM)                   */
/*             : 2024/01/17 HISOL日比野 セクション追加(FLUSHH,CLUSTERIC,PWRDIST,PWRIN,PWHS)                             */
/************************************************************************************************************************/
/*                                                                                    Copyright(c)  AISIN SEIKI CO.,LTD */
/************************************************************************************************************************/
/*""FILE COMMENT END""***************************************************************************************************/

/* Prohibited_Section = .rosda_start,.rosdata,.D_SDATA,.rosda_end,.text,.syscall,.secinfo,.sda_start,.sdata,.sbss,.tdata,.sda_end */
/* Elim_From_Rst = .debug_info,.debug_abbrev,.debug_line,.debug_macinfo,.debug_frame,.note.renesas,.gstackfix,.rosda_start,.rosda_end,.sda_start,.sda_end,.linfix,.debug_str,.debug_loc,.ghrettbl,.ghcalltbl,.ghtailcalltbl,.rominfo */
/* No_Calc_Section = .OS_CONST,.OS_CONST_FAST,.OS_CORE0_CONST_FAST,.stack,.sect_stack_start,.OS_CORE0_VAR_FAST_NOINIT,.OS_BARRIER_CORE0_VAR_FAST_NOCACHE_NOINIT,.OS_VAR_FAST_NOCACHE_NOINIT,.OS_CORESTATUS_CORE0_VAR_FAST_NOCACHE_NOINIT */

/* *** MEMORY(ROM/RAM) Usage Calculation Formula *** */
/* -----MEMORY(ROM/RAM) Category-----  */
/* ROM CAL       = ROM_CAL             */
/* ROM APL       = ROM_APL             */
/* Local RAM     = LRAM                */
/* Global RAM    = GRAM                */
/* Retention RAM = RRAM                */
/* -----MEMORY(TOTAL) Category-----    */
/* Calibration   = ROM_CAL             */
/* Application   = ROM_APL             */
/* ROM           = ROM_CAL + ROM_APL   */
/* RAM           = LRAM + GRAM + RRAM  */
/* *** MEMORY(ROM/RAM) Usage Calculation Formula END *** */

/* *** MEMORY(FUNCTION) Usage Calculation Formula *** */
/* -----MEMORY(ROM/RAM) Category-----  */
/* ROM           = ROM_CAL + ROM_APL   */
/* LRAM          = LRAM                */
/* GRAM          = GRAM                */
/* RRAM          = RRAM                */
/* -----MEMORY(FUNCTION) Category----- */
/* APLOS                               */
/* DL                                  */
/* FH                                  */
/* MR                                  */
/* WR                                  */
/* APS                                 */
/* BSW                                 */
/* CDD                                 */
/* LIB                                 */
/* MCAL                                */
/* MIDDLE                              */
/* PAL                                 */
/* RTE                                 */
/* CHKSUM                              */
/* DEFSEC                              */
/* EXAPL                               */
/* GHSLIB                              */
/* OTHER                               */
/* *** MEMORY(FUNCTION) Usage Calculation Formula END *** */

MEMORY {

    /*------  コードフラッシュ 4MB ------*/
    MEMBLOCK_STARTUP_BOOT: ORIGIN = 0x00000000, LENGTH = 0x00008000 /* None */
    MEMBLOCK_REPROG_ROM  : ORIGIN = 0x00008000, LENGTH = 0x00030000 /* None */
    MEMBLOCK_PLANT_ROM   : ORIGIN = 0x00038000, LENGTH = 0x00010000 /* None */
    MEMBLOCK_KEYMGR_ROM  : ORIGIN = 0x00048000, LENGTH = 0x00010000 /* None */
    MEMBLOCK_FBLHEDER    : ORIGIN = 0x00058000, LENGTH = 0x00000200 /* None */
    MEMBLOCK_BOOT        : ORIGIN = 0x00058200, LENGTH = 0x00007600 /* ROM_APL */

    /*------  boot ------*/
    MEMBLOCK_APLBOOT     : ORIGIN = 0x0005F800, LENGTH = 0x00000800 /* None */

    /*------  MEMBLOCK_CAL_DATA ------*/
    MEMBLOCK_CAL_DATA    : ORIGIN = 0x00060000, LENGTH = 0x00002000 /* ROM_CAL */

    /*------  MEMBLOCK_CONST_DATA ------*/
    MEMBLOCK_CONST_DATA  : ORIGIN = 0x00062000, LENGTH = 0x001CEF80 /* ROM_APL */

    /*------  MEMBLOCK_APL_CODE ------*/
    MEMBLOCK_APL_CODE    : ORIGIN = 0x00230F80, LENGTH = 0x001CEF80 /* ROM_APL */

    /*------  MEMBLOCK_ROMCHECK ------*/
    MEMBLOCK_ROMCHECK    : ORIGIN = 0x003FFF00, LENGTH = 0x00000100 /* ROM_APL */

    /*------  ローカルRAM(CPU1領域) 256KB ------*/
    MEMBLOCK_LOCAL_RAM   : ORIGIN = 0xFEBC0000, LENGTH = 0x00040000 /* LRAM */

    /*------  グローバルRAM A 96KB ------*/
    MEMBLOCK_GLOBAL_RAM_A: ORIGIN = 0xFEEE8000, LENGTH = 0x00018000 /* GRAM */

    /*------  リテンションRAM 64KB ------*/
    MEMBLOCK_RRAM_NOCLR_CPU1: ORIGIN = 0xFEF00000, LENGTH = 0x00010000 /* RRAM */

    /*------  データフラッシュ 128KB ------*/
    DATA                 : ORIGIN = 0xFF200000, LENGTH = 0x00020000 /* None */

}

DEFAULTS {
    stack_reserve    = 4K

}

/*************************************************************************************************/
/* セクション定義                                                                                */
/*************************************************************************************************/
SECTIONS {

    /*------  コードフラッシュ 4MB ------*/
    .BOOTVECT                       ALIGN(4)   :                             > MEMBLOCK_STARTUP_BOOT  /*------ FUNCTYPE:EXAPL ------*/     /*------  BOOTVECTOR(暫定) ------*/

    .REPROG_ROM                     ALIGN(4)   :                             > MEMBLOCK_REPROG_ROM  /*------ FUNCTYPE:EXAPL ------*/     /*------  リプログROM領域 ------*/

    .PLANT_ROM                      ALIGN(4)   :                             > MEMBLOCK_PLANT_ROM  /*------ FUNCTYPE:EXAPL ------*/     /*------  完検ROM領域 ------*/

    .KEYMGR_ROM                     ALIGN(4)   :                             > MEMBLOCK_KEYMGR_ROM  /*------ FUNCTYPE:EXAPL ------*/     /*------  鍵管理ROM領域 ------*/

    .FBLHEADER                      ALIGN(4)   :                             > MEMBLOCK_FBLHEDER   /*------ FUNCTYPE:EXAPL ------*/     /*------  FBLヘッダ ------*/

    .sect_pf_startup_ebase          ALIGN(512)   :                           > MEMBLOCK_BOOT       /*------ FUNCTYPE:CDD ------*/     /*------  HOST STARTUP ------*/
    .sect_pf_startup_intvect        ALIGN(512)   :                           > .                   /*------ FUNCTYPE:CDD ------*/
    .start_host                     ALIGN(4)   :                             > .                   /*------ FUNCTYPE:CDD ------*/
    .sect_pf_startup_prg            ALIGN(4)   :                             > .                   /*------ FUNCTYPE:CDD ------*/
    .sect_pf_startup_hook           ALIGN(4)   :                             > .                   /*------ FUNCTYPE:CDD ------*/
    .sect_pf_startup_rom            ALIGN(4)   :                             > .                   /*------ FUNCTYPE:CDD ------*/
    .sect_pf_startup_cfg            ALIGN(4)   :                             > .                   /*------ FUNCTYPE:CDD ------*/

    /*------  boot ------*/
    .APLBOOT_ROM_TOP                   :                                     > MEMBLOCK_APLBOOT    /*------ FUNCTYPE:EXAPL ------*/
    #define OS_LINK_EXCVEC_CODE                                                                       /*------  「コードセクション」しか含まれないため、OSのリンカディレクティブを使用する。 ------*/
    #include "Os_Link_Core0.ld"
    #define OS_LINK_INTVEC_CODE                                                                       /*------  「コードセクション」しか含まれないため、OSのリンカディレクティブを使用する。 ------*/
    #include "Os_Link_Core0.ld"
    .APLBOOT_ROM_END               endaddr(MEMBLOCK_APLBOOT)  :              > .                   /*------ FUNCTYPE:EXAPL ------*/

    /*------  MEMBLOCK_CAL_DATA ------*/
    .CAL_DATA_TOP                        :                                   > MEMBLOCK_CAL_DATA   /*------ FUNCTYPE:EXAPL ------*/     /*------  ROM SDA開始指示 ------*/
    .rosda_start                    ALIGN(4)   :                             > .                   /*------ FUNCTYPE:DEFSEC ------*/
    .version                        ALIGN(4)   :                             > .                   /*------ FUNCTYPE:EXAPL ------*/     /*------  NEXT-DRCK機能で読み出すECU情報用セクション ------*/
    /*------  APL_CAL ------*/
    .APS_CAL                        ALIGN(4)   :                             > .                   /*------ FUNCTYPE:APS ------*/
    .MR_CAL                         ALIGN(4)   :                             > .                   /*------ FUNCTYPE:MR ------*/
    .FH_CAL                         ALIGN(4)   :                             > .                   /*------ FUNCTYPE:FH ------*/
    .WR_CAL                         ALIGN(4)   :                             > .                   /*------ FUNCTYPE:WR ------*/
    .DL_CAL                         ALIGN(4)   :                             > .                   /*------ FUNCTYPE:DL ------*/
    .APLOS_CAL                      ALIGN(4)   :                             > .                   /*------ FUNCTYPE:APLOS ------*/
    /*------  MIDDLE_CAL ------*/
    .NWS_CAL                        ALIGN(4)   :                             > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .SAS_CAL                        ALIGN(4)   :                             > .                   /*------ FUNCTYPE:MIDDLE ------*/
    /*------  CDD_CAL ------*/
    .SLPS_CAL                       ALIGN(4)   :                             > .                   /*------ FUNCTYPE:CDD ------*/
    .MEMS_CAL                       ALIGN(4)   :                             > .                   /*------ FUNCTYPE:CDD ------*/
    .CAL_DATA_END                  endaddr(MEMBLOCK_CAL_DATA)  :             > .                   /*------ FUNCTYPE:EXAPL ------*/

    /*------  MEMBLOCK_CONST_DATA ------*/
    .CONST_DATA_TOP                      :                                   > MEMBLOCK_CONST_DATA  /*------ FUNCTYPE:EXAPL ------*/
    /*------  APL_CONST ------*/
    .APS_CONST                      ALIGN(4)   :                             > .                   /*------ FUNCTYPE:APS ------*/
    .MR_CONST                       ALIGN(4)   :                             > .                   /*------ FUNCTYPE:MR ------*/
    .FH_CONST                       ALIGN(4)   :                             > .                   /*------ FUNCTYPE:FH ------*/
    .WR_CONST                       ALIGN(4)   :                             > .                   /*------ FUNCTYPE:WR ------*/
    .DL_CONST                       ALIGN(4)   :                             > .                   /*------ FUNCTYPE:DL ------*/
    .APLOS_CONST                    ALIGN(4)   :                             > .                   /*------ FUNCTYPE:APLOS ------*/
    /*------  LIB_CONST ------*/
    .CMNPKG_CONST                   ALIGN(4)   :                             > .                   /*------ FUNCTYPE:LIB ------*/
    /*------  PAL_CONST ------*/
    .PAL_CONST                      ALIGN(4)   :                             > .                   /*------ FUNCTYPE:PAL ------*/
    /*------  MIDDLE_CONST ------*/
    .NWS_CONST                      ALIGN(4)   :                             > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .SAS_CONST                      ALIGN(4)   :                             > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .NVS_CONST                      ALIGN(4)   :                             > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .SYSS_CONST                     ALIGN(4)   :                             > .                   /*------ FUNCTYPE:MIDDLE ------*/
    /*------  BSW_CONST ------*/
    .E2E_CONST                      ALIGN(4)   :                             > .                   /*------ FUNCTYPE:CDD ------*/
    .CRC_CONST                      ALIGN(4)   :                             > .                   /*------ FUNCTYPE:CDD ------*/
    .OS_CONST                       ALIGN(4)   :                             > .                   /*------ FUNCTYPE:BSW ------*/     /*------  OSで生成されたリンカディレクティブを使うべきだが、「定数セクション」と「初期値有り変数の初期値を格納するセクション」が混在する可能があるため、手動追加 ------*/
    .OS_CONST_FAST                  ALIGN(4)   :                             > .                   /*------ FUNCTYPE:BSW ------*/     /*------  OSで生成されたリンカディレクティブを使うべきだが、「定数セクション」と「初期値有り変数の初期値を格納するセクション」が混在する可能があるため、手動追加 ------*/
    .OS_CORE0_CONST_FAST            ALIGN(4)   :                             > .                   /*------ FUNCTYPE:BSW ------*/     /*------  OSで生成されたリンカディレクティブを使うべきだが、「定数セクション」と「初期値有り変数の初期値を格納するセクション」が混在する可能があるため、手動追加 ------*/
    #define OS_LINK_INTVEC_CONST                                                                      /*------  割り込みベクタテーブルに関連する「定数セクション」しか含まれないため、OSで生成されたリンカディレクティブを使用する。 ------*/
    #include "Os_Link_Core0.ld"
    #define OS_LINK_EXCVEC_CONST                                                                      /*------  例外ベクタテーブルに関連する「定数セクション」しか含まれないため、OSで生成されたリンカディレクティブを使用する。 ------*/
    #include "Os_Link_Core0.ld"
    .RTE_CONST                      ALIGN(4)   :                             > .                   /*------ FUNCTYPE:RTE ------*/
    .BSWM_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ECUM_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .WDGM_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .WDGIF_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DCM_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DEM_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DET_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FIM_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NVM_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .MEMIF_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FEE_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANTP_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .PDUR_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COM_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COMM_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANSM_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANNM_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NM_CONST                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANIF_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .PIO_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ADI_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .VSTDLIB_CONST                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .LINIF_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .LINSM_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    /*------  CDD_CONST ------*/
    .CDD_EXAUTOSAR_CONST            ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .WDGS_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .DMA_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .STARTUPS_CONST                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SLPS_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MEMS_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .ADDRV_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PORTDRV_CONST                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MTRS_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SWITCH_CONST                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDDMAIN_CONST                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .NDRCK_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_MEASURES_CONST             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_TRCVS_CONST                ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SLFTSTS_CONST                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MIRM_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWSW_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWMDRV_CONST                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .LED_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .DBGS_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .FLUSHH_CONST                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CLUSTERIC_CONST                ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRDIST_CONST                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRIN_CONST                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWHS_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_EXS_CONST                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    /*------  MCAL_CONST ------*/
    .GPT_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .MCU_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .WDG_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CORTST_CONST                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLSTST_CONST                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .RAMTST_CONST                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLS_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CAN_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .SPI_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .ADC_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .PORT_CONST                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .DIO_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .PWM_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .ICU_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .LIN_CONST                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .rosdata                        ALIGN(4) :                               > .                   /*------ FUNCTYPE:DEFSEC ------*/
    .romsdata_cpy_start             ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    .D_SDATA                        ALIGN(4) ROM( .sdata ) :                 > .                   /*------ FUNCTYPE:DEFSEC ------*/     /*------  デフォルトセクション ------*/
    /*------  D_APL_VAR_INIT ------*/
    .D_APS_VAR_INIT                 ALIGN(4) ROM( .APS_VAR_INIT ) :          > .                   /*------ FUNCTYPE:APS ------*/
    .D_MR_VAR_INIT                  ALIGN(4) ROM( .MR_VAR_INIT ) :           > .                   /*------ FUNCTYPE:MR ------*/
    .D_FH_VAR_INIT                  ALIGN(4) ROM( .FH_VAR_INIT ) :           > .                   /*------ FUNCTYPE:FH ------*/
    .D_WR_VAR_INIT                  ALIGN(4) ROM( .WR_VAR_INIT ) :           > .                   /*------ FUNCTYPE:WR ------*/
    .D_DL_VAR_INIT                  ALIGN(4) ROM( .DL_VAR_INIT ) :           > .                   /*------ FUNCTYPE:DL ------*/
    .D_APLOS_VAR_INIT               ALIGN(4) ROM( .APLOS_VAR_INIT ) :        > .                   /*------ FUNCTYPE:APLOS ------*/
    /*------  D_LIB_VAR_INIT ------*/
    .D_CMNPKG_VAR_INIT              ALIGN(4) ROM( .CMNPKG_VAR_INIT ) :       > .                   /*------ FUNCTYPE:LIB ------*/
    /*------  D_PAL_VAR_INIT ------*/
    .D_PAL_VAR_INIT                 ALIGN(4) ROM( .PAL_VAR_INIT ) :          > .                   /*------ FUNCTYPE:PAL ------*/
    /*------  D_MIDDLE_VAR_INIT ------*/
    .D_NWS_VAR_INIT                 ALIGN(4) ROM( .NWS_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .D_SAS_VAR_INIT                 ALIGN(4) ROM( .SAS_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .D_NVS_VAR_INIT                 ALIGN(4) ROM( .NVS_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .D_SYSS_VAR_INIT                ALIGN(4) ROM( .SYSS_VAR_INIT ) :         > .                   /*------ FUNCTYPE:MIDDLE ------*/
    /*------  D_RTE_VAR_INIT ------*/
    .D_RTE_VAR_INIT                 ALIGN(4) ROM( .RTE_VAR_INIT ) :          > .                   /*------ FUNCTYPE:RTE ------*/
    /*------  D_BSW_VAR_INIT ------*/
    .D_E2E_VAR_INIT                 ALIGN(4) ROM( .E2E_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_CRC_VAR_INIT                 ALIGN(4) ROM( .CRC_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_BSWM_VAR_INIT                ALIGN(4) ROM( .BSWM_VAR_INIT ) :         > .                   /*------ FUNCTYPE:BSW ------*/
    .D_ECUM_VAR_INIT                ALIGN(4) ROM( .ECUM_VAR_INIT ) :         > .                   /*------ FUNCTYPE:BSW ------*/
    .D_WDGM_VAR_INIT                ALIGN(4) ROM( .WDGM_VAR_INIT ) :         > .                   /*------ FUNCTYPE:BSW ------*/
    .D_WDGIF_VAR_INIT               ALIGN(4) ROM( .WDGIF_VAR_INIT ) :        > .                   /*------ FUNCTYPE:BSW ------*/
    .D_DCM_VAR_INIT                 ALIGN(4) ROM( .DCM_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_DEM_VAR_INIT                 ALIGN(4) ROM( .DEM_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_DET_VAR_INIT                 ALIGN(4) ROM( .DET_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_FIM_VAR_INIT                 ALIGN(4) ROM( .FIM_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_NVM_VAR_INIT                 ALIGN(4) ROM( .NVM_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_MEMIF_VAR_INIT               ALIGN(4) ROM( .MEMIF_VAR_INIT ) :        > .                   /*------ FUNCTYPE:BSW ------*/
    .D_FEE_VAR_INIT                 ALIGN(4) ROM( .FEE_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_CANTP_VAR_INIT               ALIGN(4) ROM( .CANTP_VAR_INIT ) :        > .                   /*------ FUNCTYPE:BSW ------*/
    .D_PDUR_VAR_INIT                ALIGN(4) ROM( .PDUR_VAR_INIT ) :         > .                   /*------ FUNCTYPE:BSW ------*/
    .D_COM_VAR_INIT                 ALIGN(4) ROM( .COM_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_COMM_VAR_INIT                ALIGN(4) ROM( .COMM_VAR_INIT ) :         > .                   /*------ FUNCTYPE:BSW ------*/
    .D_CANSM_VAR_INIT               ALIGN(4) ROM( .CANSM_VAR_INIT ) :        > .                   /*------ FUNCTYPE:BSW ------*/
    .D_CANNM_VAR_INIT               ALIGN(4) ROM( .CANNM_VAR_INIT ) :        > .                   /*------ FUNCTYPE:BSW ------*/
    .D_NM_VAR_INIT                  ALIGN(4) ROM( .NM_VAR_INIT ) :           > .                   /*------ FUNCTYPE:BSW ------*/
    .D_CANIF_VAR_INIT               ALIGN(4) ROM( .CANIF_VAR_INIT ) :        > .                   /*------ FUNCTYPE:BSW ------*/
    .D_PIO_VAR_INIT                 ALIGN(4) ROM( .PIO_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_ADI_VAR_INIT                 ALIGN(4) ROM( .ADI_VAR_INIT ) :          > .                   /*------ FUNCTYPE:BSW ------*/
    .D_LINIF_VAR_INIT               ALIGN(4) ROM( .LINIF_VAR_INIT ) :        > .                   /*------ FUNCTYPE:BSW ------*/
    .D_LINSM_VAR_INIT               ALIGN(4) ROM( .LINSM_VAR_INIT ) :        > .                   /*------ FUNCTYPE:BSW ------*/
    /*------  D_CDD_VAR_INIT ------*/
    .D_CDD_EXAUTOSAR_VAR_INIT       ALIGN(4) ROM( .CDD_EXAUTOSAR_VAR_INIT ) :   > .                /*------ FUNCTYPE:CDD ------*/
    .D_WDGS_VAR_INIT                ALIGN(4) ROM( .WDGS_VAR_INIT ) :         > .                   /*------ FUNCTYPE:CDD ------*/
    .D_DMA_VAR_INIT                 ALIGN(4) ROM( .DMA_VAR_INIT ) :          > .                   /*------ FUNCTYPE:CDD ------*/
    .D_STARTUPS_VAR_INIT            ALIGN(4) ROM( .STARTUPS_VAR_INIT ) :     > .                   /*------ FUNCTYPE:CDD ------*/
    .D_SLPS_VAR_INIT                ALIGN(4) ROM( .SLPS_VAR_INIT ) :         > .                   /*------ FUNCTYPE:CDD ------*/
    .D_MEMS_VAR_INIT                ALIGN(4) ROM( .MEMS_VAR_INIT ) :         > .                   /*------ FUNCTYPE:CDD ------*/
    .D_ADDRV_VAR_INIT               ALIGN(4) ROM( .ADDRV_VAR_INIT  ) :       > .                   /*------ FUNCTYPE:CDD ------*/
    .D_PORTDRV_VAR_INIT             ALIGN(4) ROM( .PORTDRV_VAR_INIT  ) :     > .                   /*------ FUNCTYPE:CDD ------*/
    .D_MTRS_VAR_INIT                ALIGN(4) ROM( .MTRS_VAR_INIT  ) :        > .                   /*------ FUNCTYPE:CDD ------*/
    .D_SWITCH_VAR_INIT              ALIGN(4) ROM( .SWITCH_VAR_INIT  ) :      > .                   /*------ FUNCTYPE:CDD ------*/
    .D_CDDMAIN_VAR_INIT             ALIGN(4) ROM( .CDDMAIN_VAR_INIT  ) :     > .                   /*------ FUNCTYPE:CDD ------*/
    .D_CDD_TRCVS_VAR_INIT           ALIGN(4) ROM( .CDD_TRCVS_VAR_INIT  ) :   > .                   /*------ FUNCTYPE:CDD ------*/
    .D_MIRM_VAR_INIT                ALIGN(4) ROM( .MIRM_VAR_INIT  ) :        > .                   /*------ FUNCTYPE:CDD ------*/
    .D_PWSW_VAR_INIT                ALIGN(4) ROM( .PWSW_VAR_INIT  ) :        > .                   /*------ FUNCTYPE:CDD ------*/
    .D_PWMDRV_VAR_INIT              ALIGN(4) ROM( .PWMDRV_VAR_INIT  ) :      > .                   /*------ FUNCTYPE:CDD ------*/
    .D_LED_VAR_INIT                 ALIGN(4) ROM( .LED_VAR_INIT  ) :         > .                   /*------ FUNCTYPE:CDD ------*/
    .D_DBGS_VAR_INIT                ALIGN(4) ROM( .DBGS_VAR_INIT  ) :        > .                   /*------ FUNCTYPE:CDD ------*/
    .D_FLUSHH_VAR_INIT              ALIGN(4) ROM( .FLUSHH_VAR_INIT  ) :      > .                   /*------ FUNCTYPE:CDD ------*/
    .D_CLUSTERIC_VAR_INIT           ALIGN(4) ROM( .CLUSTERIC_VAR_INIT  ) :   > .                   /*------ FUNCTYPE:CDD ------*/
    .D_PWRDIST_VAR_INIT             ALIGN(4) ROM( .PWRDIST_VAR_INIT  ) :     > .                   /*------ FUNCTYPE:CDD ------*/
    .D_PWRIN_VAR_INIT               ALIGN(4) ROM( .PWRIN_VAR_INIT  ) :       > .                   /*------ FUNCTYPE:CDD ------*/
    .D_PWHS_VAR_INIT                ALIGN(4) ROM( .PWHS_VAR_INIT  ) :        > .                   /*------ FUNCTYPE:CDD ------*/
    .D_CDD_EXS_VAR_INIT             ALIGN(4) ROM( .CDD_EXS_VAR_INIT  ) :     > .                   /*------ FUNCTYPE:CDD ------*/
    /*------  D_MCAL_VAR_INIT ------*/
    .D_GPT_VAR_INIT                 ALIGN(4) ROM( .GPT_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_MCU_VAR_INIT                 ALIGN(4) ROM( .MCU_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_WDG_VAR_INIT                 ALIGN(4) ROM( .WDG_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_CORTST_VAR_INIT              ALIGN(4) ROM( .CORTST_VAR_INIT ) :       > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_FLSTST_VAR_INIT              ALIGN(4) ROM( .FLSTST_VAR_INIT ) :       > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_RAMTST_VAR_INIT              ALIGN(4) ROM( .RAMTST_VAR_INIT ) :       > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_FLS_VAR_INIT                 ALIGN(4) ROM( .FLS_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_CAN_VAR_INIT                 ALIGN(4) ROM( .CAN_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_SPI_VAR_INIT                 ALIGN(4) ROM( .SPI_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_ADC_VAR_INIT                 ALIGN(4) ROM( .ADC_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_PORT_VAR_INIT                ALIGN(4) ROM( .PORT_VAR_INIT ) :         > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_DIO_VAR_INIT                 ALIGN(4) ROM( .DIO_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_PWM_VAR_INIT                 ALIGN(4) ROM( .PWM_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_ICU_VAR_INIT                 ALIGN(4) ROM( .ICU_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_LIN_VAR_INIT                 ALIGN(4) ROM( .LIN_VAR_INIT ) :          > .                   /*------ FUNCTYPE:MCAL ------*/
    .romsdata_cpy_end               ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/     /*------  ROM SDA終了指示 ------*/
    .romsdata_cpy_start_r           ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    /*------  D_BSW_VAR_POWER_ON_INIT ------*/
    .D_BSWM_VAR_POWER_ON_INIT       ALIGN(4) ROM(.BSWM_VAR_POWER_ON_INIT) :   > .                  /*------ FUNCTYPE:BSW ------*/
    .D_NVM_VAR_POWER_ON_INIT        ALIGN(4) ROM(.NVM_VAR_POWER_ON_INIT) :   > .                   /*------ FUNCTYPE:BSW ------*/
    .D_FEE_VAR_POWER_ON_INIT        ALIGN(4) ROM(.FEE_VAR_POWER_ON_INIT) :   > .                   /*------ FUNCTYPE:BSW ------*/
    .D_COM_VAR_POWER_ON_INIT        ALIGN(4) ROM(.COM_VAR_POWER_ON_INIT) :   > .                   /*------ FUNCTYPE:BSW ------*/
    .D_COMM_VAR_POWER_ON_INIT       ALIGN(4) ROM(.COMM_VAR_POWER_ON_INIT) :   > .                  /*------ FUNCTYPE:BSW ------*/
    .D_CANNM_VAR_POWER_ON_INIT      ALIGN(4) ROM(.CANNM_VAR_POWER_ON_INIT) :   > .                 /*------ FUNCTYPE:BSW ------*/
    .D_NM_VAR_POWER_ON_INIT         ALIGN(4) ROM(.NM_VAR_POWER_ON_INIT) :    > .                   /*------ FUNCTYPE:BSW ------*/
    .D_ICU_VAR_POWER_ON_INIT        ALIGN(4) ROM(.ICU_VAR_POWER_ON_INIT) :   > .                   /*------ FUNCTYPE:BSW ------*/
    /*------  D_MCAL_VAR_POWER_ON_INIT ------*/
    .D_FLS_VAR_POWER_ON_INIT        ALIGN(4) ROM(.FLS_VAR_POWER_ON_INIT) :   > .                   /*------ FUNCTYPE:MCAL ------*/
    .D_CAN_VAR_POWER_ON_INIT        ALIGN(4) ROM(.CAN_VAR_POWER_ON_INIT) :   > .                   /*------ FUNCTYPE:MCAL ------*/
    .romsdata_cpy_end_r             ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    .rosda_end                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:DEFSEC ------*/     /*------  ROM SDA終了指示 ------*/
    .CONST_DATA_END                endaddr(MEMBLOCK_CONST_DATA)  :           > .                   /*------ FUNCTYPE:EXAPL ------*/

    /*------  MEMBLOCK_APL_CODE ------*/
    .APLCODE_ROM_TOP                     :                                   > MEMBLOCK_APL_CODE   /*------ FUNCTYPE:EXAPL ------*/
    /*------  APL_CODE ------*/
    .APS_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:APS ------*/
    .MR_CODE                        ALIGN(4) :                               > .                   /*------ FUNCTYPE:MR ------*/
    .FH_CODE                        ALIGN(4) :                               > .                   /*------ FUNCTYPE:FH ------*/
    .WR_CODE                        ALIGN(4) :                               > .                   /*------ FUNCTYPE:WR ------*/
    .DL_CODE                        ALIGN(4) :                               > .                   /*------ FUNCTYPE:DL ------*/
    .APLOS_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:APLOS ------*/
    /*------  LIB_CODE ------*/
    .CMNPKG_CODE                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:LIB ------*/
    /*------  PAL_CODE ------*/
    .PAL_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:PAL ------*/
    /*------  MIDDLE_CODE ------*/
    .NWS_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .SAS_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .NVS_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .SYSS_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    /*------  RTE_CODE ------*/
    .RTE_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:RTE ------*/
    /*------  BSW_CODE ------*/
    .E2E_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CRC_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    #define OS_LINK_CODE                                                                              /*------  「コードセクション」しか含まれないため、OSのリンカディレクティブを使用する。 ------*/
    #include "Os_Link.ld"
    #define OS_LINK_CALLOUT_CODE                                                                      /*------  「コードセクション」しか含まれないため、OSのリンカディレクティブを使用する。 ------*/
    #include "Os_Link.ld"
    #define OS_LINK_CALLOUT_CODE                                                                      /*------  「コードセクション」しか含まれないため、OSのリンカディレクティブを使用する。 ------*/
    #include "Os_Link_Core0.ld"
    .BSWM_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ECUM_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .WDGM_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .WDGIF_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DCM_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DEM_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DET_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FIM_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NVM_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .MEMIF_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FEE_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANTP_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .PDUR_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COM_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COMM_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANSM_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANNM_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NM_CODE                        ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANIF_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .PIO_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ADI_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .VSTDLIB_CODE                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .LINIF_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .LINSM_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    /*------  CDD_CODE ------*/
    .CDD_EXAUTOSAR_CODE             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .WDGS_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .DMA_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .STARTUPS_CODE                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .STUB_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SLPS_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MEMS_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .ADDRV_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PORTDRV_CODE                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MTRS_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SWITCH_CODE                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDDMAIN_CODE                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .NDRCK_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .sect_pf_prg                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/     /*------  aipf_ndrck_sect_map.incにより配置されるセクション ------*/
    .CDD_MEASURES_CODE              ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_TRCVS_CODE                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SLFTSTS_CODE                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MIRM_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWSW_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWMDRV_CODE                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .LED_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .DBGS_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .FLUSHH_CODE                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CLUSTERIC_CODE                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRDIST_CODE                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRIN_CODE                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWHS_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_EXS_CODE                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    /*------  MCAL_CODE ------*/
    .GPT_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .MCU_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .WDG_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CORTST_CODE                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLSTST_CODE                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .RAMTST_CODE                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLS_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CAN_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .SPI_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .ADC_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .PORT_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .DIO_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .PWM_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .ICU_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .MCFD_CODE                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/     /*------  RamTst,CorTst,FlsTstアセンブラコード用のセクション ------*/
    .LIN_CODE                       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .GHSLIB_CODE                     : {libstartup.a(*(.text)) libarch.a(*(.text))}  > .           /*------ FUNCTYPE:GHSLIB ------*/
    .text                           ALIGN(4) :                               > .                   /*------ FUNCTYPE:DEFSEC ------*/     /*------  デフォルトセクション ------*/
    .syscall                        ALIGN(4) :                               > .                   /*------ FUNCTYPE:DEFSEC ------*/     /*------  デフォルトセクション ------*/
    .secinfo                        ALIGN(4) :                               > .                   /*------ FUNCTYPE:DEFSEC ------*/     /*------  デフォルトセクション ------*/
    .APLCODE_ROM_END               endaddr(MEMBLOCK_APL_CODE)  :             > .                   /*------ FUNCTYPE:EXAPL ------*/

    /*------  MEMBLOCK_ROMCHECK ------*/
    .FLSTST_CHKSUM                  ALIGN(4) :                               > MEMBLOCK_ROMCHECK   /*------ FUNCTYPE:CHKSUM ------*/     /*------  製品ROMチェック領域 ------*/

    /*------  ローカルRAM(CPU1領域) 256KB ------*/
    .LRAM_TOP                            :                                   > MEMBLOCK_LOCAL_RAM  /*------ FUNCTYPE:EXAPL ------*/
    .sda_start                      ALIGN(4) :                               > .                   /*------ FUNCTYPE:DEFSEC ------*/     /*------  .sda_start-endはRAM領域全体 ------*/
    .VAR_INIT_TOP                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    /*------  sdata ------*/
    .sdata_cpy_start                ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    .sdata                          ALIGN(4) :                               > .                   /*------ FUNCTYPE:DEFSEC ------*/     /*------  デフォルトセクション ------*/
    /*------  LIB_VAR_INIT ------*/
    .CMNPKG_VAR_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:LIB ------*/
    /*------  PAL_VAR_INIT ------*/
    .PAL_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:PAL ------*/
    /*------  MIDDLE_VAR_INIT ------*/
    .NWS_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .SAS_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .NVS_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .SYSS_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    /*------  RTE_VAR_INIT ------*/
    .RTE_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:RTE ------*/
    /*------  BSW_VAR_INIT ------*/
    .E2E_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CRC_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .BSWM_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ECUM_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .WDGM_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .WDGIF_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DCM_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DEM_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DET_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FIM_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NVM_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .MEMIF_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FEE_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANTP_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .PDUR_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COM_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COMM_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANSM_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANNM_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NM_VAR_INIT                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANIF_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANTRCV_VAR_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .PIO_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ADI_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .LINIF_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .LINSM_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    /*------  CDD_VAR_INIT ------*/
    .CDD_EXAUTOSAR_VAR_INIT         ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .WDGS_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .DMA_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .STARTUPS_VAR_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SLPS_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MEMS_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .ADDRV_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PORTDRV_VAR_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MTRS_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SWITCH_VAR_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDDMAIN_VAR_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_TRCVS_VAR_INIT             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MIRM_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWSW_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWMDRV_VAR_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .LED_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .DBGS_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .FLUSHH_VAR_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CLUSTERIC_VAR_INIT             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRDIST_VAR_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRIN_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWHS_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_EXS_VAR_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    /*------  MCAL_VAR_INIT ------*/
    .GPT_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .MCU_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .WDG_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CORTST_VAR_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLSTST_VAR_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .RAMTST_VAR_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLS_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CAN_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .SPI_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .ADC_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .PORT_VAR_INIT                  ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .DIO_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .PWM_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .ICU_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .LIN_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .VAR_INIT_END                      :                                     > .                   /*------ FUNCTYPE:EXAPL ------*/
    /*------  SBSS ------*/
    .VAR_CLEARED_TOP                   :                                     > .                   /*------ FUNCTYPE:EXAPL ------*/
    /*------  LIB_VAR_CLEARED ------*/
    .CMNPKG_VAR_CLEARED             ALIGN(4) :                               > .                   /*------ FUNCTYPE:LIB ------*/
    /*------  PAL_VAR_CLEARED ------*/
    .PAL_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:PAL ------*/
    /*------  MIDDLE_VAR_CLEARED ------*/
    .NWS_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .SAS_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .NVS_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    .SYSS_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:MIDDLE ------*/
    /*------  RTE_VAR_CLEARED ------*/
    .RTE_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:RTE ------*/
    /*------  BSW_VAR_CLEARED ------*/
    .E2E_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CRC_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .BSWM_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ECUM_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .WDGM_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .WDGIF_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DCM_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DEM_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DET_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FIM_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NVM_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .MEMIF_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FEE_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANTP_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .PDUR_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COM_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COMM_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANSM_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANNM_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NM_VAR_CLEARED                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANIF_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .PIO_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ADI_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    /*------  CDD_VAR_CLEARED ------*/
    .sect_pf_startup_sbss           ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_EXAUTOSAR_VAR_CLEARED      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .WDGS_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .DMA_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .STUB_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .STARTUPS_VAR_CLEARED           ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SLPS_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MEMS_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .ADDRV_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PORTDRV_VAR_CLEARED            ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MTRS_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SWITCH_VAR_CLEARED             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDDMAIN_VAR_CLEARED            ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_TRCVS_VAR_CLEARED          ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .NDRCK_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SLFTSTS_VAR_CLEARED            ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MIRM_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWSW_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWMDRV_VAR_CLEARED             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .LED_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .DBGS_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .FLUSHH_VAR_CLEARED             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CLUSTERIC_VAR_CLEARED          ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRDIST_VAR_CLEARED            ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRIN_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWHS_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_EXS_VAR_CLEARED            ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    /*------  MCAL_VAR_CLEARED ------*/
    .GPT_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .MCU_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .WDG_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CORTST_VAR_CLEARED             ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLSTST_VAR_CLEARED             ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .RAMTST_VAR_CLEARED             ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLS_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CAN_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .SPI_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .ADC_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .PORT_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .DIO_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .PWM_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .ICU_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .MCFD_VAR_CLEARED               ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/     /*------  RamTst,CorTst,FlsTstアセンブラコード用のセクション ------*/
    .sbss                           ALIGN(4) :                               > .                   /*------ FUNCTYPE:DEFSEC ------*/     /*------  デフォルトセクション ------*/
    .VAR_CLEARED_END                   :                                     > .                   /*------ FUNCTYPE:EXAPL ------*/
    .OS_STACK_TOP                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    #define OS_LINK_KERNEL_STACKS                                                                     /*------  スタック領域であり「初期値無し変数セクション」しか含まれないため、OSのリンカディレクティブを使用する。 ------*/
    #include "Os_Link_Core0_Stacks.ld"
    .OS_STACK_END                      :                                     > .                   /*------ FUNCTYPE:EXAPL ------*/
    /*------  stack ------*/
    .stack                          ALIGN(4) PAD(stack_reserve) ABS :        > .
    .sect_stack_start               ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    /*------  other ------*/
    .tdata                          ALIGN(4) ABS :                           > .                   /*------ FUNCTYPE:DEFSEC ------*/     /*------  デフォルトセクション ------*/
    .LRAM_END                      endaddr(MEMBLOCK_LOCAL_RAM)  :            > .                   /*------ FUNCTYPE:EXAPL ------*/

    /*------  グローバルRAM A 96KB ------*/
    .GRAM_A_TOP                          :                                   > MEMBLOCK_GLOBAL_RAM_A  /*------ FUNCTYPE:EXAPL ------*/
    /*------  APL_VAR_CLEARED ------*/
    .APS_VAR_CLEARED                ALIGN(4) :                               > .                   /*------ FUNCTYPE:APS ------*/
    .MR_VAR_CLEARED                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:MR ------*/
    .FH_VAR_CLEARED                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:FH ------*/
    .WR_VAR_CLEARED                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:WR ------*/
    .DL_VAR_CLEARED                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:DL ------*/
    .APLOS_VAR_CLEARED              ALIGN(4) :                               > .                   /*------ FUNCTYPE:APLOS ------*/
    /*------  APL_VAR_INIT ------*/
    .APS_VAR_INIT                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:APS ------*/
    .MR_VAR_INIT                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:MR ------*/
    .FH_VAR_INIT                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:FH ------*/
    .WR_VAR_INIT                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:WR ------*/
    .DL_VAR_INIT                    ALIGN(4) :                               > .                   /*------ FUNCTYPE:DL ------*/
    .APLOS_VAR_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:APLOS ------*/
    .GRAM_A_END                    endaddr(MEMBLOCK_GLOBAL_RAM_A)  :         > .                   /*------ FUNCTYPE:EXAPL ------*/

    /*------  リテンションRAM 64KB ------*/
    .RRAM_TOP                            :                                   > MEMBLOCK_RRAM_NOCLR_CPU1  /*------ FUNCTYPE:EXAPL ------*/
    .soft_ram_noclr_start           ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    .sdata_cpy_start_r              ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    /*------  BSW_VAR_POWER_ON_INIT ------*/
    .BSWM_VAR_POWER_ON_INIT         ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NVM_VAR_POWER_ON_INIT          ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FEE_VAR_POWER_ON_INIT          ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COM_VAR_POWER_ON_INIT          ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COMM_VAR_POWER_ON_INIT         ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANNM_VAR_POWER_ON_INIT        ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NM_VAR_POWER_ON_INIT           ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ICU_VAR_POWER_ON_INIT          ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    /*------  MCAL_VAR_POWER_ON_INIT ------*/
    .FLS_VAR_POWER_ON_INIT          ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CAN_VAR_POWER_ON_INIT          ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .sdata_cpy_end_r                ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    .sbss_start_r                   ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    .NVRAM_DATA                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    /*------  APL_VAR_NO_INIT ------*/
    .APS_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:APS ------*/
    .MR_VAR_NO_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:MR ------*/
    .FH_VAR_NO_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:FH ------*/
    .WR_VAR_NO_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:WR ------*/
    .DL_VAR_NO_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:DL ------*/
    .APLOS_VAR_NO_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:APLOS ------*/
    /*------  RTE_VAR_NO_INIT ------*/
    .RTE_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:RTE ------*/
    /*------  BSW_VAR_NO_INIT ------*/
    .OS_CORE0_VAR_FAST_NOINIT       ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/     /*------  OSで生成されたリンカディレクティブを使うべきだが、「初期値有り変数セクション」と「初期値無し変数セクション」が混在する可能性があるため、手動追加。 ------*/
    .OS_BARRIER_CORE0_VAR_FAST_NOCACHE_NOINIT  ALIGN(4) :                    > .                   /*------ FUNCTYPE:BSW ------*/     /*------  OSで生成されたリンカディレクティブを使うべきだが、「初期値有り変数セクション」と「初期値無し変数セクション」が混在する可能性があるため、手動追加。 ------*/
    .OS_VAR_FAST_NOCACHE_NOINIT     ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/     /*------  OSで生成されたリンカディレクティブを使うべきだが、「初期値有り変数セクション」と「初期値無し変数セクション」が混在する可能性があるため、手動追加。 ------*/
    .OS_CORESTATUS_CORE0_VAR_FAST_NOCACHE_NOINIT  ALIGN(4) :                 > .                   /*------ FUNCTYPE:BSW ------*/     /*------  OSで生成されたリンカディレクティブを使うべきだが、「初期値有り変数セクション」と「初期値無し変数セクション」が混在する可能性があるため、手動追加。 ------*/
    .BSWM_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .ECUM_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .WDGM_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DCM_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .PDUR_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COM_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .COMM_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANSM_VAR_NO_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANNM_VAR_NO_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NM_VAR_NO_INIT                 ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .CANIF_VAR_NO_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .DEM_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FIM_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/     /*------  Sleep/WakeUp時に値を保持する必要がある為、リテンションRAM領域に割り当てる ------*/
    .DET_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .NVM_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .FEE_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/     /*------  Sleep/WakeUp時に値を保持する必要がある為、リテンションRAM領域に割り当てる ------*/
    .CANTP_VAR_NO_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/     /*------  Sleep/WakeUp時に値を保持する必要がある為、リテンションRAM領域に割り当てる ------*/
    .LINIF_VAR_NO_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    .LINSM_VAR_NO_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:BSW ------*/
    /*------  CDD_VAR_NO_INIT ------*/
    .SLPS_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MEMS_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_EXAUTOSAR_VAR_NO_INIT      ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .ADDRV_VAR_NO_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PORTDRV_VAR_NO_INIT            ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MTRS_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .SWITCH_VAR_NO_INIT             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDDMAIN_VAR_NO_INIT            ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CDD_TRCVS_VAR_NO_INIT          ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .MIRM_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWSW_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWMDRV_VAR_NO_INIT             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .LED_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .DBGS_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .FLUSHH_VAR_NO_INIT             ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .CLUSTERIC_VAR_NO_INIT          ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRDIST_VAR_NO_INIT            ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWRIN_VAR_NO_INIT              ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    .PWHS_VAR_NO_INIT               ALIGN(4) :                               > .                   /*------ FUNCTYPE:CDD ------*/
    /*------  MCAL_VAR_NO_INIT ------*/
    .ICU_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CORTST_VAR_NO_INIT             ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLSTST_VAR_NO_INIT             ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FLS_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .CAN_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .LIN_VAR_NO_INIT                ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    /*------  MIDDLE_VAR_POWER_ON_CLEARED ------*/
    .SAS_VAR_POWER_ON_CLEARED       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    /*------  BSW_VAR_POWER_ON_CLEARED ------*/
    .NVM_VAR_POWER_ON_CLEARED       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .FEE_VAR_POWER_ON_CLEARED       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    /*------  CDD_VAR_POWER_ON_CLEARED ------*/
    .MEMS_VAR_POWER_ON_CLEARED      ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .NDRCK_VAR_POWER_ON_CLEARED     ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    /*------  MCAL_VAR_POWER_ON_CLEARED ------*/
    .FLS_VAR_POWER_ON_CLEARED       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .ICU_VAR_POWER_ON_CLEARED       ALIGN(4) :                               > .                   /*------ FUNCTYPE:MCAL ------*/
    .sect_noclr_sbss                MIN_ENDADDRESS(addr(.RRAM_END) - 4) MAX_ENDADDRESS(addr(.RRAM_END) - 4) :   > .  /*------ FUNCTYPE:EXAPL ------*/
    .sbss_end_r                     ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    .soft_ram_noclr_end             ALIGN(4) :                               > .                   /*------ FUNCTYPE:EXAPL ------*/
    .sect_noclr_clr_check_pattern   ALIGN(4) MIN_SIZE(4) :                   > .                   /*------ FUNCTYPE:EXAPL ------*/
    .sda_end                             :                                   > .                   /*------ FUNCTYPE:DEFSEC ------*/
    .RRAM_END                      endaddr(MEMBLOCK_RRAM_NOCLR_CPU1)  :      > .                   /*------ FUNCTYPE:EXAPL ------*/

    /* ------SYMBOL for MICROSAR OS------ */
    __OS_CODE_START = ADDR(.OS_CODE);
    __OS_CODE_LIMIT = ENDADDR(.OS_CODE) - 1;

    /* ------製品ソフトクリアなしRAMシンボル------ */
    _u4g_ptr_sect_romsdata_cpy_start_r = addr(.romsdata_cpy_start_r);   /* リテンションRAM初期値有り変数の初期値格納領域開始アドレス */
    _u4g_ptr_sect_romsdata_cpy_end_r = addr(.romsdata_cpy_end_r);  /* リテンションRAM初期値有り変数の初期値格納領域終了アドレス */
    _u4g_ptr_sect_sdata_cpy_start_r = addr(.sdata_cpy_start_r);      /* リテンションRAM初期値有り変数領域開始アドレス */
    _u4g_ptr_sect_sbss_start_r = addr(.sbss_start_r);            /* リテンションRAM初期値無し変数領域開始アドレス */
    _u4g_ptr_sect_sbss_end_r = addr(.sbss_end_r);            /* リテンションRAM初期値無し変数領域終了アドレス */
    _u4g_ptr_sect_ram_noclr_start      = addr(.soft_ram_noclr_start);          /* 製品ソフトクリアなしRAM開始アドレス         */
    _u4g_ptr_sect_ram_noclr_end        = addr(.soft_ram_noclr_end);    /* 製品ソフトクリアなしRAM終了アドレス         */
    _u4g_ptr_sect_ram_noclr_clrchk_pattern = addr(.sect_noclr_clr_check_pattern);  /*製品ソフトクリア無しRAM  クリア完了チェック用パターン配置アドレス*/

}

