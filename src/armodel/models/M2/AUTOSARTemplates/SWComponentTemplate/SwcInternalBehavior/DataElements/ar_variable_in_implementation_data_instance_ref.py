"""ArVariableInImplementationDataInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class ArVariableInImplementationDataInstanceRef(ARObject):
    """AUTOSAR ArVariableInImplementationDataInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_datas", None, False, True, any (AbstractImplementation)),  # contextDatas
        ("port_prototype", None, False, False, PortPrototype),  # portPrototype
        ("root_variable", None, False, False, VariableDataPrototype),  # rootVariable
        ("target_data", None, False, False, any (AbstractImplementation)),  # targetData
    ]

    def __init__(self) -> None:
        """Initialize ArVariableInImplementationDataInstanceRef."""
        super().__init__()
        self.context_datas: list[Any] = []
        self.port_prototype: Optional[PortPrototype] = None
        self.root_variable: Optional[VariableDataPrototype] = None
        self.target_data: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ArVariableInImplementationDataInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArVariableInImplementationDataInstanceRef":
        """Create ArVariableInImplementationDataInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ArVariableInImplementationDataInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ArVariableInImplementationDataInstanceRef since parent returns ARObject
        return cast("ArVariableInImplementationDataInstanceRef", obj)


class ArVariableInImplementationDataInstanceRefBuilder:
    """Builder for ArVariableInImplementationDataInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArVariableInImplementationDataInstanceRef = ArVariableInImplementationDataInstanceRef()

    def build(self) -> ArVariableInImplementationDataInstanceRef:
        """Build and return ArVariableInImplementationDataInstanceRef object.

        Returns:
            ArVariableInImplementationDataInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
