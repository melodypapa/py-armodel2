"""BuildActionEnvironment AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class BuildActionEnvironment(Identifiable):
    """AUTOSAR BuildActionEnvironment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sdgs", None, False, True, Sdg),  # sdgs
    ]

    def __init__(self) -> None:
        """Initialize BuildActionEnvironment."""
        super().__init__()
        self.sdgs: list[Sdg] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BuildActionEnvironment to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionEnvironment":
        """Create BuildActionEnvironment from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BuildActionEnvironment instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BuildActionEnvironment since parent returns ARObject
        return cast("BuildActionEnvironment", obj)


class BuildActionEnvironmentBuilder:
    """Builder for BuildActionEnvironment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionEnvironment = BuildActionEnvironment()

    def build(self) -> BuildActionEnvironment:
        """Build and return BuildActionEnvironment object.

        Returns:
            BuildActionEnvironment instance
        """
        # TODO: Add validation
        return self._obj
