"""SwComponentType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.consistency_needs import (
    ConsistencyNeeds,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation.sw_component_documentation import (
    SwComponentDocumentation,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit_group import (
    UnitGroup,
)


class SwComponentType(ARElement):
    """AUTOSAR SwComponentType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("consistency_needses", None, False, True, ConsistencyNeeds),  # consistencyNeedses
        ("ports", None, False, True, PortPrototype),  # ports
        ("port_groups", None, False, True, PortGroup),  # portGroups
        ("swc_mappings", None, False, True, any (SwComponentMapping)),  # swcMappings
        ("sw_component_documentation", None, False, False, SwComponentDocumentation),  # swComponentDocumentation
        ("unit_groups", None, False, True, UnitGroup),  # unitGroups
    ]

    def __init__(self) -> None:
        """Initialize SwComponentType."""
        super().__init__()
        self.consistency_needses: list[ConsistencyNeeds] = []
        self.ports: list[PortPrototype] = []
        self.port_groups: list[PortGroup] = []
        self.swc_mappings: list[Any] = []
        self.sw_component_documentation: Optional[SwComponentDocumentation] = None
        self.unit_groups: list[UnitGroup] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwComponentType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentType":
        """Create SwComponentType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwComponentType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwComponentType since parent returns ARObject
        return cast("SwComponentType", obj)


class SwComponentTypeBuilder:
    """Builder for SwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentType = SwComponentType()

    def build(self) -> SwComponentType:
        """Build and return SwComponentType object.

        Returns:
            SwComponentType instance
        """
        # TODO: Add validation
        return self._obj
