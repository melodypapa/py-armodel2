"""GlobalTimeGateway AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)


class GlobalTimeGateway(Identifiable):
    """AUTOSAR GlobalTimeGateway."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("host", None, False, False, EcuInstance),  # host
        ("master", None, False, False, GlobalTimeMaster),  # master
        ("slave", None, False, False, GlobalTimeSlave),  # slave
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeGateway."""
        super().__init__()
        self.host: Optional[EcuInstance] = None
        self.master: Optional[GlobalTimeMaster] = None
        self.slave: Optional[GlobalTimeSlave] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeGateway to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeGateway":
        """Create GlobalTimeGateway from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeGateway instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeGateway since parent returns ARObject
        return cast("GlobalTimeGateway", obj)


class GlobalTimeGatewayBuilder:
    """Builder for GlobalTimeGateway."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeGateway = GlobalTimeGateway()

    def build(self) -> GlobalTimeGateway:
        """Build and return GlobalTimeGateway object.

        Returns:
            GlobalTimeGateway instance
        """
        # TODO: Add validation
        return self._obj
