"""DiagnosticResponseOnEventClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class DiagnosticResponseOnEventClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticResponseOnEventClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_number_of", None, True, False, None),  # maxNumberOf
        ("max_num", None, True, False, None),  # maxNum
        ("max_supported", None, True, False, None),  # maxSupported
        ("response_on", None, True, False, None),  # responseOn
        ("store_event", None, True, False, None),  # storeEvent
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticResponseOnEventClass."""
        super().__init__()
        self.max_number_of: Optional[PositiveInteger] = None
        self.max_num: Optional[PositiveInteger] = None
        self.max_supported: Optional[PositiveInteger] = None
        self.response_on: Optional[TimeValue] = None
        self.store_event: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticResponseOnEventClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticResponseOnEventClass":
        """Create DiagnosticResponseOnEventClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticResponseOnEventClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticResponseOnEventClass since parent returns ARObject
        return cast("DiagnosticResponseOnEventClass", obj)


class DiagnosticResponseOnEventClassBuilder:
    """Builder for DiagnosticResponseOnEventClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticResponseOnEventClass = DiagnosticResponseOnEventClass()

    def build(self) -> DiagnosticResponseOnEventClass:
        """Build and return DiagnosticResponseOnEventClass object.

        Returns:
            DiagnosticResponseOnEventClass instance
        """
        # TODO: Add validation
        return self._obj
