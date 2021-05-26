from rest_framework_xml.parsers import XMLParser


class XMLParserAttributes(XMLParser):
    list_tags = [
        'BillTrxInf',
        'PymtTrxInf',
        'gepgSpReconcReq',
        'gepgSpReconcReqAck',
        'gepgSpReconcResp',
        'gepgSpReconcRespAck',
    ]

    def _check_xml_list(self, element):
        return len(element) > 1 >= len(set([child.tag for child in element]))

    def _xml_convert(self, element):
        children = list(element)
        if len(children) == 0:
            return self._type_convert(element.text)
        else:
            if self._check_xml_list(element) or children[0].tag in self.list_tags:
                data = []
                for child in children:
                    data.append(self._xml_convert(child))
            else:
                data = {}
                for child in children:
                    data[child.tag] = self._xml_convert(child)
        return data
