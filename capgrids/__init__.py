import csv
from itertools import islice
import os

def mapcols(mapid):
    # "i" and "o" are omitted from barrington atlas columns in maps 100-102
    if int(mapid) in (100, 101, 102):
        return 'abcdefghjklmnpqrstuvwxyz'
    else:
        return 'abcdefghijklmnopqrstuvwxyz'

scales = {'10000': 5.0, '5000': 5.0, '1000': 1.0, '500': 0.5, '150': 0.25}
f = open(os.path.join(os.path.dirname(__file__), 'maps.csv'))
reader = csv.reader(f)

data = {}
for r in islice(reader, 1, None):
    key = r[0]
    value = data.get(key, [])
    value.append(r)
    data[key] = value

def box(mapid, gridsquare=None):
    alphanums = mapcols(mapid)
    if gridsquare is not None and gridsquare.lower() == "inset":
        inset = data[mapid][0][-2]
        return tuple(eval(inset))
    for rec in data[mapid]:
        assert rec[0] == mapid
        try:
            cols = [alphanums[i] for i in range(alphanums.index(rec[7].lower()), alphanums.index(rec[8].lower())+1)]
            rows = [k for k in range(int(rec[9]), int(rec[10])+1)]
            bbox = float(rec[3]), float(rec[5]), float(rec[4]), float(rec[6])
            if gridsquare is None:
                return bbox
            row = int(gridsquare[1:])
            col = gridsquare[0].lower()
            assert row in rows
            assert col in cols
            dx = (bbox[2] - bbox[0])/len(cols)
            dy = (bbox[3] - bbox[1])/len(rows)
            minx = bbox[0] + cols.index(col)*dx
            maxy = bbox[3] - rows.index(row)*dy
            return (minx, maxy-dy, minx+dx, maxy)
        except AssertionError:
            pass
        except:
            raise
    raise IndexError, "No gridsquare %s in map %s" % (gridsquare, mapid)

