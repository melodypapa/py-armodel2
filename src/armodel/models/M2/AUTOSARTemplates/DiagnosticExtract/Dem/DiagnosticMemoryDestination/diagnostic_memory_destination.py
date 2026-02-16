"""DiagnosticMemoryDestination AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticMemoryDestination(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMemoryDestination."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("aging_requires", None, True, False, None),  # agingRequires
        ("clear_dtc", None, False, False, any (DiagnosticClearDtc)),  # clearDtc
        ("dtc_status", None, True, False, None),  # dtcStatus
        ("event", None, False, False, DiagnosticEvent),  # event
        ("max_number_of", None, True, False, None),  # maxNumberOf
        ("memory_entry", None, False, False, DiagnosticMemoryEntryStorageTriggerEnum),  # memoryEntry
        ("status_bit", None, True, False, None),  # statusBit
        ("type_of_freeze", None, False, False, any (DiagnosticTypeOf)),  # typeOfFreeze
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestination."""
        super().__init__()
        self.aging_requires: Optional[Boolean] = None
        self.clear_dtc: Optional[Any] = None
        self.dtc_status: Optional[PositiveInteger] = None
        self.event: Optional[DiagnosticEvent] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.memory_entry: Optional[DiagnosticMemoryEntryStorageTriggerEnum] = None
        self.status_bit: Optional[Boolean] = None
        self.type_of_freeze: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticMemoryDestination to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryDestination":
        """Create DiagnosticMemoryDestination from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticMemoryDestination instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticMemoryDestination since parent returns ARObject
        return cast("DiagnosticMemoryDestination", obj)


class DiagnosticMemoryDestinationBuilder:
    """Builder for DiagnosticMemoryDestination."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestination = DiagnosticMemoryDestination()

    def build(self) -> DiagnosticMemoryDestination:
        """Build and return DiagnosticMemoryDestination object.

        Returns:
            DiagnosticMemoryDestination instance
        """
        # TODO: Add validation
        return self._obj
