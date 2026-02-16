"""BuildActionEntity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_invocator import (
    BuildActionInvocator,
)


class BuildActionEntity(Identifiable):
    """AUTOSAR BuildActionEntity."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("delivery_artifacts", None, False, True, AutosarEngineeringObject),  # deliveryArtifacts
        ("invocation", None, False, False, BuildActionInvocator),  # invocation
    ]

    def __init__(self) -> None:
        """Initialize BuildActionEntity."""
        super().__init__()
        self.delivery_artifacts: list[AutosarEngineeringObject] = []
        self.invocation: Optional[BuildActionInvocator] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BuildActionEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionEntity":
        """Create BuildActionEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BuildActionEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BuildActionEntity since parent returns ARObject
        return cast("BuildActionEntity", obj)


class BuildActionEntityBuilder:
    """Builder for BuildActionEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionEntity = BuildActionEntity()

    def build(self) -> BuildActionEntity:
        """Build and return BuildActionEntity object.

        Returns:
            BuildActionEntity instance
        """
        # TODO: Add validation
        return self._obj
