"""DltMessage AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_argument import (
    DltArgument,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.privacy_level import (
    PrivacyLevel,
)


class DltMessage(Identifiable):
    """AUTOSAR DltMessage."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dlt_arguments", None, False, True, DltArgument),  # dltArguments
        ("message_id", None, True, False, None),  # messageId
        ("message_line", None, True, False, None),  # messageLine
        ("message_source", None, True, False, None),  # messageSource
        ("message_type_info", None, True, False, None),  # messageTypeInfo
        ("privacy_level", None, False, False, PrivacyLevel),  # privacyLevel
    ]

    def __init__(self) -> None:
        """Initialize DltMessage."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.message_id: Optional[PositiveInteger] = None
        self.message_line: Optional[PositiveInteger] = None
        self.message_source: Optional[String] = None
        self.message_type_info: Optional[String] = None
        self.privacy_level: Optional[PrivacyLevel] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DltMessage to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltMessage":
        """Create DltMessage from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DltMessage instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DltMessage since parent returns ARObject
        return cast("DltMessage", obj)


class DltMessageBuilder:
    """Builder for DltMessage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltMessage = DltMessage()

    def build(self) -> DltMessage:
        """Build and return DltMessage object.

        Returns:
            DltMessage instance
        """
        # TODO: Add validation
        return self._obj
