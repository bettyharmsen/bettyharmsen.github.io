import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000012xx/00001221/IMG_1229.jpg"
artifact.imageAltText = "IMG_1229"
artifact.imageTitle = "IMG_1229"
artifact.title = "Playing in the Pumpkin Patch"
artifact.eBaySale.title = "Playing in the Pumpkin Patch - original watercolor painting for sale by artist"
artifact.eBaySale.description = """<p>This signed original watercolor painting depicts a child
playing in a pumpkin pitch.  This painting is a pleasant reminder that children can have fun
without television or video games.</p>
<p>This cheerful watercolor painting was done on 140 lb acid-free watercolor paper. The picture 
itself is 9&frac12; inches by 8&frac12; inches but it is painted on a 10&frac12; inch by 9&frac12;
inch sheet.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor, acid-free paper"
artifact.eBaySale.firstBidPrice = "-" 
artifact.eBaySale.reservePrice = "-"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "-"
artifact.eBaySale.links = []
artifact.etsySale.title = "Original watercolor painting - Playing in the Pumpkin Patch"
artifact.etsySale.description = """<p>This signed original watercolor painting depicts a child
playing in a pumpkin pitch. This painting is a pleasant reminder that children can have fun without
television or video games.</p>
<p>This cheerful watercolor painting was done on 140 lb acid-free watercolor paper. The picture
itself is 9&frac12; inches by 8&frac12; inches but it is painted on a 10&frac12; inch by 9&frac12;
inch sheet.</p>
"""
artifact.etsySale.tags = "art, original painting, watercolor, idyllic, autumn, children"
artifact.etsySale.purchasePrice = "$12.00"
artifact.etsySale.singleItemShippingPrice = "$6.00"
artifact.etsySale.multipleItemShippingPrice = "$2.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/58171055/original-watercolor",
                            "Etsy posting of 2010/10/05")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact1229.html")
print "Updated Artifact1229.html."