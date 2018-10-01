import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000032xx/00003217/IMG_3219.JPG"
artifact.imageAltText = "IMG_3219"
artifact.imageTitle = "IMG_3219"
artifact.title = "Playing in the Woods"
artifact.eBaySale.title = "Playing in the Woods - original watercolor painting for sale by artist"
artifact.eBaySale.description = """<p>This signed original watercolor painting depicts children
playing in the woods.</p>
<p>This painting is a pleasant reminder that children can have fun without television or video
games.</p>
<p>This cheerful watercolor painting was done on 145 lb acid-free watercolor paper. The picture
is 10 inches by 6 &frac12; inches.  The matte shown is not included in this sale.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor"
artifact.eBaySale.firstBidPrice = "$3.00" 
artifact.eBaySale.reservePrice = "$14.99"
artifact.eBaySale.buyItNowPrice = "$19.99"
artifact.eBaySale.singleItemShippingPrice = "$8.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140654698776",
                            "eBay posting of 2011/12/02"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140644445542",
                            "eBay posting of 2011/11/18")]
artifact.etsySale.title = "Original watercolor painting - Playing in the Woods"
artifact.etsySale.description = """<p>This signed original watercolor painting depicts children
playing in the woods.</p>
<p>This painting is a pleasant reminder that children can have fun without television or video
games.</p>
<p>This cheerful watercolor painting was done on 145 lb acid-free watercolor paper. The picture is
10 inches by 6&frac12; inches. The matte shown is not included in this sale.</p>
<p>Thanks for taking the time to view my work.</p>
"""
artifact.etsySale.tags = "art, original painting, watercolor, idyllic, children, woods"
artifact.etsySale.purchasePrice = "$25.00"
artifact.etsySale.singleItemShippingPrice = "$8.00"
artifact.etsySale.multipleItemShippingPrice = "$4.00"
artifact.etsySale.links = []
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = [("http://www.etsy.com/listing/62357475/original-watercolor-playing-in-the-woods",
                              "Etsy posting of 2010/11/19")]

renderer = page.Renderer(artifact)

renderer.render("../Artifact3219.html")
print "Updated Artifact3219.html."