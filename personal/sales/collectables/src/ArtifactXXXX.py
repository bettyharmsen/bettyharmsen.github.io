import page

artifact = page.Artifact()
        
artifact.imageUrl = ""
artifact.imageAltText = ""
artifact.imageTitle = ""
artifact.title = ""
artifact.eBaySale.title = ""
artifact.eBaySale.description = ""
artifact.eBaySale.materials = ""
artifact.eBaySale.firstBidPrice = "-" 
artifact.eBaySale.reservePrice = "-"
artifact.eBaySale.buyItNowPrice = "-"
artifact.eBaySale.singleItemShippingPrice = "-"
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

renderer.render("../ArtifactXXXX.html")
print "Updated ArtifactXXXX.html."
