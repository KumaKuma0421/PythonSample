import Creator
import Product

class FactoryMethod():
    """
    FactoryMethod
    ProductをCreatorで作ります。
    """

    def factoryMethod(self):
        return Creator.BaseCreator.factoryMethod(self)

"""
ここで簡単なテスト
"""
__factory = FactoryMethod()
myProduct = __factory.factoryMethod()
myProduct.action()