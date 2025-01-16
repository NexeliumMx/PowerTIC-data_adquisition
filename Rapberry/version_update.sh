stat ./File_downloads/Powertick.bin 
rm ./File_downloads/Powertick.bin

python ./image_download.py

echo "File Downloaded successfully"
stat ./File_downloads/Powertick.bin 

