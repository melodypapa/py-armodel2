"""SwcBswMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_runnable_mapping import (
    SwcBswRunnableMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcBswMapping(ARElement):
    """AUTOSAR SwcBswMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_behavior", None, False, False, BswInternalBehavior),  # bswBehavior
        ("runnable_mappings", None, False, True, SwcBswRunnableMapping),  # runnableMappings
        ("swc_behavior", None, False, False, SwcInternalBehavior),  # swcBehavior
        ("synchronizeds", None, False, True, any (SwcBswSynchronized)),  # synchronizeds
    ]

    def __init__(self) -> None:
        """Initialize SwcBswMapping."""
        super().__init__()
        self.bsw_behavior: Optional[BswInternalBehavior] = None
        self.runnable_mappings: list[SwcBswRunnableMapping] = []
        self.swc_behavior: Optional[SwcInternalBehavior] = None
        self.synchronizeds: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcBswMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswMapping":
        """Create SwcBswMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcBswMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcBswMapping since parent returns ARObject
        return cast("SwcBswMapping", obj)


class SwcBswMappingBuilder:
    """Builder for SwcBswMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswMapping = SwcBswMapping()

    def build(self) -> SwcBswMapping:
        """Build and return SwcBswMapping object.

        Returns:
            SwcBswMapping instance
        """
        # TODO: Add validation
        return self._obj
