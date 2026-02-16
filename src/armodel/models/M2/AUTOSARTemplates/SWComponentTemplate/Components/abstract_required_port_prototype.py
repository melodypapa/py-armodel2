"""AbstractRequiredPortPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)


class AbstractRequiredPortPrototype(PortPrototype):
    """AUTOSAR AbstractRequiredPortPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("required_coms", None, False, True, RPortComSpec),  # requiredComs
    ]

    def __init__(self) -> None:
        """Initialize AbstractRequiredPortPrototype."""
        super().__init__()
        self.required_coms: list[RPortComSpec] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractRequiredPortPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractRequiredPortPrototype":
        """Create AbstractRequiredPortPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractRequiredPortPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractRequiredPortPrototype since parent returns ARObject
        return cast("AbstractRequiredPortPrototype", obj)


class AbstractRequiredPortPrototypeBuilder:
    """Builder for AbstractRequiredPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractRequiredPortPrototype = AbstractRequiredPortPrototype()

    def build(self) -> AbstractRequiredPortPrototype:
        """Build and return AbstractRequiredPortPrototype object.

        Returns:
            AbstractRequiredPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
