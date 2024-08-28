import json
import requests
import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from navCompanion.src.useme.postgres_utility import PostgresUtil



mutuals_ = ["tata-small-cap-fund-direct-growth", "tata-digital-india-fund-direct-growth", "nippon-india-growth-fund-direct-growth",
           "nippon-india-multi-cap-fund-direct-growth", "nippon-india-small-cap-fund-direct-growth",
           "quant-small-cap-fund-direct-plan-growth", "quant-mid-cap-fund-direct-growth",
           "motilal-oswal-small-cap-fund-direct-growth", "motilal-oswal-most-focused-midcap-30-fund-regular-growth",
           "hdfc-mid-cap-opportunities-fund-direct-growth", "mahindra-manulife-small-cap-fund-direct-growth",
           "aditya-birla-sun-life-psu-equity-fund-direct-growth", "kotak-emerging-equity-scheme-direct-growth"]

mutuals_dict = {
    "small_cap": [
    "axis-small-cap-fund-direct-growth",
    "bandhan-small-cap-fund-direct-growth",
    "bank-of-india-small-cap-fund-direct-growth",
    "baroda-bnp-paribas-small-cap-fund-direct-growth",
    "birla-sun-life-small-midcap-fund-direct-growth",
    "boi-axa-small-cap-fund-direct-growth",
    "canara-robeco-small-cap-fund-direct-growth",
    "dsp-blackrock-micro-cap-fund-direct-growth",
    "edelweiss-small-cap-fund-direct-growth",
    "franklin-india-smaller-companies-fund-direct-growth",
    "hdfc-small-cap-fund-direct-growth",
    "hsbc-midcap-equity-fund-direct-growth",
    "hsbc-small-cap-fund-direct-growth",
    "icici-prudential-indo-asia-equity-fund-direct-growth",
    "idbi-small-cap-fund-direct-growth",
    "idfc-emerging-businesses-fund-direct-growth",
    "invesco-india-smallcap-fund-direct-direct-growth",
    "iti-small-cap-fund-direct-growth",
    "jm-small-cap-fund-direct-growth",
    "kotak-midcap-fund-direct-growth",
    "lic-mf-small-cap-fund-direct-growth",
    "mahindra-manulife-small-cap-fund-direct-growth",
    "motilal-oswal-small-cap-fund-direct-growth",
    "nippon-india-small-cap-fund-direct-growth",
    "pgim-india-small-cap-fund-direct-growth",
    "principal-small-cap-fund-direct-growth",
    "quant-small-cap-fund-direct-plan-growth",
    "quantum-small-cap-fund-direct-growth",
    "sbi-small-midcap-fund-direct-growth",
    "sundaram-smile-fund-direct-growth",
    "tata-small-cap-fund-direct-growth",
    "union-small-and-midcap-fund-direct-growth",
    "uti-small-cap-fund-direct-growth"
],
    "large_cap": [
    "axis-equity-fund-direct-growth",
    "axis-s-p-bse-sensex-index-fund-direct-growth",
    "bank-of-india-bluechip-fund-direct-growth",
    "baroda-bnp-paribas-large-cap-fund-direct-growth",
    "baroda-pioneer-large-cap-fund-direct-growth",
    "birla-sun-life-frontline-equity-fund-direct-growth",
    "boi-axa-bluechip-fund-direct-growth",
    "canara-robeco-large-cap-fund-direct-growth",
    "dsp-blackrock-top-100-equity-fund-direct-growth",
    "edelweiss-top-100-fund-direct-growth",
    "franklin-india-bluechip-direct-growth",
    "groww-large-cap-fund-direct-fund-growth",
    "hdfc-top-200-direct-growth",
    "hsbc-dividend-yield-equity-fund-direct-growth",
    "hsbc-equity-fund-direct-growth",
    "icici-prudential-focused-bluechip-equity-fund-direct-growth",
    "idbi-india-top-100-equity-fund-direct-growth",
    "idfc-equity-fund-direct-growth",
    "invesco-india-business-leaders-fund-direct-growth",
    "iti-large-cap-fund-direct-growth",
    "jm-equity-direct-growth",
    "kotak-50-direct-growth",
    "lic-mf-growth-fund-direct-growth",
    "mahindra-pragati-bluechip-yojana-direct-growth",
    "mirae-asset-india-opportunities-fund-direct-growth",
    "motilal-oswal-large-cap-fund-direct-growth",
    "navi-large-cap-equity-fund-direct-growth",
    "nippon-india-large-cap-fund-direct-growth",
    "pgim-india-large-cap-fund-direct-plan-growth",
    "principal-large-cap-fund-direct-growth",
    "quant-large-cap-fund-direct-growth",
    "sbi-bluechip-fund-direct-growth",
    "sundaram-bluechip-fund-direct-growth",
    "tata-large-cap-fund-direct-growth",
    "taurus-bonanza-fund-direct-growth",
    "taurus-large-cap-fund-direct-growth",
    "union-focussed-largecap-fund-direct-growth",
    "uti-unit-scheme-1986-mastershare-direct-growth",
    "whiteoak-capital-large-cap-fund-direct-growth"
],
    "mid_cap": [
    "axis-midcap-fund-direct-growth",
    "baroda-bnp-paribas-midcap-direct-growth",
    "baroda-pioneer-mid-cap-fund-direct-growth",
    "birla-sun-life-mid-cap-fund-plan-a-direct-growth",
    "canara-robeco-mid-cap-fund-direct-growth",
    "dsp-blackrock-small-and-midcap-fund-direct-growth",
    "edelweiss-mid-and-small-cap-fund-direct-growth",
    "franklin-india-prima-fund-direct-growth",
    "hdfc-mid-cap-opportunities-fund-direct-growth",
    "hsbc-mid-cap-fund-direct-growth",
    "hsbc-midcap-fund-direct-growth",
    "icici-prudential-midcap-fund-direct-growth",
    "idbi-midcap-fund-direct-growth",
    "idfc-midcap-fund-direct-growth",
    "invesco-india-mid-cap-fund-direct-growth",
    "iti-mid-cap-fund-direct-growth",
    "jm-midcap-fund-direct-growth",
    "kotak-emerging-equity-scheme-direct-growth",
    "lic-mf-midcap-fund-direct-growth",
    "mahindra-unnati-emerging-business-yojana-direct-growth",
    "mirae-asset-midcap-fund-direct-growth",
    "motilal-oswal-most-focused-midcap-30-fund-direct-growth",
    "nippon-india-growth-fund-direct-growth",
    "pgim-india-midcap-opportunities-fund-direct-growth",
    "principal-midcap-fund-direct-growth",
    "quant-mid-cap-fund-direct-growth",
    "sbi-magnum-midcap-fund-direct-growth",
    "sundaram-select-midcap-direct-growth",
    "tata-mid-cap-growth-fund-direct-growth",
    "taurus-discovery-fund-direct-growth",
    "taurus-mid-cap-fund-direct-growth",
    "union-midcap-fund-direct-growth",
    "uti-mid-cap-fund-direct-growth",
    "whiteoak-capital-mid-cap-fund-direct-growth"
]
}

job_arg = sys.argv[0]

mutuals = mutuals_dict[job_arg]


insert_query = ""

for each_mf in mutuals:
    origin_url = f"https://groww.in/v1/api/data/mf/web/v3/scheme/search/{each_mf}"
    response = requests.get(origin_url)
    if response.status_code == 200:
        mutual_fund_data = json.loads(response.text)
        companies_list = mutual_fund_data.get("holdings", [])
        green_stocks, red_stocks = 0, 0
        green_perc, red_perc = [], []
        search_id = []
        for each_company in companies_list:
            try:
                fund_details = f"https://groww.in/v1/api/stocks_data/v1/company/search_id/{each_company['stock_search_id']}?page=0&size=10"
                stock_url = requests.get(fund_details)
                stock_data = json.loads(stock_url.text)
                nse_code = stock_data.get("header", {}).get("nseScriptCode", "")
                if not stock_data:
                    continue
                companies_data = f"https://groww.in/v1/api/stocks_data/v1/accord_points/exchange/NSE/segment/CASH/latest_prices_ohlc/{nse_code}"
                price_data = requests.get(companies_data)
                price_data = json.loads(price_data.text)

                prev_closing_price = price_data["close"]
                present_price = price_data["ltp"]
                perc = round(((present_price - prev_closing_price)*100)/prev_closing_price, 2)
                red_perc.append(perc) if perc < 0 else green_perc.append(perc)

                if present_price - prev_closing_price > 0:
                    green_stocks += 1
                else:
                    red_stocks += 1
            except Exception as e:
                # print(str(e))
                continue

        red_avg = f"{round((sum(red_perc)/len(red_perc)), 2)}%" if len(red_perc) else "0%"
        green_avg = f"+{round((sum(green_perc)/len(green_perc)), 2)}%" if len(green_perc) else "0%"
        insert_query += f"""UPDATE mutual_funds SET red_stocks={red_stocks}, green_stocks={green_stocks},
         green_avg='{green_avg}', red_avg='{red_avg}' WHERE mf_id='{each_mf}';"""
        print(f"********************************{each_mf}********************************")
        print("RED STOCKS", red_stocks, f"{round((sum(red_perc)/len(red_perc)), 2)}%" if len(red_perc) else "0%")
        print("GREEN STOCKS", green_stocks, f"+{round((sum(green_perc)/len(green_perc)), 2)}%" if len(green_perc) else "0%")
        print()

        PostgresUtil().execute_query(query=insert_query)

