import page

artifact = page.Artifact()

artifact.imageUrl = "images/IMG_3919.JPG"
artifact.imageAltText = "IMG_3919.JPG"
artifact.imageTitle = "IMG_3919.JPG"
artifact.title = "Misprint Canadian Two Dollar Bill"
artifact.eBaySale.title = "Misprint Canadian Two Dollar Bill"
artifact.eBaySale.description = """<p>This Canadian Two Dollar Bill is a misprint with a line crossing the Queen's face. In addition to this line, the one side of the Queen's face is slightly discolored.</p>
<p>This bill was in circulation.</p>"""
artifact.eBaySale.materials = ""
artifact.eBaySale.firstBidPrice = "$2.00" 
artifact.eBaySale.reservePrice = "$19.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$7.00"
artifact.eBaySale.links = []
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = ""
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
artifact.etsySale.links = []
artifact.kijijiSale.title = ""
artifact.kijijiSale.description = ""
artifact.kijijiSale.askingPrice = "-"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "-"
artifact.kijijiSale.multipleItemShippingPrice = "-"
artifact.kijijiSale.links = []
artifact.statisticsUrl = ""

renderer = page.Renderer(artifact)

renderer.render("../twodollarbill.html")
print "Updated twodollarbill.html."
