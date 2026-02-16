"""SwcServiceDependencyInSystemInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)


class SwcServiceDependencyInSystemInstanceRef(ARObject):
    """AUTOSAR SwcServiceDependencyInSystemInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_root_sw", None, False, False, RootSwCompositionPrototype),  # contextRootSw
        ("context_sw_prototypes", None, False, True, any (SwComponent)),  # contextSwPrototypes
        ("target_swc", None, False, False, any (SwcService)),  # targetSwc
    ]

    def __init__(self) -> None:
        """Initialize SwcServiceDependencyInSystemInstanceRef."""
        super().__init__()
        self.context_root_sw: Optional[RootSwCompositionPrototype] = None
        self.context_sw_prototypes: list[Any] = []
        self.target_swc: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcServiceDependencyInSystemInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcServiceDependencyInSystemInstanceRef":
        """Create SwcServiceDependencyInSystemInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcServiceDependencyInSystemInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcServiceDependencyInSystemInstanceRef since parent returns ARObject
        return cast("SwcServiceDependencyInSystemInstanceRef", obj)


class SwcServiceDependencyInSystemInstanceRefBuilder:
    """Builder for SwcServiceDependencyInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcServiceDependencyInSystemInstanceRef = SwcServiceDependencyInSystemInstanceRef()

    def build(self) -> SwcServiceDependencyInSystemInstanceRef:
        """Build and return SwcServiceDependencyInSystemInstanceRef object.

        Returns:
            SwcServiceDependencyInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
