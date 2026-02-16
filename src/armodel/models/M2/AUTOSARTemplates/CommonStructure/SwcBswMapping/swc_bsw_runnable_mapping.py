"""SwcBswRunnableMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)


class SwcBswRunnableMapping(ARObject):
    """AUTOSAR SwcBswRunnableMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_entity", None, False, False, BswModuleEntity),  # bswEntity
        ("swc_runnable", None, False, False, RunnableEntity),  # swcRunnable
    ]

    def __init__(self) -> None:
        """Initialize SwcBswRunnableMapping."""
        super().__init__()
        self.bsw_entity: Optional[BswModuleEntity] = None
        self.swc_runnable: Optional[RunnableEntity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcBswRunnableMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswRunnableMapping":
        """Create SwcBswRunnableMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcBswRunnableMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcBswRunnableMapping since parent returns ARObject
        return cast("SwcBswRunnableMapping", obj)


class SwcBswRunnableMappingBuilder:
    """Builder for SwcBswRunnableMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswRunnableMapping = SwcBswRunnableMapping()

    def build(self) -> SwcBswRunnableMapping:
        """Build and return SwcBswRunnableMapping object.

        Returns:
            SwcBswRunnableMapping instance
        """
        # TODO: Add validation
        return self._obj
