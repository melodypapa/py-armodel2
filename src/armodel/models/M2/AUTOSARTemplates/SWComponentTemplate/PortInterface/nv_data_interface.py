"""NvDataInterface AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvDataInterface(DataInterface):
    """AUTOSAR NvDataInterface."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("nv_datas", None, False, True, VariableDataPrototype),  # nvDatas
    ]

    def __init__(self) -> None:
        """Initialize NvDataInterface."""
        super().__init__()
        self.nv_datas: list[VariableDataPrototype] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NvDataInterface to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvDataInterface":
        """Create NvDataInterface from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NvDataInterface instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NvDataInterface since parent returns ARObject
        return cast("NvDataInterface", obj)


class NvDataInterfaceBuilder:
    """Builder for NvDataInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvDataInterface = NvDataInterface()

    def build(self) -> NvDataInterface:
        """Build and return NvDataInterface object.

        Returns:
            NvDataInterface instance
        """
        # TODO: Add validation
        return self._obj
