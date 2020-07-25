
class Entity1:
    # "種別", "配信者","受信日時","日付","内容","場所","メール本文"
    def __init__(self, kind, distributor, received, occured, category, place, contents):
        self._kind = kind
        self._distributor = distributor
        self._received = received
        self._occured = occured
        self._category = category
        self._place = place
        self._contents = contents

        self._kind_org = kind
        self._distributor_org = distributor
        self._received_org = received
        self._occured_org = occured
        self._category_org = category
        self._place_org = place
        self._contents_org = contents

    def row_context(self):
        return (self.Kind, self.Distributor, self.Received, self.Occured, self.Category, self.Place, self.Contents)

    def row_context_debug(self):
        return (self.Occured, self.Category_org, self.Category, self.Place_org, self.Place)

    @property
    def Kind(self):
        return self._kind

    @Kind.setter
    def Kind(self, value):
        self._kind = value

    def is_kind_changed(self):
        return False if self._kind == self._kind_org else True

    @property
    def Kind_org(self):
        return self._kind

    @property
    def Distributor(self):
        return self._distributor

    @Distributor.setter
    def Distributor(self, value):
        self._distributor = value

    def is_distributor_changed(self):
        return False if self._distributor == self._distributor_org else True

    @property
    def Distributor_org(self):
        return self._distributor_org

    @property
    def Received(self):
        return self._received

    @Received.setter
    def Received(self, value):
        self._received = value

    def is_received_changed(self):
        return False if self._received == self._received_org else True

    @property
    def Received_org(self):
        return self._received_org

    @property
    def Occured(self):
        return self._occured

    @Occured.setter
    def Occured(self, value):
        self._occured = value

    def is_occured_changed(self):
        return False if self._occured == self._occured_org else True

    @property
    def Occured_org(self):
        return self._received_org

    @property
    def Category(self):
        return self._category

    @Category.setter
    def Category(self, value):
        self._category = value

    def is_category_changed(self):
        return False if self._category == self._category_org else True

    @property
    def Category_org(self):
        return self._category_org

    @property
    def Place(self):
        return self._place

    @Place.setter
    def Place(self, value):
        self._place = value

    def is_place_changed(self):
        return False if self._place == self._place_org else True

    @property
    def Place_org(self):
        return self._place_org

    @property
    def Contents(self):
        return self._contents

    @Contents.setter
    def Contents(self, value):
        self._contents = value

    def is_contents_changed(self):
        return False if self._contents == self._contents_org else True

    @property
    def Contents_org(self):
        return self._contents_org


class Table1:
    def __init__(self):
        self._container = list()

    def append(self, value):
        self._container.append(value)

    def yield_data(self):
        for row in self._container:
            yield row

    def count(self):
        return len(self._container)


class Entity2:
    def __init__(self, code, ward, description):
        self._code = code
        self._ward = ward
        self._description = description

    @property
    def Code(self):
        return self._code

    @Code.setter
    def Code(self, value):
        self._code = value

    @property
    def Ward(self):
        return self._ward

    @Ward.setter
    def Ward(self, value):
        self._ward = value

    @property
    def Description(self):
        return self._description

    @Description.setter
    def Description(self, value):
        self._description = value

    def get_combine_address(self):
        return self._ward + self._description

    def get_combine_address2(self):
        # 福岡市、北九州市は配下に区があるので
        # 区名以下を返す。
        position = self._ward.find('市')
        if position > 0:
            return self._ward[position:]
        else:
            return self.get_combine_address()


class Table2:
    def __init__(self):
        self._container = list()

    def find(self, keyword):
        for row in self._container:
            place1 = row.get_combine_address2()
            if place1 == keyword:
                return row
            else:
                place2 = row.get_combine_address()
                if place2 == keyword:
                    return row
                else:
                    return None

    def append(self, value):
        self._container.append(value)

    def yield_data(self):
        for row in self._container:
            yield row
