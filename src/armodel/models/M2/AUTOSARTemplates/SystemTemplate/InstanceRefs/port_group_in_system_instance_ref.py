"""PortGroupInSystemInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class PortGroupInSystemInstanceRef(ARObject):
    """AUTOSAR PortGroupInSystemInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, System),  # base
        ("context", None, False, False, RootSwCompositionPrototype),  # context
        ("target", None, False, False, PortGroup),  # target
    ]

    def __init__(self) -> None:
        """Initialize PortGroupInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.target: PortGroup = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortGroupInSystemInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortGroupInSystemInstanceRef":
        """Create PortGroupInSystemInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortGroupInSystemInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortGroupInSystemInstanceRef since parent returns ARObject
        return cast("PortGroupInSystemInstanceRef", obj)


class PortGroupInSystemInstanceRefBuilder:
    """Builder for PortGroupInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortGroupInSystemInstanceRef = PortGroupInSystemInstanceRef()

    def build(self) -> PortGroupInSystemInstanceRef:
        """Build and return PortGroupInSystemInstanceRef object.

        Returns:
            PortGroupInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
