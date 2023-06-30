from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting
from saleae.data import GraphTime, GraphTimeDelta
from MessageHandling import *

encoding_lookup = {
    0B0000: 0B11110,
    0B0001: 0B01001,
    0B0010: 0B10100,
    0B0011: 0B10101,
    0B0100: 0B01010,
    0B0101: 0B01011,
    0B0110: 0B01110,
    0B0111: 0B01111,
    0B1000: 0B10010,
    0B1001: 0B10011,
    0B1010: 0B10110,
    0B1011: 0B10111,
    0B1100: 0B11010,
    0B1101: 0B11011,
    0B1110: 0B11100,
    0B1111: 0B11101,
}

Preamble_LSB ={
    'preamble': [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
    'preamble_63': [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
}

addresses = {
    'SOP': [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    'SOP_prime': [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    'SOP_double_prime': [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    'Hard Reset': [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    'Cable Reset': [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    'SOP_prime_debug': [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
    'SOP_double_prime_debug': [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
}

EOP_LSB = {
    'EOP': [1,0,1,1,0],
}

data_commands = {
    0b00000: 'Reserved',
    0b00001: 'Source_Capabilities',
    0b00010: 'Request',
    0b00011: 'BIST',
    0b00100: 'Sink_Capabilities',
    0b00101: 'Battery_Status',
    0b00110: 'Alert',
    0b00111: 'Get_Country_Info',
    0b01000: 'Enter_USB',
    0b01001: 'EPR_Request',
    0b01010: 'EPR_Mode',
    0b01011: 'Source_Info',
    0b01100: 'Revision',
    0b01101: 'Reserved',
    0b01110: 'Reserved',
    0b01111: 'Vendor_Defined',
    0b10000: 'Reserved',
    0b10001: 'Reserved',
    0b10010: 'Reserved',
    0b10011: 'Reserved',
    0b10100: 'Reserved',
    0b10101: 'Reserved',
    0b10110: 'Reserved',
    0b10111: 'Reserved',
    0b11000: 'Reserved',
    0b11001: 'Reserved',
    0b11010: 'Reserved',
    0b11011: 'Reserved',
    0b11100: 'Reserved',
    0b11101: 'Reserved',
    0b11110: 'Reserved',
    0b11111: 'Reserved'
}

control_commands = {
    0b00000: 'Reserved',
    0b00001: 'GoodCRC',
    0b00010: 'GotoMin',
    0b00011: 'Accept',
    0b00100: 'Reject',
    0b00101: 'Ping',
    0b00110: 'PS_RDY',
    0b00111: 'Get_Source_Cap',
    0b01000: 'Get_Sink_Cap',
    0b01001: 'DR_Swap',
    0b01010: 'PR_Swap',
    0b01011: 'VCONN_Swap',
    0b01100: 'Wait',
    0b01101: 'Soft_Reset',
    0b01110: 'Data_Reset',
    0b01111: 'Data_Reset_Complete',
    0b10000: 'Not_Supported',
    0b10001: 'Get_Source_Cap_Extended',
    0b10010: 'Get_Status',
    0b10011: 'FR_Swap',
    0b10100: 'Get_PPS_Status',
    0b10101: 'Get_Country_Codes',
    0b10110: 'Get_Sink_Cap_extended',
    0b10111: 'Get_Source_Info',
    0b11000: 'Get_Revision',
    0b11001: 'Reserved',
    0b11010: 'Reserved',
    0b11011: 'Reserved',
    0b11100: 'Reserved',
    0b11101: 'Reserved',
    0b11110: 'Reserved',
    0b11111: 'Reserved',
}

power_port_role = {
    0: 'Sink',
    1: 'Source'
}
cable_plug = {
    0: 'from DFP or UFP',
    1: 'from cable plug'
}

revision = {
    0b00: '1.0',
    0b01: '2.0',
    0b10: '3.0',
    0b11: 'Reserved'
}

port_data_role = {
    0: 'UFP',
    1: 'DFP'
}

class Word():
    start_time = None
    end_time = None
    data = None

    def __init__(self, start_time, end_time, data):
        self.start_time = start_time
        self.end_time = end_time
        self.data = data

class Hla(HighLevelAnalyzer):

    result_types = {
        'preamble': {'format': 'Preamble'},
        
        'preamble_63': {'format': 'Preamble:first UI out of range'},

        'address': {'format': '{{data.address}}'},

        'header': {'format': '[Message Header][{{data.command_code}}]--Message ID: [{{data.message_id}}]--Number of Objects: [{{data.number_of_objects}}]--Spec Rev: [{{data.spec_revision}}]'},

        'source_fixed_supply_pdo': {'format': 'Obj:[{{data.index}}][{{data.raw}}] [{{data.pdo_type}}] [{{data.voltage_V}}V/{{data.maximum_current_A}}A]--DRP: [{{data.dual_role_power}}]--USB Suspend Supported: [{{data.usb_suspend_supported}}]--USB Communications Supported: [{{data.usb_communications_capable}}]--DRD: [{{data.dual_role_data}}]--Unchecked Ext. Messages Supported: [{{data.unchecked_extended_messages_supported}}]--Peak Current=[{{data.peak_current}}A]'},

        'source_variable_supply_pdo': {'format': 'Obj:[{{data.index}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}V]--Min_Voltage=[{{data.minimum_voltage_V}}V]--Max_Current=[{{data.maximum_current_A}}A]'},

        'source_battery_supply_pdo': {'format': 'Obj:[{{data.index}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}V]--Min_Voltage=[{{data.minimum_voltage_V}}V]--Max_allowable_power=[{{data.maximum_allowable_power_W}}W]'},

        'source_programmable_supply_pdo': {'format': 'Obj:[{{data.index}}][{{data.raw}}][{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}V]--Min_voltage=[{{data.minimum_voltage_V}}V]--Max_Current=[{{data.maximum_current_A}}A]'},

        'sink_fixed_supply_pdo': {'format': 'Obj:[{{data.index}}][{{data.raw}}] [{{data.pdo_type}}] Voltage=[{{data.voltage_V}}]V--Operational_Current=[{{data.operational_current_A}}]A--DRP: [{{data.dual_role_power}}]--USB Suspend Supported: [{{data.usb_suspend_supported}}]--Unconstrained Power: [{{data.unconstrained_power}}]--USB Communications Supported: [{{data.usb_communications_capable}}]--DRD: [{{data.dual_role_data}}]--FRS Required Current: [{{data.fast_role_swap_required_current}}]'},

        'sink_variable_supply_pdo': {'format': 'Obj:[{{data.index}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}V]--Min_Voltage=[{{data.minimum_voltage_V}}V]--Max_Current=[{{data.maximum_current_A}}A]'},

        'sink_battery_supply_pdo': {'format': 'Obj:[{{data.index}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}V]--Min_Voltage=[{{data.minimum_voltage_V}}V]--Max_allowable_power=[{{data.maximum_allowable_W}}W]'},

        'sink_programmable_supply_pdo': {'format': 'Obj:[{{data.index}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}V]--Min_voltage=[{{data.minimum_voltage_V}}V]; Max_current=[{{data.maximum_current_A}}A]'},

        'bist_bdo': {'format': '[{{data.data_object_type}}] [{{data.index}}] BIST Mode: {{data.bist_mode}}'},
        
        'bist_test_data': {'format': '[{{data.data_object_type}}] [{{data.index}}] [{{data.raw}}]'},

        'fixed_supply_rdo': {'format': 'Obj:[{{data.object_position}}] Operating_Current=[{{data.operating_current_A}}A]--Max_Operating_Current=[{{data.maximum_operating_current_A}}A]--Giveback Flag: [{{data.giveback_flag}}]--Capability Missmatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]'},
        
        'fixed_supply_rdo_giveback': {'format': 'Obj:[{{data.object_position}}] Operating_Current=[{{data.operating_current_A}}A]--Min_Operating_Current=[{{data.minimum_operating_current_A}}A--Giveback Flag: [{{data.giveback_flag}}]--Capability Missmatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]'},

        'variable_supply_rdo': {'format': 'Obj:[{{data.object_position}}] Operating_current=[{{data.operating_current_A}}A]--Max_operating_current=[{{data.maximum_operating_current_A}}A]--Giveback Flag: [{{data.giveback_flag}}]--Capability Missmatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]'},
        
        'variable_supply_rdo_giveback': {'format': 'Obj:[{{data.object_position}}] Operating_current=[{{data.operating_current_A}}A]--Min_operating_current=[{{data.minimum_operating_current_A}}A]--Giveback Flag: [{{data.giveback_flag}}]--Capability Missmatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]'},

        'battery_rdo': {'format': 'Obj:[{{data.object_position}}] Operating_Power=[{{data.operating_power_W}}W]--Max_Operating_Power=[{{data.maximum_operating_power_W}}W]--Giveback_flag: [{{data.giveback_flag}}]--Capability_mismatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]'},
        
        'battery_rdo_giveback': {'format': 'Obj:[{{data.object_position}}] Operating_Power=[{{data.operating_power_W}}W]--Min_Operating_Power=[{{data.minimum_operating_power_W}}W]--Giveback_flag: [{{data.giveback_flag}}]--Capability_mismatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]'},

        'programmable_supply_rdo': {'format': 'Obj: [{{data.object_position}}] Output_Voltage=[{{data.output_voltage_V}}V]--Operating_Current=[{{data.operating_current_A}}A]--Capability_mismatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]'},

        'structured_header_vdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.command}}]({{data.command_type}})--VDM_Type: [{{data.vdm_type}}]; SVID: [{{data.vendor_id}}]--VDM VER.: [{{data.structured_vdm_version}}]--OBJ_position: [{{data.object_position}}]'},

        'unstructured_header_vdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] Vendor_id: [{{data.vendor_id}}]--Vdm_type: [{{data.vdm_type}}]'},

        'bsdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] Battery Capacity: [{{data.battery_preset_Capacity_WH}}WH]--Invalid_battery_reference: [{{data.invalid_battery_reference}}]--Battery_present: [{{data.battery_present}}]--Battery_charging_status: [{{data.battery_charging_status}}]'},

        'ado': {'format': ']{{data.data_object_type}}] Fixed_batteries: [{{data.fixed_batteries}}]--hot_swappable_batteries: [{{data.hot_swappable_batteries}}]--Battery_status_change_event: [{{data.battery_status_change_event}}]--Ocp_event: [{{data.ocp_event}}]--Otp_event: [{{data.otp_event}}]--Operating_condition_change: [{{data.operating_condition_change}}]--Source_input_change: [{{data.source_input_change}}]--Ovp_event: [{{data.ovp_event}}]'},

        'ccdo': {'format': '[{{data.data_object_type}}] Country_code: [{{data.country_code}}]'},

        'eudo': {'format': '[{{data.data_object_type}}] Usb_mode:[{{data.usb_mode}}]--Usb4_drd:[{{data.usb4_drd}}]--Usb3_drd:[{{data.usb3_drd}}]--Cable_speed:[{{data.cable_speed}}]--Cable_type:[{{data.cable_type}}]--Cable_current:[{{data.cable_current}}]--Pcie_support:[{{data.pcie_support}}]--Dp_support:[{{data.dp_support}}]--TBT_support:[{{data.tbt_support}}]--Host_present:[{{data.host_present}}]'},

        'object': {'format': '[{{data.index}}] [{{data.data}}]'},

        'crc': {'format': 'CRC: {{data.crc}}'},

        'eop': {'format': '{{data.eop}}'},

        'error': { 'format': 'error: {{{data.error}}} [{{data.raw}}]' },
        
        'id_header_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] USB Capable as Host: [{{data.usb_communications_capable_as_usb_host}}]--USB capable as Device: [{{data.usb_communications_capable_as_usb_device}}]--Product Type UFP: [{{data.product_type_ufp}}]--Product Type DFP: [{{data.product_type_dfp}}]--Modal Operation Supported: [{{data.modal_operation_supported}}]--Connector Type: [{{data.connector_type}}]--USB vendor ID: [{{data.usb_vendor_id}}]'},
        
        'cert_stat_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}]'},
        
        'product_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] USB Product ID: [{{data.usb_product_id}}]--bcdDevice: [{{data.bcddevice}}]'},
        
        'ufp_vdo1': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.ufp_vdo1_ver}}] USB4 Device Capable:[{{data.usb4_capable}}]--USB3.2 Device Capable:[{{data.usb3_capable}}]--USB2 Device Capable(Billboard only):[{{data.usb2_capable_billboardonly}}]--USB2 Device Capable:[{{data.usb2_capable}}]--Connector Type:[{{data.ufp_vdo1_connector_type}}]--USB Highest Speed:[{{data.usb_highest_speed}}]--Support ALT Modes reconfigured the signals on USB2 except for TBT3:[{{data.supports_alt_modes_reconfigured_signals_on_usb2}}]--Support ALT Modes not reconfigured the signals on USB2:[{{data.supports_alt_modes_do_not_reconfigured_signals_on_usb2}}]--Support TBT3 ALT Mode:[{{data.support_tbt3_alt_mode}}]'},
        
        'ufp_vdo2': { 'format': '[{{data.data_object_type}}][{{data.raw}}] USB4 Min Power: [{{data.usb4_min_power}}W]--USB4 Max Power: [{{data.usb4_max_power}}W]--USB3 Min Power: [{{data.usb3_min_power}}W]--USB3 Max Power: [{{data.usb3_max_power}}W]'},
        
        'dfp_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.dfp_vdo_ver}}] USB4 Host Capable: [{{data.usb4_host_capable}}]--USB3.2 Host Capable: [{{data.usb3_host_capable}}]--USB2 Host Capable: [{{data.usb2_host_capable}}]--Connector Type: [{{data.dfp_vdo_connector_type}}]--Port Number: [{{data.port_number}}]'},
        
        'ama_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.vdo_version}}] HW Version: [{{data.hw_version}}]--FW Version: [{{data.fw_version}}]--Vconn Power: [{{data.vconn_power}}]--Vconn required: [{{data.vconn_required}}]--Vbus required: [{{data.vbus_required}}]--USB Highest Speed: [{{data.ama_usb_highest_speed}}]'},
        
        'vdp_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.vdo_version}}] HW Version: [{{data.hw_version}}]--FW Version: [{{data.fw_version}}]--Max_Vbus_Voltage: [{{data.maximum_vbus_voltage}}]--Charge Through Current Support: [{{data.charge_through_current_support}}]--Vbus Impedance: [{{data.vbus_impedance}}mohm]--Ground Impedance: [{{data.ground_impedance}}mohm]--Charge Through Support: [{{data.charge_through_support}}]'},
        
        'activecable_vdo1': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.vdo_version}}] HW Version: [{{data.hw_version}}]--FW Version: [{{data.fw_version}}]--Connector Type: [{{data.connector_type}}]--Cable Latency: [{{data.cable_latency}}]--Cable Termination Type: [{{data.cable_terminiation_type}}]--Max Vbus Voltage: [{{data.maximum_vbus_voltage}}]--SBU Supported: [{{data.sbu_supported}}]--SBU Type: [{{data.sbu_type}}]--Vbus Current Handling Capability: [{{data.vbus_current_handling_capability}}]--VBUS Through Cable: [{{data.vbus_through_cable}}]--SOP" Present: [{{data.sop_double_prime_controller_present}}]--USB Highest Speed: [{{data.usb_highest_speed}}]'},
        
        'activecable_vdo2': { 'format': '[{{data.data_object_type}}][{{data.raw}}] Maximum Operating Temperature: [{{data.maximum_operating_temperature}}]--Shutdown Temperature: {{data.shutdown_temperature}}]--U3/CLd Power: [{{data._u3cld_power}}]--U3toU0 transition mode: [{{data.u3tou0_transition_mode}}]--Physical connection: [{{data.physical_connection}}]--Active element: [{{data.active_element}}]--USB4 Supported: [{{data.usb4_supported}}]--USB2 Hub Hops Consumed: [{{data.usb2_hub_hops_consumed}}]--USB2 Supported: [{{data.usb2_supported}}]--USB3.2 Supported: [{{data.usb3_supported}}]--USB Lanes Supported: [{{data.usb_lanes_supported}}]--Optically Isolated Active Cable: [{{data.optically_isolated_active_cable}}]--USB Gen: [{{data.usb_gen}}'},
        
        'passivecable_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.vdo_version}}] HW Version: [{{data.hw_version}}]--FW Version: [{{data.fw_version}}]--Connector Type: [{{data.connector_type}}]--Cable Latency: [{{data.cable_latency}}]--Cable Termination Type: [{{data.cable_terminiation_type}}]--Max Vbus Voltage: [{{data.maximum_vbus_voltage}}]--Vbus Current Handling Capability: [{{data.vbus_current_handling_capability}}]--USB Highest Speed: [{{data.usb_highest_speed}}]'},
        
        'dsvid_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] SVID{{data.svidn_number}}: [{{data.svidn}}]--SVID{{data.svidn1_number}}: [{{data.svidn1}}]'},
        
        'dp_mode': { 'format': '[{{data.data_object_type}}][{{data.raw}}] Mode[{{data.mode_index}}]--UFP_D pin assignment: [{{data.ufp_d_pin_assignment_supported}}]--DFP_D pinassignment: [{{data.dfp_d_pin_assignment_supported}}]--USBr2.0 signaling not used: [{{data.usb2_signaling_not_used}}]--[{{data.receptacle_indication}}]--[{{data.signaling_for_transport_of_dp_protocol}}]--Port capability: [{{data.port_capability}}]'},
        
        'dp_status': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--HPD status: [{{data.hpd_state}}]--DFP/UFP connected: [{{data.dfp_ufp_connected}}]--[{{data.irq_hpd}}]--Exit DisplayPort mode request: [{{data.exit_dp_mode_request}}]--[{{data.usb_config_request}}]--[{{data.multifunction_preferred}}]--[{{data.enabled}}]--[{{data.power_low}}]'},
        
        'dp_configure': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--Configure UFP_U Pin Assignment: [{{data.configure_ufp_pin_assignment}}]--[{{data.signaling_for_transport_of_dp_protocol}}]--[{{data.select_configuration}}]'},
        
        'tbt_mode_adapter': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--[{{data.tbt_alt_mode}}]--[{{data.legacy_tbt_adapter}}]'},
        
        'tbt_mode_device': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--[{{data.tbt_alt_mode}}]--[{{data.legacy_tbt_adapter}}]--Vpro Avaliable: [{{data.vpro_avaliable}}]'},
        
        'tbt_cable_mode': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--[{{data.tbt_alt_mode}}]--Cable Speed: [{{data.cable_speed}}]--TBT Cable Gen: [{{data.tbt_cable_gen}}]--[{{data.cable_type}}]--[{{data.cable_active_passive}}]--[{{data.active_cable_plug_link_training}}]'},

        'tbt_enter_mode': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--[{{data.tbt_alt_mode}}]--Cable Speed: [{{data.cable_speed}}]--TBT Cable Gen: [{{data.tbt_cable_gen}}]--[{{data.cable_type}}]--[{{data.cable_active_passive}}]--[{{data.active_cable_plug_link_training}}]--[{{data.dfp_legacy_tbt_adapter}}]--[{{data.vpro_dock_and_host}}]'},
        
        'tbt_attention': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--Exit TBT Mode: [{{data.exit_tbt_mode_request}}]--USB2 Billboard Status: [{{data.usb2_billboard_status}}]--Legacy TBT mDP Cable Status: [{{data.legacy_tbt_mdp_cable_status}}]'},
        
    }

    def __init__(self):
        self.engine = None
        self.leftover_bits = []
        self.leftover_time=[]
        self.leftover_time_end=[]
        self.source_capabilities_pdo_types = {}

    def decode(self, frame: AnalyzerFrame):
        if self.engine is None:
            self.engine = self.state_machine()
            self.engine.send(None)

        try:
            output_frame = self.engine.send(frame)
            if output_frame is not None:
                return output_frame
        except StopIteration:
            self.engine = None

    def state_machine(self):
        next = None
        self.leftover_bits.clear()
        self.leftover_time.clear()
        self.leftover_time_end.clear()
        while True:
            while len(self.leftover_bits) < 64:
                yield from self.get_bits(64)
                if len(self.leftover_bits) >= 64:   
                    z=63
                    x=0
                    while x < z:
                        if float(self.leftover_time[x + 1]-self.leftover_time[x]) >= 4.7e-06:
                            del self.leftover_bits[:x+1]
                            del self.leftover_time[:x+1]
                            del self.leftover_time_end[:x+1]
                            x=0
                            z=len(self.leftover_bits)-1
                        else:
                            x=x+1  
            #
            preamble_cmd = self.decode_preamble(self.leftover_bits)
            if preamble_cmd == 'preamble_63':
                print('Preamble:first UI out of range')
                next = yield AnalyzerFrame('preamble_63', self.leftover_time[0], self.leftover_time_end[62],{'preamble_63':'first UI out of range'})
                self.leftover_bits = self.leftover_bits[63:]
                self.leftover_time = self.leftover_time[63:]
                self.leftover_time_end = self.leftover_time_end[63:]
                self.leftover_bits.append(next.data['data'])
                self.leftover_time.append(next.start_time)
                self.leftover_time_end.append(next.end_time)    
            elif preamble_cmd == 'preamble':
                print(preamble_cmd)
                next = yield AnalyzerFrame('preamble', self.leftover_time[0], self.leftover_time_end[63], {'preamble':preamble_cmd})
                self.leftover_bits = self.leftover_bits[64:]
                self.leftover_time = self.leftover_time[64:]
                self.leftover_time_end = self.leftover_time_end[64:]
                self.leftover_bits.append(next.data['data'])
                self.leftover_time.append(next.start_time)
                self.leftover_time_end.append(next.end_time)
            else:
                continue
            #
            yield from self.get_bits(20)
            address_cmd = self.decode_address(self.leftover_bits)
            print(address_cmd)
            next = yield AnalyzerFrame('address', self.leftover_time[0], self.leftover_time_end[19], {'address': address_cmd})
            self.leftover_bits = self.leftover_bits[20:]
            self.leftover_time = self.leftover_time[20:]
            self.leftover_time_end = self.leftover_time_end[20:]
            self.leftover_bits.append(next.data['data'])
            self.leftover_time.append(next.start_time)
            self.leftover_time_end.append(next.end_time)
            if address_cmd == 'Hard Reset' :
               continue
            if address_cmd == 'Cable Reset' :
               continue
            #
            yield from self.get_bits(20)
            header_decoded = self.bits_to_bytes(self.leftover_bits, 2)
            header_int = int.from_bytes(header_decoded, "little")
            object_count = (header_int >> 12) & 0x07
            header_data = self.decode_header(header_int, address_cmd)
            header_data['raw'] = hex(header_int)
            print('Message Header',':',header_data)
            next = yield AnalyzerFrame('header', self.leftover_time[0], self.leftover_time_end[19], header_data)
            self.leftover_bits = self.leftover_bits[20:]
            self.leftover_time = self.leftover_time[20:]
            self.leftover_time_end = self.leftover_time_end[20:]
            self.leftover_bits.append(next.data['data'])
            self.leftover_time.append(next.start_time)
            self.leftover_time_end.append(next.end_time)
            #
            VDO_header_command = []
            VDO_header_command_type = []
            product_type_ufp = []
            product_type_dfp = []
            n = 0
            SVID = []
            for object_index in range(1, object_count+1):
                yield from self.get_bits(40)
                object_decoded = self.bits_to_bytes(self.leftover_bits, 4)
                object_int = int.from_bytes(object_decoded, "little")
                data_object_data = {
                    'index': object_index, 'data': hex(object_int)}
                data_object_type = 'object'

                if header_data['command_code'] == 'Source_Capabilities':
                    frame_type, data_object_data = decode_source_power_data_object(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['index'] = object_index
                    data_object_data['raw'] = hex(object_int)
                    self.source_capabilities_pdo_types[object_index] = data_object_data['pdo_type']
                elif header_data['command_code'] == 'Request':
                    object_position = (object_int >> 28) & 0x7
                    if len(self.source_capabilities_pdo_types) >= object_position:
                        source_capabilities_pdo_type = self.source_capabilities_pdo_types[object_position]
                        frame_type, data_object_data = decode_request_data_object(
                            object_int, source_capabilities_pdo_type)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                    else:
                        data_object_type = 'error'
                        data_object_data = { 'error': '"Request" for object position "{}" did not exist in "Source_Capabilities"', 'raw': hex(object_int) }
                elif header_data['command_code'] == 'BIST':
                    frame_type, data_object_data = decode_bist_data_object(
                        object_int, object_index)
                    data_object_type = frame_type
                    data_object_data['index'] = object_index
                    data_object_data['raw'] = hex(object_int)
                elif header_data['command_code'] == 'Sink_Capabilities':
                    frame_type, data_object_data = decode_sink_power_data_object(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['index'] = object_index
                    data_object_data['raw'] = hex(object_int)
                elif header_data['command_code'] == 'Battery_Status':
                    frame_type, data_object_data = decode_battery_status_data_object(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['index'] = object_index
                    data_object_data['raw'] = hex(object_int)
                elif header_data['command_code'] == 'Alert':
                    frame_type, data_object_data = decode_alert_data_object(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['index'] = object_index
                    data_object_data['raw'] = hex(object_int)
                elif header_data['command_code'] == 'Get_Country_Info':
                    frame_type, data_object_data = decode_get_country_info_data_object(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['index'] = object_index
                    data_object_data['raw'] = hex(object_int)
                elif header_data['command_code'] == 'Enter_USB':
                    frame_type, data_object_data = decode_enter_usb_data_object(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['index'] = object_index
                    data_object_data['raw'] = hex(object_int)
                elif header_data['command_code'] == 'Vendor_Defined' and object_index == 1:
                    frame_type, data_object_data = decode_vendor_header_data_object(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['index'] = object_index
                    data_object_data['raw'] = hex(object_int)
                    if data_object_type == 'structured_header_vdo':
                        VDO_header_command = data_object_data['command']
                        VDO_header_command_type = data_object_data['command_type']
                        SVID = data_object_data['vendor_id']
                elif VDO_header_command == 'Discover Identity' and VDO_header_command_type == 'ACK':
                    if object_index == 2:
                        frame_type, data_object_data = decode_id_header_data_object(
                            object_int, address_cmd)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                        product_type_ufp = data_object_data['product_type_ufp']
                        product_type_dfp = data_object_data['product_type_dfp']
                    elif object_index == 3:
                        frame_type, data_object_data = decode_cert_stat_vdo(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                    elif object_index == 4:
                        frame_type, data_object_data = decode_product_vdo(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                    elif object_index == 5:
                        if product_type_ufp == 'PDUSB Hub' or product_type_ufp == 'PDUSB Peripheral':
                            frame_type, data_object_data = decode_ufp_vdo1(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                        elif product_type_ufp == 'Alternate Mode Adapter':
                            frame_type, data_object_data = decode_ama_vdo(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                        elif product_type_ufp == 'VCONN-Powered USB Device':
                            frame_type, data_object_data = decode_vdp_vdo(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                        elif product_type_ufp == 'Active Cable':
                            frame_type, data_object_data = decode_activecable_vdo1(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                        elif product_type_ufp == 'Passive Cable':
                            frame_type, data_object_data = decode_passivecable_vdo(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                    elif object_index == 6:
                        if product_type_ufp == 'PDUSB Hub' or product_type_ufp == 'PDUSB Peripheral':
                            frame_type, data_object_data = decode_ufp_vdo2(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                        elif product_type_ufp == 'Active Cable':
                            frame_type, data_object_data = decode_activecable_vdo2(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                    elif object_index == 7:
                        if product_type_dfp == 'PDUSB Hub' or product_type_dfp == 'PDUSB Host' or product_type_dfp == 'Power Brick':
                            frame_type, data_object_data = decode_dfp_vdo(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                elif VDO_header_command == 'Discover SVIDs' and VDO_header_command_type == 'ACK':    
                    frame_type, data_object_data, n = decode_dsvid_vdo(
                        object_int, n)
                    data_object_type = frame_type
                    data_object_data['raw'] = hex(object_int) 
                elif VDO_header_command == 'Discover Modes' and VDO_header_command_type == 'ACK' and SVID == '0xff01' and object_index == 2 :    
                    frame_type, data_object_data, n = decode_dp_mode(
                        object_int, n)
                    data_object_type = frame_type
                    data_object_data['mode_index'] = n
                    data_object_data['raw'] = hex(object_int)   
                elif VDO_header_command == 'DisplayPort Status update' and SVID == '0xff01' and object_index == 2 :    
                    frame_type, data_object_data = decode_dp_status(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['raw'] = hex(object_int)
                elif VDO_header_command == 'DisplayPort Configure' and SVID == '0xff01' and object_index == 2 :    
                    frame_type, data_object_data = decode_dp_configure(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['raw'] = hex(object_int)
                elif VDO_header_command == 'Discover Modes' and VDO_header_command_type == 'ACK' and SVID == '0x8087' and object_index == 2 :    
                    frame_type, data_object_data = decode_tbt_mode(
                        object_int, address_cmd)
                    data_object_type = frame_type
                    data_object_data['raw'] = hex(object_int)
                elif VDO_header_command == 'Enter Mode' and VDO_header_command_type == 'REQ' and SVID == '0x8087' and object_index == 2 :    
                    frame_type, data_object_data = decode_tbt_enter_mode(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['raw'] = hex(object_int)
                elif VDO_header_command == 'Attention' and VDO_header_command_type == 'REQ' and SVID == '0x8087' and object_index == 2 :    
                    frame_type, data_object_data = decode_tbt_attention(
                        object_int)
                    data_object_type = frame_type
                    data_object_data['raw'] = hex(object_int)

                print(data_object_data)
                next = yield AnalyzerFrame(data_object_type, self.leftover_time[0], self.leftover_time_end[39], data_object_data)
                self.leftover_bits = self.leftover_bits[40:]
                self.leftover_time = self.leftover_time[40:]
                self.leftover_time_end = self.leftover_time_end[40:]
                self.leftover_bits.append(next.data['data'])
                self.leftover_time.append(next.start_time)
                self.leftover_time_end.append(next.end_time)
            #
            yield from self.get_bits(40)
            crc_decoded = self.bits_to_bytes(self.leftover_bits, 4)
            crc_int = int.from_bytes(crc_decoded, "little")
            print('crc {crc}'.format(crc=hex(crc_int)))
            next = yield AnalyzerFrame('crc', self.leftover_time[0], self.leftover_time_end[39], {'crc': hex(crc_int)})
            self.leftover_bits = self.leftover_bits[40:]
            self.leftover_time = self.leftover_time[40:]
            self.leftover_time_end = self.leftover_time_end[40:]
            self.leftover_bits.append(next.data['data'])
            self.leftover_time.append(next.start_time)
            self.leftover_time_end.append(next.end_time)
            #
            #
            yield from self.get_bits(5)
            eop_cmd = self.decode_eop(self.leftover_bits)
            print(eop_cmd)
            next = yield AnalyzerFrame('eop', self.leftover_time[0], self.leftover_time_end[4], {'eop': eop_cmd})
            self.leftover_bits = self.leftover_bits[5:]
            self.leftover_time = self.leftover_time[5:]
            self.leftover_time_end = self.leftover_time_end[5:]
            self.leftover_bits.append(next.data['data'])
            self.leftover_time.append(next.start_time)
            self.leftover_time_end.append(next.end_time)


    def get_bits(self, num_bits):
        bits_needed = int(num_bits - len(self.leftover_bits))
        if bits_needed == 0:

            return Word(self.leftover_time, self.leftover_time_end, self.leftover_bits)
        else:       
            for x in range(bits_needed):
                frame = yield
                #print(frame.data)
                self.leftover_bits.append(frame.data['data'])
                self.leftover_time.append(frame.start_time)
                self.leftover_time_end.append(frame.end_time)
            return Word(self.leftover_time, self.leftover_time_end, self.leftover_bits)

    def bits_to_bytes(self, new_bits, num_bytes):
        decoded = bytearray(num_bytes)
        for i in range(num_bytes):
            fiver = new_bits[:5]
            nibble = self.decode5bits(fiver)
            new_bits = new_bits[5:]
            decoded[i] = nibble
            nibble = self.decode5bits(new_bits[:5])
            new_bits = new_bits[5:]
            decoded[i] |= nibble << 4
        return decoded

    def decode5bits(self, bit_array):
        raw_word = 0
        for i in range(5):
            raw_word = raw_word | (bit_array[i] << i)
        new_word = -1
        for entry in encoding_lookup:
            if encoding_lookup[entry] == raw_word:
                new_word = entry
                break
        if new_word == -1:
            new_word = 0
        return new_word

    def decode_preamble(self, bits):
        for preamble in Preamble_LSB:
            raw_preamble = Preamble_LSB[preamble]
            match = True
            if bits[0]==0:
                for i in range(64):
                    if bits[i] != raw_preamble[i]:
                        match = False
                if match == True:
                    return preamble
            elif bits[0]==1:
                for i in range(63):
                    if bits[i] != raw_preamble[i]:
                        match = False
                if match == True:
                    return preamble
        return 'Unknown Start'


    def decode_address(self, bits):
        for address in addresses:
            raw_address = addresses[address]
            fiddle_sop = []
            for word in range(4):
                for bit in range(5):
                    fiddle_sop.append(raw_address[word * 5 + 4 - bit])
            match = True
            for i in range(20):
                if bits[i] != fiddle_sop[i]:
                    match = False
            if match == True:
                return address
        return 'Unknown adderess*'

    def decode_header(self, header, sop_type):
        number_of_objects = (header >> 12) & 0x07
        message_id = (header >> 9) & 0x07
        spec_revision = (header >> 6) & 0x03
        spec_revision = revision[spec_revision]
        command_code = header & 0x1F
        if number_of_objects == 0:
            if command_code in control_commands:
                command_code = control_commands[command_code]
        else:
            if command_code in data_commands:
                command_code = data_commands[command_code]

        data = {
            'command_code': str(command_code),
            'number_of_objects': number_of_objects,
            'message_id': message_id,
            'spec_revision': str(spec_revision),
        }

        if sop_type == 'SOP':
            _power_port_role = (header >> 8) & 0x01
            _port_data_role = (header >> 5) & 0x01
            data['power_port_role'] = power_port_role[_power_port_role]
            data['port_data_role'] = port_data_role[_port_data_role]
        else:
            _cable_plug = (header >> 8) & 0x01
            data['cable_plug'] = cable_plug[_cable_plug]
        return data

    def decode_eop(self, bits):
        for EOP in EOP_LSB:
            raw_eop = EOP_LSB[EOP]
            match = True
            for i in range(5):
                if bits[i] != raw_eop[i]:
                    match = False
            if match == True:
                return EOP
        return 'Unknown END'