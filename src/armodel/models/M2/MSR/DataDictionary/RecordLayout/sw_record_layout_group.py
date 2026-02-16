"""SwRecordLayoutGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AsamRecordLayoutSemantics,
    Identifier,
    RecordLayoutIteratorPoint,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwRecordLayoutGroup(ARObject):
    """AUTOSAR SwRecordLayoutGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category", None, True, False, None),  # category
        ("desc", None, False, False, MultiLanguageOverviewParagraph),  # desc
        ("short_label", None, True, False, None),  # shortLabel
        ("sw_generic_axis_param", None, False, False, SwGenericAxisParam),  # swGenericAxisParam
        ("sw_record", None, True, False, None),  # swRecord
    ]

    def __init__(self) -> None:
        """Initialize SwRecordLayoutGroup."""
        super().__init__()
        self.category: Optional[AsamRecordLayoutSemantics] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.short_label: Optional[Identifier] = None
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None
        self.sw_record: Optional[RecordLayoutIteratorPoint] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwRecordLayoutGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutGroup":
        """Create SwRecordLayoutGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwRecordLayoutGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwRecordLayoutGroup since parent returns ARObject
        return cast("SwRecordLayoutGroup", obj)


class SwRecordLayoutGroupBuilder:
    """Builder for SwRecordLayoutGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayoutGroup = SwRecordLayoutGroup()

    def build(self) -> SwRecordLayoutGroup:
        """Build and return SwRecordLayoutGroup object.

        Returns:
            SwRecordLayoutGroup instance
        """
        # TODO: Add validation
        return self._obj
