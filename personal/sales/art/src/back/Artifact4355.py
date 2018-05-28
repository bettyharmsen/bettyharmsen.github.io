import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000043xx/00004349/IMG_4355.JPG"
artifact.imageAltText = "IMG_4355"
artifact.imageTitle = "IMG_4355"
artifact.title = "Playing In The Snow"
artifact.eBaySale.title = "Playing In The Snow - original oil painting for sale by artist"
artifact.eBaySale.description = """<p>I painted and signed this original oil painting. THIS IS NOT A PRINT.</p>
<p>This painting shows an idyllic scene of children playing in the snow in a rustic village.</p>
<p>It is in the primitive style which I feel helps emphasize the beauty of simpler times.</p>
<p>I used bright, clean colors to highlight the purity of this scene. The sky is clear blue, the
trees are deep green, and the snow is a pristine white. </p>
<p>This painting is on canvas board and is mounted in a wood frame. This painting is ready-to-hang.</p>
<p>The dimensions, including frame, are 15 inches wide by 12 inches high.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "oil, canvas board "
artifact.eBaySale.firstBidPrice = "$5.00"
artifact.eBaySale.reservePrice = "$19.99"
artifact.eBaySale.buyItNowPrice = "$24.99"
artifact.eBaySale.singleItemShippingPrice = "$14.00"
artifact.eBaySale.links = [("http://www.ebay.com/itm/-/141825706369?",
                            "eBay posting of 2015/11/11"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140963597167",
                            "eBay posting of 2013/04/26"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140654695981",
                            "eBay posting of 2011/12/02"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140644454678",
                            "eBay posting of 2011/11/18"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140539595367",
                            "eBay posting of 2011/04/25"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140527958360",
                            "eBay posting of 2011/03/25"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140487421671",
                            "eBay posting of 2010/12/06")]
artifact.etsySale.title = "Original oil on canvas board - Playing In The Snow"
artifact.etsySale.description = """<p>I painted and signed this original oil painting. THIS IS NOT
A PRINT.</p>
<p>This painting shows an idyllic scene of children playing in the snow in a rustic village.</p>
<p>It is in the primitive style which I feel helps emphasize the beauty of simpler times.</p>
<p>I used bright, clean colors to highlight the purity of this scene. The sky is clear blue, the
 trees are deep green, and the snow is a pristine white.</p>
<p>This painting is on canvas board and is mounted in a wood frame. This painting is 
ready-to-hang.</p>
<p>The dimensions, including frame, are 15 inches wide by 12 inches high.</p>
<p>Thanks for taking the time to look at my art.</p>
"""
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

renderer.render("../Artifact4355.html")
print "Updated Artifact4355.html."
