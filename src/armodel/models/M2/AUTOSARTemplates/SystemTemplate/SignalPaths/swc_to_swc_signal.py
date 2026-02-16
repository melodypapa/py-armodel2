"""SwcToSwcSignal AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SwcToSwcSignal(ARObject):
    """AUTOSAR SwcToSwcSignal."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_elements", None, False, True, VariableDataPrototype),  # dataElements
    ]

    def __init__(self) -> None:
        """Initialize SwcToSwcSignal."""
        super().__init__()
        self.data_elements: list[VariableDataPrototype] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcToSwcSignal to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToSwcSignal":
        """Create SwcToSwcSignal from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcToSwcSignal instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcToSwcSignal since parent returns ARObject
        return cast("SwcToSwcSignal", obj)


class SwcToSwcSignalBuilder:
    """Builder for SwcToSwcSignal."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToSwcSignal = SwcToSwcSignal()

    def build(self) -> SwcToSwcSignal:
        """Build and return SwcToSwcSignal object.

        Returns:
            SwcToSwcSignal instance
        """
        # TODO: Add validation
        return self._obj
