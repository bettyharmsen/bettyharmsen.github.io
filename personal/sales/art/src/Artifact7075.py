import page

artifact = page.Artifact()        
        
artifact.imageUrl = "images/IMG_7075.JPG"
artifact.imageAltText = "IMG_7075"
artifact.imageTitle = "IMG_7075"
artifact.title = "Field-stone House in Field of Poppies"
artifact.eBaySale.title = "Field-stone House in Field of Poppies - Original oil painting on canvas board for sale by artist"
artifact.eBaySale.description = """<p>This painting shows a quaint old field-stone house in a peaceful field of poppies.</p>
<p>This was painted with oil paints on canvas board. Including the attractive wooden frame, it is 21 1/2" by 17 1/2".</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything else that I could use.
 I had been working in watercolors and oils for more than thirty years before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The simplicity and the cheerful colors
were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay, Etsy, Kijiji and in various 
galleries in Canada.</p>
<p>Thanks for taking the time to view my work.</p>
"""
artifact.eBaySale.materials = "oil paint, canvas board"
artifact.eBaySale.firstBidPrice = "24.99"
artifact.eBaySale.reservePrice = "24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "13.99"
artifact.eBaySale.links = [("http://www.ebay.com/itm/Field-stone-House-in-Field-of-Poppies-Original-oil-painting-on-canvas-board-/141551571663",
                            "eBay sale starting 2015/01/23"),]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, original painting, oil painting, landscape, folk-art, primitive,"
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
artifact.etsySale.links = []
artifact.kijijiSale.title = "Field-stone House in Field of Poppies - Original painting"
artifact.kijijiSale.description = """<p>This painting shows a quaint old field-stone house in a peaceful field of poppies.</p>
<p>This was painted with oil paints on canvas board. Including the attractive wooden frame, it is 21 1/2" by 17 1/2".</p>
<p>This is a signed original painting by me Betty Harmsen.  It is not a print.</p>
<p>I am asking for $30 or your best offer.</p>
"""
artifact.kijijiSale.askingPrice = "$30.00"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "$12.00"
artifact.kijijiSale.multipleItemShippingPrice = "$8.00"
artifact.kijijiSale.links = [("http://london.kijiji.ca/c-buy-and-sell-art-collectibles-Original-oil-painting-on-canvas-board-for-sale-by-artist-W0QQAdIdZ533848306",
                              "Kijiji sale starting 2013/10/10"),]
renderer = page.Renderer(artifact)

renderer.render("../Artifact7075.html")
print "Updated Artifact7075.html."
