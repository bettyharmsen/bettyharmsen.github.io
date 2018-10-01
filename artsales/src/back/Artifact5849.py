import page

artifact = page.Artifact()        
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000058xx/00005839/IMG_5849.JPG"
artifact.imageAltText = "IMG_5849"
artifact.imageTitle = "IMG_5849"
artifact.title = "Charming Village in the Mountains"
artifact.eBaySale.title = "Charming Village in the Mountains - Original watercolor painting for sale by artist"
artifact.eBaySale.description = """<p>I painted and signed this original watercolor painting.
This is not a print.</p>
<p>This painting shows a charming village in the mountains. It shows an early snowfall that has
come before that last leaves have fallen off of the trees.</p>
<p>Wouldn't this be a great place to visit? Aren't the brightly colored buildings inviting?</p>
<p>This painting is on acid-free paper and includes a lovely frame.</p>
<p>Including the frame, the dimensions of this artwork are 12 inches wide by 10 inches high.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "art, painting, original painting, watercolor"
artifact.eBaySale.firstBidPrice = "$7.00"
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "$34.99"
artifact.eBaySale.singleItemShippingPrice = "$12.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140963582135", 
                            "eBay posting of 2013/04/26"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140914965607", 
                            "eBay posting of 2013/02/08"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140769922215", 
                            "eBay posting of 2012/06/08")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = ""
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
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

renderer.render("../Artifact5849.html")
print "Updated Artifact5849.html."
