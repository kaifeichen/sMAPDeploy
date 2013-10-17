import re

def pathnamer(dev_name, obj_name):
    obj_name = re.sub('\.|:|_','/', obj_name, 2)
    obj_name = obj_name.replace(' ', '_')
    return '/%s/%s' % (dev_name, obj_name)

other_points = [
  'SDH.STEAM_FLOW',
  'SDH_OAT',

  'SDH.AH2_SDSP.STP',
  'SDH.AH2A-B.MIN_DUCT_STATIC_A-B',
  'SDH.AH2A-B.DUCT_STATIC_LOOPOUT',

  'SDH.AH2B.AH2B.RF_CFM',
  'SDH.AH2B.SF_CFM',
  'SDH.AH2B_CCV',
  'SDH.AH2B_EAD',
  'SDH.AH2B_ISO.DMPR',
  'SDH.AH2B_MAT',
  'SDH.AH2B_MIN.OAD',
  'SDH.AH2B_OAD',
  'SDH.AH2B_RAD',
  'SDH.AH2B_RAH',
  'SDH.AH2B_RAT',
  'SDH.AH2B_RDSP',
  'SDH.AH2B_SAT',
  'SDH.AH2B_SAT.STP',
  'SDH.AH2B_SDSP',
  'SDH.AH2B.SUP_AIR_TEMP_LOOPOUT',

  'SDH.AH2A.AH2B.RF_CFM',
  'SDH.AH2A.SF_CFM',
  'SDH.AH2A_CCV',
  'SDH.AH2A_EAD',
  'SDH.AH2A_ISO.DMPR',
  'SDH.AH2A_MAT',
  'SDH.AH2A_MIN.OAD',
  'SDH.AH2A_OAD',
  'SDH.AH2A_RAD',
  'SDH.AH2A_RAH',
  'SDH.AH2A_RAT',
  'SDH.AH2A_RDSP',
  'SDH.AH2A_SAT',
  'SDH.AH2A_SAT.STP',
  'SDH.AH2A_SDSP',
  'SDH.AH2A.SUP_AIR_TEMP_LOOPOUT',
  'SDH.AH2A.RTN_FAN_CFM_LOOPOUT',

  'SDH.AH1A_CCV',
  'SDH.AH1B_CCV',
  #'SDH.AH3_CCV',
  #'SDH.AH4_CCV',
  'SDH.SCHW.CHW.BYP_VLV',

  #'SDH.AH3_RM.TEMP',
  #'SDH.AH4_RM.TEMP',

  'SDH.AUDITORIUM_CO2',

  'SDH.HW.HE1_VLV',
  'SDH.HW.HE2_VLV',
  'SDH.HW.BYP_VLV',
  'SDH.HW_HWRT',
  'SDH.HW_HWST',
  'SDH.HW_HWST.STP',
  'SDH.HW_DP',
  'SDH.HW_DP.STP',

  'SDH.FCU-1:VLV 1 POS',

  'SDH.WIN.4FS6_TEMP.2',
  'SDH.WIN.4FS6_TEMP.3', 
  'SDH.WIN.4FS6_TEMP.4', 
  'SDH.WIN.4FS8_TEMP.2', 
  'SDH.WIN.5FS6_TEMP.2', 
  'SDH.WIN.6FS6_TEMP.2',
  'SDH.WIN.6FS6_TEMP.3', 
  'SDH.WIN.6FS7_TEMP.2',
  'SDH.WIN.7FS5_TEMP.2', 
  'SDH.WIN.7FS6_TEMP.2', 
  'SDH.WIN.7FS6_TEMP.3',

  'SDH.S4-16:AI 3',
  'SDH.AH1.3M88_DP',
  'SDH.AH1.5M88_DP',

  'SDH.FIRE_ALARM',
  'SDH.HAZMAT_ALARM',
  'SDH.REF.RFG_ALM',

  'SDH.ONICON_CHW.FLOW',
  'SDH.CHW1.FL.METER.1',
  'SDH.CHW1.FL.METER.2',
  'SDH.CHW1.FL.METER.3',
  'SDH.CHW1.FL.METER.4',
  'SDH.CHW1.FL.METER.5',
  'SDH.CHW1.FL.METER.6',
]

def filter(dev_name, obj_name):
  return (obj_name.endswith('VFD:POWER') or     \
     obj_name.endswith('VFD:INPUT REF 1') or    \
     obj_name.endswith('.PWR REAL 3P') or       \
     obj_name.endswith('.PWR REAL 3 P') or      \
     obj_name.endswith('.REACTIVE 3 P') or      \
     obj_name.endswith('.ENERGY TOTAL') or      \
     obj_name.endswith('.PWR FACTOR') or        \
     obj_name.endswith('.DEMAND') or            \
     obj_name.endswith('.REACTIVE PWR') or      \
     obj_name.endswith('.POWER FACTOR') or      \
     obj_name.endswith(':DEMAND') or            \
     obj_name.endswith(':REACTIVE PWR') or      \
     obj_name.endswith(':POWER FACTOR') or      \
     obj_name.endswith('_CT') or                \
     obj_name.endswith(':DMPR POS') or          \
     obj_name.endswith(':VLV POS') or           \
     obj_name.endswith(':ROOM TEMP') or         \
     obj_name.endswith(':HEAT.COOL') or         \
     obj_name.endswith(':AIR VOLUME') or        \
     obj_name.endswith(':CTL FLOW MIN') or      \
     obj_name.endswith(':CTL FLOW MAX') or      \
     obj_name.endswith(':CTL STPT') or          \
     obj_name.endswith(':CLG LOOPOUT') or       \
     obj_name.endswith(':HTG LOOPOUT') or       \
     obj_name.endswith('_RMT') or               \
     obj_name.endswith('_RMT.STP') or           \
     obj_name.endswith('_CWRT') or              \
     obj_name.endswith('_CWST') or              \
     obj_name.endswith('_CWST.STP') or          \
     obj_name.endswith('_CWST2') or             \
     obj_name.endswith('_CHWST') or             \
     obj_name.endswith('_CHWRT') or             \
     obj_name.endswith('_CCV') or             \
     obj_name.endswith('.FLOW') or              \
     obj_name.endswith('.REF.TEMP') or          \
     obj_name.endswith('.RESET') or             \
     obj_name.startswith('SDH.CW.BLOW.DOWN') or \
     obj_name.startswith('SDH.CW.MAKE.UP') or   \
     obj_name.endswith('VIBRATION.SW') or       \
     obj_name.endswith('CHW_DP') or             \
     obj_name.endswith('CHW_DP.STP') or         \
     obj_name.endswith('CHW.DP') or             \
     obj_name.endswith('CHW.DP.STP') or         \
     obj_name.endswith('ECHWT') or              \
     obj_name.endswith('ECWT') or               \
     obj_name.endswith('LCHWT') or              \
     obj_name.endswith('LCWT') or               \
     obj_name.endswith('LSCT') or               \
     obj_name.endswith('.LOAD') or              \
     obj_name.endswith('.TONS') or              \
     obj_name.endswith('.BYP_VLV') or           \
     obj_name.endswith('CHW_BYP.VLV') or        \
     obj_name.endswith('.CHW_DP') or            \
     obj_name.startswith('SDH.CHW_BYPASS') or   \
     obj_name.startswith('SDH.CITY.WATER') or   \
     obj_name.startswith('SDH.CW.BYP') or       \
     obj_name.startswith('SDH.ELA') or          \
     obj_name.startswith('SDH.WIN.') or         \
     #obj_name.endswith('_ALM') or               \
     #obj_name.endswith('.ALM') or               \
     (obj_name.startswith('SDH.RAH') and obj_name.endswith('.TEMP')) or  \
     (obj_name.startswith('SDH.RAH') and obj_name.endswith('.TEMP.STP')) or  \
     (obj_name.startswith('SDH.RAH') and obj_name.endswith('_SAT')) or  \
     (obj_name.startswith('SDH.RAH') and obj_name.endswith('_SAT.STP')) or  \
     (obj_name.startswith('SDH.RAH') and obj_name.endswith('_CFM')) or  \
     (obj_name.startswith('SDH.RAH') and obj_name.endswith('_CFM.STP')) or  \
     (obj_name.startswith('SDH.RAH') and obj_name.endswith('_OCCUPIED')) or  \
     (obj_name.startswith('SDH.RAH') and obj_name.endswith('.SF_SPD')) or  \
     obj_name in other_points) and not obj_name.startswith('SDH.AH3_CCV')
