

## config var
epc_dict = {

             'EPC_1E33001H' : 'EPC_13_100_0040',
             'EPC_133001X'  : 'EPC_13_100_0110',
             'EPC_133019C'  : 'EPC_13_100_0235',
             'EPC_130038J'  : 'EPC_13_101_0040',
             'EPC_133036J'  : 'EPC_13_102_0040',
             'EPC_133034J'  : 'EPC_13_103_0040',
             'EPC_133032J'  : 'EPC_13_104_0040',
             'EPC_133030J'  : 'EPC_13_105_0040',
             'EPC_133028H'  : 'EPC_13_106_0040',
             'EPC_133026H'  : 'EPC_13_107_0040',
             'EPC_133024H'  : 'EPC_13_108_0040',
             'EPC_133022H'  : 'EPC_13_109_0040',
             'EPC_133020J'  : 'EPC_13_110_0040',
             'EPC_133060 '  : 'EPC_13_601_0065',
             'EPC_133050 '  : 'EPC_13_600_0100',
             'EPC_133075D'  : 'EPC_13_700_0025',
             'EPC_133070 '  : 'EPC_13_701_0035'
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


ae = 13



#######
with open('outputFB_Pilot_Beacon.txt', 'w') as f:


    f.write(f'EmergencyCircuitOK_All := SafetyOutput.EmergencyCircuitOk.AE{ae} \n')
    for sg in sg_List:
        if sg == sg_List[-1]:
            f.write(f'                AND SafetyOutput.EmergencyCircuitOk.SG{sg}; \n \n \n \n ')
        else:
            f.write(f'                AND SafetyOutput.EmergencyCircuitOk.SG{sg} \n ')







    f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.BCN1_{ae}_000_0000.Beacon_Red:=  SafetyOutput.EmergencyActivated.AE{ae}  AND fbBlink_500ms.Pulse; \n')
    for layoutNum in epc_dict.keys():
        f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.{layoutNum}.PL_Red :=  SafetyOutput.EmergencyActivated.{epc_dict[layoutNum]}  AND fbBlink_500ms.Pulse; \n')

    f.write('\n \n \n')


    f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.BCN1_{ae}_000_0000.Beacon_Green:=  SafetyOutput.EmergencyActivated.AE{ae}; \n')
    for layoutNum in epc_dict.keys():
        f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.{layoutNum}.PL_Green :=  SafetyOutput.EmergencyActivated.{epc_dict[layoutNum]}   AND SafetyOutput.EmergencyCircuitOk.{epc_dict[layoutNum][7:10]}; \n')
















