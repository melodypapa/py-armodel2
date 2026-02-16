"""ArgumentDataPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)


class ArgumentDataPrototype(AutosarDataPrototype):
    """AUTOSAR ArgumentDataPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("direction", None, False, False, ArgumentDirectionEnum),  # direction
        ("server_argument_impl", None, False, False, ServerArgumentImplPolicyEnum),  # serverArgumentImpl
    ]

    def __init__(self) -> None:
        """Initialize ArgumentDataPrototype."""
        super().__init__()
        self.direction: Optional[ArgumentDirectionEnum] = None
        self.server_argument_impl: Optional[ServerArgumentImplPolicyEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ArgumentDataPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArgumentDataPrototype":
        """Create ArgumentDataPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ArgumentDataPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ArgumentDataPrototype since parent returns ARObject
        return cast("ArgumentDataPrototype", obj)


class ArgumentDataPrototypeBuilder:
    """Builder for ArgumentDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArgumentDataPrototype = ArgumentDataPrototype()

    def build(self) -> ArgumentDataPrototype:
        """Build and return ArgumentDataPrototype object.

        Returns:
            ArgumentDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
