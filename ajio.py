from requests import *
import pandas as pd
from fake_useragent import UserAgent

name, catalog_name, brandtypename, brickname, couponstatus, code, currency_iso, pricetype, actualprice, offerprice, brandname, colorgroup, discount = [], [], [], [], [], [], [], [], [], [], [], [], []
for pg in range(1, 1026, 1):
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    url = get(f'https://www.ajio.com/api/category/83?currentPage={pg}&pageSize=45&format=json&query=%3Arelevance%3Al1l3nestedcategory%3AMen%20-%20Casual%20Shoes%3Al1l3nestedcategory%3AWomen%20-%20Casual%20Shoes&sortBy=relevance&curated=true&curatedid=footwear-4792-56591&gridColumns=3&facets=l1l3nestedcategory%3AMen%20-%20Casual%20Shoes%3Al1l3nestedcategory%3AWomen%20-%20Casual%20Shoes&advfilter=true&platform=Desktop&showAdsOnNextPage=false&is_ads_enable_plp=true&displayRatings=true', headers=headers)
    try:
        products = url.json()['products']
        print(f'https://www.ajio.com/api/category/83?currentPage={pg}&pageSize=45&format=json&query=%3Arelevance%3Al1l3nestedcategory%3AMen%20-%20Casual%20Shoes%3Al1l3nestedcategory%3AWomen%20-%20Casual%20Shoes&sortBy=relevance&curated=true&curatedid=footwear-4792-56591&gridColumns=3&facets=l1l3nestedcategory%3AMen%20-%20Casual%20Shoes%3Al1l3nestedcategory%3AWomen%20-%20Casual%20Shoes&advfilter=true&platform=Desktop&showAdsOnNextPage=false&is_ads_enable_plp=true&displayRatings=true')
        if products is not None:
            for i in products:
                name.append('NA') if 'name' not in i else name.append(i['name'])
                catalog_name.append('NA') if 'catalogName' not in i else catalog_name.append(i['catalogName'])
                brandtypename.append('NA') if 'brandTypeName' not in i else brandtypename.append(i['brandTypeName'])
                brickname.append('NA') if 'brickName' not in i else brickname.append(i['brickName'])
                couponstatus.append('NA') if 'couponStatus' not in i else couponstatus.append(i['couponStatus'])
                code.append('NA') if 'code' not in i else code.append(i['code'])
                currency_iso.append('NA') if 'wasPriceData' not in i else currency_iso.append(i['wasPriceData']['currencyIso'])
                pricetype.append('NA') if 'wasPriceData' not in i else pricetype.append(i['wasPriceData']['priceType'])
                actualprice.append('NA') if 'wasPriceData' not in i else actualprice.append(i['wasPriceData']['formattedValue'])
                offerprice.append('No offer available') if 'offerPrice' not in i else offerprice.append(i['offerPrice']['formattedValue'])
                brandname.append('NA') if 'fnlColorVariantData' not in i else brandname.append(i['fnlColorVariantData']['brandName'])
                colorgroup.append('NA') if 'fnlColorVariantData' not in i else colorgroup.append(i['fnlColorVariantData']['colorGroup'])
                discount.append('0% off') if 'discountPercent' not in i else discount.append(i['discountPercent'])
                print(i['name'])
        else:
            pass
    except :
        print('Error', f'https://www.ajio.com/api/category/83?currentPage={pg}&pageSize=45&format=json&query=%3Arelevance%3Al1l3nestedcategory%3AMen%20-%20Casual%20Shoes%3Al1l3nestedcategory%3AWomen%20-%20Casual%20Shoes&sortBy=relevance&curated=true&curatedid=footwear-4792-56591&gridColumns=3&facets=l1l3nestedcategory%3AMen%20-%20Casual%20Shoes%3Al1l3nestedcategory%3AWomen%20-%20Casual%20Shoes&advfilter=true&platform=Desktop&showAdsOnNextPage=false&is_ads_enable_plp=true&displayRatings=true')
        continue
df = pd.DataFrame({'Name': name, 'Catalog_Name': catalog_name, 'BrandTypeName': brandtypename, 'BrickName': brickname, 'CouponStatus': couponstatus,
                   'code': code, 'CurrencyISO': currency_iso, 'PriceType': pricetype, 'ActualPrice': actualprice, 'OfferPrice': offerprice,
                   'BrandName': brandname, 'ColorGroup': colorgroup, 'Discount (%)': discount})
print(df)
df.to_csv('F:/ajio.csv', index=False)
print('CSV Saved Successfully....')