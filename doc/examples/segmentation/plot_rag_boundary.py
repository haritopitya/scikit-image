"""
==========================
Region Boundary based RAGs
==========================

This example demonstrates construction of region boundary based RAGs with the
:py:func:`skimage.future.graph.rag_boundary` function. The function taken an
``edge_map`` argument, which gives the significance of a feature (such as
edges) being present at each pixel. In a region boundary RAG, the edge between
two regions is the average value of the corresponding pixels in ``edge_map``
along their shared boundary.

"""
from skimage.future import graph
from skimage import data, segmentation, color, filters, io
from matplotlib import pyplot as plt


img = data.coffee()
gimg = color.rgb2gray(img)

labels = segmentation.slic(img, compactness=30, n_segments=400)
edges = filters.sobel(gimg)
edges_rgb = color.gray2rgb(edges)

g = graph.rag_boundary(labels, edges)
lc = graph.show_rag(labels, g, edges_rgb, img_cmap=None, edge_cmap='viridis',
                    edge_width=1.2)

plt.colorbar(lc, fraction=0.03)
io.show()
