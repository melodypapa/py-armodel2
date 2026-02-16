"""ExtIdClassEnum primitive type."""

# This is in fact an enumerator. The possible values are all legal XML names of identifiable objects even those of other XML files. If the schemas of all questionable files are generated from a common meta-model, this is something like an IdentifiableSubtypesEnum. Maybe a future version of the Schema generator can generate such an enum. As of now it is specified as string. Tags: xml.xsd.customType=EXT-ID-CLASS-ENUM xml.xsd.type=string Table 9.35: ExtIdClassEnum
ExtIdClassEnum = str
