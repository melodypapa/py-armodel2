"""RPortPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class RPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR RPortPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("may_be", None, True, False, None),  # mayBe
        ("required", None, False, False, PortInterface),  # required
    ]

    def __init__(self) -> None:
        """Initialize RPortPrototype."""
        super().__init__()
        self.may_be: Optional[Boolean] = None
        self.required: Optional[PortInterface] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RPortPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RPortPrototype":
        """Create RPortPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RPortPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RPortPrototype since parent returns ARObject
        return cast("RPortPrototype", obj)


class RPortPrototypeBuilder:
    """Builder for RPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RPortPrototype = RPortPrototype()

    def build(self) -> RPortPrototype:
        """Build and return RPortPrototype object.

        Returns:
            RPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
