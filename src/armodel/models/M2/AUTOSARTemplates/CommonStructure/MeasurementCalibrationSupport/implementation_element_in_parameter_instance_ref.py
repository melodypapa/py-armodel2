"""ImplementationElementInParameterInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ImplementationElementInParameterInstanceRef(ARObject):
    """AUTOSAR ImplementationElementInParameterInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context", None, False, False, ParameterDataPrototype),  # context
        ("target", None, False, False, any (AbstractImplementation)),  # target
    ]

    def __init__(self) -> None:
        """Initialize ImplementationElementInParameterInstanceRef."""
        super().__init__()
        self.context: Optional[ParameterDataPrototype] = None
        self.target: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ImplementationElementInParameterInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationElementInParameterInstanceRef":
        """Create ImplementationElementInParameterInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ImplementationElementInParameterInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ImplementationElementInParameterInstanceRef since parent returns ARObject
        return cast("ImplementationElementInParameterInstanceRef", obj)


class ImplementationElementInParameterInstanceRefBuilder:
    """Builder for ImplementationElementInParameterInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationElementInParameterInstanceRef = ImplementationElementInParameterInstanceRef()

    def build(self) -> ImplementationElementInParameterInstanceRef:
        """Build and return ImplementationElementInParameterInstanceRef object.

        Returns:
            ImplementationElementInParameterInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
