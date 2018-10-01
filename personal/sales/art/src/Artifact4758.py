import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_4758.JPG"
artifact.imageAltText = "IMG_4758"
artifact.imageTitle = "IMG_4758"
artifact.title = "IMG_4758"
artifact.eBaySale.title = "IMG_4758"
artifact.eBaySale.description = """<p><em>TODO</em></p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = ""
artifact.eBaySale.firstBidPrice = "-" 
artifact.eBaySale.reservePrice = "-"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "-"
artifact.eBaySale.links = []
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = ""
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
artifact.etsySale.links = []
artifact.kijijiSale.title = "Watercolour painting - Decorative bottles and flower"
# 10 x 12
artifact.kijijiSale.description = """<p>This was painted with
watercolor paints on 140 lb acid free paper board. It is 12" by 10".
This is a still-life painting of decorative bottles and a flower.
The original artist is asking for $35 or your best offer.</p>
"""
artifact.kijijiSale.askingPrice = "$35"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact4758.html")
print "Updated Artifact4758.html."
