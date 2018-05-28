import page

artifact = page.Artifact()        
        
artifact.imageUrl = "images/IMG_4963.JPG"
artifact.imageAltText = "IMG_4963"
artifact.imageTitle = "IMG_4963"
artifact.title = "Cowboy Herding Cattle"
artifact.eBaySale.title = "Cowboy Herding Cattle - signed original watercolor"
artifact.eBaySale.description = """<p>This is a signed original painting.  It is not a print.</p>
<p>This painting shows a cowboy hard at work herding cattle. The pace of life might be slower but
it is still hard work.</p>
<p>This was painted on 145 pound acid free paper. Including the attractive wooden frame, it is 
16" by 13".</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor, paper"
artifact.eBaySale.firstBidPrice = "$5.00" 
artifact.eBaySale.reservePrice = "$24.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$12.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140624866124",
                            "eBay listing starting 2011/11/21"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140554035222",
                            "eBay listing starting 2011/05/23"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140539606690",
                            "eBay listing starting 2011/04/25")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, original painting, watercolor, folk-art, primitive, cowboy, cows"
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

renderer.render("../Artifact4963.html")
print "Updated Artifact4963.html."
