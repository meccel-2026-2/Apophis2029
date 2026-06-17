import sys, codecs, json
f_in = 'Estudio Dinamico Apophis en 2029.ipynb'
f_out = 'Estudio Dinamico Apophis en 2029_utf8.ipynb'
print('INPUT:', f_in)
with open(f_in, 'rb') as fh:
    b = fh.read()
# Try common encodings
encodings = ['utf-8','utf-8-sig','utf-16','utf-16-le','utf-16-be','latin-1']
for enc in encodings:
    try:
        s = b.decode(enc)
        print('DECODE_OK', enc)
        break
    except Exception as e:
        #print('FAIL', enc, e)
        s = None
if s is None:
    print('NO_ENCODINGS_WORKED')
    sys.exit(2)
# Validate JSON
try:
    j = json.loads(s)
    print('JSON_PARSED', 'cells=', len(j.get('cells', [])))
except Exception as e:
    print('JSON_PARSE_ERR', e)
    # Try to salvage by replacing nulls
    try:
        s2 = s.replace('\x00','')
        j = json.loads(s2)
        s = s2
        print('JSON_PARSED_AFTER_REMOVE_NULLS', 'cells=', len(j.get('cells', [])))
    except Exception as e2:
        print('STILL_JSON_ERR', e2)
        print('Preview start:', repr(s[:200]))
        sys.exit(3)
# Write UTF-8 output
with open(f_out, 'w', encoding='utf-8') as fh:
    fh.write(s)
print('WROTE', f_out)
print('OUT_SIZE', len(s))
