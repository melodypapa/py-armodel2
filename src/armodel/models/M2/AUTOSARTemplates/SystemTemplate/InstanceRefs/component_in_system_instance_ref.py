"""ComponentInSystemInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class ComponentInSystemInstanceRef(ARObject):
    """AUTOSAR ComponentInSystemInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, System),  # base
        ("context", None, False, False, RootSwCompositionPrototype),  # context
        ("target", None, False, False, any (SwComponent)),  # target
    ]

    def __init__(self) -> None:
        """Initialize ComponentInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.target: Any = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ComponentInSystemInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComponentInSystemInstanceRef":
        """Create ComponentInSystemInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ComponentInSystemInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ComponentInSystemInstanceRef since parent returns ARObject
        return cast("ComponentInSystemInstanceRef", obj)


class ComponentInSystemInstanceRefBuilder:
    """Builder for ComponentInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentInSystemInstanceRef = ComponentInSystemInstanceRef()

    def build(self) -> ComponentInSystemInstanceRef:
        """Build and return ComponentInSystemInstanceRef object.

        Returns:
            ComponentInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
