"""ParameterDataPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class ParameterDataPrototype(AutosarDataPrototype):
    """AUTOSAR ParameterDataPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("init_value", None, False, False, ValueSpecification),  # initValue
    ]

    def __init__(self) -> None:
        """Initialize ParameterDataPrototype."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ParameterDataPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterDataPrototype":
        """Create ParameterDataPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ParameterDataPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ParameterDataPrototype since parent returns ARObject
        return cast("ParameterDataPrototype", obj)


class ParameterDataPrototypeBuilder:
    """Builder for ParameterDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterDataPrototype = ParameterDataPrototype()

    def build(self) -> ParameterDataPrototype:
        """Build and return ParameterDataPrototype object.

        Returns:
            ParameterDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
