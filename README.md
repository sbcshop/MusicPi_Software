# MusicPi_Software
<!--
<img src="https://github.com/sbcshop/IdentiPi_Software/blob/main/images/IdentiPi_banner.jpg">
-->

An in-depth setup and working guide for MusicPi is available on this github. 

### Features:
- Powered by Raspberry Pi Pico/Pico W microcontroller which is having Dual-core Arm Cortex-M0+ processor, running up to 133 MHz
- 1.14" TFT display for visual interaction
- Type C interface for power with supply indicator LED
- Onboard microSD card compatibility is useful for data logging and extended storage purposes
- Multipurpose GPIOs breakout for additional peripheral interfacing
- 3 Programmable Buttons to add additional controls to project 
- 2 channel RAW and Mono Class D Audio Amplified Output supporting 3W speaker per channel 
- [PCM5100A](https://github.com/sbcshop/MusicPi_Software/blob/main/Documents/pcm5100a_datasheet.pdf) 2VRMS DirectPath™ Stereo DAC

### Specifications:
- **Microcontroller:** Supports Raspberry Pi Pico/Pico W
- **Supply Voltage:** 5V
- **Operating pin voltage:** 3.3V
- **Display:** 
  - Display Size: 1.14”
  - Display Type: IPS TFT 
  - Display Resolution:  135(H) X 240(V) pixels
  - Display colors: 65K RGB
  - Luminance(cd/m2): 400(TYP)
  - Display interface: SPI
  - Display Driver: [ST7789V](https://github.com/sbcshop/MusicPi_Software/blob/main/Documents/TFT_ST7789V_Datasheet.pdf) 
- **Amplifier:** [NS4150](https://github.com/sbcshop/MusicPi_Software/blob/main/Documents/NS4150EN_datasheet.pdf) 3W Mono Class D Audio Amplifier
- **Audio Outputs:**
  - Amplified Headphones (3.5mm) with [PAM8908JER](https://github.com/sbcshop/MusicPi_Software/blob/main/Documents/PAM8904_datasheet.pdf) stereo headphone amp
  - Unamplified Line-Level
  - 3W Speaker Output per channel
- **PCM5100A DAC:** 
  - DAC Resolution: 32-bit
  - DAC Sampling Rate: Up to 384kHz
  - Operating Temperature Range: -20°C ~ +70°C 


## Getting Started with MusicPi
### Hardware Overview
#### Pinout

<img src="https://github.com/sbcshop/MusicPi_Software/blob/main/images/MusicPi_Pinouts.png">


### Interfacing Details

<img src="https://github.com/sbcshop/MusicPi_Software/blob/main/images/musicpi_setup.png" width="583" height="357">

When Raspberry Pico/Pico W connected with MusicPi following pins consumed,  

- I2S Audio Hardware Interfacing 
  | Pico | DAC PCM5100 | Function |
  |---|---|---|
  |GP11 | LRCK | I2S   |
  |GP9  | DIN  | |
  |GP10 | BCK  |  |
  |GP22 | XSMT  |  |

  Headphone Amplifier
  | Pico | PAM8908 | Function |
  |---|---|---|
  |GP20  | GAIN 0  | GAIN select pin 0 |
  |GP21  | GAIN 1  |  GAIN select pin 1 |
  
- Display interfacing details
  | Pico | Hardware Pin | Function |
  |---|---|---|
  |GP14 | SCLK  | Clock pin of SPI interface for display |
  |GP15 | DIN   | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP6  | D/C   | Data/command line of SPI interface for display |
  |GP12 | RESET | Display reset pin |
  |GP13 | CS    | Chip Select pin of SPI interface for display| 
  |GP7  | BL    | Backlight pin for display |

- SD Card interfacing : SPI0 of Pico is used for interfacing SDcard 
  | Pico | SDCard | Function |
  |---|---|---|
  |GP18 | SCK | SPI clock pin|
  |GP19 | MOSI | SPI Master OUT Slave IN interface pin|
  |GP16 | MISO | SPI Master IN Slave OUT interface pin |
  |GP17 | CS | Chip Select pin|
  
- Buttons and RGB interfacing details
  | Pico | Hardware | Function |
  |---|---|---|
  |GP2 | BT1 |Programmable button|
  |GP3 | BT2 |Programmable button|
  |GP4 | BT3 |Programmable button|
  |GP26 | DIN | Data in pin of WS2812 RGB Led|

With Pico or Pico W connected to MusicPi, you can proceed to follow below steps to get start working with MusicPi. 

## Step 1: Setup MusicPi and Development Environment 
1. Download and Install Thonny IDE for your respective OS from Link [Download Thonny](https://thonny.org/). This will be used for writing code script.
   
   <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img.JPG" />
   
2. Adding **CircuitPython** bootloader in Pico/Pico W of  

- For this first you need to *Press and Hold* the boot button of Pico, without releasing the button connect it to USB port of PC/laptop.

  <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif" width="340" height="228">

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure. Either copy or drag & drop ["MusicPi_firmware.uf2"](https://github.com/sbcshop/MusicPi_Software/blob/main/MusicPi_firmware.uf2) firmware file available in this repository to the device as shown in figure.
     
  <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" /> 
     
- If bootloader installed properly inside Pico of MusicPi. So device will reboot or you can reconnect without pressing boot button to see a device with some initial file as shown in the below image:-
  
  <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />

<!--
## Step 2: Running First Code in MusicPi
1. Start Thonny IDE application, after this go to run->select interpreter, choose device and suitable com port
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img18.png" />
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img19.png" />

    Write simple python code and click on green run button or you can open any demo example files provided here in github. 

2. Now you are ready to try out your own codes. Even you can try some of below Example codes provided, for that just copy all the files (library files) from [```lib```](https://github.com/sbcshop/HackyPi-Software/tree/main/lib) folder of this repository and paste inside the HackyPi ```lib``` folder

### Run Script Standalone without Thonny IDE
   Follow below steps to save your script to device, once done then remove device and reinsert in PC to run your script without the need of Thonny IDE. Meaning you can now plug to USB Port and your code will be executed by HackyPi.
   
   **And remember to save your script as _code.py_ name into device otherwise script will not run after inserting into USB.**
   
<img src= "https://github.com/sbcshop/HackyPi-Software/blob/main/images/Run-Script-standalone.gif" />
-->

### Example Codes
   Try reference demo codes to test onboard components of MusicPi, make sure to move [Lib files]() into Pico before trying example codes. 
   - [Display Demo]() : code to test display
   - [RGB LED Demo]() : code to blink or experiment with onboard RGB LEDs.
   - [Demo Audio I2S]() : to play music using Pico/Pico W
   - and [More..](https://github.com/sbcshop/MusicPi_Software/tree/main/examples)
   
   Using this sample code as a guide, you can modify, build, and share codes!!
   
## Resources
  * [Schematic](https://github.com/sbcshop/MusicPi_Hardware/blob/main/Design%20Data/Sch%20MusicPi.pdf)
  * [Hardware Files](https://github.com/sbcshop/MusicPi_Hardware)
  * [Step File](https://github.com/sbcshop/MusicPi_Hardware/blob/main/Mechanical%20Data/MusicPi.step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)

## Related Products

  * [Audio Codec HAT](https://shop.sb-components.co.uk/products/audio-codec-hat-for-raspberry-pi?_pos=2&_sid=dca87c6f7&_ss=r) 
  
    ![Audio Codec HAT](https://shop.sb-components.co.uk/cdn/shop/products/AudioCodecHATForRaspberryPi.png?v=1649074353&width=300)
  
  * [TRRS 3.5mm Audio Jack Breakout](https://shop.sb-components.co.uk/products/trrs-3-5mm-audio-jack-breakout?_pos=3&_sid=dca87c6f7&_ss=r)
  
    ![TRRS 3.5mm Audio Jack Breakout](https://shop.sb-components.co.uk/cdn/shop/files/1_93fe94b5-e09f-4f4f-9b16-65348c47343d.jpg?v=1690882465&width=300)
  
  * [BoomBit - Music Player for microbit](https://shop.sb-components.co.uk/products/boombit?_pos=10&_sid=39ade3b9b&_ss=r) 
  
    ![BoomBit - Music Player for microbit](https://shop.sb-components.co.uk/cdn/shop/products/BoomBitProductImage.png?v=1622521944&width=300)

 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
