"""DiagEventDebounceAlgorithm AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class DiagEventDebounceAlgorithm(Identifiable):
    """AUTOSAR DiagEventDebounceAlgorithm."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagEventDebounceAlgorithm."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagEventDebounceAlgorithm to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagEventDebounceAlgorithm":
        """Create DiagEventDebounceAlgorithm from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagEventDebounceAlgorithm instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagEventDebounceAlgorithm since parent returns ARObject
        return cast("DiagEventDebounceAlgorithm", obj)


class DiagEventDebounceAlgorithmBuilder:
    """Builder for DiagEventDebounceAlgorithm."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagEventDebounceAlgorithm = DiagEventDebounceAlgorithm()

    def build(self) -> DiagEventDebounceAlgorithm:
        """Build and return DiagEventDebounceAlgorithm object.

        Returns:
            DiagEventDebounceAlgorithm instance
        """
        # TODO: Add validation
        return self._obj
