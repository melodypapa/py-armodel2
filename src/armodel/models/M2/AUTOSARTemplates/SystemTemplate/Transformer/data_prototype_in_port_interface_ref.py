"""DataPrototypeInPortInterfaceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR DataPrototypeInPortInterfaceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_prototype_in", None, False, False, DataPrototype),  # dataPrototypeIn
    ]

    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceRef."""
        super().__init__()
        self.data_prototype_in: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototypeInPortInterfaceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInPortInterfaceRef":
        """Create DataPrototypeInPortInterfaceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototypeInPortInterfaceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototypeInPortInterfaceRef since parent returns ARObject
        return cast("DataPrototypeInPortInterfaceRef", obj)


class DataPrototypeInPortInterfaceRefBuilder:
    """Builder for DataPrototypeInPortInterfaceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInPortInterfaceRef = DataPrototypeInPortInterfaceRef()

    def build(self) -> DataPrototypeInPortInterfaceRef:
        """Build and return DataPrototypeInPortInterfaceRef object.

        Returns:
            DataPrototypeInPortInterfaceRef instance
        """
        # TODO: Add validation
        return self._obj
