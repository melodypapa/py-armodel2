"""InnerDataPrototypeGroupInCompositionInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
    DataPrototypeGroup,
)


class InnerDataPrototypeGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerDataPrototypeGroupInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, CompositionSwComponentType),  # base
        ("context_sws", None, False, True, any (SwComponent)),  # contextSws
        ("target_data", None, False, False, DataPrototypeGroup),  # targetData
    ]

    def __init__(self) -> None:
        """Initialize InnerDataPrototypeGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_sws: list[Any] = []
        self.target_data: Optional[DataPrototypeGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InnerDataPrototypeGroupInCompositionInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """Create InnerDataPrototypeGroupInCompositionInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InnerDataPrototypeGroupInCompositionInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InnerDataPrototypeGroupInCompositionInstanceRef since parent returns ARObject
        return cast("InnerDataPrototypeGroupInCompositionInstanceRef", obj)


class InnerDataPrototypeGroupInCompositionInstanceRefBuilder:
    """Builder for InnerDataPrototypeGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerDataPrototypeGroupInCompositionInstanceRef = InnerDataPrototypeGroupInCompositionInstanceRef()

    def build(self) -> InnerDataPrototypeGroupInCompositionInstanceRef:
        """Build and return InnerDataPrototypeGroupInCompositionInstanceRef object.

        Returns:
            InnerDataPrototypeGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
