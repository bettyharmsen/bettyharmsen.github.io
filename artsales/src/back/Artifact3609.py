import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000036xx/00003609/IMG_3609.JPG"
artifact.imageAltText = "IMG_3609"
artifact.imageTitle = "IMG_3609"
artifact.title = "Horse and Buggies"
artifact.eBaySale.title = "Horse and Buggies - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>This oil painting depicts people travelling by old-fashioned
horse and carriage in a peaceful country setting.</p>
<p>I used deep reds, greens and blues to bring out the freshness of this way of life.  The dirty,
grimy grays of modern roadways and buildings are nowhere to be found.</p>
<p>This oil painting is framed and measures 17 &frac12;" by 13 &frac12;".  It is ready-to-hang.</p>
<p>This is a signed original painting. IT IS NOT A PRINT.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil paints, canvas board"
artifact.eBaySale.firstBidPrice = "$7.00" 
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$12.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140460323207",
                            "eBay posting starting 2010/09/30"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140450511531",
                            "eBay posting starting 2010/09/07")]
artifact.etsySale.title = "Horses and Buggies - original primitive oil painting on canvas board"
artifact.etsySale.description = """<p>This oil painting depicts people travelling by old-fashioned
horse and carriage in a peaceful country setting. </p>
<p>I used deep reds, greens and blues to bring out the freshness of this way of life. The dirty, 
grimy grays of modern roadways and buildings are nowhere to be found. </p>
<p>This oil painting is framed and measures 17&frac12;" by 13&frac12;". It is ready-to-hang. </p>
<p>This is a signed original painting. IT IS NOT A PRINT. </p>
"""
artifact.etsySale.tags = "art, original painting, oil painting, canvas board, folk art, primitive, landscape, pastoral, amish"
artifact.etsySale.purchasePrice = "$45.00"
artifact.etsySale.singleItemShippingPrice = "$10.00"
artifact.etsySale.multipleItemShippingPrice = "$7.00"
artifact.etsySale.links = [("http://www.etsy.com/view_listing.php?listing_id=44116360",
                            "Etsy posting of 2010/04/04"),
                           ("http://www.etsy.com/view_listing.php?listing_id=33638567",
                            "Etsy posting of 2009/11/01")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact3609.html")
print "Updated Artifact3609.html."