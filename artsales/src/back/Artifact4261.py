import page

artifact = page.Artifact()
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000042xx/00004257/IMG_4261.JPG"
artifact.imageAltText = "IMG_4261"
artifact.imageTitle = "IMG_4261"
artifact.title = "Rustic Fish-pond"
artifact.eBaySale.title = "Rustic Fish-pond"
artifact.eBaySale.description = """<p>This signed original water-color painting shows a fish-pond
in a very natural setting.  In the background is a cat looking to pluck an easy meal from its 
depths.</p>
<p>This painting is not a photocopy or a print.  It is a pleasing painting with many vivid colors.
It would look great on any wall.</p>
<p>This cheerful watercolor painting was done on 145 lb acid-free watercolor paper. The picture is
12 inches by 9&#189; inches.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor"
artifact.eBaySale.firstBidPrice = "$5.00 USD"
artifact.eBaySale.reservePrice = "$19.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$10.00"
artifact.eBaySale.links = []
artifact.etsySale.title = "Original watercolor painting - Rustic Fish Pond"
artifact.etsySale.description = """<p>This signed original water-color painting shows a fish-pond
in a very natural setting. In the background is a cat looking to pluck an easy meal from its
depths.</p>
<p>This painting is not a photocopy or a print. It is a pleasing painting with many vivid colors.
It would look great on any wall.</p>
<p>This cheerful watercolor painting was done on 145 lb acid-free watercolor paper. The picture
is 12 inches by 9&frac12; inches.</p>
<p>Thanks for taking the time to view my work.</p>
"""
artifact.etsySale.tags = "art, original painting, watercolor, pond, nature, wild, idyllic"
artifact.etsySale.purchasePrice = "$20.00"
artifact.etsySale.singleItemShippingPrice = "$10.00"
artifact.etsySale.multipleItemShippingPrice = "$5.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/63758218/rustic-fish-pond-original-watercolor",
                            "Etsy posting of 2010/12/06")]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact4261.html")
print "Updated Artifact4261.html."