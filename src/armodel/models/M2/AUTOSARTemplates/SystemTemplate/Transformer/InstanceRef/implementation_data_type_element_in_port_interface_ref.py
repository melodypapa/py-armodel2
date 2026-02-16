"""ImplementationDataTypeElementInPortInterfaceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)


class ImplementationDataTypeElementInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR ImplementationDataTypeElementInPortInterfaceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("contexts", None, False, True, any (AbstractImplementation)),  # contexts
        ("root_data", None, False, False, AutosarDataPrototype),  # rootData
        ("target", None, False, False, AbstractImplementationDataType),  # target
    ]

    def __init__(self) -> None:
        """Initialize ImplementationDataTypeElementInPortInterfaceRef."""
        super().__init__()
        self.contexts: list[Any] = []
        self.root_data: Optional[AutosarDataPrototype] = None
        self.target: Optional[AbstractImplementationDataType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ImplementationDataTypeElementInPortInterfaceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """Create ImplementationDataTypeElementInPortInterfaceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ImplementationDataTypeElementInPortInterfaceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ImplementationDataTypeElementInPortInterfaceRef since parent returns ARObject
        return cast("ImplementationDataTypeElementInPortInterfaceRef", obj)


class ImplementationDataTypeElementInPortInterfaceRefBuilder:
    """Builder for ImplementationDataTypeElementInPortInterfaceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataTypeElementInPortInterfaceRef = ImplementationDataTypeElementInPortInterfaceRef()

    def build(self) -> ImplementationDataTypeElementInPortInterfaceRef:
        """Build and return ImplementationDataTypeElementInPortInterfaceRef object.

        Returns:
            ImplementationDataTypeElementInPortInterfaceRef instance
        """
        # TODO: Add validation
        return self._obj
