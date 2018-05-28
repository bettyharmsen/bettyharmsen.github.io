import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_4291.JPG"
artifact.imageAltText = "IMG_4291"
artifact.imageTitle = "IMG_4291"
artifact.title = "Amish Barn Raising"
artifact.eBaySale.title = "Amish Barn Raising - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>This is a signed original painting.  This painting portrays a
group of Amish farmers getting together to raise a barn.</p>
<p>Can you imagine how they managed to put up a barn without the help of a modern crane to lift
those heavy beams?  Luckily neighbors and friends came in droves to give a helping hand and enjoy
the opportunity to socialize and feast on the meals the Amish women provided.</p>
<p>This oil painting is on canvas board.  Its size is 15 inches by 12 inches including the frame.</p>
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
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140624880950",
                            "eBay posting starting 2011/11/21"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140460323741",
                            "eBay posting starting 2010/09/30"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140450520376",
                            "eBay posting starting 2010/09/07")]
artifact.etsySale.title = "Original oil painting on canvas board - Amish Barn Raising"
artifact.etsySale.description = """<p>This is a signed original painting. This painting portrays a
group of Amish farmers getting together to raise a barn.</p>
<p>Can you imagine how they managed to put up a barn without the help of a modern crane to lift 
those heavy beams? Luckily neighbors and friends came in droves to give a helping hand and enjoy
the opportunity to socialize and feast on the meals the Amish women provided.</p>
<p>This oil painting is on canvas board. Its size is 15 inches by 12 inches including the frame.</p>
<p>Thank you very much for looking at my art and I hope you like it.</p>
"""
artifact.etsySale.tags = "art, original painting, oil painting, canvas board, folk art, primitive, amish"
artifact.etsySale.purchasePrice = "$45.0"
artifact.etsySale.singleItemShippingPrice = "$10.00"
artifact.etsySale.multipleItemShippingPrice = "$7.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/45553920/original-oil-painting-on-canvas-board", 
                            "Etsy posting starting 2010/04/25")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact4291.html")
print "Updated Artifact4291.html."
