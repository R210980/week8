inputfile='/home/rguktrkvalley/Documents/audio.mp3'
outputfile='/home/rguktrkvalley/Documents/audio.mp3'
[y,Fs]=audioread(inputfile);
reversedData=flipud(y);
audiowrite(outputfile,reversedData,Fs);
disp('audio is reversed and successfully saved')
