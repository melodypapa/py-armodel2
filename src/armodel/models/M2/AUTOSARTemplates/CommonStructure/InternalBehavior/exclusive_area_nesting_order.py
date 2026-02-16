"""ExclusiveAreaNestingOrder AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class ExclusiveAreaNestingOrder(Referrable):
    """AUTOSAR ExclusiveAreaNestingOrder."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("exclusive_areas", None, False, True, ExclusiveArea),  # exclusiveAreas
    ]

    def __init__(self) -> None:
        """Initialize ExclusiveAreaNestingOrder."""
        super().__init__()
        self.exclusive_areas: list[ExclusiveArea] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ExclusiveAreaNestingOrder to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExclusiveAreaNestingOrder":
        """Create ExclusiveAreaNestingOrder from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ExclusiveAreaNestingOrder instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ExclusiveAreaNestingOrder since parent returns ARObject
        return cast("ExclusiveAreaNestingOrder", obj)


class ExclusiveAreaNestingOrderBuilder:
    """Builder for ExclusiveAreaNestingOrder."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExclusiveAreaNestingOrder = ExclusiveAreaNestingOrder()

    def build(self) -> ExclusiveAreaNestingOrder:
        """Build and return ExclusiveAreaNestingOrder object.

        Returns:
            ExclusiveAreaNestingOrder instance
        """
        # TODO: Add validation
        return self._obj
