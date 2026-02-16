"""LinMaster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config import (
    LinSlaveConfig,
)


class LinMaster(ARObject):
    """AUTOSAR LinMaster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lin_slaves", None, False, True, LinSlaveConfig),  # linSlaves
        ("time_base", None, True, False, None),  # timeBase
        ("time_base_jitter", None, True, False, None),  # timeBaseJitter
    ]

    def __init__(self) -> None:
        """Initialize LinMaster."""
        super().__init__()
        self.lin_slaves: list[LinSlaveConfig] = []
        self.time_base: Optional[TimeValue] = None
        self.time_base_jitter: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinMaster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinMaster":
        """Create LinMaster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinMaster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinMaster since parent returns ARObject
        return cast("LinMaster", obj)


class LinMasterBuilder:
    """Builder for LinMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinMaster = LinMaster()

    def build(self) -> LinMaster:
        """Build and return LinMaster object.

        Returns:
            LinMaster instance
        """
        # TODO: Add validation
        return self._obj
