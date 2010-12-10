Places in the Classical Atlas Project (http://www.unc.edu/depts/cl_atlas/)
gazetteer are located by map number and grid square within the map. This
package includes the bounding coordinates of all grid squares and a function to
get the (left, bottom, top, right) bounding box of any grid square or map.

Usage:

  >>> from capgrids import box

Get the bounding box of grid cell B2 from map 43

  >>> box('43', 'b2')
  (12.25, 41.75, 12.5, 42.0)

Get the bounding box of map 43

  >>> box('43')
  (12.0, 41.25, 13.25, 42.25)

