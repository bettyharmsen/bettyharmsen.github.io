import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000038xx/00003889/IMG_3891.JPG"
artifact.imageAltText = "IMG_3891"
artifact.imageTitle = "IMG_3891"
artifact.title = "Field of Many Colors"
artifact.eBaySale.title = "Field of Many Colors - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>This signed original oil painting is a rural scene with a
field filled with wild-flowers.  It has many bright colors and would be a beautiful addition to
any wall.</p>
<p>This painting is 14" by 11" and continues over the edges.  There are no staples on any of the
edges.  It does not need a frame and is ready to hang.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil paints, canvas"
artifact.eBaySale.firstBidPrice = "$5.00"
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$15.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140516994458",
                            "eBay listing starting 2011/02/25")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, original painting, oil painting, canvas, landscape, pastoral, wild flowers, flowers"
artifact.etsySale.purchasePrice = "$60.00"
artifact.etsySale.singleItemShippingPrice = "$15.00"
artifact.etsySale.multipleItemShippingPrice = "$10.00"
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

renderer.render("../Artifact3891.html")
print "Updated Artifact3891.html."