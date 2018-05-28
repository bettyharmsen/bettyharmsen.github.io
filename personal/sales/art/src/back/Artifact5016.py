import page

artifact = page.Artifact()        
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000050xx/00005014/IMG_5016.JPG"
artifact.imageAltText = "IMG_5016"
artifact.imageTitle = "IMG_5016"
artifact.title = "Old Barn in the Country"
artifact.eBaySale.title = "Old Barn in the Country - signed original watercolor"
artifact.eBaySale.description = """<p>I painted and signed this original oil painting. THIS IS NOT
A PRINT.</p>
<p>This painting shows a traditional barn like you used to be able to find all over rural America.
Unfortunately, these days, barns like this are getting to be harder to find.</p>
<p>The dimensions of this painting, including frame, are 11 &#188; inches wide by 12 &#189; inches
high.</p>
<p>This watercolor painting was done on 145 pound acid-free paper.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor, paper"
artifact.eBaySale.firstBidPrice = "$3.00" 
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$12.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140554041007", 
                            "eBay posting of 2011/05/23"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140539612589", 
                            "eBay posting of 2011/04/25")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, painting, original painting, watercolor, folk art, primitive, pastoral, farm, barn"
artifact.etsySale.purchasePrice = "$25.00"
artifact.etsySale.singleItemShippingPrice = "$12.00"
artifact.etsySale.multipleItemShippingPrice = "$6.00"
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

renderer.render("../Artifact5016.html")
print "Updated Artifact5016.html."
