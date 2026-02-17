"""DateTime primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 109)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# A datatype representing a timestamp. The smallest granularity is 1 second. This datatype represents a timestamp in the format yyyy-mm-dd followed by an optional time. The lead-in character for the time is "T" and the format is hh:mm:ss. In addition, a time zone designator shall be specified. The time zone designator can either be "Z" (for UTC) or the time offset to UTC, i.e. (+|-)hh:mm. Examples: 2009-07-23 2009-07-23T14:38:00+01:00 2009-07-23T13:38:00Z Tags: xml.xsd.customType=DATE xml.xsd.pattern=([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))? xml.xsd.type=string Table 4.48: DateTime
DateTime = str
