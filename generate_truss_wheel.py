import ezdxf
import numpy as np

# Initialize DXF Document for Autodesk
doc = ezdxf.new("R2010")
msp = doc.modelspace()

# Geometry Parameters derived from Sanskrit Technical Text
segments = 10  # Decagonal radial symmetry
R_outer = 100.0  # Outer ring radius
R_inner = 50.0  # Inner hub radius
angles = np.linspace(0, 2 * np.pi, segments, endpoint=False)

# Compute Vertex Coordinates for Radial Truss Structure
outer_pts = [(R_outer * np.cos(a), R_outer * np.sin(a)) for a in angles]
inner_pts = [(R_inner * np.cos(a), R_inner * np.sin(a)) for a in angles]

# Draw Inner & Outer Rings + Structural Triangulation Struts
for i in range(segments):
  next_i = (i + 1) % segments
  msp.add_line(outer_pts[i], outer_pts[next_i])
  msp.add_line(inner_pts[i], inner_pts[next_i])
  msp.add_line(inner_pts[i], outer_pts[i])
  msp.add_line(inner_pts[i], outer_pts[next_i])

doc.saveas("sanskrit_truss_wheel.dxf")
