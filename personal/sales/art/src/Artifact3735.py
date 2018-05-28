import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_3735.JPG"
artifact.imageAltText = "IMG_3735"
artifact.imageTitle = "IMG_3735"
artifact.title = "Poppies"
artifact.eBaySale.title = "Poppies - original watercolor for sale by artist"
artifact.eBaySale.description = """<p>This painting shows many beautiful poppies.  It is a simple
but appealing image.</p>
<p>This was painted on 145 pound acid free paper. Including the attractive wooden frame, it is 
12 &frac12; by 10".  It is ready to hang.</p>
<p>It is a signed original painting.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor paints"
artifact.eBaySale.firstBidPrice = "$7.00" 
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$12.00"
artifact.eBaySale.links = []
artifact.etsySale.title = "Original watercolor painting for sale by artist - Poppies"
artifact.etsySale.description = """<p>This painting shows many beautiful poppies. It is a simple
but appealing image.</p>
<p>This was painted on 145 pound acid free paper. Including the attractive wooden frame, it is
12&frac12;" by 10". It is ready to hang.</p>
<p>It is a signed original painting.</p>
<p>Thanks for taking the time to view my work.</p>
"""
artifact.etsySale.tags = "art, original painting, watercolor, wild flowers, flowers"
artifact.etsySale.purchasePrice = "$40.00"
artifact.etsySale.singleItemShippingPrice = "$10.00"
artifact.etsySale.multipleItemShippingPrice = "$7.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/62360397/original-watercolor-poppies",
                            "Etsy listing starting 2010/11/19")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact3735.html")
print "Updated Artifact3735.html."