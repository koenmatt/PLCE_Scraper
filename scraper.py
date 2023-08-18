import requests
from bs4 import BeautifulSoup
import pandas as pd

number_of_products= 23503

start_list = list(range(0, 23503 + 1, 20))

def get_inventory_info(inv_q, offset):

    url = f"https://search.unbxd.io/8870d5f30d9bebafac29a18cd12b801d/childrensplace-com702771523455856/search?variants=true&variants.count=100&version=V2&rows=20&start={offset}&pagetype=boolean&q={inv_q}&promotion=false&fields=c_accessories,TCPPromotions,TCPUSPromotions,TCPCAPromotions,productimage,alt_img,style_partno,swatchimage,giftcard,TCPProductIndUSStore,TCPWebOnlyFlagUSStore,TCPWebOnlyFlagCanadaStore,TCPFitMessageUSSstore,TCPFit,product_name,TCPColor,top_rated,imagename,productid,uniqueId,favoritedcount,TCPBazaarVoiceReviewCount,categoryPath3_catMap,categoryPath2_catMap,product_short_description,style_long_description,min_list_price,min_offer_price,TCPBazaarVoiceRating,product_long_description,seo_token,variantCount,prodpartno,variants,v_tcpfit,v_qty,v_tcpsize,style_name,v_item_catentry_id,v_listprice,v_offerprice,v_qty,variantId,auxdescription,list_of_attributes,additional_styles,TCPLoyaltyPromotionTextUSStore,TCPLoyaltyPLCCPromotionTextUSStore,v_variant,low_offer_price,high_offer_price,low_list_price,high_list_price,long_product_title,TCPOutOfStockFlagUSStore,TCPOutOfStockFlagCanadaStore,TCPMultiPackUSStore,TCPMultiPackCanadaStore,TCPMultiPackReferenceUSStore,TCPMultiPackReferenceCanadaStore,single_mapping,multipack_mapping,set_mapping,TCPStyleTypeUS,TCPStyleTypeCA,TCPStyleQTYCA,TCPStyleQTYUS,productfamily,TCPStyleColorCA,TCPStyleColorUS,TCPProductIndCanadaStore,TCPLoyaltyPromoPLCCMultiplierUSStore,TCPLoyaltyPromoMultiplierUSStore,TCPLoyaltyPromoPLCCMultiplierCAStore,TCPLoyaltyPromoMultiplierCAStore,TCPCustomSalePrice,TCPCustomListPrice,v_clothingsize,v_shoessize,v_accessoriessize,isVMPEnabled,is_hard_mark_enable,product_badge,influencer_tags,v_qty_boss&uid=uid-1692391842480-24209"

    response = requests.get(url)

    data = response.json()
    
    return data['response']['products']