"""EndToEndProtectionVariablePrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class EndToEndProtectionVariablePrototype(ARObject):
    """AUTOSAR EndToEndProtectionVariablePrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("receivers", None, False, True, VariableDataPrototype),  # receivers
        ("sender", None, False, False, VariableDataPrototype),  # sender
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize EndToEndProtectionVariablePrototype."""
        super().__init__()
        self.receivers: list[VariableDataPrototype] = []
        self.sender: Optional[VariableDataPrototype] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EndToEndProtectionVariablePrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtectionVariablePrototype":
        """Create EndToEndProtectionVariablePrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EndToEndProtectionVariablePrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EndToEndProtectionVariablePrototype since parent returns ARObject
        return cast("EndToEndProtectionVariablePrototype", obj)


class EndToEndProtectionVariablePrototypeBuilder:
    """Builder for EndToEndProtectionVariablePrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtectionVariablePrototype = EndToEndProtectionVariablePrototype()

    def build(self) -> EndToEndProtectionVariablePrototype:
        """Build and return EndToEndProtectionVariablePrototype object.

        Returns:
            EndToEndProtectionVariablePrototype instance
        """
        # TODO: Add validation
        return self._obj
