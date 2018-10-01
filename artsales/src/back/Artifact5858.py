import page

artifact = page.Artifact()        
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000058xx/00005854/IMG_5858.JPG"
artifact.imageAltText = "IMG_5858"
artifact.imageTitle = "IMG_5858"
artifact.title = "Camp on the Edge of a Forest"
artifact.eBaySale.title = "Camp on the Edge of a Forest - Original watercolor painting for sale by artist"
artifact.eBaySale.description = """<p>I painted and signed this original watercolor painting. 
This is not a print.</p>
<p>This painting shows a native encampment on the edge of a forest. It has two wig-wams and we can 
see someone enjoying the warmth of a camp-fire.</p>
<p>This painting is on acid-free paper. The matte is not included.</p>
<p>The dimensions of this painting, with the matte shown, are 14 inches wide by 11 inches high.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything 
else that I could use. I had been working in watercolors and oils for more than thirty years before
discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay, Etsy,
Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor"
artifact.eBaySale.firstBidPrice = "$3.00"
artifact.eBaySale.reservePrice = "24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$8.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140769914241", 
                            "eBay posting of 2012/06/08"),]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, painting, original painting, watercolor"
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

renderer.render("../Artifact5858.html")
print "Updated Artifact5858.html."
