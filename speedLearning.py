import sys
import os
import subprocess
import tempfile

fpath = os.path.abspath(sys.argv[1])
fbasename = os.path.basename(fpath)
fname, fext = os.path.splitext(fbasename)
outpath = os.path.abspath(sys.argv[2])

with tempfile.TemporaryDirectory() as tmpdir:
    tmpwav = os.path.join(tmpdir, "%s.wav" % fname)
    args = ["sox", fpath, tmpwav]
    subprocess.run(args)

    tmpwav_fast = os.path.join(tmpdir, "%s_fast.wav" % fname)
    args = ["sonic", "-s", "1.1", tmpwav, tmpwav_fast]
    subprocess.run(args)

    tmpwav_superfast = os.path.join(tmpdir, "%s_superfast.wav" % fname)
    args = ["sonic", "-s", "1.8", tmpwav, tmpwav_superfast]
    subprocess.run(args)

    tmpwav_joined = os.path.join(tmpdir, "%s_joined.wav" % fname)
    args = ["sox", tmpwav_fast, tmpwav_superfast, tmpwav_fast, tmpwav_joined]
    subprocess.run(args)

    args = ["lame", "-V1", tmpwav_joined, outpath]
    subprocess.run(args)
