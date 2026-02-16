"""ArParameterInImplementationDataInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class ArParameterInImplementationDataInstanceRef(ARObject):
    """AUTOSAR ArParameterInImplementationDataInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_datas", None, False, True, any (AbstractImplementation)),  # contextDatas
        ("port_prototype", None, False, False, PortPrototype),  # portPrototype
        ("root_parameter", None, False, False, ParameterDataPrototype),  # rootParameter
        ("target_data", None, False, False, any (AbstractImplementation)),  # targetData
    ]

    def __init__(self) -> None:
        """Initialize ArParameterInImplementationDataInstanceRef."""
        super().__init__()
        self.context_datas: list[Any] = []
        self.port_prototype: Optional[PortPrototype] = None
        self.root_parameter: Optional[ParameterDataPrototype] = None
        self.target_data: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ArParameterInImplementationDataInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArParameterInImplementationDataInstanceRef":
        """Create ArParameterInImplementationDataInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ArParameterInImplementationDataInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ArParameterInImplementationDataInstanceRef since parent returns ARObject
        return cast("ArParameterInImplementationDataInstanceRef", obj)


class ArParameterInImplementationDataInstanceRefBuilder:
    """Builder for ArParameterInImplementationDataInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArParameterInImplementationDataInstanceRef = ArParameterInImplementationDataInstanceRef()

    def build(self) -> ArParameterInImplementationDataInstanceRef:
        """Build and return ArParameterInImplementationDataInstanceRef object.

        Returns:
            ArParameterInImplementationDataInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
