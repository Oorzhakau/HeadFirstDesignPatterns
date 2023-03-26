"""
Паттерн Шаблонный метод.
Паттерн определеет "скелет" алгоритма в методе, оставляя определенные реализации некоторых шагов
субклассам. Субклассы могут переопределять некоторые части алгоритма без изменения его структуры.
"""
import abc


class CaffeineBeverage(abc.ABC):
    def prepareRecipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.custom_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print("Boiling water!")

    def pour_in_cup(self):
        print("Pouring into cup!")

    @abc.abstractmethod
    def brew(self): ...

    @abc.abstractmethod
    def add_condiments(self): ...

    def custom_wants_condiments(self):
        """Метод Перехватчи дает возможность субклассам "подключаться" к алгоритму, описанному в шаблонном методе,
         в разных точках"""
        return True


class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea!")

    def add_condiments(self):
        print("Adding lemon!")


class TeaWithoutLemon(Tea):
    def custom_wants_condiments(self):
        return False


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping Coffee through filter!")

    def add_condiments(self):
        print("Adding suggar and milk!")


if __name__ == "__main__":
    print("==Preparing Tea!==")
    tea = Tea()
    tea.prepareRecipe()
    print("==Preparing Tea without Lemon!==")
    tea = TeaWithoutLemon()
    tea.prepareRecipe()
    print("==Preparing Coffee!==")
    coffee = Coffee()
    coffee.prepareRecipe()
