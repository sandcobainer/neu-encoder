# Using Neu-Encoder in Max4Live


1. Download the repo from 
2. Place the folder nue-encoder under Music/Ableton/User\ Library/Presets/Instruments/Max\ Instruments/
3. Download wavenet-ckpt folder and place under nue-encoder 
4. Make a Conda environment named 'py27' with Python 2.7 and Magenta (already done)
5. Open Ableton Live and drag the .amxd file onto a MIDI track
6. Place your samples under Music/Ableton/User\ Library/Presets/Instruments/Max\ Instruments/input/ folder
7. Enter output folder in .amxd, set sample rate, sample length
8. Hit Train
9. Wait till all samples are done synthesizing
10. Click 'Read' on the left side to read all samples under /input
11. Click 'Read' on the right side to read all samples under the selected output folder

12. Use keys a-z to play input samples
13. Use keys A-Z to play corresponding generated sample
 