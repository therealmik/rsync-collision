Rsync Collisions
================
These are some blocks that collide under the rsync algorithm (both the md5 sum and the rsync checksum).

They were generated using a slightly modified [fastcoll](https://marc-stevens.nl/research/software/download.php?file=fastcoll_v1.0.0.5-1_source.zip) by Marc Stevens.  The license for fastcoll doesn't permit much, but here's a description of how to generate the collions:

- If you require a prefix (passed implicity or explicitly into your target file), put it in a file, padded up to 64 bytes.
- Generate a collision using that prefix to generate an IHV.
- Take note of the XOR difference between the rsync checksums of the two files
- Generate collisions with your colliding files as a prefix until you get one with the same difference
- Swap around the "original" and "modified" files, so each collision has one of each

FIXME: Provide a better description of this and why it works
