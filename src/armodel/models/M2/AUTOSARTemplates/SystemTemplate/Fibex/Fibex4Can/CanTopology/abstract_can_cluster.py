"""AbstractCanCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.can_cluster_bus_off_recovery import (
    CanClusterBusOffRecovery,
)


class AbstractCanCluster(ARObject):
    """AUTOSAR AbstractCanCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bus_off_recovery", None, False, False, CanClusterBusOffRecovery),  # busOffRecovery
        ("can_fd_baudrate", None, True, False, None),  # canFdBaudrate
        ("can_xl_baudrate", None, True, False, None),  # canXlBaudrate
    ]

    def __init__(self) -> None:
        """Initialize AbstractCanCluster."""
        super().__init__()
        self.bus_off_recovery: Optional[CanClusterBusOffRecovery] = None
        self.can_fd_baudrate: Optional[PositiveUnlimitedInteger] = None
        self.can_xl_baudrate: Optional[PositiveUnlimitedInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractCanCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCluster":
        """Create AbstractCanCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractCanCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractCanCluster since parent returns ARObject
        return cast("AbstractCanCluster", obj)


class AbstractCanClusterBuilder:
    """Builder for AbstractCanCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCluster = AbstractCanCluster()

    def build(self) -> AbstractCanCluster:
        """Build and return AbstractCanCluster object.

        Returns:
            AbstractCanCluster instance
        """
        # TODO: Add validation
        return self._obj
