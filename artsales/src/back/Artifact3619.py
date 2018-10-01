import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000036xx/00003616/IMG_3619.JPG"
artifact.imageAltText = "IMG_3619"
artifact.imageTitle = "IMG_3619"
artifact.title = "Quaint Village Scene"
artifact.eBaySale.title = "Quaint Village Scene - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>I painted and signed this original oil painting. THIS IS NOT A PRINT.</p>
<p>This painting portrays an idyllic village scene in winter time.</p>
<p>It is in the primitive style which I feel helps emphasize the beauty of simpler times.</p>
<p>I used bright, clean colors to highlight the purity of this scene. The sky is clear blue, the
trees are deep green, and the snow is a pristine white.</p>
<p>This painting is on canvas board and is mounted in a lovely stained wood frame. This is painting
is ready-to-hang.</p>
<p>The dimensions, including frame, are 16 inches wide by 13 inches high.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil, canvas board"
artifact.eBaySale.firstBidPrice = "$7.00" 
artifact.eBaySale.reservePrice = "$24.99 USD"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$12.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140539601344",
                            "eBay posting of 2011/04/25"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140487417877",
                            "eBay posting of 2010/12/06"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140480471757",
                            "eBay posting of 2010/11/19")]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, original painting, oil painting, canvas board, folk art, primitive, pastoral"
artifact.etsySale.purchasePrice = "$45.00"
artifact.etsySale.singleItemShippingPrice = "$10.00"
artifact.etsySale.multipleItemShippingPrice = "$7.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/32829422/quaint-village-scene-original-primitive",
                            "Etsy posting of 2010/07/12"),
                           ("http://www.etsy.com/view_listing.php?listing_id=42219037",
                            "Etsy posting of 2010/03/07"),
                           ("http://www.etsy.com/view_listing.php?listing_id=32829422",
                            "Etsy posting of 2009/10/18")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact3619.html")
print "Updated Artifact3619.html."