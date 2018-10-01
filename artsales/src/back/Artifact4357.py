import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000043xx/00004357/IMG_4357.JPG"
artifact.imageAltText = "IMG_4357"
artifact.imageTitle = "IMG_4357"
artifact.title = "Majestic Mount Rushmore"
artifact.eBaySale.title = "Majestic Mount Rushmore"
artifact.eBaySale.description = """<p>I painted this picture of this American icon because I felt
that, despite the fact that I am not American, it was quite inspirational.</p>
<p>I tried to capture the majesty of the monument, as well as the mountains and pines surrounding it.</p>
<p>I painted and signed this original water-color painting. This is not a photocopy or print.</p>
<p>The dimensions, including matte, are 9&#189; inches wide by 7 inches high.  It is painted on
145 pound acid-free watercolor paper.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor"
artifact.eBaySale.firstBidPrice = "$4.00" 
artifact.eBaySale.reservePrice = "$19.99"
artifact.eBaySale.buyItNowPrice = "$20.00"
artifact.eBaySale.singleItemShippingPrice = "$5.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140527967893",
                            "eBay posting of 2011/03/25"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140487425783",
                            "eBay posting of 2010/12/06")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, painting, original painting, watercolor, monument, americana"
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

renderer.render("../Artifact4357.html")
print "Updated Artifact4357.html."
