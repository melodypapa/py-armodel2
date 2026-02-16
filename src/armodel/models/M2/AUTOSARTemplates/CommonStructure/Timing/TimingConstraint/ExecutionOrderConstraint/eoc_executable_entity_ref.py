"""EOCExecutableEntityRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)


class EOCExecutableEntityRef(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCExecutableEntityRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_module", None, False, False, BswImplementation),  # bswModule
        ("component", None, False, False, any (SwComponent)),  # component
        ("executable_entity", None, False, False, ExecutableEntity),  # executableEntity
        ("successors", None, False, True, any (EOCExecutableEntity)),  # successors
    ]

    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRef."""
        super().__init__()
        self.bsw_module: Optional[BswImplementation] = None
        self.component: Optional[Any] = None
        self.executable_entity: Optional[ExecutableEntity] = None
        self.successors: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EOCExecutableEntityRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRef":
        """Create EOCExecutableEntityRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EOCExecutableEntityRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EOCExecutableEntityRef since parent returns ARObject
        return cast("EOCExecutableEntityRef", obj)


class EOCExecutableEntityRefBuilder:
    """Builder for EOCExecutableEntityRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRef = EOCExecutableEntityRef()

    def build(self) -> EOCExecutableEntityRef:
        """Build and return EOCExecutableEntityRef object.

        Returns:
            EOCExecutableEntityRef instance
        """
        # TODO: Add validation
        return self._obj
