"""LifeCyclePeriod AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    RevisionLabelString,
)


class LifeCyclePeriod(ARObject):
    """AUTOSAR LifeCyclePeriod."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ar_release", None, True, False, None),  # arRelease
        ("date", None, True, False, None),  # date
        ("product_release", None, True, False, None),  # productRelease
    ]

    def __init__(self) -> None:
        """Initialize LifeCyclePeriod."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.date: Optional[DateTime] = None
        self.product_release: Optional[RevisionLabelString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LifeCyclePeriod to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCyclePeriod":
        """Create LifeCyclePeriod from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LifeCyclePeriod instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LifeCyclePeriod since parent returns ARObject
        return cast("LifeCyclePeriod", obj)


class LifeCyclePeriodBuilder:
    """Builder for LifeCyclePeriod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCyclePeriod = LifeCyclePeriod()

    def build(self) -> LifeCyclePeriod:
        """Build and return LifeCyclePeriod object.

        Returns:
            LifeCyclePeriod instance
        """
        # TODO: Add validation
        return self._obj
