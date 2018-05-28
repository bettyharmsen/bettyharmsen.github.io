#!/usr/bin/python
import sys

currentSales = [
    ('Artifact_2018-05-24_15.23.57', 'images/2018-05-24_15.23.57_cropped.jpg', '2018-05-24_15.23.57_cropped')
]

futureSales = [
    ('Artifact2777', 'images/IMG_2777.JPG', 'IMG_2777'),
    ('Artifact2107', 'images/IMG_2107.JPG', 'IMG_2107'),
    ('Artifact3000', 'images/IMG_3000.JPG', 'IMG_3000'),
    ('Artifact3256', 'images/IMG_3256.JPG', 'IMG_3256'),
    ('Artifact3907', 'images/IMG_3907.JPG', 'IMG_3907'),
    ('Artifact4355', 'images/IMG_4355.JPG', 'IMG_4355'),
    ('Artifact4363', 'images/IMG_4363.JPG', 'IMG_4363'),
    ('Artifact4379', 'images/IMG_4379.JPG', 'IMG_4379'),
    ('Artifact4514', 'images/IMG_4514.JPG', 'IMG_4514'),
    ('Artifact4758', 'images/IMG_4758.JPG', 'IMG_4758'),
    ('Artifact4988', 'images/IMG_4988.JPG', 'IMG_4988'),
    ('Artifact5083', 'images/IMG_5083.JPG', 'IMG_5083'),
    ('Artifact7029', 'images/IMG_7029.JPG', 'IMG_7029'),
    ('Artifact8639', 'images/IMG_8639.JPG', 'IMG_8639'),
    ('Artifact8666', 'images/IMG_8666.JPG', 'IMG_8666'),
    ('Artifact8695', 'images/IMG_8695.JPG', 'IMG_8695'),
    ('Artifact8702', 'images/IMG_8702.JPG', 'IMG_8702')
]

unsoldPastSales = [
    ('Artifact0308', 'images/IMG_0308.JPG', 'IMG_0308'),
    ('Artifact1229', 'images/IMG_1229.JPG', 'IMG_1229'),
    ('Artifact3219', 'images/IMG_3219.JPG', 'IMG_3219'),
    ('Artifact3609', 'images/IMG_3609.JPG', 'IMG_3609'),
    ('Artifact4261', 'images/IMG_4261.JPG', 'IMG_4261'),
    ('Artifact4357', 'images/IMG_4357.JPG', 'IMG_4357'),
    ('Artifact5009', 'images/IMG_5009.JPG', 'IMG_5009'),
    ('Artifact5849', 'images/IMG_5849.JPG', 'IMG_5849'),
    ('Artifact5858', 'images/IMG_5858.JPG', 'IMG_5858'),
    ('Artifact7072', 'images/IMG_7072.JPG', 'IMG_7072'),
]


soldPastSales = [
    ('Artifact1546', 'images/IMG_1546.JPG', 'IMG_1546'),
    ('Artifact3208', 'images/IMG_3208.JPG', 'IMG_3208'),
    ('Artifact3619', 'images/IMG_3619.JPG', 'IMG_3619'),
    ('Artifact3735', 'images/IMG_3735.JPG', 'IMG_3735'),
    ('Artifact3891', 'images/IMG_3891.JPG', 'IMG_3891'),
    ('Artifact3900', 'images/IMG_3900.JPG', 'IMG_3900'),
    ('Artifact4500', 'images/IMG_4500.JPG', 'IMG_4500'),
    ('Artifact4291', 'images/IMG_4291.JPG', 'IMG_4291'),
    ('Artifact4963', 'images/IMG_4963.JPG', 'IMG_4963'),
    ('Artifact5016', 'images/IMG_5016.JPG', 'IMG_5016'),
    ('Artifact5580', 'images/IMG_5580.JPG', 'IMG_5580'),
    ('Artifact6392', 'images/IMG_6392.JPG', 'IMG_6392'),
    ('Artifact7075', 'images/IMG_7075.JPG', 'IMG_7075'),
]

def mktable(htmlfile, values):
    index = len(values) - 1
    while index >= 0:
        htmlfile.write("<tr>\n")
        for j in range(0, 5):
            if index >= 0:
                htmlfile.write('<td><a href="%s.html"><img src="%s" alt="%s" title="%s" height="120"/></a></td>\n' % (values[index][0],
                                                                                                                      values[index][1],
                                                                                                                      values[index][2],
                                                                                                                      values[index][2]))
            else:
                htmlfile.write('<td>&nbsp;</td>\n')
            index -= 1
        htmlfile.write("</tr>\n")

htmlfile = file('../index.html', 'wt')
htmlfile.write("<!DOCTYPE html>\n")
htmlfile.write("<html>\n")
htmlfile.write("<head>\n")
htmlfile.write("  <meta charset=\"utf-8\">\n")
htmlfile.write("  <meta name=\"viewport\" content=\"width=device-width\">\n")
htmlfile.write("  <title>Betty Harmsen&apos;s Art Sales</title>\n")
htmlfile.write("</head>\n")
htmlfile.write("<body>\n")
htmlfile.write("  <header>\n")
htmlfile.write("    <h1>Betty Harmsen&apos;s Art Sales</h1>\n")
htmlfile.write("  </header>\n")
htmlfile.write("  <nav>\n")


htmlfile.write('<section id="currentSales">');
htmlfile.write('<h2>Current Sales</h2>\n')
htmlfile.write('<table border="0">\n')
htmlfile.write('<tbody>\n')
mktable(htmlfile, currentSales)
htmlfile.write('</tbody>\n')
htmlfile.write('</table>\n')
htmlfile.write('</section>');

htmlfile.write('<section id="futureSales">');
htmlfile.write('<h2>Future Sales</h2>\n')
htmlfile.write('<table border="0">\n')
htmlfile.write('<tbody>\n')
mktable(htmlfile, futureSales)
htmlfile.write('</tbody>\n')
htmlfile.write('</table>\n')
htmlfile.write('</section>');

htmlfile.write('<section id="pastSales">');
htmlfile.write('<h2>Past Sales</h2>\n')

htmlfile.write('<section id="unsoldPastSales">');
htmlfile.write('<h2>Unsold Past Sales</h2>\n')
htmlfile.write('<table border="0">\n')
htmlfile.write('<tbody>\n')
mktable(htmlfile, unsoldPastSales)
htmlfile.write('</tbody>\n')
htmlfile.write('</table>\n')
htmlfile.write('</section>');

htmlfile.write('<section id="soldPastSales">');
htmlfile.write('<h2>Sold Past Sales</h2>\n')
htmlfile.write('<table border="0">\n')
htmlfile.write('<tbody>\n')
mktable(htmlfile, soldPastSales)
htmlfile.write('</tbody>\n')
htmlfile.write('</table>\n')
htmlfile.write('</section>');

htmlfile.write('</section>');

htmlfile.write("</nav>")
htmlfile.write("</body>")
htmlfile.close()

print "Done"
