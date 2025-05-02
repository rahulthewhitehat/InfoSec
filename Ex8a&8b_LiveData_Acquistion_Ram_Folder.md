## Live acquisition of system RAM and store the memory dump for forensic analysis.

🛠️ Tools Used
LiME (Linux Memory Extractor)

dd or memdump (alternative method)
Volatility (for later analysis – optional)

### Steps - CLI Tools
Clone and compile LiME:

git clone https://github.com/504ensicsLabs/LiME
cd LiME/src
make
Insert the kernel module to dump RAM:

sudo insmod lime.ko "path=/home/rahul/ram_dump.lime format=lime"
Check output file:

ls -lh /home/rahul/ram_dump.lime
(Optional) Analyze with Volatility:

volatility -f ram_dump.lime --profile=LinuxUbuntu_20_04x64 pslist

### Also FTK Manager

- Open FTK Imager as Administrator.
- Go to File > Capture Memory.
- In the "Capture Memory" window:
- Set destination path for .mem file (e.g., D:\Forensics\ram_capture.mem)
- (Optional) Check Include pagefile.sys if you want it
- (Optional) Select Create AD1 file for AccessData format
- Click Start – It will acquire and save the memory image.

Verify the Image File:

Note the file size.

Optionally open it in Volatility or FTK Imager for viewing.
