"""DiagnosticFreezeFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)


class DiagnosticFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFreezeFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("custom_trigger", None, True, False, None),  # customTrigger
        ("record_number", None, True, False, None),  # recordNumber
        ("trigger", None, False, False, DiagnosticRecordTriggerEnum),  # trigger
        ("update", None, True, False, None),  # update
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticFreezeFrame."""
        super().__init__()
        self.custom_trigger: Optional[String] = None
        self.record_number: Optional[PositiveInteger] = None
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None
        self.update: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticFreezeFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFreezeFrame":
        """Create DiagnosticFreezeFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticFreezeFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticFreezeFrame since parent returns ARObject
        return cast("DiagnosticFreezeFrame", obj)


class DiagnosticFreezeFrameBuilder:
    """Builder for DiagnosticFreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFreezeFrame = DiagnosticFreezeFrame()

    def build(self) -> DiagnosticFreezeFrame:
        """Build and return DiagnosticFreezeFrame object.

        Returns:
            DiagnosticFreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
