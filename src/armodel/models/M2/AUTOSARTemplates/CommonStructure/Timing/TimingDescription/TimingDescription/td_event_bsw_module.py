"""TDEventBswModule AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
    TDEventBsw,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw_module import (
    TDEventBswModule,
)


class TDEventBswModule(TDEventBsw):
    """AUTOSAR TDEventBswModule."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_module_entry_entry", None, False, False, BswModuleEntry),  # bswModuleEntryEntry
        ("td_event_bsw", None, False, False, TDEventBswModule),  # tdEventBsw
    ]

    def __init__(self) -> None:
        """Initialize TDEventBswModule."""
        super().__init__()
        self.bsw_module_entry_entry: Optional[BswModuleEntry] = None
        self.td_event_bsw: Optional[TDEventBswModule] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventBswModule to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswModule":
        """Create TDEventBswModule from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventBswModule instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventBswModule since parent returns ARObject
        return cast("TDEventBswModule", obj)


class TDEventBswModuleBuilder:
    """Builder for TDEventBswModule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswModule = TDEventBswModule()

    def build(self) -> TDEventBswModule:
        """Build and return TDEventBswModule object.

        Returns:
            TDEventBswModule instance
        """
        # TODO: Add validation
        return self._obj
