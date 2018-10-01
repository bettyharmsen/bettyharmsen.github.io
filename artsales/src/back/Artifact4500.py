import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000044xx/00004499/IMG_4500.JPG"
artifact.imageAltText = "IMG_4500"
artifact.imageTitle = "IMG_4500"
artifact.title = "Poppies and Daisies"
artifact.eBaySale.title = "Poppies and Daisies - Reverse painting on glass"
artifact.eBaySale.description = """<p>This painting shows an arrangement of daisies, poppies and
other plants in a bowl. The bowl, background and frame use simple earth-tones that contrast well
with the bright flowers. This is a reverse painting on glass which really brings out the colors
of the oil paints.</p>
<p>Including the wooden frame, this signed, original painting is 15" by 12".  It is ready to hang.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil paints, glass."
artifact.eBaySale.firstBidPrice = "$7.00" 
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$20.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140649361987",
                            "eBay Listing starting 2011/11/25"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140639107526",
                            "eBay Listing starting 2011/11/11")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, original painting, reverse painting, glass, daisies, poppies, flowers, still-life"
artifact.etsySale.purchasePrice = "$40.00"
artifact.etsySale.singleItemShippingPrice = "$20.00"
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

renderer.render("../Artifact4500.html")
print "Updated Artifact4500.html."
