## Not done yet

import json
from typing import List
import requests

BASE_URL = "https://play.google.com"

def get_body_for_requests(opts):
    lang = opts['lang']
    country = opts['country']
    num = opts['num']
    collection = opts['collection']
    category = opts['category']

    url = f"{BASE_URL}/_/PlayStoreUi/data/batchexecute?rpcids=vyAe2&source-path=%2Fstore%2Fapps&f.sid=-4178618388443751758&bl=boq_playuiserver_20220612.08_p0&authuser=0&soc-app=121&soc-platform=1&soc-device=1&_reqid=82003&rt=c&hl={lang}&gl={country}"
    

    num = requests.utils.quote(str(num))
    collection = requests.utils.quote(collection)
    category = requests.utils.quote(category)

    body = f"f.req=%5B%5B%5B%22vyAe2%22%2C%22%5B%5Bnull%2C%5B%5B8%2C%5B20%2C{num}%2C%5B%5D%5D%5D%2Cnull%2Cnull%2C%5B96%2C108%2C72%2C100%2C27%2C183%2C222%2C8%2C57%2C169%2C110%2C11%2C184%2C16%2C1%2C139%2C152%2C194%2C165%2C68%2C163%2C211%2C9%2C71%2C31%2C195%2C12%2C64%2C151%2C150%2C148%2C113%2C104%2C55%2C56%2C145%2C32%2C34%2C10%2C122%5D%2C%5Bnull%2Cnull%2C%5B%5B%5B1%2Cnull%2C1%5D%2Cnull%2C%5B%5Bnull%2C%5B%5D%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2C2%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5Bnull%2C%5B%5Bnull%2C%5B%5D%5D%5D%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5Bnull%2C%5B%5Bnull%2C%5B%5D%5D%5D%2Cnull%2C%5B1%5D%5D%2C%5Bnull%2C%5B%5Bnull%2C%5B%5D%5D%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B%5Bnull%2C%5B%5D%5D%5D%5D%2C%5B%5B%5Bnull%2C%5B%5D%5D%5D%5D%5D%2C%5B%5B%5B%5B7%2C68%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C1%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C31%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C104%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C9%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C8%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C27%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C12%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C65%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C110%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C11%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C56%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C55%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C96%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C10%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C122%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C72%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C71%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C64%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C113%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C139%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C150%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C169%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C165%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C151%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C163%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C32%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C16%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C108%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C100%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C194%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C211%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C184%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B7%2C183%5D%2C%5B%5B1%2C73%2C96%2C103%2C97%2C58%2C50%2C92%2C52%2C112%2C69%2C19%2C31%2C101%2C123%2C74%2C49%2C80%2C20%2C10%2C14%2C79%2C43%2C42%2C139%5D%5D%5D%2C%5B%5B9%2C68%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C1%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C31%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C104%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C9%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C8%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C27%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C12%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C65%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C110%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C11%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C56%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C55%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C96%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C10%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C122%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C72%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C71%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C64%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C113%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C139%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C150%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C169%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C165%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C151%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C163%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C32%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C16%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C108%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C100%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C194%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C211%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C184%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B9%2C183%5D%2C%5B%5B1%2C7%2C9%2C24%2C12%2C31%2C5%2C15%2C27%2C8%2C13%2C10%5D%5D%5D%2C%5B%5B17%2C68%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C1%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C31%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C104%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C9%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C8%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C27%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C12%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C65%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C110%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C11%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C56%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C55%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C96%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C10%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C122%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C72%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C71%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C64%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C113%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C139%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C150%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C169%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C165%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C151%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C163%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C32%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C16%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C108%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C100%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C194%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C211%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C184%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B17%2C183%5D%2C%5B%5B1%2C7%2C9%2C25%2C13%2C31%2C5%2C41%2C27%2C8%2C14%2C10%5D%5D%5D%2C%5B%5B65%2C68%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C1%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C31%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C104%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C9%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C8%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C27%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C12%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C65%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C110%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C11%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C56%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C55%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C96%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C10%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C122%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C72%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C71%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C64%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C113%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C139%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C150%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C169%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C165%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C151%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C163%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C32%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C16%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C108%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C100%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C194%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C211%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C184%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B65%2C183%5D%2C%5B%5B1%2C5%2C4%2C7%2C11%2C6%5D%5D%5D%2C%5B%5B10%2C68%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C1%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C31%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C104%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C9%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C8%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C27%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C12%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C65%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C110%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C11%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C56%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C55%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C96%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C10%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C122%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C72%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C71%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C64%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C113%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C139%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C150%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C169%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C165%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C151%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C163%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C32%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C16%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C108%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C100%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C194%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C211%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C184%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B10%2C183%5D%2C%5B%5B1%2C7%2C6%2C9%2C15%2C8%5D%5D%5D%2C%5B%5B58%2C68%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C1%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C31%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C104%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C9%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C8%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C27%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C12%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C65%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C110%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C11%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C56%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C55%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C96%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C10%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C122%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C72%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C71%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C64%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C113%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C139%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C150%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C169%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C165%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C151%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C163%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C32%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C16%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C108%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C100%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C194%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C211%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C184%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B58%2C183%5D%2C%5B%5B5%2C3%2C1%2C2%2C6%2C8%5D%5D%5D%2C%5B%5B44%2C68%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C1%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C31%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C104%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C9%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C8%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C27%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C12%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C65%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C110%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C11%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C56%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C55%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C96%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C10%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C122%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C72%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C71%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C64%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C113%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C139%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C150%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C169%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C165%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C151%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C163%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C32%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C16%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C108%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C100%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C194%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C211%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C184%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B44%2C183%5D%2C%5B%5B3%2C4%2C9%2C6%2C7%2C2%2C8%2C1%2C10%2C11%2C5%5D%5D%5D%2C%5B%5B1%2C68%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C1%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C31%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C104%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C9%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C8%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C27%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C12%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C65%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C110%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C11%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C56%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C55%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C96%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C10%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C122%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C72%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C71%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C64%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C113%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C139%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C150%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C169%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C165%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C151%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C163%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C32%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C16%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C108%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C100%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C194%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C211%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C184%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B1%2C183%5D%2C%5B%5B1%2C5%2C14%2C38%2C19%2C29%2C34%2C4%2C12%2C11%2C6%2C30%2C43%2C40%2C42%2C16%2C10%2C7%5D%5D%5D%2C%5B%5B4%2C68%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C1%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C31%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C104%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C9%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C8%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C27%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C12%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C65%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C110%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C11%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C56%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C55%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C96%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C10%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C122%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C72%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C71%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C64%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C113%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C139%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C150%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C169%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C165%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C151%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C163%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C32%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C16%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C108%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C100%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C194%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C211%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C184%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B4%2C183%5D%2C%5B%5B1%2C3%2C5%2C4%2C7%2C6%2C11%2C19%2C21%2C17%2C15%2C12%2C16%2C20%5D%5D%5D%2C%5B%5B3%2C68%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C1%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C31%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C104%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C9%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C8%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C27%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C12%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C65%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C110%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C11%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C56%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C55%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C96%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C10%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C122%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C72%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C71%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C64%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C113%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C139%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C150%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C169%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C165%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C151%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C163%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C32%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C16%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C108%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C100%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C194%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C211%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C184%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B3%2C183%5D%2C%5B%5B1%2C5%2C14%2C4%2C10%2C17%5D%5D%5D%2C%5B%5B2%2C68%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C1%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C31%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C104%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C9%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C8%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C27%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C12%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C65%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C110%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C11%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C56%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C55%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C96%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C10%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C122%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C72%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C71%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C64%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C113%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C139%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C150%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C169%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C165%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C151%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C163%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C32%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C16%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C108%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C100%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C194%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C211%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C184%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%2C%5B%5B2%2C183%5D%2C%5B%5B1%2C5%2C7%2C4%2C13%2C16%2C12%2C18%5D%5D%5D%5D%5D%5D%2Cnull%2Cnull%2C%5B%5B%5B1%2C2%5D%2C%5B10%2C8%2C9%5D%2C%5B%5D%2C%5B%5D%5D%5D%5D%2C%5B2%2C%5C%22{collection}%5C%22%2C%5C%22{category}%5C%22%5D%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AHEfX0v-0GUJFJSNOPFH4gVRyhHw%3A1699525674172"
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    options = {
        'url': url,
        'data': body,
        'headers': headers,
    }
    options.update(opts.get('requestOptions', {}))

    response = requests.post(**options, allow_redirects=True)
    html = response.text
    return html

def parse_collection_apps(category_object):
    # apps_mappings = {
    #     'title': [0, 3],
    #     'appId': [0, 0, 0],
    #     'url': {
    #         'path': [0, 10, 4, 2],
    #         'fun': lambda path: urlparse.urljoin(BASE_URL, path)
    #     },
    #     'icon': [0, 1, 3, 2],
    #     'developer': [0, 14],
    #     'currency': [0, 8, 1, 0, 1],
    #     'price': {
    #         'path': [0, 8, 1, 0, 0],
    #         'fun': lambda price: price / 1000000
    #     },
    #     'free': {
    #         'path': [0, 8, 1, 0, 0],
    #         'fun': lambda price: price == 0
    #     },
    #     'summary': [0, 13, 1],
    #     'scoreText': [0, 4, 0],
    #     'score': [0, 4, 1]
    # }
    # apps_path = [0, 1, 0, 28, 0]
    appID = [ single_app[0][0][0] for single_app in category_object[0][1][0][28][0] ]
    return appID

def parse_response(html):
    input_data = json.loads(html.split('\n')[3])
    collection_object = json.loads(input_data[0][2])
    return parse_collection_apps(collection_object)


def list(collection: str, category: str, num: int = 45, lang: str = 'en', country: str = 'us') -> List[str]:
    """
    List apps from a collection and category.
    """
    body = get_body_for_requests({'num': num, 'lang': lang, 'country': country, 'collection': collection, 'category': category, 'start': 0})
    return parse_response(body)