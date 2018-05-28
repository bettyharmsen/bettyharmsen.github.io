import page

artifact = page.Artifact()
        
artifact.imageUrl = "images/IMG_3931.JPG"
artifact.imageAltText = "IMG_3931.JPG"
artifact.imageTitle = "IMG_3931.JPG"
artifact.title = "Tortoise Shell Plastic Thimble Kit"
artifact.eBaySale.title = "Tortoise Shell Plastic Thimble Kit"
artifact.eBaySale.description = """<p>This is an old thimble kit. (How old is it?)</p>
<p>It looks like it is made of tortoise shell but I believe that it is made of an early plastic. </p>"""
artifact.eBaySale.materials = ""
artifact.eBaySale.firstBidPrice = "$2.00" 
artifact.eBaySale.reservePrice = "$19.99"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "$10.00"
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

renderer.render("../thimblekit.html")
print "Updated thimblekit.html."
