"""BuildAction AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_entity import (
    BuildActionEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action import (
    BuildAction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_environment import (
    BuildActionEnvironment,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_io_element import (
    BuildActionIoElement,
)


class BuildAction(BuildActionEntity):
    """AUTOSAR BuildAction."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("created_datas", None, False, True, BuildActionIoElement),  # createdDatas
        ("follow_up_actions", None, False, True, BuildAction),  # followUpActions
        ("input_datas", None, False, True, BuildActionIoElement),  # inputDatas
        ("modified_datas", None, False, True, BuildActionIoElement),  # modifiedDatas
        ("predecessors", None, False, True, BuildAction),  # predecessors
        ("required", None, False, False, BuildActionEnvironment),  # required
    ]

    def __init__(self) -> None:
        """Initialize BuildAction."""
        super().__init__()
        self.created_datas: list[BuildActionIoElement] = []
        self.follow_up_actions: list[BuildAction] = []
        self.input_datas: list[BuildActionIoElement] = []
        self.modified_datas: list[BuildActionIoElement] = []
        self.predecessors: list[BuildAction] = []
        self.required: BuildActionEnvironment = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BuildAction to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildAction":
        """Create BuildAction from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BuildAction instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BuildAction since parent returns ARObject
        return cast("BuildAction", obj)


class BuildActionBuilder:
    """Builder for BuildAction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildAction = BuildAction()

    def build(self) -> BuildAction:
        """Build and return BuildAction object.

        Returns:
            BuildAction instance
        """
        # TODO: Add validation
        return self._obj
