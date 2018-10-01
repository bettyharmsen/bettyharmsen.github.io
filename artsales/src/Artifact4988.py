import page

artifact = page.Artifact()        
        
artifact.imageUrl = "images/IMG_4988.JPG"
artifact.imageAltText = "IMG_4988"
artifact.imageTitle = "IMG_4988"
artifact.title = "Barn in the Country"
artifact.eBaySale.title = "Barn in the Country - Original oil painting on canvas board for sale by artist"
artifact.eBaySale.description = """<p>I painted and signed this original oil painting. This is not a print.
</p>
<p>This painting shows a lonely barn in the country.</p>
<p>This painting is on canvas board and is mounted in a wood frame. This painting is ready-to-hang.</p>
<p>The dimensions, including frame, are 19 inches wide by 15 inches high.</p>
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
artifact.eBaySale.materials = "oil, canvas board "
artifact.eBaySale.firstBidPrice = "7.00"
artifact.eBaySale.reservePrice = "24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "10.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140554039124",
                            "eBay posting of 2011/05/23"),]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, painting, original painting, oil, canvas board, folk art, primitive, pastoral"
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
artifact.etsySale.links = []
artifact.kijijiSale.title = "Pheasant in Fir Tree - Original painting for sale by artist"
artifact.kijijiSale.description = """<p>Painting shows a lonely barn in the country.</p>
<p>It is 19" by 15" with wood frame and is ready-to-hang.</p>
<p>Painted with oil paints on canvas board.</p>
<p>This is a signed original painting by me, Betty Harmsen.  It is not a print.</p>
<p>I am asking for $20 but I am willing to negotiate.</p>
"""
artifact.kijijiSale.askingPrice = "$20.00"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = [("http://www.kijiji.ca/v-view-details.html?adId=1096668553",
                              "Kijiji sale starting 2015/08/21"),
                              ("http://london.kijiji.ca/c-buy-and-sell-art-collectibles-Original-oil-painting-on-canvas-board-for-sale-by-artist-W0QQAdIdZ543560036",
                              "Kijiji sale starting 2013/11/15")]

renderer = page.Renderer(artifact)

renderer.render("../Artifact4988.html")
print "Updated Artifact4988.html."
