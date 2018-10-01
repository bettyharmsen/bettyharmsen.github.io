import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_3256.JPG"
artifact.imageAltText = "IMG_3256"
artifact.imageTitle = "IMG_3256"
artifact.title = "Marilyn Munroe"
artifact.eBaySale.title = "Marilyn Munroe - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>This oil painting portrays Marilyn Munroe in one of her more
memorable poses.</p>
<p>I used soft pinks and whites to emphasize the femininity of this beauty.</p>
<p>This framed oil painting measures 7" by 6". It is a signed original.</p>
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
artifact.etsySale.tags = "art, original painting, ?"
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
artifact.etsySale.links = []
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact3256.html")
print "Updated Artifact3256.html."