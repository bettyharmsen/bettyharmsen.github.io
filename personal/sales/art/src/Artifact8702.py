import page

artifact = page.Artifact()        
        
artifact.imageUrl = "images/IMG_8702.JPG"
artifact.imageAltText = "IMG_8702"
artifact.imageTitle = "IMG_8702"
artifact.title = "Autumn Scene Along Lonely Lake - Original watercolor painting."
artifact.eBaySale.title = "Autumn Scene Along Lonely Lake - Original watercolor painting for sale by artist"
artifact.eBaySale.description = """<p>This is a signed original painting.  It is not a print.</p>
<p>This is a pleasant memory of mine of a remote lake in Northern Ontario in Autumn.</p>
<p>This was painted with watercolor paints on 140 lb acid free paper board. It is 11" by 9".</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The 
simplicity and the cheerful colours were so appealing to me that I had made up my mind to try it.
</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay, Etsy, 
Kijiji and in various galleries in Canada.</p>
<p>Thanks for taking the time to view my work.</p>
"""
artifact.eBaySale.materials = "watercolor, paper"
artifact.eBaySale.firstBidPrice = "-"
artifact.eBaySale.reservePrice = "-"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "-"
artifact.eBaySale.links = []
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art original painting watercolor painting landscape folk-art primitive"
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
artifact.etsySale.links = []
artifact.kijijiSale.title = "Watercolour painting - Autumn Scene Along Lonely Lake."
# 12 1/2 x 14 1/2
artifact.kijijiSale.description = """<p>This was painted with
watercolor paints on 140 lb acid free paper board. It is 12&frac12;" by 14&frac12;".
This painting brings back memories of a lonely lake in Autumn.
The original artist is asking for $35 or your best offer.</p>
"""
artifact.kijijiSale.askingPrice = "$35.00"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "$12.00"
artifact.kijijiSale.multipleItemShippingPrice = "$8.00"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact8702.html")
print "Updated Artifact8702.html."