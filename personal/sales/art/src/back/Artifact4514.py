import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000047xx/00004764/IMG_4769.JPG"
artifact.imageAltText = "IMG_4769"
artifact.imageTitle = "IMG_4769"
artifact.title = "Profusion of Poppies"
artifact.eBaySale.title = "Profusion of Poppies - signed original oil on canvas"
artifact.eBaySale.description = """<p>This signed original oil painting shows a field in the wild
that is bursting with the colors of poppies and other wild-flowers.</p>
<p>Wild-flowers are always appealing to me because the varieties change from one place to another
and you can always find new surprises, if you take the time to look.</p>
<p>This painting was done with oil paints on canvas. The painting extends over the staple-free
edges on all four sides. It is 10 inches wide by 8 inches high.</p>
<p>This painting would be a beautiful addition to any wall.</p>
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
artifact.eBaySale.links = [("http://www.ebay.com/itm/-/141825724279?",
                            "eBay listing starting 2015/11/11"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140963605288", 
                            "eBay listing starting 2013/04/26"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140914980969", 
                            "eBay listing starting 2013/02/08"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140769908185",
                            "eBay listing starting 2012/06/08"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140741867259",
                            "eBay listing starting 2012/04/20"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140736106519",
                            "eBay listing starting 2012/04/06"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140649369080",
                            "eBay listing starting 2011/11/25"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140639068406",
                            "eBay listing starting 2011/11/11"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140624872936",
                            "eBay listing starting 2011/10/21")]
artifact.etsySale.title = "Original oil painting - Profusion of Poppies"
artifact.etsySale.description = """<p>This signed original oil painting shows a field in the wild
that is bursting with the colors of poppies and other wild-flowers.</p>
<p>Wild-flowers are always appealing to me because the varieties change from one place to another
and you can always find new surprises, if you take the time to look.</p>
<p>This painting was done with oil paints on canvas. The painting extends over the staple-free
edges on all four sides. It is 10 inches wide by 8 inches high. This painting would be a
beautiful addition to any wall.</p>
<p>I enjoyed making this peaceful and colorful painting. I hope that you enjoyed looking at it.
</p>
<p>Thank you for taking the time to look at my work.</p>
"""
artifact.etsySale.tags = "art, original painting, oil painting, canvas, landscape, pastoral, wild flowers, flowers"
artifact.etsySale.purchasePrice = "$35.00"
artifact.etsySale.singleItemShippingPrice = "$15.00"
artifact.etsySale.multipleItemShippingPrice = "$10.00 USD"
artifact.etsySale.links = [("http://www.etsy.com/listing/68850919/profusion-of-poppies-signed-original-oil", 
                            "Etsy listing starting 2011/02/25")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact4514.html")
print "Updated Artifact4514.html."
