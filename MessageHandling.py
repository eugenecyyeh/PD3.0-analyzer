
pdo_type = {
    0b00: 'Fixed Supply',
    0b01: 'Battery',
    0b10: 'Variable Supply',
    0b11: 'Augmented Power Data Object',
}
augmented_pdo_type = {
    0b00: 'SPR Programmable Power Supply',
    0b01: 'EPR Adjustable Voltage Supply',
    0b10: 'Reserved',
    0b11: 'Reserved',
}

fixed_supply_sink_fast_role_swap_required_current = {
    0b00: 'Fast Swap not supported',
    0b01: 'Default USB Power',
    0b10: '1.5A @ 5V',
    0b11: '3.0A @ 5V',
}

bist_modes = {
    0b0000: 'Reserved',
    0b0001: 'Reserved',
    0b0010: 'Reserved',
    0b0011: 'Reserved',
    0b0100: 'Reserved',
    0b0101: 'BIST Carrier Mode',
    0b0110: 'Reserved',
    0b0111: 'Reserved',
    0b1000: 'BIST Test Data',
    0b1001: 'BIST Shared Test Mode Entry',
    0b1010: 'BIST Shared TestMode Exit',
    0b1011: 'Reserved',
    0b1100: 'Reserved',
    0b1101: 'Reserved',
    0b1110: 'Reserved',
    0b1111: 'Reserved',
}

vdm_type = {
    0b0: 'Unstructured VDM',
    0b1: 'Structured VDM',
}

structured_vdm_version_major = {
    0b00: 'Version 1.0',
    0b01: 'Version 2.0',
    0b10: 'Reserved',
    0b11: 'Reserved',
}

structured_vdm_version_minor = {
    0b00: 'Version 2.0',
    0b01: 'Version 2.1',
    0b10: 'Reserved',
    0b11: 'Reserved',
}

vdo_object_position = {
    0b000: 'Reserved',
    0b001: 1,
    0b010: 2,
    0b011: 3,
    0b100: 4,
    0b101: 5,
    0b110: 6,
    0b111: 'Exit all Active Modes',
}

vdo_command_type = {
    0b00: 'REQ',
    0b01: 'ACK',
    0b10: 'NAK',
    0b11: 'BUSY',
}

battery_charging_status = {
    0b00: 'Battery is Charging',
    0b01: 'Battery is Discharging',
    0b10: 'Battery is Idle',
    0b11: 'Reserved',
}

vdo_command= {
    0b00000: 'Reserved',
    0b00001: 'Discover Identity',
    0b00010: 'Discover SVIDs',
    0b00011: 'Discover Modes',
    0b00100: 'Enter Mode',
    0b00101: 'Exit Mode',
    0b00110: 'Attention',
    0b00111: 'Reserved',
    0b01000: 'Reserved',
    0b01001: 'Reserved',
    0b01010: 'Reserved',
    0b01011: 'Reserved',
    0b01100: 'Reserved',
    0b01101: 'Reserved',
    0b01110: 'Reserved',
    0b01111: 'Reserved',
    0b10000: 'DisplayPort Status update',
    0b10001: 'DisplayPort Configure',
    0b10010: 'SVID Specific Command [18]',
    0b10011: 'SVID Specific Command [19]',
    0b10100: 'SVID Specific Command [20]',
    0b10101: 'SVID Specific Command [21]',
    0b10110: 'SVID Specific Command [22]',
    0b10111: 'SVID Specific Command [23]',
    0b11000: 'SVID Specific Command [24]',
    0b11001: 'SVID Specific Command [25]',
    0b11010: 'SVID Specific Command [26]',
    0b11011: 'SVID Specific Command [27]',
    0b11100: 'SVID Specific Command [28]',
    0b11101: 'SVID Specific Command [29]',
    0b11110: 'SVID Specific Command [30]',
    0b11111: 'SVID Specific Command [31]'
}

usb_mode = {
    0b000: 'USB 2.0',
    0b001: 'USB 3.2',
    0b010: 'USB 4',
    0b011: 'Reserved',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

cable_speed = {
    0b000: 'USB2.0',
    0b001: 'USB3.1 Gen1',
    0b010: 'USB3.2 Gen2/USB4 Gen2',
    0b011: 'USB4 Gen3',
    0b100: 'USB4 Gen4',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

cable_type = {
    0b00: 'Passive',
    0b01: 'Active Re-timer',
    0b10: 'Active Re-driver',
    0b11: 'Optically Isolated',
}

cable_current = {
    0b00: 'Vbus not supported',
    0b01: 'Reserved',
    0b10: '3A',
    0b11: '5A',
}

usb4_drd = {
    0b0: 'Not capable of operating as a USB4 Device',
    0b1: 'Capable of operating as a USB4 Device',
}

usb3_drd = {
    0b0: 'Not capable of operating as a USB3.2 Device',
    0b1: 'Capable of operating as a USB3.2 Device',
}

product_type_ufp_sop = {
    0b000: 'Not a UFP',
    0b001: 'PDUSB Hub',
    0b010: 'PDUSB Peripheral',
    0b011: 'PSD',
    0b100: 'Reserved',
    0b101: 'Alternate Mode Adapter',
    0b110: 'VCONN-Powered USB Device',
    0b111: 'Reserved',
}

product_type_ufp_sop_prime = {
    0b000: 'Undefined',
    0b001: 'Reserved',
    0b010: 'Reserved',
    0b011: 'Passive Cable',
    0b100: 'Active Cable',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

product_type_dfp_sop = {
    0b000: 'Not a DFP',
    0b001: 'PDUSB Hub',
    0b010: 'PDUSB Host',
    0b011: 'Power Brick',
    0b100: 'Alternate Mode Controller',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

connector_type = {
    0b00: 'Reserved, for compatibility with legacy systems',
    0b01: 'Reserved',
    0b10: 'USB Type-C Receptacle',
    0b11: 'USB Type-C Plug',
}

product_vdo_ver = {
    0b000: 'Reserved',
    0b001: 'Ver.1.1',
    0b010: 'Ver.1.2',
    0b011: 'Reserved',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

product_vdo_connector_type = {
    0b00: 'Reserved',
    0b01: 'Reserved',
    0b10: 'USB Type-C Receptacle',
    0b11: 'USB Type-C Captive Plug',
}

usb_highest_speed = {
    0b000: 'USB2.0 Only',
    0b001: 'USB3.2 Gen1',
    0b010: 'USB3.2 Gen2/USB4 Gen2',
    0b011: 'USB4 Gen3',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

ama_vdo_ver = {
    0b000: 'Ver.1.0',
    0b001: 'Reserved',
    0b010: 'Reserved',
    0b011: 'Reserved',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

vconn_power = {
    0b000: '1W',
    0b001: '1.5W',
    0b010: '2W',
    0b011: '3W',
    0b100: '4W',
    0b101: '5W',
    0b110: '6W',
    0b111: 'Reserved',
}

yesno = {
    0b0: 'No',
    0b1: 'Yes',
}

ama_usb_highest_speed = {
    0b000: 'USB2 Only',
    0b001: 'USB3.2 Gen1 and USB2',
    0b010: 'USB3.2 Gen1/Gen2 and USB2',
    0b011: 'USB2 billboard only',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

maximum_vbus_voltage = {
    0b00: '20V',
    0b01: '30V',
    0b10: '40V',
    0b11: '50V',
}

cable_connector_type = {
    0b00: 'Reserved',
    0b01: 'Reserved',
    0b10: 'USB Type-C',
    0b11: 'Captive',
}

activecable_latency = {
    0b0000: 'Reserved',
    0b0001: '<10ns(1m)',
    0b0010: '10ns~20ns(2m)',
    0b0011: '20ns~30ns(3m)',
    0b0100: '30ns~40ns(4m)',
    0b0101: '40ns~50ns(5m)',
    0b0110: '50ns~60ns(6m)',
    0b0111: '60ns~70ns(7m)',
    0b1000: '1000ns(100m)',
    0b1001: '2000ns(200m)',
    0b1010: '3000ns(300m)',
    0b1011: 'Reserved',
    0b1100: 'Reserved',
    0b1101: 'Reserved',
    0b1110: 'Reserved',
    0b1111: 'Reserved',
}

passivecable_latency = {
    0b0000: 'Reserved',
    0b0001: '<10ns(1m)',
    0b0010: '10ns~20ns(2m)',
    0b0011: '20ns~30ns(3m)',
    0b0100: '30ns~40ns(4m)',
    0b0101: '40ns~50ns(5m)',
    0b0110: '50ns~60ns(6m)',
    0b0111: '60ns~70ns(7m)',
    0b1000: '>70ns(>7m)',
    0b1001: 'Reserved',
    0b1010: 'Reserved',
    0b1011: 'Reserved',
    0b1100: 'Reserved',
    0b1101: 'Reserved',
    0b1110: 'Reserved',
    0b1111: 'Reserved',
}

vbus_current_handling_capability = {
    0b00: 'USB Type-C Default current',
    0b01: '3A',
    0b10: '5A',
    0b11: 'Reserved',
}

u3cld_power = {
    0b000: '>10mW',
    0b001: '5~10mW',
    0b010: '1~5mW',
    0b011: '0.5~1mW',
    0b100: '0.2~0.5mW',
    0b101: '50~200µW',
    0b110: '<50µW',
    0b111: 'Reserved',
}

svid_mode = {
    0xFF01: 'VESA/DisplayPort',
    0x8087: 'Thunderbolt',
}

port_capability = {
    0b00: 'Reserved',
    0b01: 'UFP_D capable',
    0b10: 'DFP_D capable',
    0b11: 'DFP_D and UFP_D capable',
}

dfp_ufp_connected = {
    0b00: 'Neither DFP_D nor UFP_D is connected',
    0b01: 'DFP_D is connected',
    0b10: 'UFP_D is connected',
    0b11: 'Both DFP_D and UFP_D are connected',
}

configure_ufp_pin_assignment = {
    0b00000000: 'De-select',
    0b00000001: 'A',
    0b00000010: 'B',
    0b00000100: 'C',
    0b00001000: 'D',
    0b00010000: 'E',
    0b00100000: 'F',
}

signaling_for_transport_of_dp_protocol = {
    0b0000: 'Signaling unspecified',
    0b0001: 'Select DP v1.3 signaling rates and electrical settings',
    0b0010: 'Select Gen 2 signaling rates and electrical specifications',
    0b0011: 'Reserved',
    0b0100: 'Reserved',
    0b0101: 'Reserved',
    0b0110: 'Reserved',
    0b0111: 'Reserved',
    0b1000: 'Reserved',
    0b1001: 'Reserved',
    0b1010: 'Reserved',
    0b1011: 'Reserved',
    0b1100: 'Reserved',
    0b1101: 'Reserved',
    0b1110: 'Reserved',
    0b1111: 'Reserved',
}

select_configuration = {
    0b00: 'Set configuration for USB',
    0b01: 'Set configuration for UFP_U as DFP_D',
    0b10: 'Set configuration for UFP_U as UFP_D',
    0b11: 'Reserved',
}

legacy_tbt_mdp_cable_status = {
    0b00: 'No Cable connected',
    0b01: 'TBT Cable',
    0b10: 'DP Cable',
    0b11: 'Other Cable/Adapter',
}


def decode_source_power_data_object(word):
    data = {
        'data_object_type': 'PDO'
    }
    frame_type = 'object'
    _pdo_type = (word >> 30) & 0x3
    pdo_type_str = pdo_type[_pdo_type]
    if _pdo_type == 0b11:
        _augmented_pdo_type = (word >> 28) & 0x3
        pdo_type_str = str(augmented_pdo_type[_augmented_pdo_type])
        if _augmented_pdo_type == 0b00:
            pps_power_limited = (word >> 27) & 0x1
            maximum_voltage = int((word >> 17) & 0xFF)*0.1
            minimum_voltage = int((word >> 8) & 0xFF)*0.1
            maximum_current = int(word & 0x7F)*0.05
            data['maximum_voltage_V'] = maximum_voltage
            data['minimum_voltage_V'] = minimum_voltage
            data['maximum_current_A'] = maximum_current
            frame_type = 'source_programmable_supply_pdo'
    else:
        if _pdo_type == 0b00:
            dual_role_power = (word >> 29) & 0x1
            usb_suspend_supported = (word >> 28) & 0x1
            unconstrained_power = (word >> 27) & 0x1
            usb_communications_capable = (word >> 26) & 0x1
            dual_role_data = (word >> 25) & 0x1
            unchecked_extended_messages_supported = (word >> 24) & 0x1
            epr_mode_capable = (word >> 23) & 0x1
            peak_current = (word >> 20) & 0x3
            voltage = int((word >> 10) & 0x3FF) * 0.05
            maximum_current = int((word & 0x3FF)) * 0.01
            data['dual_role_power'] = dual_role_power
            data['usb_suspend_supported'] = usb_suspend_supported
            data['unconstrained_power'] = unconstrained_power
            data['usb_communications_capable'] = usb_communications_capable
            data['dual_role_data'] = dual_role_data
            data['unchecked_extended_messages_supported'] = unchecked_extended_messages_supported
            data['peak_current'] = peak_current
            data['voltage_V'] = voltage
            data['maximum_current_A'] = maximum_current

            frame_type = 'source_fixed_supply_pdo'

        elif _pdo_type == 0b10:
            maximum_voltage = int((word >> 20) & 0x3FF) * 0.05
            minimum_voltage = int((word >> 10) & 0x3FF) * 0.05
            maximum_current = int(word & 0x3FF) * 0.01
            data['maximum_voltage_V'] = maximum_voltage
            data['minimum_voltage_V'] = minimum_voltage
            data['maximum_current_A'] = maximum_current
            frame_type = 'source_variable_supply_pdo'
        elif _pdo_type == 0b01:
            maximum_voltage_50mv_units = int((word >> 20) & 0x3FF) * 0.05
            minimum_voltage_50mv_units = int((word >> 10) & 0x3FF) * 0.05
            maximum_allowable_power = int(word & 0x3FF) * 0.25
            data['maximum_voltage_V'] = maximum_voltage
            data['minimum_voltage_V'] = minimum_voltage
            data['maximum_allowable_power_W'] = maximum_allowable_power
            frame_type = 'source_battery_supply_pdo'

    data['pdo_type'] = pdo_type_str

    return frame_type, data

def decode_sink_power_data_object(word):
    data = {
        'data_object_type': 'PDO-Sink'
    }
    frame_type = 'object'

    _pdo_type = (word >> 30) & 0x3
    pdo_type_str = pdo_type[_pdo_type]
    if _pdo_type == 0b11:
        _augmented_pdo_type = (word >> 28) & 0x3
        pdo_type_str = augmented_pdo_type[_augmented_pdo_type]
        if _augmented_pdo_type == 0b00:
            maximum_voltage_V = int((word >> 17) & 0xFF) * 0.1
            minimum_voltage_V = int((word >> 8) & 0xFF) * 0.1
            maximum_current_A = int(word & 0x7F) * 0.05
            data['maximum_voltage_V'] = maximum_voltage_V
            data['minimum_voltage_V'] = minimum_voltage_V
            data['maximum_current_A'] = maximum_current_A
            frame_type = 'sink_programmable_supply_pdo'
        elif _augmented_pdo_type == 0b11:
            maximum_voltage_V = int((word >> 17) & 0x1FF) * 0.1
            minimum_voltage_V = int((word >> 8) & 0xFF) * 0.1
            pd_power_W = int(word & 0xFF) * 1
            data['maximum_voltage_V'] = maximum_voltage_V
            data['minimum_voltage_V'] = minimum_voltage_V
            data['pd_power_W'] = pd_power_W
            frame_type = 'sink_programmable_supply_pdo'
    else:
        if _pdo_type == 0b00:
            dual_role_power = (word >> 29) & 0x1
            usb_suspend_supported = (word >> 28) & 0x1
            unconstrained_power = (word >> 27) & 0x1
            usb_communications_capable = (word >> 26) & 0x1
            dual_role_data = (word >> 25) & 0x1
            fast_role_swap_required_current = (word >> 23) & 0x3
            voltage_V = int((word >> 10) & 0x3FF) * 0.05
            operational_current_A = int(word & 0x3FF) * 0.01
            data['dual_role_power'] = dual_role_power
            data['usb_suspend_supported'] = usb_suspend_supported
            data['unconstrained_power'] = unconstrained_power
            data['usb_communications_capable'] = usb_communications_capable
            data['dual_role_data'] = dual_role_data
            data['fast_role_swap_required_current'] = fixed_supply_sink_fast_role_swap_required_current[fast_role_swap_required_current]
            data['voltage_V'] = voltage_V
            data['operational_current_A'] = operational_current_A
            frame_type = 'sink_fixed_supply_pdo'

        elif _pdo_type == 0b10:
            maximum_voltage_V = int((word >> 20) & 0x3FF) * 0.05
            minimum_voltage_V = int((word >> 10) & 0x3FF) * 0.05
            maximum_current_A = int(word & 0x3FF) * 0.01
            data['maximum_voltage_V'] = maximum_voltage_V
            data['minimum_voltage_V'] = minimum_voltage_V
            data['maximum_current_A'] = maximum_current_A
            frame_type = 'sink_variable_supply_pdo'
        elif _pdo_type == 0b01:
            maximum_voltage_V = int((word >> 20) & 0x3FF) * 0.05
            minimum_voltage_V = int((word >> 10) & 0x3FF) * 0.05
            maximum_allowable_power_W = int(word & 0x3FF) * 0.25
            data['maximum_voltage_V'] = maximum_voltage_V
            data['minimum_voltage_V'] = minimum_voltage_V
            data['maximum_allowable_W'] = maximum_allowable_power_W
            frame_type = 'sink_battery_supply_pdo'

    data['pdo_type'] = pdo_type_str

    return frame_type, data

def decode_bist_data_object(word, object_index):
    if object_index == 1:
        data = {
            'data_object_type': 'BIST Data Object'
        }
        frame_type = 'bist_bdo'
        bist_mode = (word >> 28) & 0xF
        data['bist_mode'] = bist_modes[bist_mode] 
    else:
        data = {
            'data_object_type': 'BIST Test Data'
        }
        frame_type = 'bist_test_data'
    return frame_type, data

def decode_request_data_object(word, pdo_type):
    data = {
        'data_object_type': 'Request Data Object'
    }
    frame_type = 'object'
    if pdo_type == 'Fixed Supply' or pdo_type == 'Variable Supply':
        object_position = (word >> 28) & 0x7
        giveback_flag = (word >> 27) & 0x1
        capability_mismatch = (word >> 26) & 0x1
        usb_communications_capable = (word >> 25) & 0x1
        no_usb_suspend = (word >> 24) & 0x1
        unchunked_extended_messages_supported = (word >> 23) & 0x1
        operating_current_A = int((word >> 10) & 0x3FF) * 0.01
        maximum_operating_current_A = int(word & 0x3FF) * 0.01
        data['object_position'] = object_position
        data['giveback_flag'] = giveback_flag
        data['capability_mismatch'] = capability_mismatch
        data['usb_communications_capable'] = usb_communications_capable
        data['no_usb_suspend'] = no_usb_suspend
        data['unchunked_extended_messages_supported'] = unchunked_extended_messages_supported
        data['operating_current_A'] = operating_current_A
        if giveback_flag == 0b1:
            data['minimum_operating_current_A'] = maximum_operating_current_A
            if pdo_type == 'Fixed Supply':
                frame_type = 'fixed_supply_rdo_giveback'
            if pdo_type == 'Variable Supply':
                frame_type = 'variable_supply_rdo_giveback'
        else:
            data['maximum_operating_current_A'] = maximum_operating_current_A
            if pdo_type == 'Fixed Supply':
                frame_type = 'fixed_supply_rdo'
            if pdo_type == 'Variable Supply':
                frame_type = 'variable_supply_rdo'
        pass
    elif pdo_type == 'Battery':
        object_position = (word >> 28) & 0x7
        giveback_flag = (word >> 27) & 0x1
        capability_mismatch = (word >> 26) & 0x1
        usb_communications_capable = (word >> 25) & 0x1
        no_usb_suspend = (word >> 24) & 0x1
        unchunked_extended_messages_supported = (word >> 23) & 0x1
        operating_power_W = int((word >> 10) & 0x3FF) * 0.25
        maximum_operating_power_W = int(word & 0x3FF) * 0.25
        data['object_position'] = object_position
        data['giveback_flag'] = giveback_flag
        data['capability_mismatch'] = capability_mismatch
        data['usb_communications_capable'] = usb_communications_capable
        data['no_usb_suspend'] = no_usb_suspend
        data['unchunked_extended_messages_supported'] = unchunked_extended_messages_supported
        data['operating_power_W'] = operating_power_W
        if giveback_flag == 0b1:
            data['minimum_operating_power_W'] = maximum_operating_power_W
            frame_type = 'battery_rdo_giveback'
        else:
            data['maximum_operating_power_W'] = maximum_operating_power_W
            frame_type = 'battery_rdo'

    elif pdo_type == 'Programmable Power Supply':
        object_position = (word >> 28) & 0x7
        capability_mismatch = (word >> 26) & 0x1
        usb_communications_capable = (word >> 25) & 0x1
        no_usb_suspend = (word >> 24) & 0x1
        unchunked_extended_messages_supported = (word >> 23) & 0x1
        output_voltage_V = int((word >> 9) & 0x7FF) * 0.02
        operating_current_A = int(word & 0x7F) * 0.05
        data['object_position'] = object_position
        data['capability_mismatch'] = capability_mismatch
        data['usb_communications_capable'] = usb_communications_capable
        data['no_usb_suspend'] = no_usb_suspend
        data['unchunked_extended_messages_supported'] = unchunked_extended_messages_supported
        data['output_voltage_V'] = output_voltage_V
        data['operating_current_A'] = operating_current_A
        frame_type = 'programmable_supply_rdo'
    return frame_type, data

def decode_vendor_header_data_object(word):
    data = {
        'data_object_type': 'VDM_Header'
    }
    frame_type = 'header_vdo'

    vendor_id = (word >> 16) & 0xFFFF
    _vdm_type = (word >> 15) & 0x1
    data['vendor_id'] = str(hex(vendor_id))
    data['vdm_type'] = vdm_type[_vdm_type]
    if _vdm_type == 0b1:
        frame_type = 'structured_header_vdo'
        _structured_vdm_version_major = (word >> 13) & 0x3
        object_position = (word >> 8) & 0x7
        command_type = (word >> 6) & 0x3
        command = word & 0x1F
        data['structured_vdm_version'] = structured_vdm_version_major[_structured_vdm_version_major]
        data['object_position'] = vdo_object_position[object_position]
        data['command_type'] = vdo_command_type[command_type]
        data['command'] = vdo_command[command]
    else :
        frame_type = 'unstructured_header_vdo'
        
    return frame_type, data

def decode_id_header_data_object(word, address_cmd):
    data = {
        'data_object_type': 'ID Header VDO'
    }
    frame_type = 'id_header_vdo'

    usb_communications_capable_as_usb_host = (word >> 31) & 0x1
    usb_communications_capable_as_usb_device = (word >> 30) & 0x1
    _product_type_ufp = (word >> 27) & 0x7
    modal_operation_supported = (word >> 26) & 0x1
    _product_type_dfp = (word >> 27) & 0x7
    _connector_type = (word >> 21) & 0x3
    usb_vendor_id = word & 0xFFFF
    data['usb_communications_capable_as_usb_host'] = usb_communications_capable_as_usb_host
    data['usb_communications_capable_as_usb_device'] = usb_communications_capable_as_usb_device
    if address_cmd == 'SOP':
        data['product_type_ufp'] = product_type_ufp_sop[_product_type_ufp]
        data['product_type_dfp'] = product_type_dfp_sop[_product_type_dfp]
    elif address_cmd == 'SOP_prime':
        data['product_type_ufp'] = product_type_ufp_sop_prime[_product_type_ufp]
        data['product_type_dfp'] = str('Reserved')
    data['modal_operation_supported'] = modal_operation_supported
    data['connector_type'] = connector_type[_connector_type]
    data['usb_vendor_id'] = str(hex(usb_vendor_id))
        
    return frame_type, data
    
def decode_cert_stat_vdo(word):
    data = {
        'data_object_type': 'Cert Stat VDO'
    }
    frame_type = 'cert_stat_vdo'

    xid = word & 0xFFFFFFFF
    data['xid'] = str(hex(xid))
        
    return frame_type, data

def decode_product_vdo(word):
    data = {
        'data_object_type': 'Product VDO'
    }
    frame_type = 'product_vdo'

    usb_product_id = (word >> 16) & 0xFFFF
    bcddevice = word & 0xFF
    data['usb_product_id'] = str(hex(usb_product_id))
    data['bcddevice'] = str(hex(bcddevice))
        
    return frame_type, data
    
def decode_ufp_vdo1(word):
    data = {
        'data_object_type': 'UFP VDO1'
    }
    frame_type = 'ufp_vdo1'

    _ufp_vdo1_ver = (word >> 29) & 0x7
    usb4_capable = (word >> 27) & 0x1
    usb3_capable = (word >> 26) & 0x1
    usb2_capable_billboardonly = (word >> 25) & 0x1
    usb2_capable = (word >> 24) & 0x1
    _ufp_vdo1_connector_type = (word >> 22) & 0x3
    supports_alt_modes_not_reconfigured_signals_on_usb2 = (word >> 5) & 0x1
    supports_alt_modes_reconfigured_signals_on_usb2 = (word >> 4) & 0x1 
    support_tbt3_alt_mode = (word >> 3) & 0x1
    _usb_highest_speed = word & 0x7
    data['ufp_vdo1_ver'] = product_vdo_ver[_ufp_vdo1_ver]
    data['usb4_capable'] = usb4_capable
    data['usb3_capable'] = usb3_capable
    data['usb2_capable_billboardonly'] = usb2_capable_billboardonly
    data['usb2_capable'] = usb2_capable
    data['ufp_vdo1_connector_type'] = product_vdo_connector_type[_ufp_vdo1_connector_type]
    data['supports_alt_modes_do_not_reconfigured_signals_on_usb2'] = supports_alt_modes_not_reconfigured_signals_on_usb2
    data['supports_alt_modes_reconfigured_signals_on_usb2'] = supports_alt_modes_reconfigured_signals_on_usb2
    data['support_tbt3_alt_mode'] = support_tbt3_alt_mode
    data['usb_highest_speed'] = usb_highest_speed[_usb_highest_speed]
        
    return frame_type, data

def decode_ufp_vdo2(word):
    data = {
        'data_object_type': 'UFP VDO2'
    }
    frame_type = 'ufp_vdo2'

    usb4_min_power = (word >> 23) & 0x7F
    usb4_max_power = (word >> 16) & 0x7F
    usb3_min_power = (word >> 7) & 0x7F
    usb3_max_power = word & 0x7F
    data['usb4_min_power'] = usb4_min_power
    data['usb4_max_power'] = usb4_max_power
    data['usb3_min_power'] = usb3_min_power
    data['usb3_max_power'] = usb3_max_power
        
    return frame_type, data

def decode_dfp_vdo(word):
    data = {
        'data_object_type': 'DFP VDO'
    }
    frame_type = 'dfp_vdo'
    
    _dfp_vdo_ver = (word >> 29) & 0x7
    dfp_usb4_capable = (word >> 26) & 0x1
    dfp_usb3_capable = (word >> 25) & 0x1
    dfp_usb2_capable = (word >> 24) & 0x1
    _dfp_vdo_connector_type = (word >> 22) & 0x3
    port_number = word &  0x1F
    data['dfp_vdo_ver'] = product_vdo_ver[_dfp_vdo_ver]
    data['usb4_host_capable'] = dfp_usb4_capable
    data['usb3_host_capable'] = dfp_usb3_capable
    data['usb2_host_capable'] = dfp_usb2_capable
    data['dfp_vdo_connector_type'] = product_vdo_connector_type[_dfp_vdo_connector_type]
    data['port_number'] = port_number
        
    return frame_type, data
    
def decode_ama_vdo(word):
    data = {
        'data_object_type': 'Alternate Mode Adapter VDO'
    }
    frame_type = 'ama_vdo'
    
    hw_version = (word >> 28) & 0xF
    fw_version = (word >> 24) & 0xF
    _vdo_version = (word >> 21) & 0x7
    _vconn_power = (word >> 5) & 0x7
    _vconn_required = (word >> 4) & 0x1
    _vbus_required = (word >> 3) & 0x1
    _ama_usb_highest_speed = word &  0x7
    data['hw_version'] = str(hex(hw_version))
    data['fw_version'] = str(hex(fw_version))
    data['vdo_version'] = ama_vdo_ver[_vdo_version]
    data['vconn_power'] = vconn_power[_vconn_power]
    data['vconn_required'] = yesno[_vconn_required]
    data['vbus_required'] = yesno[_vbus_required]
    data['ama_usb_highest_speed'] = ama_usb_highest_speed[_ama_usb_highest_speed]
        
    return frame_type, data
    
def decode_vdp_vdo(word):
    data = {
        'data_object_type': 'VCONN-Powered Device'
    }
    frame_type = 'vdp_vdo'
    
    hw_version = (word >> 28) & 0xF
    fw_version = (word >> 24) & 0xF
    _vdo_version = (word >> 21) & 0x7
    _maximum_vbus_voltage = (word >> 15) & 0x3
    charge_through_current_support = (word >> 14) & 0x1
    vbus_impedance = (word >> 7) & 0x3F
    ground_impedance = (word >> 1) & 0x3F
    charge_through_support = word & 0x1
    data['hw_version'] = str(hex(hw_version))
    data['fw_version'] = str(hex(fw_version))
    data['vdo_version'] = ama_vdo_ver[_vdo_version]
    data['maximum_vbus_voltage'] = maximum_vbus_voltage[_maximum_vbus_voltage]
    if charge_through_current_support == 0x0:
        data['charge_through_current_support'] = str('3A capable')
    elif charge_through_current_support == 0x1:
        data['charge_through_current_support'] = str('5A capable')
    else:
        data['charge_through_current_support'] = str(hex(charge_through_current_support))
    if charge_through_support == 0x0:
        data['vbus_impedance'] = vbus_impedance & 0x0
        data['ground_impedance'] = ground_impedance & 0x0
        data['charge_through_support'] = str('VPD does not support Charge Through')
    elif charge_through_support == 0x1:
        data['vbus_impedance'] = int(vbus_impedance) * 2
        data['ground_impedance'] = int(ground_impedance) * 1
        data['charge_through_support'] = str('VPD supports Charge Through')
    else:
        data['vbus_impedance'] = str(hex(vbus_impedance))
        data['ground_impedance'] = str(hex(ground_impedance))
        data['charge_through_support'] = str(hex(charge_through_support))
        
    return frame_type, data
    
def decode_activecable_vdo1(word):
    data = {
        'data_object_type': 'Active Cable VDO1'
    }
    frame_type = 'activecable_vdo1'
    
    hw_version = (word >> 28) & 0xF
    fw_version = (word >> 24) & 0xF
    vdo_version = (word >> 21) & 0x7
    _connector_type = (word >> 18) & 0x3
    _activecable_latency = (word >> 13) & 0xF
    cable_terminiation_type = (word >> 11) & 0x3
    _maximum_vbus_voltage = (word >> 9) & 0x3
    sbu_supported = (word >> 8) & 0x1
    sbu_type = (word >> 7) & 0x1
    _vbus_current_handling_capability = (word >> 5) & 0x3
    _vbus_through_cable = (word >> 4) & 0x1
    sop_double_prime_present = (word >> 3) & 0x1
    _usb_highest_speed = word & 0x3

    data['hw_version'] = str(hex(hw_version))
    data['fw_version'] = str(hex(fw_version))
    if vdo_version == 0x3:
        data['vdo_version'] = str('Ver.1.3')
    elif vdo_version == 0x1 or vdo_version == 0x2:
        data['vdo_version'] = str(bin(vdo_version))
    else:
        data['vdo_version'] = str('Reserved')
    data['connector_type'] = cable_connector_type[_connector_type]
    data['cable_latency'] = activecable_latency[_activecable_latency]
    if cable_terminiation_type == 0b10:
        data['cable_terminiation_type'] = str('One end Active,one end passive,VCONN required')
    elif cable_terminiation_type == 0b11:
        data['cable_terminiation_type'] = str('Both ends Active,VCONN required')
    else:
        data['cable_terminiation_type'] = str('Reserved')
    data['maximum_vbus_voltage'] = maximum_vbus_voltage[_maximum_vbus_voltage]
    if sbu_supported == 0x0:
        data['sbu_supported'] = str('SBUs connections supported')
        if sbu_type == 0x0:
            data['sbu_type'] = str('SBU is passive')
        elif sbu_type == 0x1:
            data['sbu_type'] = str('SBU is active')
        else:
            data['sbu_type'] = str(hex(sbu_type))
    elif sbu_supported == 0x1:
        data['sbu_supported'] = str('SBU connections are not supported')
        data['sbu_type'] = str('ignored')
    else:
        data['sbu_supported'] = str(bin(sbu_supported))
        data['sbu_type'] = str(hex(sbu_type))
    if _vbus_through_cable == 0x1:
        data['vbus_current_handling_capability'] = vbus_current_handling_capability[_vbus_current_handling_capability]
    elif _vbus_through_cable == 0x0:
        data['vbus_current_handling_capability'] = str('ignored')
    else:
        data['vbus_current_handling_capability'] = str(hex(_vbus_current_handling_capability))
    data['vbus_through_cable'] = yesno[_vbus_through_cable]
    if sop_double_prime_present == 0x0:
        data['sop_double_prime_controller_present'] = str('No SOP" controller present')
    elif sop_double_prime_present == 0x1:
        data['sop_double_prime_controller_present'] = str('SOP" controller present')
    data['usb_highest_speed'] = usb_highest_speed[_usb_highest_speed]
    
    return frame_type, data
    
def decode_activecable_vdo2(word):
    data = {
        'data_object_type': 'Active Cable VDO2'
    }
    frame_type = 'activecable_vdo2'
    
    maximum_operating_temperature = (word >> 24) & 0xFF
    shutdown_temperature = (word >> 16) & 0xFF
    _u3cld_power = (word >> 12) & 0x7
    u3tou0_transition_mode = (word >> 11) & 0x1
    physical_connection = (word >> 10) & 0x1
    active_element = (word >> 9) & 0x1
    usb4_supported = (word >> 8) & 0x1
    usb2_hub_hops_consumed = (word >> 6) & 0x3
    usb2_supported = (word >> 5) & 0x1
    usb3_supported = (word >> 4) & 0x1
    usb_lanes_supported = (word >> 3) & 0x1
    _optically_isolated_active_cable = (word >> 2) & 0x1
    usb_gen = word & 0x1
    data['maximum_operating_temperature'] = maximum_operating_temperature
    data['shutdown_temperature'] = shutdown_temperature
    data['_u3cld_power'] = u3cld_power[_u3cld_power]
    if u3tou0_transition_mode == 0x0:
        data['u3tou0_transition_mode'] = str('U3toU0 direct')
    elif u3tou0_transition_mode == 0x1:
        data['u3tou0_transition_mode'] = str('U3toU0 through U3S')
    else:
        data['u3tou0_transition_mode'] = str(u3tou0_transition_mode)
    if physical_connection == 0x0:
        data['physical_connection'] = str('Copper')
    elif physical_connection == 0x1:
        data['physical_connection'] = str('Optical')
    else:
        data['physical_connection'] = str(hex(physical_connection))
    if active_element == 0x0:
        data['active_element'] = str('Active Redriver')
    elif active_element == 0x1:
        data['active_element'] = str('Active Retimer')
    else:
        data['active_element'] = str(hex(active_element))
    if usb4_supported == 0x0:
        data['usb4_supported'] = str('USB4 supported')
    elif usb4_supported == 0x1:
        data['usb4_supported'] = str('USB4 not supported')
    else:
        data['usb4_supported'] = str(hex(usb4_supported))
    data['usb2_hub_hops_consumed'] = usb2_hub_hops_consumed
    if usb2_supported == 0x0:
        data['usb2_supported'] = str('USB2 supported')
    elif usb2_supported == 0x1:
        data['usb2_supported'] = str('USB2 not supported')
    else:
        data['usb2_supported'] = str(hex(usb2_supported))
    if usb3_supported == 0x0:
        data['usb3_supported'] = str('USB3 SS supported')
    elif usb3_supported == 0x1:
        data['usb3_supported'] = str('USB3 SS not supported')
    else:
        data['usb3_supported'] = str(hex(usb3_supported))
    if usb_lanes_supported == 0x0:
        data['usb_lanes_supported'] = str('One lane')
    elif usb_lanes_supported == 0x1:
        data['usb_lanes_supported'] = str('Two lanes')
    else:
        data['usb_lanes_supported'] = str(hex(usb_lanes_supported))
    data['optically_isolated_active_cable'] = yesno[_optically_isolated_active_cable]
    if usb_gen == 0x0:
        data['usb_gen'] = str('Gen1')
    elif usb_gen == 0x1:
        data['usb_gen'] = str('Gen2 or higher')
    else:
        data['usb_gen'] = str(hex(usb_gen))
    
    return frame_type, data
    
def decode_passivecable_vdo(word):
    data = {
        'data_object_type': 'Passive Cable VDO'
    }
    frame_type = 'passivecable_vdo'
    
    hw_version = (word >> 28) & 0xF
    fw_version = (word >> 24) & 0xF
    _vdo_version = (word >> 21) & 0x7
    _connector_type = (word >> 18) & 0x3
    _passivecable_latency = (word >> 13) & 0xF
    cable_terminiation_type = (word >> 11) & 0x3
    _maximum_vbus_voltage = (word >> 9) & 0x3
    _vbus_current_handling_capability = (word >> 5) & 0x3
    _usb_highest_speed = word & 0x3

    data['hw_version'] = str(hex(hw_version))
    data['fw_version'] = str(hex(fw_version))
    data['vdo_version'] = ama_vdo_ver[_vdo_version]
    data['connector_type'] = cable_connector_type[_connector_type]
    data['cable_latency'] = passivecable_latency[_passivecable_latency]
    if cable_terminiation_type == 0b00:
        data['cable_terminiation_type'] = str('VCONN not required')
    elif cable_terminiation_type == 0b01:
        data['cable_terminiation_type'] = str('VCONN required')
    else:
        data['cable_terminiation_type'] = str('Reserved')
    data['maximum_vbus_voltage'] = maximum_vbus_voltage[_maximum_vbus_voltage]
    if _vbus_current_handling_capability == 0x0:
        data['vbus_current_handling_capability'] = str('Reserved')
    else:
        data['vbus_current_handling_capability'] = vbus_current_handling_capability[_vbus_current_handling_capability]
    data['usb_highest_speed'] = usb_highest_speed[_usb_highest_speed]
    
    return frame_type, data
    
def decode_dsvid_vdo(word, n):
    data = {
        'data_object_type': 'Discovery SVIDs VDO'
    }
    frame_type = 'dsvid_vdo'
    _svidn = (word >> 16) & 0xFFFF
    _svidn1 = word & 0xFFFF
    data['svidn_number'] = n
    
    if svid_mode.get(_svidn, None) == None:
        data['svidn'] = str(hex(_svidn))
    else:
        data['svidn'] = str(hex(_svidn) + '(' + svid_mode[_svidn] + ')')
    data['svidn1_number'] = n + 1
    if svid_mode.get(_svidn1, None) == None:
        data['svidn1'] = str(hex(_svidn1))
    else:
        data['svidn1'] = str(hex(_svidn1) + '(' + svid_mode[_svidn1] + ')')
    n = n + 2

    return frame_type, data, n

def decode_dp_mode(word, n):
    data = {
        'data_object_type': 'DP mode'
    }
    frame_type = 'dp_mode'

    ufp_pin_assignment_supported = []
    dfp_pin_assignment_supported = []
    signaling_for_transport_of_dp_protocol = []
    ufp_pin_assignment_e = (word >> 20) & 0x1
    ufp_pin_assignment_d = (word >> 19) & 0x1
    ufp_pin_assignment_c = (word >> 18) & 0x1
    ufp_pin_assignment_b = (word >> 17) & 0x1
    ufp_pin_assignment_a = (word >> 16) & 0x1
    dfp_pin_assignment_f = (word >> 13) & 0x1
    dfp_pin_assignment_e = (word >> 12) & 0x1
    dfp_pin_assignment_d = (word >> 11) & 0x1
    dfp_pin_assignment_c = (word >> 10) & 0x1
    dfp_pin_assignment_b = (word >> 9) & 0x1
    dfp_pin_assignment_a = (word >> 8) & 0x1
    _usb2_signaling_not_used = (word >> 7) & 0x1
    receptacle_indication = (word >> 6) & 0x1
    sinaling_of_protocol_usb = (word >> 3) & 0x1
    sinaling_of_protocol_dp = (word >> 2) & 0x1
    _port_capability = word & 0x3
    
    if (word >> 16) & 0x1F == 0x0:
        data['ufp_d_pin_assignment_supported'] = str('not supported')
    else:
        if ufp_pin_assignment_a == 0x1:
            ufp_pin_assignment_a = str('A')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_a)
        if ufp_pin_assignment_b == 0x1:
            ufp_pin_assignment_b = str('B')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_b)
        if ufp_pin_assignment_c == 0x1:
            ufp_pin_assignment_c = str('C')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_c)
        if ufp_pin_assignment_d == 0x1:
            ufp_pin_assignment_d = str('D')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_d)
        if ufp_pin_assignment_e == 0x1:
            ufp_pin_assignment_e = str('E')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_e)
        data['ufp_d_pin_assignment_supported'] = str(','.join(ufp_pin_assignment_supported))

    if (word >> 8) & 0x3F == 0x0:
        data['dfp_d_pin_assignment_supported'] = str('not supported')
    else:
        if dfp_pin_assignment_a == 0x1:
            dfp_pin_assignment_a = str('A')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_a)
        if dfp_pin_assignment_b == 0x1:
            dfp_pin_assignment_b = str('B')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_b)
        if dfp_pin_assignment_c == 0x1:
            dfp_pin_assignment_c = str('C')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_c)
        if dfp_pin_assignment_d == 0x1:
            dfp_pin_assignment_d = str('D')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_d)
        if dfp_pin_assignment_e == 0x1:
            dfp_pin_assignment_e = str('E')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_e)
        if dfp_pin_assignment_f == 0x1:
            dfp_pin_assignment_f = str('F')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_f)
        data['dfp_d_pin_assignment_supported'] = str(','.join(dfp_pin_assignment_supported))
    data['usb2_signaling_not_used'] = yesno[_usb2_signaling_not_used]
    if receptacle_indication == 0x0:
       data['receptacle_indication'] = str('Type-C Plug')
    else:
       data['receptacle_indication'] = str('Type-C Receptacle')
    
    if sinaling_of_protocol_dp == 0x1:
        sinaling_of_protocol_dp = str('Supports DP v1.3')
        signaling_for_transport_of_dp_protocol.append(sinaling_of_protocol_dp)
    elif sinaling_of_protocol_usb == 0x1:
        sinaling_of_protocol_usb = str('Supports USB Gen2 rate')
        signaling_for_transport_of_dp_protocol.append(sinaling_of_protocol_usb)
    else:
        signaling_for_transport_of_dp_protocol.append(str('Reserved'))
    data['signaling_for_transport_of_dp_protocol'] = str(','.join(signaling_for_transport_of_dp_protocol))
    data['port_capability'] = port_capability[_port_capability]
    n = n + 1
    
    return frame_type, data, n
    
def decode_dp_status(word):
    data = {
        'data_object_type': 'DP Status Update'
    }
    
    frame_type = 'dp_status'
    
    irq_hpd = (word >> 8) & 0x1
    hpd_state = (word >> 7) & 0x1
    _exit_dp_mode_request = (word >> 6) & 0x1
    usb_config_request = (word >> 5) & 0x1
    multifunction_preferred = (word >> 4) & 0x1
    enabled = (word >> 3) & 0x1
    power_low = (word >> 2) & 0x1
    _dfp_ufp_connected = word & 0x3
    if (word >> 8) & 0x1 == 0x0:
        data['irq_hpd'] = str('No IRQ_HPD')
    elif (word >> 8) & 0x1 == 0x1:
        data['irq_hpd'] = str('IRQ_HPD.e')
    else:
        data['irq_hpd'] = str(hex(irq_hpd))
    if (word >> 7) & 0x1 == 0x0:
        data['hpd_state'] = str('HPD_Low')
    elif (word >> 7) & 0x1 == 0x1:
        data['hpd_state'] = str('HPD_High')
    else:
        data['hpd_state'] = str(hex(hpd_state))
    data['exit_dp_mode_request'] = yesno[_exit_dp_mode_request]
    if (word >> 5) & 0x1 == 0x0:
        data['usb_config_request'] = str('Maintain current configuration')
    elif (word >> 5) & 0x1 == 0x1:
        data['usb_config_request'] = str('Request switch to USB configuration')
    else:
        data['usb_config_request'] = str(hex(usb_config_request))
    if (word >> 4) & 0x1 == 0x0:
        data['multifunction_preferred'] = str('No preference for multifunction')
    elif (word >> 4) & 0x1 == 0x1:
        data['multifunction_preferred'] = str('Multi-function preferred')
    else:
        data['multifunction_preferred'] = str(hex(multifunction_preferred))
    if (word >> 3) & 0x1 == 0x0:
        data['enabled'] = str('Adaptor DisplayPort functionality is disabled')
    elif (word >> 3) & 0x1 == 0x1:
        data['enabled'] = str('Adaptor DisplayPort functionality is enabled')
    else:
        data['enabled'] = str(hex(enabled))
    if (word >> 2) & 0x1 == 0x0:
        data['power_low'] = str('Adaptor is functioning normally or is disabled')
    elif (word >> 2) & 0x1 == 0x1:
        data['power_low'] = str('Adaptor has detected low power and disabled DisplayPort support')
    else:
        data['power_low'] = str(hex(power_low))
    data['dfp_ufp_connected'] = dfp_ufp_connected[_dfp_ufp_connected]
    
    return frame_type, data
    
def decode_dp_configure(word):
    data = {
        'data_object_type': 'DP Configure'
    }
    
    frame_type = 'dp_configure'
    _configure_ufp_pin_assignment = (word >> 8) & 0xFF
    _signaling_for_transport_of_dp_protocol = (word >> 2) & 0xF
    _select_configuration = word & 0x3
    if configure_ufp_pin_assignment.get(_configure_ufp_pin_assignment, None) == None:
        data['configure_ufp_pin_assignment'] = str('Reserved')
    else:
        data['configure_ufp_pin_assignment'] = configure_ufp_pin_assignment[_configure_ufp_pin_assignment]
    data['signaling_for_transport_of_dp_protocol'] = signaling_for_transport_of_dp_protocol[_signaling_for_transport_of_dp_protocol]
    data['select_configuration'] = select_configuration[_select_configuration]
    
    return frame_type, data
    
def decode_tbt_mode(word, sop_type):
    data = {
        'data_object_type': 'TBT mode VDO'
    }
    
    if sop_type == 'SOP':
        frame_type = 'tbt_mode_adapter'
        legacy_tbt_adapter = (word >> 16) & 0x1
        tbt_alt_mode = word & 0xFFFF
        if legacy_tbt_adapter == 0x1:
            data['legacy_tbt_adapter'] = str('1h(2nd Gen TBT Adapter)')
            if tbt_alt_mode == 0x0001:
                data['tbt_alt_mode'] = str('0001h(TBT mode)')
            else:
                data['tbt_alt_mode'] = str(hex(tbt_alt_mode))
        else:
            frame_type = 'tbt_mode_device'
            _vpro_avaliable = (word >> 18) & 0x1F
            data['vpro_avaliable'] = yesno[_vpro_avaliable]
            data['legacy_tbt_adapter'] = str('0h(3rd Gen TBT Device)')
            if tbt_alt_mode == 0x0001:
                data['tbt_alt_mode'] = str('0001h(TBT mode)')
            else:
                data['tbt_alt_mode'] = str(hex(tbt_alt_mode))
    else:
        frame_type = 'tbt_cable_mode'
        active_cable_plug_link_training = (word >> 23) & 0x1
        cable_active_passive = (word >> 22) & 0x1
        cable_type = (word >> 21) & 0x1
        tbt_cable_gen = (word >> 19) & 0x3
        cable_speed = (word >> 16) & 0x7
        tbt_alt_mode = word & 0xFFFF
        if active_cable_plug_link_training == 0x0:
            data['active_cable_plug_link_training'] = str('0h(Passive/Active with bi-directional LSRX)')
        else:
            data['active_cable_plug_link_training'] = str('1h(Active with uni-directional LSRX)')
        if cable_active_passive == 0x0:
            data['cable_active_passive'] = str('Passive Cable')
        else:
            data['cable_active_passive'] = str('Active Cable')
        if cable_type == 0x0:
            data['cable_type'] = str('Non-Optical Cable')
        else:
            data['cable_type'] = str('Optical Cable')
        if tbt_cable_gen == 0x0:
            data['tbt_cable_gen'] = str('3rd Gen Non-Rounded TBT')
        elif tbt_cable_gen == 0x1:
            data['tbt_cable_gen'] = str('4th Gen Rounded and Non-Rounded TBT')
        else:
            data['tbt_cable_gen'] = str(hex(tbt_cable_gen) + ' ' + 'Reserved')
        if cable_speed == 0x1:
            data['cable_speed'] = str('01h(USB3.1 Gen1 Cable)')
        elif cable_speed == 0x2:
            data['cable_speed'] = str('02h(10Gbps)')
        elif cable_speed == 0x3:
            data['cable_speed'] = str('03h(10Gbps and 20Gbps)')
        else:
            data['cable_speed'] = str('Reserved')
        if tbt_alt_mode == 0x0001:
            data['tbt_alt_mode'] = str('0001h(TBT mode)')
        else:
            data['tbt_alt_mode'] = str(hex(tbt_alt_mode))
    
    return frame_type, data
    
def decode_tbt_enter_mode(word):
    data = {
        'data_object_type': 'TBT Enter Mode VDO'
    }
    
    frame_type = 'tbt_enter_mode'
    vpro_dock_and_host = (word >> 26) & 0x1
    dfp_legacy_tbt_adapter = (word >> 24) & 0x1
    active_cable_plug_link_training = (word >> 23) & 0x1
    cable_active_passive = (word >> 22) & 0x1
    cable_type = (word >> 21) & 0x1
    tbt_cable_gen = (word >> 19) & 0x3
    cable_speed = (word >> 16) & 0x7
    mode = word & 0xFFFF
    if vpro_dock_and_host == 0x0:
        data['vpro_dock_and_host'] = str('Host/Dock do not support vPro')
    else:
        data['vpro_dock_and_host'] = str('vPro Host and Dock detected')
    if dfp_legacy_tbt_adapter == 0x0:
        data['dfp_legacy_tbt_adapter'] = str('3rd Gen TBT')
    else:
        data['dfp_legacy_tbt_adapter'] = str('2nd Gen TBT Adapter')
    if active_cable_plug_link_training == 0x0:
        data['active_cable_plug_link_training'] = str('0h(Passive/Active with bi-directional LSRX)')
    else:
        data['active_cable_plug_link_training'] = str('1h(Active with uni-directional LSRX)')
    if cable_active_passive == 0x0:
        data['cable_active_passive'] = str('Passive Cable')
    else:
        data['cable_active_passive'] = str('Active Cable')
    if cable_type == 0x0:
        data['cable_type'] = str('Non-Optical Cable')
    else:
        data['cable_type'] = str('Optical Cable')
    if tbt_cable_gen == 0x0:
        data['tbt_cable_gen'] = str('3rd Gen Non-Rounded TBT')
    elif tbt_cable_gen == 0x1:
        data['tbt_cable_gen'] = str('4th Gen Rounded and Non-Rounded TBT')
    else:
        data['tbt_cable_gen'] = str(hex(tbt_cable_gen) + ' ' + 'Reserved')
    if cable_speed == 0x0:
        data['cable_speed'] = str('00h(No TBT support)')
    elif cable_speed == 0x1:
        data['cable_speed'] = str('01h(USB3.1 Gen1 Cable)')
    elif cable_speed == 0x2:
        data['cable_speed'] = str('02h(10Gbps)')
    elif cable_speed == 0x3:
        data['cable_speed'] = str('03h(10Gbps and 20Gbps)')
    else:
        data['cable_speed'] = str('Reserved')
    if mode == 0x0001:
        data['tbt_alt_mode'] = str('0001h(TBT mode)')
    else:
        data['tbt_alt_mode'] = str(hex(tbt_alt_mode))
            
    return frame_type, data
    
def decode_tbt_attention(word):
    data = {
        'data_object_type': 'TBT Status VDO'
    }
    
    frame_type = 'tbt_attention'
    exit_tbt_mode_request = (word >> 4) & 0x1
    usb2_billboard_status = (word >> 2) & 0x3
    _legacy_tbt_mdp_cable_status = word & 0x3
    if exit_tbt_mode_request == 0x0:
        data['exit_tbt_mode_request'] = str('0b(Maintain TBT Mode)')
    else:
        data['exit_tbt_mode_request'] = str('1b(Exit TBT Mode)')
    if usb2_billboard_status == 0x0:
        data['usb2_billboard_status'] = str('00b(USB2 billboard not being presented.In TBT Mode)')
    elif usb2_billboard_status == 0x3:
        data['usb2_billboard_status'] = str('11b(USB2 billboard being presented.Exit TBT Mode)')
    else:
        data['usb2_billboard_status'] = str('Reserved')
    data['legacy_tbt_mdp_cable_status'] = legacy_tbt_mdp_cable_status[_legacy_tbt_mdp_cable_status]
            
    return frame_type, data

def decode_battery_status_data_object(word):
    data = {
        'data_object_type': 'Battery Status Data Object'
    }
    frame_type = 'bsdo'
    battery_present_capacity = (word >> 16) & 0xFFFF
    if battery_present_capacity == 0xFFFF:
        data['battery_preset_Capacity_WH'] = str('SOC unknown')
    else:
        data['battery_preset_Capacity_WH'] = int(battery_present_capacity) * 0.1
    battery_info = (word >> 8) & 0xFF
    invalid_battery_reference = battery_info & 0x1
    battery_is_present = (battery_info >> 1) & 0x1
    _battery_charging_status = (battery_info >> 2) & 0x3
    data['invalid_battery_reference'] = invalid_battery_reference
    if battery_is_present == 0b0:
        data['battery_present'] = str('Battery is not present')
        data['battery_charging_status'] = str('Reserved')
    elif battery_is_present == 0b1:
        data['battery_present'] = str('battery_is_present')
        data['battery_charging_status'] = battery_charging_status[_battery_charging_status]

    return frame_type, data

def decode_alert_data_object(word):
    data = {
        'data_object_type': 'Alert Data Object'
    }
    frame_type = 'ado'

    type_of_alert = (word >> 24) & 0x7

    fixed_batteries = (word >> 20) & 0xF
    hot_swappable_batteries = (word >> 16) & 0xF
    battery_status_change_event = (type_of_alert >> 1) & 0x1
    ocp_event = (type_of_alert >> 2) & 0x1
    otp_event = (type_of_alert >> 3) & 0x1
    operating_condition_change = (type_of_alert >> 4) & 0x1
    source_input_change = (type_of_alert >> 5) & 0x1
    ovp_event = (type_of_alert >> 6) & 0x1

    data['fixed_batteries'] = fixed_batteries
    data['hot_swappable_batteries'] = hot_swappable_batteries
    data['battery_status_change_event'] = battery_status_change_event
    data['ocp_event'] = ocp_event
    data['otp_event'] = otp_event
    data['operating_condition_change'] = operating_condition_change
    data['source_input_change'] = source_input_change
    data['ovp_event'] = ovp_event

    return frame_type, data


def decode_get_country_info_data_object(word):
    data = {
        'data_object_type': 'Country Code Data Object'
    }
    frame_type = 'ccdo'

    first_character = (word >> 24) & 0xF
    second_character = (word >> 16) & 0xF

    data['country_code'] = '{first}{second}'.format(
        first=chr(first_character), second=char(second_character))

    return frame_type, data

def decode_enter_usb_data_object(word):
    data = {
        'data_object_type': 'Enter USB'
    }
    frame_type = 'eudo'

    _usb_mode = (word >> 28) & 0x7
    _usb4_drd = (word >> 26) & 0x1
    _usb3_drd = (word >> 25) & 0x1
    _cable_speed = (word >> 21) & 0x7
    _cable_type = (word >> 21) & 0x7
    _cable_current = (word >> 17) & 0x3
    pcie_support = (word >> 16) & 0x1
    dp_support = (word >> 15) & 0x1
    tbt_support = (word >> 14) & 0x1
    host_present = (word >> 13) & 0x1

    data['usb_mode'] = usb_mode[_usb_mode]
    data['usb4_drd'] = usb4_drd[_usb4_drd]
    data['usb3_drd'] = usb3_drd[_usb3_drd]
    data['cable_speed'] = cable_speed[_cable_speed]
    data['cable_type'] = cable_type[_cable_type]
    data['cable_current'] = cable_current[_cable_current]
    data['pcie_support'] = pcie_support
    data['dp_support'] = dp_support
    data['tbt_support'] = tbt_support
    data['host_present'] = host_present

    return frame_type, data
