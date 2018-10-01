import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_3907.JPG"
artifact.imageAltText = "IMG_3907"
artifact.imageTitle = "IMG_3907"
artifact.title = "Poppies in a Field"
artifact.eBaySale.title = "Poppies in a Field - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>This oil painting on canvas depicts a group of bright red
poppies standing in front of a golden grain field.</p>
<p>In the background, you can see a few simple buildings, evergreen trees and a clear blue sky.</p>
<p>I used clear bold colours in this painting to emphasize the purity and vibrance of this scene.
The field is full of life.</p>
<p>This painting is 10" by 8" and continues over the edges.  There are no staples on the visible
edges. It is a signed original.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil paints, canvas"
artifact.eBaySale.firstBidPrice = "$5.00" 
artifact.eBaySale.reservePrice = "$14.99"
artifact.eBaySale.buyItNowPrice = "$24.99"
artifact.eBaySale.singleItemShippingPrice = "$10.00"
artifact.eBaySale.links = [("http://www.ebay.com/itm/-/141825712425?",
                            "eBay listing starting 2015/11/11"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140963613546",
                            "eBay listing starting 2013/04/26"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140914983596",
                            "eBay listing starting 2013/02/08"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140769905494",
                            "eBay listing starting 2012/06/08"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140741865306",
                            "eBay listing starting 2012/04/20"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140736109048",
                            "eBay listing starting 2012/04/06"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140649364388",
                            "eBay listing starting 2011/11/25"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140639082268",
                            "eBay listing starting 2011/11/11")]
artifact.etsySale.title = "Oil painting on canvas - Poppies in a Field"
artifact.etsySale.description = """<p>This oil painting on canvas depicts a group of bright red
poppies standing in front of a golden grain field.</p>
<p>In the background, you can see a few simple buildings, evergreen trees and a clear blue sky.</p>
<p>I used clear bold colours in this painting to emphasize the purity and vibrance of this scene.
The field is full of life.</p>
<p>This painting is 10" by 8" and continues over the edges. There are no staples on the visible
edges. It is a signed original.</p>
<p>Thanks for taking the time to view my work.</p>
"""
artifact.etsySale.tags = "art, original painting, oil painting, canvas, landscape, pastoral, wild flowers, flowers"
artifact.etsySale.purchasePrice = "$35.00"
artifact.etsySale.singleItemShippingPrice = "$10.00"
artifact.etsySale.multipleItemShippingPrice = "$7.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/63757239/poppies-in-a-field-oil-painting-on",
                            "Etsy listing starting 2010/12/06")]
artifact.kijijiSale.title = "Oil Painting - Poppies in a Field"
artifact.kijijiSale.description = """<p>This an oil painting on canvas.
This painting is 10" by 8" and continues over the edges.  There are no
staples on the visible edges. This painting depicts a group of bright red
poppies standing in front of a golden grain field. The original artist is
asking for $35 or your best offer.
</p>"""
artifact.kijijiSale.askingPrice = "$35"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact3907.html")
print "Updated Artifact3907.html."
