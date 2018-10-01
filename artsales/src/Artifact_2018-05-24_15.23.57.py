import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/2018-05-24_15.23.57_cropped.jpg"
artifact.imageAltText = "2018-05-24_15.23.57_cropped.jpg"
artifact.imageTitle = "2018-05-24_15.23.57_cropped.jpg"
artifact.title = "Old Town in Holland"

artifact.eBaySale.title = "Old Town in Holland - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>I painted and signed this original watercolour painting. THIS IS NOT A PRINT.</p>
<p>This painting shows an old Dutch town like the one I grew up in long ago.</p><p>It is in the primitive style which I feel helps emphasize the beauty of simpler times.</p>
<p>I used bright, clean colors to highlight the purity of this scene. The sky is clear blue, the
trees are deep green, and the snow is a pristine white. </p>
<p>This painting is on watercolour paper. This painting is ready-to-hang.</p>
<p>The dimensions, including frame, are 15 &frac14; inches wide by 12 &frac14; inches high.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil, canvas board "
artifact.eBaySale.firstBidPrice = "$5.00"
artifact.eBaySale.reservePrice = "$19.99"
artifact.eBaySale.buyItNowPrice = "$24.99"
artifact.eBaySale.singleItemShippingPrice = "$14.00"
artifact.eBaySale.links = []

artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, original painting, oil painting, landscape, folk-art, primitive,"
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
artifact.etsySale.links = []

artifact.kijijiSale.title = "Matted and framed watercolor painting for sale by artist"
artifact.kijijiSale.description = """<p>Signed original watercolour painting with matt and frame for sale by original artist.<p>
<p>My Mom painted this scene from the kind of old Dutch town in which she grew up long ago.</p>
<p>This painting is on watercolour paper and is mounted in a wood frame with a matte. This painting is ready-to-hang.</p>
<p>The dimensions, including frame, are 15 &frac14; inches wide by 12 &frac14; inches high.</p>
<p>We are asking for $45 or your best offer.</p>
<p>It is in the primitive style which emphasizes the beauty of simpler times.</p>
<p>Bright, clean colors were used to highlight the purity of this scene.</p>
"""
artifact.kijijiSale.askingPrice = "45"
artifact.kijijiSale.minimumAcceptableOfferPrice = "20"
artifact.kijijiSale.maximumAutomaticRejectPrice = "15"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact_2018-05-24_15.23.57.html")
print "Updated Artifact_2018-05-24_15.23.57.html."
