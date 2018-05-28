import page

artifact = page.Artifact()        
        
artifact.imageUrl = "images/IMG_5009.JPG"
artifact.imageAltText = "IMG_5009"
artifact.imageTitle = "IMG_5009"
artifact.title = "Cat Teasing Dog"
artifact.eBaySale.title = "Cat Teasing Dog - signed original watercolor"
artifact.eBaySale.description = """<p>This is a signed original painting. It is not a print.</p>
<p>Anybody who lives with both cats and dogs will recognize this scene and will be familiar with
the chaos that may follow.</p>
<p>This was painted on 145 pound acid free paper. Including the attractive wooden frame, it is 
16" by 13".  It is ready to hang.</p>
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
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140624855756", 
                            "eBay listing starting 2011/11/21"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140554040071",
                            "eBay listing starting 2011/05/23"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140539609191", 
                            "eBay listing starting 2011/04/25")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, original painting, watercolor, still-life, cats, dogs, cute"
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

renderer.render("../Artifact5009.html")
print "Updated Artifact5009.html."
