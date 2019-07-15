import Product

class Creator():
    """
    生成を担当するインターフェース
    """
    
    def factoryMethod(self):
        """
        ファクトリメソッド本体
        Productを生成します。
        """
        pass #インターフェースとなります。

class BaseCreator(Creator):
    """
    生成を担当するベースクラス
    """
    
    def __init__(self):
        self.ID = "BaseCreator"
    
    def factoryMethod(self):
        return Product.BaseProduct()
    

