

## config var
## config var
epc_dict = {
           #drawings name      #software name
'EPC_111001' :     'EPC_11_010_0015'   ,
'EPC_111010_L' :   'EPC_11_100_0060_L' ,
'EPC_111010_R' :   'EPC_11_100_0060_R' ,
'EPC_111015_R' :   'EPC_11_200_0010'   ,
'EPC_111030_2' :   'EPC_11_202_0020'   ,
'EPC_111040_1' :   'EPC_11_030_0015'   ,
'EPC_111040_2' :   'EPC_11_030_0030'   ,
'EPC_111075_L' :   'EPC_11_300_0045_L' ,
'EPC_111075_R' :   'EPC_11_300_0045_R' ,
'EPC_111080_L' :   'EPC_11_300_0085'   ,
'EPC_111090_R' :   'EPC_11_402_0010'   ,
'EPC_112001_L' :   'EPC_11_600_0070_L' ,
'EPC_112001_R' :   'EPC_11_600_0070_R' ,
             }






















sg_List = ['100',
           '101',
           '102',
           '103',
           '104',
           '105',
           '106',
           '107',
           '108',
           '109',
           '110',
           '600',
           '601',
           '700',
           '701'
            ]
bcnBY_list = ['BCN1_13_100_0040',
           'BCN1_13_100_0055',
           'BCN1_13_100_0070',
           'BCN1_13_100_0085',
           'BCN1_13_100_0100',
           'BCN1_13_100_0115',
           'BCN1_13_100_0130',
           'BCN1_13_100_0145',
           'BCN1_13_100_0160',
           'BCN1_13_100_0170'

            ]

bcnBYGR_list = ['BCN1_13_000_0000',
                'BCN1_13_100_0185',
                'BCN1_13_100_0205',
                'BCN1_13_601_0065'

                 ]


pbl_dict = {

'PBL1_11_010_0015'   : 'safety',
'PBL1_11_100_0060'   : 'safety',
'PBL2_11_100_0060'   : 'safety',
'PBL1_11_200_0010'   : 'safety',
'PBL1_11_202_0020'   : 'safety',
'PBL1_11_030_0015'   : 'safety',
'PBL1_11_030_0030'   : 'safety',
'PBL1_11_300_0045'   : 'safety',
'PBL2_11_300_0045'   : 'safety',
'PBL1_11_300_0085'   : 'safety',
'PBL1_11_402_0010'   : 'safety'

}

ae = 11

# end of config variables
####################################



with open('outputFB_Pilot_Beacon.txt', 'w') as f:


    f.write(f'EmergencyCircuitOK_All := SafetyOutput.EmergencyCircuitOk.AE{ae} \n')
    for sg in sg_List:
        if sg == sg_List[-1]:
            f.write(f'                AND SafetyOutput.EmergencyCircuitOk.SG{sg}; \n \n \n \n ')
        else:
            f.write(f'                AND SafetyOutput.EmergencyCircuitOk.SG{sg} \n ')

    f.write(f'AE{ae}_Panel.Outputs.Control_Power_On_PL	:= (PowerOnSequence AND fbBlink_250ms.Pulse) OR ControlPowerOn OR ToggleBit_PL[1]; \n')
    f.write(f'AE{ae}_Panel.Outputs.System_Start_PL	:= (ControlPowerOn AND EmergencyCircuitOK_All AND fbBlink_100ms.Pulse AND NOT SG_Started_Any) OR \n')
    f.write(f'           (SG_Started_Any AND fbBlink_500ms.Pulse) OR SG_Started_All OR ToggleBit_PL[2]; \n')
    f.write(f'AE{ae}_Panel.Outputs.System_Estops_OK_PL	:= EmergencyCircuitOK_All OR ToggleBit_PL[3]; \n')
    f.write(f'AE{ae}_Panel.Outputs.System_Reset_PL := SafetyOutput.EmergencyActivated.AE{ae} OR \n')
    f.write(f'\t\t\t\t((SG_Error_Any OR SG_Safety_Error )\n')
    f.write(f'\t\t\t\tAND fbBlink_500ms.Pulse OR ToggleBit_PBL[1]); \n')

    f.write('\n \n \n')

    f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.BCN1_{ae}_000_0000.Beacon_Green		:= (SG_Starting_Any AND fbBlink_100ms.Pulse) OR (SG_Started_Any AND fbBlink_500ms.Pulse) OR SG_Started_All OR ToggleBit_BCN[1,1];\n')
    f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.BCN1_{ae}_000_0000.Beacon_Blue		:= (SG_Full_Any AND fbBlink_500ms.Pulse) OR ToggleBit_BCN[1,2]; \n')
    f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.BCN1_{ae}_000_0000.Beacon_Yellow	:= ToggleBit_BCN[1,3];(* ((SG_Error_Any OR SG_Safety_Error  OR ScannerError_11_200_0040 OR \n')
    f.write(f'               ScannerError_11_200_0125) AND fbBlink_500ms.Pulse) OR \n')
    f.write(f'               EIP_SW1_Error OR EIP_SW2_Error OR *) \n')
    f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.BCN1_{ae}_000_0000.Beacon_Red		:=  (NOT EmergencyCircuitOK_All AND NOT SafetyOutput.EmergencyActivated.AE{ae}) OR \n')
    f.write(f'                                  (SafetyOutput.EmergencyActivated.AE{ae} AND  fbBlink_500ms.Pulse) OR  ToggleBit_BCN[1,4]; \n')
    f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.BCN1_{ae}_000_0000.Beacon_Horn		:= (SG_Starting_Any AND fbBlink_250ms.Pulse) OR ToggleBit_BCN[1,5]; \n')


    f.write('\n \n \n')





    for idx, bcn in enumerate(bcnBY_list):
        f.write(f'//{bcn}.Beacon_Blue		:=  (DownstreamFull_13_102_0005 AND fbBlink_500ms.Pulse) OR  ToggleBit_BCN[{idx + 2},2]; \n')
        f.write(f'//{bcn}.Beacon_Yellow		:=  (DivertError_13_100_0060 AND fbBlink_500ms.Pulse)  OR EIP_Error_SG102 OR ToggleBit_BCN[{idx + 2},3]; \n')
        f.write('\n')

    f.write('\n \n \n')

    for idx, bcn in enumerate(bcnBYGR_list):
        f.write(f'{bcn}.Beacon_Green		:= (fbSG_{bcn[8:11]}.HW_Outputs.GroupIsStarting AND fbBlink_250ms.Pulse) OR \n')
        f.write(f'                                   fbSG_{bcn[8:11]}.HW_Outputs.GroupStarted OR ToggleBit_BCN[{idx + 2},1]; \n')
        f.write(f'//{bcn}.Beacon_Blue		:= (placeholder AND fbBlink_500ms.Pulse) OR ToggleBit_BCN[5,2]; \n')
        f.write(f'{bcn}.Beacon_Yellow		:= (VFDError_{bcn[5:16]} AND fbBlink_500ms.Pulse) OR (IO_{bcn[5:16]}_K1.Status_Word.7 AND fbBlink_250ms.Pulse) OR EIP_Error_SG{bcn[8:11]} OR ToggleBit_BCN[{idx + 2},3]; \n')
        f.write(f'{bcn}.Beacon_Red			:=  NOT SafetyOutput.EmergencyCircuitOk.SG{bcn[8:11]} OR ToggleBit_BCN[{idx + 2},4]; \n')
        f.write(f'{bcn}.Beacon_Horn		:= (fbSG_{bcn[8:11]}.HW_Outputs.GroupIsStarting AND fbBlink_250ms.Pulse) OR ToggleBit_BCN[{idx + 2},5]; \n')
        f.write('\n \n \n')

    f.write('\n \n \n')








    f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.BCN1_{ae}_000_0000.Beacon_Red:=  SafetyOutput.EmergencyActivated.AE{ae}  AND fbBlink_500ms.Pulse; \n')
    for layoutNum in epc_dict.keys():
        f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.{layoutNum}.PL_Red :=  SafetyOutput.EmergencyActivated.{epc_dict[layoutNum]}  AND fbBlink_500ms.Pulse; //{layoutNum} \n')

    f.write('\n \n \n')


    f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.BCN1_{ae}_000_0000.Beacon_Green:=  SafetyOutput.EmergencyActivated.AE{ae}; \n')
    for layoutNum in epc_dict.keys():
        if epc_dict[layoutNum][-4:] == '0000':
             f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.{layoutNum}.PL_Green :=  SafetyOutput.EmergencyActivated.{epc_dict[layoutNum]}   AND SafetyOutput.EmergencyCircuitOk.AE{ae};    //{layoutNum} \n')
        else:
            f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.{layoutNum}.PL_Green :=  SafetyOutput.EmergencyActivated.{epc_dict[layoutNum]}   AND SafetyOutput.EmergencyCircuitOk.SG{epc_dict[layoutNum][7:10]};    //{layoutNum} \n')

    f.write('\n \n \n')

    f.write(f'PBL1_{ae}_000_0000.Light_Yellow := SafetyOutput.EmergencyActivated.AE{ae} OR \n')
    f.write(f'                ((SG_Error_Any OR SG_Safety_Error OR SafetyOutput.ResetRequest.PBL1_{ae}_000_0000)\n')
    f.write(f'                AND fbBlink_500ms.Pulse OR ToggleBit_PBL[1]); \n')

    f.write('\n \n \n')
    toggleBit = 2
    for pbl in pbl_dict.keys():

        if  pbl_dict[pbl].lower() == 'safety':
            if  pbl[-4:] == '0000':
                f.write(f'{pbl}.Light_Yellow	:= SafetyOutput.EmergencyActivated.AE{ae} OR (SafetyOutput.ResetRequest.{pbl} AND fbBlink_500ms.Pulse) OR ToggleBit_PBL[{toggleBit}]; \n')
            else:
                f.write(f'{pbl}.Light_Yellow	:= SafetyOutput.EmergencyActivated.EPC1{pbl[4:]} OR (SafetyOutput.ResetRequest.{pbl} AND fbBlink_500ms.Pulse) OR ToggleBit_PBL[{toggleBit}]; \n')
            toggleBit += 1

        elif pbl_dict[pbl].lower() == 'divert':

            f.write(f'{pbl}.Light_Yellow	:= (DivertError{pbl[4:]} AND fbBlink_500ms.Pulse) OR ToggleBit_PBL[{toggleBit}]; \n')
            toggleBit += 1


        elif pbl_dict[pbl].lower() == 'merge':

            f.write(f'{pbl}.Light_Yellow	:= (MergeError{pbl[4:]} AND fbBlink_500ms.Pulse) OR ToggleBit_PBL[{toggleBit}]; \n')
            toggleBit += 1


        elif pbl_dict[pbl].lower() == 'transfer':

            f.write(f'{pbl}.Light_Yellow	:= (TransferError{pbl[4:]} AND fbBlink_500ms.Pulse) OR ToggleBit_PBL[{toggleBit}]; \n')
            toggleBit += 1

        elif pbl_dict[pbl].lower() == 'placeholder':

            f.write(f'//{pbl}.Light_Yellow	:= (PlaceholderAlarm{pbl[4:]} AND fbBlink_500ms.Pulse) OR ToggleBit_PBL[{toggleBit}]; \n')
            toggleBit += 1







