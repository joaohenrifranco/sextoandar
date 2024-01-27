from pydantic.dataclasses import dataclass
import requests
from typing import List, Optional


@dataclass
class SearchResponse:
    search: "Search"


@dataclass
class Search:
    result: "Result"
    totalCount: int


@dataclass
class Result:
    listings: "List[ListingResult]"


@dataclass
class ListingResult:
    listing: "Listing"
    medias: "List[Media]"


@dataclass
class Listing:
    id: str
    title: str
    description: str
    address: "Address"
    pricingInfos: "List[PricingInfo]"


@dataclass
class PricingInfo:
    rentalInfo: Optional["RentalInfo"] = None


@dataclass
class RentalInfo:
    monthlyRentalTotalPrice: Optional[float] = None


@dataclass
class Address:
    city: str
    neighborhood: str
    street: Optional[str] = None


@dataclass
class Media:
    url: str


class ZapAPI:
    def log(self, message: str) -> None:
        print(f"[ZAP_API] {message}")

    def _fetch_items_page(self, page_size: int = 50, page: int = 1) -> SearchResponse:
        url = "https://glue-api.zapimoveis.com.br/v2/listings"
        params = {
            "user": "3244c121-b5c9-4b8e-bf4c-030889184e54",
            "portal": "ZAP",
            "images": "webp",
            "includeFields": "search(result(listings(listing(listingsCount,sourceId,displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,createdDate,tier),medias,accountLink,link)),totalCount),page,facets,fullUriFragments,superPremium(search(result(listings(listing(listingsCount,sourceId,displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,createdDate,tier),medias,accountLink,link)),totalCount))",
            "schema": "",
            "categoryPage": "RESULT",
            "developmentsSize": "0",
            "superPremiumSize": "0",
            "__zt": "mtc:deduplication2023",
            "business": "RENTAL",
            "parentId": "null",
            "listingType": "USED",
            "usableAreasMin": "35",
            "rentalTotalPriceMin": "2000",
            "rentalTotalPriceMax": "4500",
            "rentTotalPrice": "true",
            "addressCity": "Rio de Janeiro,Rio de Janeiro,Rio de Janeiro,Ipanema,Rio de Janeiro,Rio de Janeiro,Rio de Janeiro,Rio de Janeiro,Rio de Janeiro",
            "addressZone": "Zona Sul,Zona Sul,Zona Sul,,Zona Sul,Zona Sul,Zona Sul,Zona Sul,Zona Sul",
            "addressLocationId": "BR>Rio de Janeiro>NULL>Rio de Janeiro>Zona Sul>Botafogo,BR>Rio de Janeiro>NULL>Rio de Janeiro>Zona Sul>Leme,BR>Rio de Janeiro>NULL>Rio de Janeiro>Zona Sul>Copacabana,BR>Minas Gerais>NULL>Ipanema,BR>Rio de Janeiro>NULL>Rio de Janeiro>Zona Sul>Leblon,BR>Rio de Janeiro>NULL>Rio de Janeiro>Zona Sul>Flamengo,BR>Rio de Janeiro>NULL>Rio de Janeiro>Zona Sul>Lagoa,BR>Rio de Janeiro>NULL>Rio de Janeiro>Zona Sul>Jardim Botanico,BR>Rio de Janeiro>NULL>Rio de Janeiro>Zona Sul>Humaita",
            "addressState": "Rio de Janeiro,Rio de Janeiro,Rio de Janeiro,Minas Gerais,Rio de Janeiro,Rio de Janeiro,Rio de Janeiro,Rio de Janeiro,Rio de Janeiro",
            "addressNeighborhood": "Botafogo,Leme,Copacabana,,Leblon,Flamengo,Lagoa,Jardim Botânico,Humaitá",
            "addressPointLat": "-22.951193,-22.961502,-22.969442,-19.800525,-22.984337,-22.936822,-22.962137,-22.962137,-22.956712",
            "addressPointLon": "-43.180784,-43.16624,-43.186845,-41.714057,-43.223142,-43.175702,-43.207691,-43.207691,-43.198498",
            "addressType": "neighborhood,neighborhood,neighborhood,city,neighborhood,neighborhood,neighborhood,neighborhood,neighborhood",
            "unitTypes": "APARTMENT,APARTMENT,APARTMENT,HOME,HOME,HOME,HOME,APARTMENT,APARTMENT,APARTMENT,ALLOTMENT_LAND,FARM",
            "unitTypesV3": "APARTMENT,UnitType_NONE,KITNET,HOME,TWO_STORY_HOUSE,CONDOMINIUM,VILLAGE_HOUSE,PENTHOUSE,FLAT,LOFT,RESIDENTIAL_ALLOTMENT_LAND,FARM",
            "unitSubTypes": "UnitSubType_NONE,DUPLEX,TRIPLEX|STUDIO|KITNET|UnitSubType_NONE,TWO_STORY_HOUSE,SINGLE_STOREY_HOUSE,KITNET|TWO_STORY_HOUSE|CONDOMINIUM|VILLAGE_HOUSE|PENTHOUSE|FLAT|LOFT|UnitSubType_NONE,CONDOMINIUM,VILLAGE_HOUSE|UnitSubType_NONE,CONDOMINIUM",
            "usageTypes": "RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL",
            "page": str(page),
            "size": str(page_size),
            "from": str(page_size * page),
            "levels": "NEIGHBORHOOD",
            "ref": "",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "*/*",
            "Accept-Language": "en,en-US;q=0.8,pt-BR;q=0.5,pt;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.zapimoveis.com.br/",
            "x-domain": ".zapimoveis.com.br",
            "X-DeviceId": "3244c121-b5c9-4b8e-bf4c-030889184e54",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTM4NzMwNDMsInVzZXJfbmFtZSI6ImpvYW9oZW5yaXF1ZS5mcmFuY29AZ21haWwuY29tIiwianRpIjoiZGEzNWI2MGMtZjY3My00NGJmLWI4YmEtNGM3NjM2ZGMxMDQ0IiwiY2xpZW50X2lkIjoiemFwLXNpdGUiLCJzY29wZSI6WyJyZWFkIiwid3JpdGUiXX0.9FCIcp6lu5LdRcb0d38NDHc8mupM-qUHk7XK31ZhYzo",
            "Origin": "https://www.zapimoveis.com.br",
            "DNT": "1",
            "Sec-GPC": "1",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "TE": "trailers",
        }

        response = requests.get(url, headers=headers, params=params)
        response.encoding = "utf-8"

        parsed = None
        try:
            parsed = SearchResponse(**response.json())
        except Exception as e:
            self.log("Error parsing response:")
            self.log(str(response.status_code))
            self.log(response.text)
            raise e

        return parsed

    def fetch_listings(self) -> List[ListingResult]:
        page_size = 100
        page = 0
        response = self._fetch_items_page(page_size, page)
        total_count = response.search.totalCount
        self.log(f"Fetching {total_count} listings...")
        fetched_listings = response.search.result.listings

        while len(fetched_listings) < total_count:
            page += 1
            response = self._fetch_items_page(page_size, page)
            fetched_listings += response.search.result.listings
            self.log(
                f"Fetched {len(fetched_listings)}/{response.search.totalCount} listings (Page {page}/{total_count // page_size})"
            )

        return fetched_listings
