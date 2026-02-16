"""NameToken primitive type."""

# This is an identifier as used in xml, e.g. xml-names. Typical usages are, for example, the names of type emitters, protocols, or profiles. For details see NMTOKEN definition on the W3C website (https://www.w3.org/TR/xml/#NT-Nmtoken). Note: Although NameToken supports a wide range of characters, the actually allowed patterns for a certain attribute typed by NameToken may be further restricted by the specification of that attribute. Tags: xml.xsd.customType=NMTOKEN-STRING xml.xsd.type=NMTOKEN Table C.38: NameToken
NameToken = str
