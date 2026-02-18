"""ViewTokens AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 340)

JSON Source: packages/M2_MSR_Documentation_BlockElements_PaginationAndView.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This primitive specifies the tokens to specify a documentation view. Tags: xml.xsd.customType=VIEW-TOKENS xml.xsd.pattern=(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)* xml.xsd.type=string Table 9.78: ViewTokens 9.5 Including generated documentation parts [TPS_GST_00336] Including generated Documentation Parts (cid:100)AUTOSAR supports an approach where parts of the documentation are automatically generated and in- cluded at a particular location within the documentation. This support is provided by the so called MSR query mechanism ( MsrQueryP1, MsrQueryP2, MsrQueryTopic1 and MsrQueryChapter). These classes allow to represent the properties of the inclusion as well as the result of the inclusion. Thereby the intermediate results can be visualized and exchanged after the generated parts 340 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11 were included. Hence it is not necessary that all parties involved in the project are able to perform the inclusion process. Details are subject to mutual agreement.(cid:99)() «atpMixed» «atpMixed» ChapterModel +chapterContent ChapterContent +topicContent TopicContentOrMsrQuery 0..1 0..1 +topicContent 1 +msrQueryP1 1 «atpMixed» Paginateable TopicContent +msrQueryResultP1 MsrQueryP1 0..1 «atpMixed» +topic1 TopicOrMsrQuery 0..1 «atpVariation,atpSplitable» +topic1 1 +msrQueryTopic1 1 Identifiable MsrQueryResultTopic1 Paginateable Paginateable +topic1 +msrQueryResultTopic1 MsrQueryTopic1 Topic1 0..* 0..1 + helpEntry: String [0..1] {ordered} «atpMixed» +chapter ChapterOrMsrQuery 0..1 «atpVariation,atpSplitable» +chapter 1 +msrQueryChapter 1 Identifiable Paginateable MsrQueryResultChapter +chapterModel Paginateable +chapter +msrQueryResultChapter MsrQueryChapter Chapter 1 0..* 0..1 + helpEntry: String [0..1] {ordered} Figure 9.12: Including generated documentation parts by MsrQuery The following meta-classes represent the alternative of manually edited documentation and included generated parts. 341 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11
class ViewTokens(ARPrimitive):
    """AUTOSAR ViewTokens primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize ViewTokens.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
