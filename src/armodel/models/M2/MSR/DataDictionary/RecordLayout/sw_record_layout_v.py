"""SwRecordLayoutV AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwRecordLayoutV(ARObject):
    """AUTOSAR SwRecordLayoutV."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base_type", None, False, False, SwBaseType),  # baseType
        ("desc", None, False, False, MultiLanguageOverviewParagraph),  # desc
        ("short_label", None, True, False, None),  # shortLabel
        ("sw_generic_axis_param", None, False, False, SwGenericAxisParam),  # swGenericAxisParam
        ("sw_record", None, True, False, None),  # swRecord
    ]

    def __init__(self) -> None:
        """Initialize SwRecordLayoutV."""
        super().__init__()
        self.base_type: Optional[SwBaseType] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.short_label: Optional[Identifier] = None
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None
        self.sw_record: Optional[NameToken] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwRecordLayoutV to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutV":
        """Create SwRecordLayoutV from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwRecordLayoutV instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwRecordLayoutV since parent returns ARObject
        return cast("SwRecordLayoutV", obj)


class SwRecordLayoutVBuilder:
    """Builder for SwRecordLayoutV."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayoutV = SwRecordLayoutV()

    def build(self) -> SwRecordLayoutV:
        """Build and return SwRecordLayoutV object.

        Returns:
            SwRecordLayoutV instance
        """
        # TODO: Add validation
        return self._obj
