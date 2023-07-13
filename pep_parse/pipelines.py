from .settings import BASE_DIR


class PepParsePipeline:
    data = {}

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        total = sum(self.data.values())
        results = BASE_DIR / 'results'
        with open(
            f'{results}/status_summary_%(time)s.csv',
            mode='w', encoding='utf-8'
        ) as f:
            f.write('Статус,Количество\n')
            for key, value in self.data.items():
                f.write(f'{key}, {str(value)}\n')
            f.write(f'Total,{total}\n')

    def process_item(self, item, spider):
        status = item['status']
        if status not in self.data:
            self.data[status] = 1
        else:
            self.data[status] += 1
        return item
