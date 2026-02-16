"""DelegatedPortAnnotation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)


class DelegatedPortAnnotation(GeneralAnnotation):
    """AUTOSAR DelegatedPortAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("signal_fan", None, False, False, SignalFanEnum),  # signalFan
    ]

    def __init__(self) -> None:
        """Initialize DelegatedPortAnnotation."""
        super().__init__()
        self.signal_fan: Optional[SignalFanEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DelegatedPortAnnotation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DelegatedPortAnnotation":
        """Create DelegatedPortAnnotation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DelegatedPortAnnotation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DelegatedPortAnnotation since parent returns ARObject
        return cast("DelegatedPortAnnotation", obj)


class DelegatedPortAnnotationBuilder:
    """Builder for DelegatedPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DelegatedPortAnnotation = DelegatedPortAnnotation()

    def build(self) -> DelegatedPortAnnotation:
        """Build and return DelegatedPortAnnotation object.

        Returns:
            DelegatedPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
