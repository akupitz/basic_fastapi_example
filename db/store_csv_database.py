import pandas as pd
from store.models import Product
from db.generic_database import GenericDatabase


class StoreCSVDatabase(GenericDatabase):
    def __init__(self, db_path):
        self._db_path = db_path
        self._db_dataframe = pd.read_csv(db_path)

    def _update_db(self, updated_db: pd.DataFrame):
        self._db_dataframe = updated_db
        self._db_dataframe.to_csv(self._db_path, index=False)

    @staticmethod
    def _product_details_to_df(product: Product):
        return pd.DataFrame({'name': product.name, 'amount': product.amount, 'price': product.price}, index=[0])

    def get(self, product_name: str):
        df = self._db_dataframe
        df_row_to_get = df[df['name'] == product_name]
        try:
            return df_row_to_get.to_dict('records')[0]
        except Exception:
            return None

    def get_all(self):
        df = self._db_dataframe
        return df.to_dict('records')

    def insert(self, product: Product):
        df = self._db_dataframe
        df_row_to_insert = self._product_details_to_df(product)
        df = df.append(df_row_to_insert, ignore_index=True)
        self._update_db(df)

    def update(self, product: Product):
        # if does not exist in get just raise exception
        self.remove(product.name)
        self.insert(product)

    def remove(self, product_name: str):
        df = self._db_dataframe
        df_without_product = df[df['name'] != product_name]
        self._update_db(df_without_product)
