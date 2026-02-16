"""FlexrayNmEcu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class FlexrayNmEcu(BusspecificNmEcu):
    """AUTOSAR FlexrayNmEcu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("nm_hw_vote", None, True, False, None),  # nmHwVote
        ("nm_main", None, True, False, None),  # nmMain
    ]

    def __init__(self) -> None:
        """Initialize FlexrayNmEcu."""
        super().__init__()
        self.nm_hw_vote: Optional[Boolean] = None
        self.nm_main: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayNmEcu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmEcu":
        """Create FlexrayNmEcu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayNmEcu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayNmEcu since parent returns ARObject
        return cast("FlexrayNmEcu", obj)


class FlexrayNmEcuBuilder:
    """Builder for FlexrayNmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmEcu = FlexrayNmEcu()

    def build(self) -> FlexrayNmEcu:
        """Build and return FlexrayNmEcu object.

        Returns:
            FlexrayNmEcu instance
        """
        # TODO: Add validation
        return self._obj
