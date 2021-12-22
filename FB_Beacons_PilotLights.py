
epc_dict = {
             #'BCN1_13_000_0000' : 'AE13',   hardcode it using the ae13 variable
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
ae = 13

with open('outputFB_Pilot_Beacon.txt', 'w') as f:
    for layoutNum in epc_dict.keys():
        f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.{layoutNum}.PL_Red :=  SafetyOutput.EmergencyActivated.{epc_dict[layoutNum]}  AND fbBlink_500ms.Pulse; \n')

        f.write('\n \n \n')

    for layoutNum in epc_dict.keys():
        f.write(f'Mapping_Cabinet_IO.AE{ae}_Panel.Outputs.{layoutNum}.PL_Green :=  SafetyOutput.EmergencyActivated.{epc_dict[layoutNum]}   AND SafetyOutput.EmergencyCircuitOk.{epc_dict[layoutNum][7:10]}; \n')
















