import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_3208.JPG"
artifact.imageAltText = "IMG_3208"
artifact.imageTitle = "IMG_3208"
artifact.title = "A Horse and Buggy Ride"
artifact.eBaySale.title = "A Horse and Buggy Ride - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>This oil painting portrays people travelling by old-fashioned
horse and carriage in a peaceful country scene.</p>
<p>I used clean, solid colors in this painting to emphasize the purity and wholesomeness of this
way of life. There are no gray asphalt, no gray buildings and no gray smog in this work.</p>
<p>This oil painting is framed and measures 17&frac12;" by 13&frac12;".</p>
<p>It is ready-to-hang.</p>
<p>This is a signed original painting. IT IS NOT A PRINT.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil paint, canvas board"
artifact.eBaySale.firstBidPrice = "$7.00" 
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$12.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140460322473",
                            "eBay posting starting 2010/09/30"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140450503913",
                            "eBay posting starting 2010/09/07")]
artifact.etsySale.title = "A Horse and Buggy Ride - original primitive oil painting on canvas board"
artifact.etsySale.description = """<p>This oil painting portrays people travelling by old-fashioned
horse and carriage in a peaceful country scene.</p>
<p>I used clean, solid colors in this painting to emphasize the purity and wholesomeness of this
way of life. There are no gray asphalt, no gray buildings and no gray smog in this work.</p>
<p>This oil painting is framed and measures 17&frac12;" by 13&frac12;".</p>
<p>It is ready-to-hang.</p>
<p>This is a signed original painting. IT IS NOT A PRINT.</p>
"""
artifact.etsySale.tags = "art, original painting, oil painting, canvas board, folk art, primitive, landscape, pastoral, amish"
artifact.etsySale.purchasePrice = "$45.00"
artifact.etsySale.singleItemShippingPrice = "$10.00"
artifact.etsySale.multipleItemShippingPrice = "$7.00"
artifact.etsySale.links = [("http://www.etsy.com/view_listing.php?listing_id=44571403",
                            "Etsy posting starting 2010/04/11"),
                           ("http://www.etsy.com/view_listing.php?listing_id=33638989",
                            "Etsy posting starting 2009/11/01")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact3208.html")
print "Updated Artifact3208.html."