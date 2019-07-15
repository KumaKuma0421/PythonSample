"""
実装を担当するクラス
"""

class Product():
    """
    実装を担当するインターフェース
    """
    
    def __preAction(self):
        """
        Productの前処理となります。
        """
        pass #インターフェースとなります。
    
    def __doAction(self):
        """
        Productの本処理となります。
        """
        pass #インターフェースとなります。
    
    def __postAction(self):
        """
        Productの後処理となります。
        """
        pass #インターフェースとなります。
    
    def action(self):
        """
        Prodctのメイン処理となります。
        """
        pass #インターフェースとなります。


class BaseProduct(Product):
    """
    実装を担当するクラス
    """
    
    def preAction(self):
        print("BaseProduct.preAction()")
        return True
    
    def doAction(self):
        print("BaseProduct.doAction()")
        return True

    def postAction(self):
        print("BaseProduct.postAction()")
        return True

    def action(self):
        ret = self.preAction()
        if (ret == True):
            ret = self.doAction()
            if (ret == True):
                ret = self.postAction()
