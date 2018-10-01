import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_3000.JPG"
artifact.imageAltText = "IMG_3000"
artifact.imageTitle = "IMG_3000"
artifact.title = "Harvesting Grain in the 19th Century"
artifact.eBaySale.title = "Harvesting Grain in the 19th Century - original watercolor painting"
artifact.eBaySale.description = """<p>This watercolor illustrates a group of farmers peacefully
stacking grain and straw on a horse-drawn wagon.</p>
<p>This quiet scene was once common in North America. Today, the graceful horses have been replaced
with loud, bulky tractors, and instead of 4 farmers working together there is usually only one 
person operating massive machinery all by himself.</p>
<p>This signed original is on 140 lb acid-free paper. The painting measures 11" by 9" but there is
a &frac12;" border around the painting on all sides. The matte is not included.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor"
artifact.eBaySale.firstBidPrice = "$3.00" 
artifact.eBaySale.reservePrice = "$8.99"
artifact.eBaySale.buyItNowPrice = ""
artifact.eBaySale.singleItemShippingPrice = "$6.00"
artifact.eBaySale.links = [("http://www.ebay.com/itm/-/141825719471?",
                            "eBay posting of 2015/11/11"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140654700038",
                            "eBay posting of 2011/12/02"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140644436398",
                            "eBay posting of 2011/11/18")]
artifact.etsySale.title = "Original Primitive Watercolor - Harvesting Grain in the 19th Century"
artifact.etsySale.description = """<p>This watercolor illustrates a group of farmers peacefully
stacking grain and straw on a horse-drawn wagon.</p>
<p>This quiet scene was once common in North America. Today, the graceful horses have been replaced
with loud, bulky tractors, and instead of 4 farmers working together there is usually only one
person operating massive machinery all by himself.</p>
<p>This signed original is on 140 lb acid-free paper. The painting measures 11" by 9" but there is
a &frac12;" border around the painting on all sides. The matte is not included.</p>
<p>Thanks for taking the time to look at my painting.</p>
"""
artifact.etsySale.tags = "art, original painting, watercolor painting, folk art, primitive, pastoral"
artifact.etsySale.purchasePrice = "$25.00"
artifact.etsySale.singleItemShippingPrice = "$7.00"
artifact.etsySale.multipleItemShippingPrice = "$3.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/51946695/original-primitive-watercolor-harvesting",
                            "Etsy posting of 2010/07/20")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact3000.html")
print "Updated Artifact3000.html."