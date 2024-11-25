# SPDX-License-Identifier: MIT
'''
  This file is part of ruri.
  MIT License
 
  Copyright (c) 2022-2024 Moe-hacker
 
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
 
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
 
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
'''
import matplotlib.pyplot as pyplot
import matplotlib.patches as patches
import math
# Set image parameters.
figure, axes = pyplot.subplots(dpi=200, figsize=(2.5, 2.5))
pyplot.box(False)
pyplot.xticks([])
pyplot.yticks([])
pyplot.subplots_adjust(bottom=0,top=1)
axes.set_aspect(1)
# Draw the sectors.
draw_circle = patches.Wedge((0, 6), 6, 210, 330, fill=False, linewidth=4.0, color='#000000')
axes.add_artist(draw_circle)
draw_circle = patches.Wedge((0, -6), 6, 30, 150, fill=False, linewidth=4.0, color='#000000')
axes.add_artist(draw_circle)
draw_circle = patches.Wedge((math.sqrt(3) * 3, 3), 6, 150, 270, fill=False, linewidth=4.0, color='#000000')
axes.add_artist(draw_circle)
draw_circle = patches.Wedge((math.sqrt(3) * 3 * (-1), 3), 6, 270, 390, fill=False, linewidth=4.0, color='#000000')
axes.add_artist(draw_circle)
draw_circle = patches.Wedge((math.sqrt(3) * 3, -3), 6, 90, 210, fill=False, linewidth=4.0, color='#000000')
axes.add_artist(draw_circle)
draw_circle = patches.Wedge((math.sqrt(3) * 3 * (-1), -3), 6, 330, 450, fill=False, linewidth=4.0, color='#000000')
axes.add_artist(draw_circle)
# Draw the diagonals.
pyplot.plot([-0.003, -0.003], [-6, 6], linewidth=4.0, color='#000000')
pyplot.plot([math.sqrt(3) * 3 * (-1), math.sqrt(3) * 3], [-3, 3], linewidth=4.0, color='#000000')
pyplot.plot([math.sqrt(3) * 3, math.sqrt(3) * 3 * (-1)], [-3, 3], linewidth=4.0, color='#000000')
pyplot.xlim(-6, 6)
pyplot.ylim(-6, 6)
# Save as logo.png.
pyplot.savefig('favicon.png', transparent=True)