import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_0308.JPG"
artifact.imageAltText = "IMG_0308"
artifact.imageTitle = "IMG_0308"
artifact.title = "Classic Car"
artifact.eBaySale.title = "Classic Car - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>This is an original oil painting on canvas board.</p>
<p>Don't you wish that this car was sitting in your garage? Well, you can have this painting of
this beautiful car on your desk or on the wall.</p>
<p>With the included frame, this painting is 6&frac12; inches by 6&frac12; inches. Without the
frame, the painting is 4 inches by 4 inches.</p>
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
artifact.eBaySale.reservePrice = "$13.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$6.00"
artifact.eBaySale.links = []
artifact.etsySale.title = "Original oil on canvas board - Classic Car"
artifact.etsySale.description = """<p>This is an original oil painting on canvas board.</p>
<p>Don't you wish that this car was sitting in your garage? Well, you can have this painting of
this beautiful car on your desk or on the wall.</p>
<p>With the included frame, this painting is 6 1/2 inches by 6 1/2 inches. Without the frame, the
painting is 4 inches by 4 inches.</p>
<p>Thanks for taking the time to look at my art.</p>
"""
artifact.etsySale.tags = "art, original painting, oil, canvas board, automobile, classic car, still life"
artifact.etsySale.purchasePrice = "$14.00"
artifact.etsySale.singleItemShippingPrice = "$6.00"
artifact.etsySale.multipleItemShippingPrice = "$3.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/63756072/classic-car-original-oil-on-canvas-board",
                            "Etsy listing starting 2010/12/06"),
                           ("http://www.etsy.com/listing/52461497/original-oil-on-canvast-board-classic",
                            "Etsy listing starting 2010/07/27")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact0308.html")
print "Updated Artifact0308.html."