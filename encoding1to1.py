# run this script from the conda environment with python encoding1to1.py
import os
import fnmatch
import numpy as np
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen
import sys

print 'Max4Live requested Python process'

# Drop samples to be encoded in /input and
# retreive generated samples in /outputGEN
script_dir =  '/Users/' + sys.argv[3]  + '/Desktop/neu-encoder'

ckpt = os.path.join(script_dir, 'wavenet-ckpt/model.ckpt-200000')
raw_samples =  'input'
inputpath = os.path.join(script_dir, raw_samples)
gen_samples =  sys.argv[4]
outputpath = os.path.join(script_dir, gen_samples)

print 'Input raw samples directory: ', inputpath
print 'Generated output directory: ', outputpath

sr = int(sys.argv[1])
sl = int(sys.argv[2])


# load_encoding function takes in the parameters and 
# returns the loaded audio and corresponding encodings
def load_encoding(fname):
    audio = utils.load_audio(fname,sample_length = sl,sr=sr)
    print 'Encoding.. ',fname
    encoding = fastgen.encode(audio, ckpt, sl)
    print 'Encoded successfully'
    return audio, encoding


def synthesizer():

    print 'Synthesizing with Sample rate: ' + str(sr) + ' and Sample length: ' + str(sl)

    for dirpath, dirnames, filenames in os.walk(inputpath):
        newdir = dirpath[len(inputpath):]
        newdir = newdir[1:]
        structure = os.path.join(outputpath,newdir)
        print structure
        if not os.path.isdir(structure):
            os.mkdir(structure)
            for fname in filenames:
                if fnmatch.fnmatch(fname, '*.wav'):
                    # print 'encoding path: ', 
                    print fname
                    audio, encoding = load_encoding(os.path.join(dirpath,fname))
                    # np.save(structure + fname + '.npy', encoding)
                    print 'Syntheszing ' + fname +'.. ' 
                    fastgen.synthesize(encoding,save_paths=[os.path.join(structure , fname)],checkpoint_path=ckpt,samples_per_save=sl)
                    print  fname + ': Done!'
        else:
            print("Folder: " + structure + " already exists!")
            return
        
                


synthesizer();
