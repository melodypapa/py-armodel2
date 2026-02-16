"""RunnableEntityInCompositionInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)


class RunnableEntityInCompositionInstanceRef(ARObject):
    """AUTOSAR RunnableEntityInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, CompositionSwComponentType),  # base
        ("context_sws", None, False, True, any (SwComponent)),  # contextSws
        ("target_runnable", None, False, False, RunnableEntity),  # targetRunnable
    ]

    def __init__(self) -> None:
        """Initialize RunnableEntityInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_sws: list[Any] = []
        self.target_runnable: Optional[RunnableEntity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RunnableEntityInCompositionInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntityInCompositionInstanceRef":
        """Create RunnableEntityInCompositionInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RunnableEntityInCompositionInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RunnableEntityInCompositionInstanceRef since parent returns ARObject
        return cast("RunnableEntityInCompositionInstanceRef", obj)


class RunnableEntityInCompositionInstanceRefBuilder:
    """Builder for RunnableEntityInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntityInCompositionInstanceRef = RunnableEntityInCompositionInstanceRef()

    def build(self) -> RunnableEntityInCompositionInstanceRef:
        """Build and return RunnableEntityInCompositionInstanceRef object.

        Returns:
            RunnableEntityInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
