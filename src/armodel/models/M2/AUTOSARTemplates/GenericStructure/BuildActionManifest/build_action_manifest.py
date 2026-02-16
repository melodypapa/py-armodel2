"""BuildActionManifest AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action import (
    BuildAction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_environment import (
    BuildActionEnvironment,
)


class BuildActionManifest(ARElement):
    """AUTOSAR BuildActionManifest."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("build_actions", None, False, True, BuildActionEnvironment),  # buildActions
        ("dynamic_actions", None, False, True, BuildAction),  # dynamicActions
        ("start_actions", None, False, True, BuildAction),  # startActions
        ("tear_down_actions", None, False, True, BuildAction),  # tearDownActions
    ]

    def __init__(self) -> None:
        """Initialize BuildActionManifest."""
        super().__init__()
        self.build_actions: list[BuildActionEnvironment] = []
        self.dynamic_actions: list[BuildAction] = []
        self.start_actions: list[BuildAction] = []
        self.tear_down_actions: list[BuildAction] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BuildActionManifest to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionManifest":
        """Create BuildActionManifest from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BuildActionManifest instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BuildActionManifest since parent returns ARObject
        return cast("BuildActionManifest", obj)


class BuildActionManifestBuilder:
    """Builder for BuildActionManifest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionManifest = BuildActionManifest()

    def build(self) -> BuildActionManifest:
        """Build and return BuildActionManifest object.

        Returns:
            BuildActionManifest instance
        """
        # TODO: Add validation
        return self._obj
