"""CouplingPortAsynchronousTrafficShaper AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_asynchronous_traffic_shaper_group_entry import (
    SwitchAsynchronousTrafficShaperGroupEntry,
)


class CouplingPortAsynchronousTrafficShaper(Identifiable):
    """AUTOSAR CouplingPortAsynchronousTrafficShaper."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("committed_burst", None, True, False, None),  # committedBurst
        ("committed", None, True, False, None),  # committed
        ("traffic_shaper", None, False, False, SwitchAsynchronousTrafficShaperGroupEntry),  # trafficShaper
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortAsynchronousTrafficShaper."""
        super().__init__()
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.traffic_shaper: Optional[SwitchAsynchronousTrafficShaperGroupEntry] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortAsynchronousTrafficShaper to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortAsynchronousTrafficShaper":
        """Create CouplingPortAsynchronousTrafficShaper from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortAsynchronousTrafficShaper instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortAsynchronousTrafficShaper since parent returns ARObject
        return cast("CouplingPortAsynchronousTrafficShaper", obj)


class CouplingPortAsynchronousTrafficShaperBuilder:
    """Builder for CouplingPortAsynchronousTrafficShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortAsynchronousTrafficShaper = CouplingPortAsynchronousTrafficShaper()

    def build(self) -> CouplingPortAsynchronousTrafficShaper:
        """Build and return CouplingPortAsynchronousTrafficShaper object.

        Returns:
            CouplingPortAsynchronousTrafficShaper instance
        """
        # TODO: Add validation
        return self._obj
