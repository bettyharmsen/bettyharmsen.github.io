import page

artifact = page.Artifact()        
        
artifact.imageUrl = "http://192.168.0.202/images/camera/Paintings/000063xx/00006380/IMG_6392.JPG"
artifact.imageAltText = "IMG_6392"
artifact.imageTitle = "IMG_6392"
artifact.title = "Amish Families Going to Market"
artifact.eBaySale.title = "Amish Families Going to Market - Original watercolor painting for sale by artist"
artifact.eBaySale.description = """<p>This painting shows two Amish families traveling in different
carriages. Perhaps they are going to the market or some gathering. One could imagine this same 
scene playing out a century earlier, if it weren't for the hint of modernity in the background.</p>
<p>This is a watercolor painting on 140 lbs acid-free paper. The size of this painting with matte
and frame are 11 by 13 inches.</p>
<p>From a young age I have been doodling and drawing whenever I found some scrap paper or anything
else that I could use. I had been working in watercolors and oils for more than thirty years before
discovering folk-art.</p>
<p>I fell in love with folk-art when I had first seen the paintings of Grandma Moses. The 
simplicity and the cheerful colors were so appealing to me that I had made up my mind to try it.
</p>
<p>I have been creating folk-art for twenty years and I have sold many of these works on eBay, Etsy
Kijiji and in various galleries in Canada.</p>
<p>Thank you for looking at my art.</p>
<p>I hope you are just as pleased to see this painting as I was to paint it.</p>
"""
artifact.eBaySale.materials = "water-color paint, acid-free paper"
artifact.eBaySale.firstBidPrice = "$7.00"
artifact.eBaySale.reservePrice = "24.99"
artifact.eBaySale.buyItNowPrice = "$39.99"
artifact.eBaySale.singleItemShippingPrice = "12.00"
artifact.eBaySale.links = [("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140963589157",
                            "eBay posting of 2013/04/26"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140917664828",
                            "eBay posting of 2013/02/15"),
                           ("http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=140912193466",
                            "eBay posting of 2013/02/02"),]
artifact.etsySale.title = ""
artifact.etsySale.description = ""
artifact.etsySale.tags = "art, painting, original painting, still-life"
artifact.etsySale.purchasePrice = "-"
artifact.etsySale.singleItemShippingPrice = "-"
artifact.etsySale.multipleItemShippingPrice = "-"
artifact.etsySale.links = []
artifact.kijijiSale.title = "Amish Families Going to Market - Original watercolor painting"
artifact.kijijiSale.description = """<p>This painting shows two Amish families traveling in
different carriages.</p>
<p>This painting is 11" by 13" with matte and frame.</p>
<p>Painted with watercolors on 140 lb acid-free paper.</p>
<p>This is a signed original painting by me, Betty Harmsen.  It is not a print.</p>
<p>I am asking for $25 or your best offer.</p>
"""
artifact.kijijiSale.askingPrice = "$25.00"
artifact.kijijiSale.minimumAcceptableOfferPrice = "-"
artifact.kijijiSale.maximumAutomaticRejectPrice = "-"
artifact.kijijiSale.singleItemShippingPrice = "$12.00"
artifact.kijijiSale.multipleItemShippingPrice = "$8.00"
artifact.kijijiSale.links = [("http://london.kijiji.ca/c-buy-and-sell-art-collectibles-Original-watercolor-painting-for-sale-by-artist-W0QQAdIdZ539850480",
                              "Kijiji sale starting 2013/11/04"),]

renderer = page.Renderer(artifact)

renderer.render("../Artifact6392.html")
print "Updated Artifact6392.html."
