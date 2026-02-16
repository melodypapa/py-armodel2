"""BswModuleCallPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)


class BswModuleCallPoint(Referrable):
    """AUTOSAR BswModuleCallPoint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("contexts", None, False, True, BswDistinguishedPartition),  # contexts
    ]

    def __init__(self) -> None:
        """Initialize BswModuleCallPoint."""
        super().__init__()
        self.contexts: list[BswDistinguishedPartition] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModuleCallPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleCallPoint":
        """Create BswModuleCallPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModuleCallPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModuleCallPoint since parent returns ARObject
        return cast("BswModuleCallPoint", obj)


class BswModuleCallPointBuilder:
    """Builder for BswModuleCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleCallPoint = BswModuleCallPoint()

    def build(self) -> BswModuleCallPoint:
        """Build and return BswModuleCallPoint object.

        Returns:
            BswModuleCallPoint instance
        """
        # TODO: Add validation
        return self._obj
