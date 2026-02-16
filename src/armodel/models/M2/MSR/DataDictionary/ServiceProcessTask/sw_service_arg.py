"""SwServiceArg AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class SwServiceArg(Identifiable):
    """AUTOSAR SwServiceArg."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("direction", None, False, False, ArgumentDirectionEnum),  # direction
        ("sw_arraysize", None, False, False, ValueList),  # swArraysize
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
    ]

    def __init__(self) -> None:
        """Initialize SwServiceArg."""
        super().__init__()
        self.direction: Optional[ArgumentDirectionEnum] = None
        self.sw_arraysize: Optional[ValueList] = None
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwServiceArg to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwServiceArg":
        """Create SwServiceArg from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwServiceArg instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwServiceArg since parent returns ARObject
        return cast("SwServiceArg", obj)


class SwServiceArgBuilder:
    """Builder for SwServiceArg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwServiceArg = SwServiceArg()

    def build(self) -> SwServiceArg:
        """Build and return SwServiceArg object.

        Returns:
            SwServiceArg instance
        """
        # TODO: Add validation
        return self._obj
