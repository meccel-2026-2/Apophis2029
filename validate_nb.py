import sys, json
try:
    import nbformat
except Exception as e:
    nbformat = None
f = 'Estudio Dinamico Apophis en 2029.ipynb'

try:
    with open(f,'rb') as fh:
        b = fh.read()
except Exception as e:
    print('OPEN_ERR', e)
    sys.exit(4)

# Try UTF-8
for enc in ('utf-8','utf-8-sig','latin-1'):
    try:
        s = b.decode(enc)
        print('DECODE_OK', enc)
        break
    except Exception as e:
        print('DECODE_FAIL', enc, str(e))
else:
    print('DECODE_ALL_FAIL')
    sys.exit(5)

# Try json
try:
    j = json.loads(s)
    print('JSON_OK', 'cells=', len(j.get('cells',[])))
    sys.exit(0)
except Exception as e:
    print('JSON_ERR', e)

# Try nbformat if available
if nbformat is not None:
    try:
        nb = nbformat.reads(s, as_version=4)
        print('NBFORMAT_OK', 'cells=', len(nb.cells))
        sys.exit(0)
    except Exception as e:
        print('NBFORMAT_ERR', e)

# Fallback: print first 300 bytes as repr
print('PREVIEW', repr(b[:300]))
sys.exit(6)
