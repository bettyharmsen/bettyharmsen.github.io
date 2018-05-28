import page

artifact = page.Artifact()        
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000050xx/00005076/IMG_5083.JPG"
artifact.imageAltText = "IMG_5083"
artifact.imageTitle = "IMG_5083"
artifact.title = "Gathering Hay"
artifact.eBaySale.title = "Gathering Hay - signed original oil on canvas board"
artifact.eBaySale.description = """<p>I painted and signed this original oil painting. This is not
a print.</p>
<p>This painting shows some farmers loading a horse-drawn wagon with hay. This sight is rare today
but was common a century ago.</p>
<p>I painted this work in the primitive style because I feel that it helps to emphasize the
beauty of simpler times.</p>
<p>This painting is on canvas board and is mounted in a beautiful wood frame. This painting
is ready-to-hang. The dimensions of this painting, including frame, are 9&frac12; inches wide
by 7&frac12; inches high.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil, canvas board"
artifact.eBaySale.firstBidPrice = "$5.00"
artifact.eBaySale.reservePrice = "$14.99"
artifact.eBaySale.buyItNowPrice = "$24.99"
artifact.eBaySale.singleItemShippingPrice = "$10.00"
artifact.eBaySale.links = [("http://www.ebay.com/itm/-/141825690786?",
                            "eBay posting of 2015/11/11"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140963593592", 
                            "eBay posting of 2013/04/26"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140914972631", 
                            "eBay posting of 2013/02/08"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140769916646", 
                            "eBay posting of 2012/06/08"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140741868362", 
                            "eBay posting of 2012/04/20"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140736098136", 
                            "eBay posting of 2012/04/06"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140649374667", 
                            "eBay posting of 2011/11/25"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140639094270",
                            "eBay posting of 2011/11/11")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, painting, original painting, oil, canvas board, folk art, primitive, pastoral"
artifact.etsySale.purchasePrice = "$45.00"
artifact.etsySale.singleItemShippingPrice = "$10.00"
artifact.etsySale.multipleItemShippingPrice = "$7.00"
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

renderer.render("../Artifact5083.html")
print "Updated Artifact5083.html."
