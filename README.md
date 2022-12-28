USB PD3.0 Analyzer

This is a modified version from the extension of USB PD(Biphase Mark Code) on the Saleae store  

It fixes some problems:
   1. Decode VDOs including VESA DP/TBT ALT mode but exclude user's defined ALT mode.
   2. Preamble detects error due to tStartDrive tolerance for first falling edge of Pramble.
   3. Hard Reset cannot detect.
   4. Inter-frame Gap timing check to prevent wrong detection. 

To implement this, you have to decode CC channel with Mechester ANA first. With the setting below:
   1. Mode: BMC(FM1)
   2. Bit Rate: 300,000
   3. One Bit per Transfer

Then add Mechster ANA as input of this extension. Also strongly recommend that sampling rate sets at 6.25MS/s for CC channel