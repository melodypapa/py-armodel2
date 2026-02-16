"""McParameterElementGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class McParameterElementGroup(ARObject):
    """AUTOSAR McParameterElementGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ram_location", None, False, False, VariableDataPrototype),  # ramLocation
        ("rom_location", None, False, False, ParameterDataPrototype),  # romLocation
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize McParameterElementGroup."""
        super().__init__()
        self.ram_location: Optional[VariableDataPrototype] = None
        self.rom_location: Optional[ParameterDataPrototype] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert McParameterElementGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McParameterElementGroup":
        """Create McParameterElementGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            McParameterElementGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to McParameterElementGroup since parent returns ARObject
        return cast("McParameterElementGroup", obj)


class McParameterElementGroupBuilder:
    """Builder for McParameterElementGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McParameterElementGroup = McParameterElementGroup()

    def build(self) -> McParameterElementGroup:
        """Build and return McParameterElementGroup object.

        Returns:
            McParameterElementGroup instance
        """
        # TODO: Add validation
        return self._obj
