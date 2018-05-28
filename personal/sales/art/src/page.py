#!C:/Python27/python.exe
""" page.py

Stupid class for rendering a page for art sales.
"""
class Sale:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.materials = ""
        self.tags = ""
        self.firstBidPrice = ""
        self.reservePrice = ""
        self.buyItNowPrice =  ""
        self.singleItemShippingPrice = ""
        self.purchasePrice = ""
        self.multipleItemShippingPrice = ""
        self.askingPrice = ""
        self.minimumAcceptableOfferPrice = ""
        self.maximumAutomaticRejectPrice = ""
        self.links = []

class Artifact:
    def __init__(self):
        self.imageUrl = ""
        self.imageAltText = ""
        self.imageTitle = ""
        self.title = "",
        self.eBaySale = Sale()
        self.etsySale = Sale()
        self.kijijiSale = Sale()
        self.statisticsUrl = ""
        
class Renderer:
    def __init__(self, artifact):
        self.artifact = artifact
    def render(self, filename):
        htmlfile = file(filename, "wt")
        htmlfile.write("<!DOCTYPE html>\n")
        htmlfile.write("<html>\n")
        htmlfile.write("<head>\n")
        htmlfile.write("  <meta charset=\"utf-8\">\n")
        htmlfile.write("  <meta name=\"viewport\" content=\"width=device-width\">\n")
        htmlfile.write("  <title>%s</title>\n" % self.artifact.title)
        htmlfile.write("</head>\n")
        htmlfile.write("<body>\n")
        htmlfile.write("  <header>\n")
        htmlfile.write('    <img src="%s" alt="%s" title="%s" width="800px">\n' % (self.artifact.imageUrl,
                                                                                   self.artifact.imageAltText,
                                                                                   self.artifact.imageTitle))
        htmlfile.write("    <h1>%s</h1>\n" % self.artifact.title)
        htmlfile.write("  </header>\n")
        htmlfile.write("  <nav>\n")
        htmlfile.write("    <ol>")
        htmlfile.write('      <li><a href="#ebayAnchor">eBay Auction</a></li>')
        htmlfile.write('      <li><a href="#etsyAnchor">Etsy Sale</a></li>')
        htmlfile.write('      <li><a href="#kijijiAnchor">Kijiji Sale</a></li>')
        htmlfile.write("    </ol>")
        htmlfile.write("  </nav>\n")

        htmlfile.write('  <section id="ebaySection">\n')
        htmlfile.write('    <a id="ebayAnchor"></a>\n')
        htmlfile.write("    <h2>1. eBay Auction</h2>\n")
        htmlfile.write("    <dl>\n")
        htmlfile.write("      <dt>Title:</dt>\n")
        htmlfile.write("      <dd>%s</dd>\n" % self.artifact.eBaySale.title)
        htmlfile.write("      <dt>Description:</dt>\n")
        htmlfile.write("      <dd>%s</dd>\n" % self.artifact.eBaySale.description)
        htmlfile.write("      <dt>Materials:</dt>\n")
        htmlfile.write("      <dd>%s</dd>\n" % self.artifact.eBaySale.materials)
        htmlfile.write("      <dt>Prices:</dt>\n")
        htmlfile.write("      <dd>\n")
        htmlfile.write('        <table border="1">\n')
        htmlfile.write("          <thead>\n")
        htmlfile.write("            <tr>\n")
        htmlfile.write("              <th>First Bid</th>\n")
        htmlfile.write("              <th>Reserve</th>\n")
        htmlfile.write("              <th>Buy-it-now</th>\n")
        htmlfile.write("              <th>Shipping</th>\n")
        htmlfile.write("            </tr>\n")
        htmlfile.write("          </thead>\n")
        htmlfile.write("          <tbody>\n")
        htmlfile.write("            <tr>\n")
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.eBaySale.firstBidPrice)
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.eBaySale.reservePrice)
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.eBaySale.buyItNowPrice)
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.eBaySale.singleItemShippingPrice)
        htmlfile.write("            </tr>\n")
        htmlfile.write("          </tbody>\n")
        htmlfile.write("        </table>\n")
        htmlfile.write("      </dd>\n")
        htmlfile.write("      <!-- %d -->\n" % len(self.artifact.eBaySale.links))
        if len(self.artifact.eBaySale.links) > 0:
            htmlfile.write("      <dt>Links:</dt>\n")
            for links in self.artifact.eBaySale.links:
                htmlfile.write('      <dd><a href="%s">%s</a></dd>\n' % links)
            htmlfile.write("    </dl>\n")
        htmlfile.write("  </section>\n")
        htmlfile.write('  <section id="etsySection">\n')
        htmlfile.write('    <a id="etsyAnchor"></a>\n')
        htmlfile.write("    <h2>2. Etsy Sale</h2>\n")
        htmlfile.write("    <dl>\n")
        htmlfile.write("      <dt>Title:</dt>\n")
        htmlfile.write("      <dd>%s</dd>\n" % self.artifact.etsySale.title)
        htmlfile.write("      <dt>Description:</dt>\n")
        htmlfile.write("      <dd>%s</dd>\n" % self.artifact.etsySale.description)
        htmlfile.write("      <dt>Tags:</dt>\n")
        htmlfile.write("      <dd>%s</dd>\n" % self.artifact.etsySale.tags)
        htmlfile.write("      <dt>Prices:</dt>\n")
        htmlfile.write("      <dd>\n")
        htmlfile.write('        <table border="1">\n')
        htmlfile.write("          <thead>\n")
        htmlfile.write("            <tr>\n")
        htmlfile.write("              <th>Purchase Price</th>\n")
        htmlfile.write("              <th>Single Item Shipping Price</th>\n")
        htmlfile.write("              <th>Multiple Item Shipping Price</th>\n")
        htmlfile.write("            </tr>\n")
        htmlfile.write("          </thead>\n")
        htmlfile.write("          <tbody>\n")
        htmlfile.write("            <tr>\n")
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.etsySale.purchasePrice)
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.etsySale.singleItemShippingPrice)
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.etsySale.multipleItemShippingPrice)
        htmlfile.write("            </tr>\n")
        htmlfile.write("          </tbody>\n")
        htmlfile.write("        </table>\n")
        htmlfile.write("      </dd>\n")
        #htmlfile.write("      <!-- %d -->\n" % len(self.artifact.etsySale.links))
        if len(self.artifact.etsySale.links) > 0:
            htmlfile.write("      <dt>Links:</dt>\n")
            for links in self.artifact.etsySale.links:
                htmlfile.write('      <dd><a href="%s">%s</a></dd>\n' % links)
            htmlfile.write("    </dl>\n")
        htmlfile.write("  </section>\n")
        htmlfile.write('  <section id="kijijiSection">\n')
        htmlfile.write('    <a id="kijijiAnchor"></a>\n')
        htmlfile.write("    <h2>3. Kijiji Sale</h2>\n")
        htmlfile.write("    <dl>\n")
        htmlfile.write("      <dt>Title:</dt>\n")
        htmlfile.write("      <dd>%s</dd>\n" % self.artifact.kijijiSale.title)
        htmlfile.write("      <dt>Description:</dt>\n")
        htmlfile.write("      <dd>%s</dd>\n" % self.artifact.kijijiSale.description)
        htmlfile.write("      <dt>Prices:</dt>\n")
        htmlfile.write("      <dd>\n")
        htmlfile.write('        <table border="1">\n')
        htmlfile.write("          <thead>\n")
        htmlfile.write("            <tr>\n")
        htmlfile.write("              <th>Asking Price</th>\n")
        htmlfile.write("              <th>Minimum Acceptable Offer Price</th>\n")
        htmlfile.write("              <th>Maximum Automatic Reject Price</th>\n")
        htmlfile.write("              <th>Single Item Shipping Price</th>\n")
        htmlfile.write("              <th>Multiple Item Shipping Price</th>\n")
        htmlfile.write("            </tr>\n")
        htmlfile.write("          </thead>\n")
        htmlfile.write("          <tbody>\n")
        htmlfile.write("            <tr>\n")
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.kijijiSale.askingPrice)
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.kijijiSale.minimumAcceptableOfferPrice)
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.kijijiSale.maximumAutomaticRejectPrice)
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.kijijiSale.singleItemShippingPrice)
        htmlfile.write('              <td align="center">%s</td>\n' % self.artifact.kijijiSale.multipleItemShippingPrice)
        htmlfile.write("            </tr>\n")
        htmlfile.write("          </tbody>\n")
        htmlfile.write("        </table>\n")
        htmlfile.write("      </dd>\n")
        #htmlfile.write("      <!-- %d -->\n" % len(self.artifact.kijijiSale.links))
        if len(self.artifact.kijijiSale.links) > 0:
            htmlfile.write("      <dt>Links:</dt>\n")
            for links in self.artifact.kijijiSale.links:
                htmlfile.write('      <dd><a href="%s">%s</a></dd>\n' % links)
            htmlfile.write("    </dl>\n")
        htmlfile.write("  </section>\n")
        htmlfile.write("</body>")
        htmlfile.close()
