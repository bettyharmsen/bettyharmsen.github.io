import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_3900.JPG"
artifact.imageAltText = "IMG_3900"
artifact.imageTitle = "IMG_3900"
artifact.title = "Village In The Country"
artifact.eBaySale.title = "Village In The Country - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>This is an original oil painting. This is the only painting 
I have made of this subject.  This is not a print.</p>
<p>This picture depicts a charming old-fashioned village that is busy with shoppers and kids
playing in the streets without fear of heavy traffic.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil paints, canvas"
artifact.eBaySale.firstBidPrice = "$7.00 USD" 
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$12.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140450516009",
                            "eBay listing starting 2010/09/07"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item!140396901910",
                            "eBay listing starting 2010/04/04"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140375344275",
                            "eBay listing starting 2010/01/17"),
                           ("http://cgi.ebay.ca/ws/eBayISAPI.dll?ViewItem&item=140360142709",
                            "eBay listing starting 2009/11/15"),
                           ("http://cgi.ebay.ca/ws/eBayISAPI.dll?ViewItem&item=140365576741",
                            "eBay listing starting 2009/12/06")]
artifact.etsySale.title = "Original oil painting on canvas - Village in the Country"
artifact.etsySale.description = """<p>This is an original oil painting. This is the only painting I
have made of this subject. This is not a print.</p>
<p>This picture depicts a charming old-fashioned village that is busy with shoppers and kids
playing in the streets without fear of heavy traffic.</p>
<p>The painting itself is on a 14 by 11 inch canvas. This painting wraps around the edges. The
staples are on the back. This painting looks great without a frame.</p>
<p>I have been painting and drawing since I was a little girl in Holland. I now live in Canada.</p>
<p>I really love paintings that depict simple rural scenes and 19th century life. I prefer to use
lively, vibrant colors - even in peaceful scenes.</p>
<p>Thanks for taking the time to view this painting.</p>
"""
artifact.etsySale.tags = "art, original painting, oil painting, canvas, folk art, primitive, pastoral"
artifact.etsySale.purchasePrice = "$45.00"
artifact.etsySale.singleItemShippingPrice = "$10.00"
artifact.etsySale.multipleItemShippingPrice = "$7.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/45063065/original-oil-painting-on-canvas---villag",
                            "Etsy listing starting 2010/04/18")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact3900.html")
print "Updated Artifact3900.html."