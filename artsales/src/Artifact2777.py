import page

artifact = page.Artifact()        
        
artifact.imageUrl = "images/IMG_2777.JPG"
artifact.imageAltText = "IMG_2777"
artifact.imageTitle = "IMG_2777"
artifact.title = "Autumn Scene in the Countryside "
artifact.eBaySale.title = "Autumn Scene in the Countryside - Original oil painting on canvas board for sale by artist"
artifact.eBaySale.description = """<p>This oil painting depicts a rustic scene in the country.</p>
<p>The ground is earthy brown or muted green, and the leaves are bright red and orange.</p>
<p>In the background, you can see some grazing beef cows.</p>
<p>The atmosphere is quiet.</p>
<p>The painting is a signed, framed original and measures 15" by 12" with frame.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay, Etsy,
Kijiji and in various galleries in Canada.</p>
<p>Thanks for taking the time to view my work.</p>
"""
artifact.eBaySale.materials = "oil, canvas board "
artifact.eBaySale.firstBidPrice = "7.00"
artifact.eBaySale.reservePrice = "24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "10.00"
artifact.eBaySale.links = []
artifact.etsySale.title = ""
artifact.etsySale.description = """<p>This oil painting depicts a rustic scene in the country.</p>
<p>The ground is earthy brown or muted green, and the leaves are bright red and orange.</p>
<p>In the background, you can see some grazing beef cows.</p>
<p>The atmosphere is quiet.</p>
<p>The painting is a signed, framed original and measures 15" by 12" with frame.</p>"""
artifact.etsySale.tags = "art, painting, original painting, oil, canvas board, folk art, primitive, pastoral"
artifact.etsySale.purchasePrice = "20.00"
artifact.etsySale.singleItemShippingPrice = "12.00"
artifact.etsySale.multipleItemShippingPrice = "8.00"
artifact.etsySale.links = [("http://www.etsy.com/view_listing.php?listing_id=36137879",
                            "Etsy posting starting 2009/12/06"),]
artifact.kijijiSale.title = "Original oil on canvas board - Autumn Scene in the Countryside"
artifact.kijijiSale.description = """<p>Painting shows a rustic country scene.</p>
<p>It is 15" by 12" with attractive wooden frame.</p>
<p>Painted with oil paints on canvas board.</p>
<p>This is a signed original painting by me, Betty Harmsen.  It is not a print.</p>
<p>I am asking for $20 or your best offer.</p>"""
artifact.kijijiSale.askingPrice = "$20.00"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = [("http://www.kijiji.ca/v-view-details.html?adId=1096669893",
                              "Kijiji posting starting 2015/08/21"),
                             ("http://london.kijiji.ca/c-buy-and-sell-art-collectibles-Original-oil-painting-on-canvas-board-for-sale-by-artist-W0QQAdIdZ546054831",
                              "Kijiji posting starting 2013/11/12")]

renderer = page.Renderer(artifact)

renderer.render("../Artifact2777.html")
print "Updated Artifact2777.html."
