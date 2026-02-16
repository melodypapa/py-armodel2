"""ImplementationDataTypeSubElementRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.ar_parameter_in_implementation_data_instance_ref import (
    ArParameterInImplementationDataInstanceRef,
)


class ImplementationDataTypeSubElementRef(SubElementRef):
    """AUTOSAR ImplementationDataTypeSubElementRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("implementation", None, False, False, any (ArVariableIn)),  # implementation
        ("parameter", None, False, False, ArParameterInImplementationDataInstanceRef),  # parameter
    ]

    def __init__(self) -> None:
        """Initialize ImplementationDataTypeSubElementRef."""
        super().__init__()
        self.implementation: Optional[Any] = None
        self.parameter: Optional[ArParameterInImplementationDataInstanceRef] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ImplementationDataTypeSubElementRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeSubElementRef":
        """Create ImplementationDataTypeSubElementRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ImplementationDataTypeSubElementRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ImplementationDataTypeSubElementRef since parent returns ARObject
        return cast("ImplementationDataTypeSubElementRef", obj)


class ImplementationDataTypeSubElementRefBuilder:
    """Builder for ImplementationDataTypeSubElementRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataTypeSubElementRef = ImplementationDataTypeSubElementRef()

    def build(self) -> ImplementationDataTypeSubElementRef:
        """Build and return ImplementationDataTypeSubElementRef object.

        Returns:
            ImplementationDataTypeSubElementRef instance
        """
        # TODO: Add validation
        return self._obj
