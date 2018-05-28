import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_4322.JPG"
artifact.imageAltText = "IMG_4322"
artifact.imageTitle = "IMG_4322"
artifact.title = "Girl Picking Wild Flowers"
artifact.eBaySale.title = "Girl Picking Wild Flowers"
artifact.eBaySale.description = """<p>This painting portrays a little girl picking wild flowers in
a field on a Spring day.</p>
<p>I used bright reds, soft blues, and various green hues to emphasize the purity and vibrancy of
this scene.</p>
<p>This is a peaceful pastoral scene under a calm blue sky. The pasture is brimming with life.  I
love painting these scenes.  I grew up in the country and I still enjoy visting the country-side.
</p>
<p>This painting includes a frame and measures 14 inches by 11 inches.  It was created using oil
paints on masonite.</p>
<p>This is a signed original painting.  It is not a print.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil paints, masonite, wood frame"
artifact.eBaySale.firstBidPrice = "$7.00" 
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "$35.00"
artifact.eBaySale.singleItemShippingPrice = "$12.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140487419295",
                            "eBay posting starting 2010/12/06"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140480468386",
                            "eBay posting starting 2010/11/19"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140460326629",
                            "eBay posting starting 2010/09/30")]
artifact.etsySale.title = "Girl Picking Wild Flowers - original oil painting on masonite"
artifact.etsySale.description = """<p>This painting portrays a little girl picking wild flowers in
a field on a Spring day.</p>
<p>I used bright reds, soft blues, and various green hues to emphasize the purity and vibrancy of
this scene.</p>
<p>This is a peaceful pastoral scene under a calm blue sky. The pasture is brimming with life.
I love painting these scenes.  I grew up in the country and I still enjoy visting the country-side.
</p>
<p>This painting includes a frame and measures 14 inches by 11 inches.  It was created using oil
paints on masonite.</p>
<p>This is a signed original painting.  It is not a print.</p>
"""
artifact.etsySale.tags = "art, original painting, oil painting, masonite, landscape, pastoral, wild flowers, flowers, girl"
artifact.etsySale.purchasePrice = "$35.00"
artifact.etsySale.singleItemShippingPrice = "$12.00"
artifact.etsySale.multipleItemShippingPrice = "$7.00"
artifact.etsySale.links = [("http://www.etsy.com/view_listing.php?listing_id=35055394",
                            "Etsy posting starting 2009/11/22")]
artifact.kijijiSale.title = "Girl Picking Wild Flowers - Original painting for sale by artist"
artifact.kijijiSale.description = """<p>Painting shows a little girl picking wild flowers in a
field on a Spring day.</p>
<p>It is 14" by 11" with wooden frame.</p>
<p>Painted with oil paints on masonite.</p>
<p>This is a signed original painting by me, Betty Harmsen.  It is not a print.</p>
<p>I am asking for $45 or your best offer.</p>
"""
artifact.kijijiSale.askingPrice = "$45.00"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact2107.html")
print "Updated Artifact2107.html."