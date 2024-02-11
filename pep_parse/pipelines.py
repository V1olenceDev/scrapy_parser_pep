import csv
import datetime as dt
from pathlib import Path

from constants import RESULTS_DIR

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    """
    Пайплайн для обработки извлеченных элементов PEP.
    """
    def open_spider(self, spider):
        self.status_sum = {}

    def process_item(self, item, spider):
        status = item['status']
        self.status_sum[status] = self.status_sum.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = BASE_DIR / RESULTS_DIR / f'status_summary_{now}.csv'
        heading = ('Status', 'Quantity')
        total = 'Всего'
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows([
                heading,
                *(self.status_sum.items()),
                [total, sum(self.status_sum.values())]
            ])
