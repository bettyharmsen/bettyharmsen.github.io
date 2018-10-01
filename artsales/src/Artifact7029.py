import page

artifact = page.Artifact()        
        
artifact.imageUrl = "images/IMG_7029.JPG"
artifact.imageAltText = "IMG_7029"
artifact.imageTitle = "IMG_7029"
artifact.title = "Pheasant in Fir Tree"
artifact.eBaySale.title = "Pheasant in Fir Tree - Original watercolor painting for sale by artist"
artifact.eBaySale.description = """<p>This is a signed original painting.  It is not a print.</p>
<p>This painting shows a pheasant sitting peacefully in a fir tree.</p>
<p>This was painted with watercolor paints on 140 lb acid free paper board. Including the 
attractive wooden frame, it is 22" by 18".</p>
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
artifact.etsySale.tags = "art original painting oil painting landscape folk-art primitive"
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
artifact.etsySale.links = []
artifact.kijijiSale.title = "Pheasant in Fir Tree - Original painting for sale by artist"
artifact.kijijiSale.description = """<p>Painting shows a pheasant sitting peacefully in a fir tree.
</p>
<p>It is 22" by 18" including the attractive wooden frame.</p>
<p>Painted with watercolor paints on 140 lb acid free paper.</p>
<p>This is a signed original painting by me Betty Harmsen.  It is not a print.</p>
<p>I am asking for $35 or your best offer.</p>
"""
artifact.kijijiSale.askingPrice = "$35.00"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "$12.00"
artifact.kijijiSale.multipleItemShippingPrice = "$8.00"
artifact.kijijiSale.links = [("http://www.kijiji.ca/v-view-details.html?adId=1096670672",
                              "Kijiji sale starting 2015/08/21"),
                             ("http://london.kijiji.ca/c-buy-and-sell-art-collectibles-Original-watercolor-painting-for-sale-by-artist-W0QQAdIdZ537682239",
                              "Kijiji sale starting 2013/10/28")]

renderer = page.Renderer(artifact)

renderer.render("../Artifact7029.html")
print "Updated Artifact7029.html."