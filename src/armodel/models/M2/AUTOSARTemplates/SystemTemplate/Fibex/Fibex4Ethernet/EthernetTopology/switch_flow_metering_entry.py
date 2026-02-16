"""SwitchFlowMeteringEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class SwitchFlowMeteringEntry(Identifiable):
    """AUTOSAR SwitchFlowMeteringEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("color_mode", None, False, False, FlowMeteringColorModeEnum),  # colorMode
        ("committed_burst", None, True, False, None),  # committedBurst
        ("committed", None, True, False, None),  # committed
        ("coupling_flag", None, True, False, None),  # couplingFlag
        ("excess_burst", None, True, False, None),  # excessBurst
        ("excess", None, True, False, None),  # excess
    ]

    def __init__(self) -> None:
        """Initialize SwitchFlowMeteringEntry."""
        super().__init__()
        self.color_mode: Optional[FlowMeteringColorModeEnum] = None
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.coupling_flag: Optional[Boolean] = None
        self.excess_burst: Optional[PositiveInteger] = None
        self.excess: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwitchFlowMeteringEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchFlowMeteringEntry":
        """Create SwitchFlowMeteringEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwitchFlowMeteringEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwitchFlowMeteringEntry since parent returns ARObject
        return cast("SwitchFlowMeteringEntry", obj)


class SwitchFlowMeteringEntryBuilder:
    """Builder for SwitchFlowMeteringEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchFlowMeteringEntry = SwitchFlowMeteringEntry()

    def build(self) -> SwitchFlowMeteringEntry:
        """Build and return SwitchFlowMeteringEntry object.

        Returns:
            SwitchFlowMeteringEntry instance
        """
        # TODO: Add validation
        return self._obj
