import page

artifact = page.Artifact()

artifact.imageUrl = "images/IMG_1546.JPG"
artifact.imageAltText = "IMG_1546"
artifact.imageTitle = "IMG_1546"
artifact.title = "Show-jumping"
artifact.eBaySale.title = "Show-jumping - original watercolor painting for sale by artist"
artifact.eBaySale.description = """<p>This watercolor portrays a horse and rider jumping over an
equestrian obstacle.</p>
<p>This watercolor painting is on 140 lb. acid free paper.</p>
<p>The dimensions are 8 &frac12" by 7".</p>
<p>This is a signed original.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years 
before discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay,
Etsy, Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>"""
artifact.eBaySale.materials = "watercolor paint, acid free paper"
artifact.eBaySale.firstBidPrice = "$7.00" 
artifact.eBaySale.reservePrice = "$19.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$5.00"
artifact.eBaySale.links = []
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, original painting, watercolor, show jumping, horse, equestrian"
artifact.etsySale.purchasePrice = "$20.00"
artifact.etsySale.singleItemShippingPrice = "$5.00"
artifact.etsySale.multipleItemShippingPrice = "$2.00"
artifact.etsySale.links = [("http://www.etsy.com/listing/48401200/watercolor-on-acid-free-paper-show",
                            "Etsy listing starting 2010/05/30"),]
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []

renderer = page.Renderer(artifact)

renderer.render("../Artifact1546.html")
print "Updated Artifact1546.html."