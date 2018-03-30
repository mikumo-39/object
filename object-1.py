#classの定義
class HumanName:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

#インスタンス形成
taro = HumanName()
taro.setName("Taro")
print(taro.getName())

jiro = HumanName()
jiro.setName("Jiro")
print(jiro.getName())
print(jiro.name)
