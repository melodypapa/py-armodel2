"""TDEventBswModeDeclaration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
    TDEventBsw,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class TDEventBswModeDeclaration(TDEventBsw):
    """AUTOSAR TDEventBswModeDeclaration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("entry_mode", None, False, False, ModeDeclaration),  # entryMode
        ("exit_mode", None, False, False, ModeDeclaration),  # exitMode
        ("mode", None, False, False, ModeDeclarationGroup),  # mode
        ("td_event_bsw_declaration_type", None, False, False, any (TDEventBswMode)),  # tdEventBswDeclarationType
    ]

    def __init__(self) -> None:
        """Initialize TDEventBswModeDeclaration."""
        super().__init__()
        self.entry_mode: Optional[ModeDeclaration] = None
        self.exit_mode: Optional[ModeDeclaration] = None
        self.mode: Optional[ModeDeclarationGroup] = None
        self.td_event_bsw_declaration_type: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventBswModeDeclaration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswModeDeclaration":
        """Create TDEventBswModeDeclaration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventBswModeDeclaration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventBswModeDeclaration since parent returns ARObject
        return cast("TDEventBswModeDeclaration", obj)


class TDEventBswModeDeclarationBuilder:
    """Builder for TDEventBswModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswModeDeclaration = TDEventBswModeDeclaration()

    def build(self) -> TDEventBswModeDeclaration:
        """Build and return TDEventBswModeDeclaration object.

        Returns:
            TDEventBswModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
