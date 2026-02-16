"""DdsResourceLimits AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsResourceLimits(ARObject):
    """AUTOSAR DdsResourceLimits."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_instances", None, True, False, None),  # maxInstances
        ("max_samples", None, True, False, None),  # maxSamples
        ("max_samples_per_instance", None, True, False, None),  # maxSamplesPerInstance
    ]

    def __init__(self) -> None:
        """Initialize DdsResourceLimits."""
        super().__init__()
        self.max_instances: Optional[PositiveInteger] = None
        self.max_samples: Optional[PositiveInteger] = None
        self.max_samples_per_instance: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsResourceLimits to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsResourceLimits":
        """Create DdsResourceLimits from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsResourceLimits instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsResourceLimits since parent returns ARObject
        return cast("DdsResourceLimits", obj)


class DdsResourceLimitsBuilder:
    """Builder for DdsResourceLimits."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsResourceLimits = DdsResourceLimits()

    def build(self) -> DdsResourceLimits:
        """Build and return DdsResourceLimits object.

        Returns:
            DdsResourceLimits instance
        """
        # TODO: Add validation
        return self._obj
