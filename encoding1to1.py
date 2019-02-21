# run this script from the conda environment with python encoding1to1.py
import os
import fnmatch
import numpy as np
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen
import optparse

ckpt = './wavenet-ckpt/model.ckpt-200000'

parser = optparse.OptionParser()

parser.add_option('-i', '--input',
    action="store", dest="input",
    help="Enter folder name of raw input samples. Make sure the folder is in the current root directory(nsynth-fastgen)!", default="")

parser.add_option('-o', '--output',
    action="store", dest="output",
    help="Enter destination name of folder for generated samples. Make sure the folder is in the current root directory(nsynth-fastgen)!", default="")

parser.add_option('-r', '--sample_rate',
    action="store", dest="sr",
    help="Enter sample rate of generated samples", default="")

parser.add_option('-l', '--sample_length',
    action="store", dest="sl",
    help="Enter sample length of generated samples", default="")

options, args = parser.parse_args()

# load_encoding function takes in the parameters and 
# returns the loaded audio and corresponding encodings
def load_encoding(fname):
    audio = utils.load_audio(fname,sample_length = sl,sr=sr)
    encoding = fastgen.encode(audio, ckpt, sl)
    return audio, encoding


def synthesizer():

    for dirpath, dirnames, filenames in os.walk(inputpath):
        newdir = dirpath[len(inputpath):]
        newdir = newdir[1:]
        structure = os.path.join(outputpath,newdir)
        if not os.path.isdir(structure):
            os.mkdir(structure)
            for fname in filenames:
                if fnmatch.fnmatch(fname, '*.wav'):
                    print('Encoding ' + fname);
                    audio, encoding = load_encoding(os.path.join(dirpath + fname))
                    np.save(structure + fname + '.npy', encoding)
                    print('Syntheszing ' + fname + ' ' + structure);
                    fastgen.synthesize(encoding,save_paths=[structure + fname],checkpoint_path=ckpt,samples_per_save=sl)
                    print('Done : ' +  fname);
        else:
            print("Folder does already exists!")
            return
        
                
# Drop samples to be encoded in /audio and
# retreive generated samples in /gen_audio
script_dir = os.path.dirname(os.path.realpath('__file__'))
raw_samples =  options.input
inputpath = os.path.join(script_dir, raw_samples)
gen_samples =  options.output
outputpath = os.path.join(script_dir, gen_samples)

print 'Input raw samples directory: ', inputpath
print 'Generated output directory: ', outputpath

sr = options.sr
sl = int(options.sl)
synthesizer();
