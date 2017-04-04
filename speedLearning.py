import sys
import os
import subprocess
import tempfile

fpath = os.path.abspath(sys.argv[1])
fbasename = os.path.basename(fpath)
fname, fext = os.path.splitext(fbasename)
fdir = os.path.dirname(fpath)

fpath = "\"%s\"" % fpath

with tempfile.TemporaryDirectory() as tmpdir:
    tmpwav = "\"%s/%s.wav\"" % (tmpdir, fname)
    subprocess.run("sox %s %s" % (fpath, tmpwav), shell=True)

    tmpwav_fast = "\"%s/%s_fast.wav\"" % (tmpdir, fname)
    subprocess.run("soundstretch %s %s -tempo=+90" % (tmpwav, tmpwav_fast), shell=True)

    tmpwav_superfast = "\"%s/%s_superfast.wav\"" % (tmpdir, fname)
    subprocess.run("soundstretch %s %s -tempo=+200" % (tmpwav, tmpwav_superfast), shell=True)

    tmpwav_joined = "\"%s/%s_concat.wav\"" % (tmpdir, fname)
    subprocess.run("sox %s %s %s %s" % (tmpwav_fast, tmpwav_superfast, tmpwav_fast, tmpwav_joined), shell=True)

    newmp3 = "\"%s/%s_fast.mp3\"" % (fdir, fname)
    subprocess.run("lame -V1 %s %s" % (tmpwav_joined, newmp3), shell=True)
