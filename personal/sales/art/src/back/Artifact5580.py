import page

artifact = page.Artifact()        
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000055xx/00005573/IMG_5580.JPG"
artifact.imageAltText = "IMG_5580"
artifact.imageTitle = "IMG_5580"
artifact.title = "Traditional Harvest"
artifact.eBaySale.title = "Traditional Harvest - signed original oil on canvas board"
artifact.eBaySale.description = """<p>I painted and signed this original oil painting. THIS IS NOT
A PRINT.  It is in the primitive style which I feel helps emphasize the beauty of simpler times.</p>
<p>This painting shows a scene that can only be found where the Amish and Mennonites live today.
Before combines and tractors burst onto the scene with their noise and pollution the country was
a much more peaceful place to be.</p>
<p>This painting is on canvas board and is mounted in a wood frame. This painting is ready-to-hang.</p>
<p>The dimensions of this painting, including frame, are 20 inches wide by 16 inches high.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil, canvas board"
artifact.eBaySale.firstBidPrice = "$7.00"
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "$34.99"
artifact.eBaySale.singleItemShippingPrice = "$15.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140741869806",
                            "eBay posting of 2012/04/20"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140736092942", 
                            "eBay posting of 2012/04/06"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140654692665", 
                            "eBay posting of 2011/12/02"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140644463060", 
                            "eBay posting of 2011/11/18")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, painting, original painting, oil, canvas board, folk art, primitive, pastoral"
artifact.etsySale.purchasePrice = "$45.00"
artifact.etsySale.singleItemShippingPrice = "$15.00"
artifact.etsySale.multipleItemShippingPrice = "$7.50"
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

renderer.render("../Artifact5580.html")
print "Updated Artifact5580.html."
