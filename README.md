USB PD3.0 Analyzer

This is a modified version from the extension of [USB PD(Biphase Mark Code)](https://github.com/saleae/hla-usb-pd) on the Saleae store. Code structure and most variants come from there since I'm not a software guy. 

This extension fixed some problems I met on debugging:
   1. Decode VDOs including VESA DP/TBT ALT mode but exclude user's defined ALT mode.
   2. Preamble detects error due to tStartDrive for first falling edge of Pramble.
   3. Hard Reset cannot detect.
   4. Inter-frame Gap timing check to prevent wrong detection. 

To implement this, you have to decode CC channel with Mechester ANA first. With the setting below:
   1. Mode: BMC(FM1)
   2. Bit Rate: 300,000
   3. One Bit per Transfer **(mandatory)
   
![Mechester ANA setting](https://user-images.githubusercontent.com/121099078/210613113-71d586c9-be14-45b8-88ba-be48b79a7ce8.jpg)

Then add Mechster ANA as input of this extension. Also strongly recommend that sampling rate sets at 6.25MS/s for CC channel
![capture](https://user-images.githubusercontent.com/121099078/210613391-19c1c583-07c6-40f9-bff6-87f84debb1ac.jpg)
