"""BuildAction AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "created_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BuildActionIoElement,
        ),  # createdDatas
        "follow_up_actions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BuildAction,
        ),  # followUpActions
        "input_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BuildActionIoElement,
        ),  # inputDatas
        "modified_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BuildActionIoElement,
        ),  # modifiedDatas
        "predecessors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BuildAction,
        ),  # predecessors
        "required": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=BuildActionEnvironment,
        ),  # required
    }

    def __init__(self) -> None:
        """Initialize BuildAction."""
        super().__init__()
        self.created_datas: list[BuildActionIoElement] = []
        self.follow_up_actions: list[BuildAction] = []
        self.input_datas: list[BuildActionIoElement] = []
        self.modified_datas: list[BuildActionIoElement] = []
        self.predecessors: list[BuildAction] = []
        self.required: BuildActionEnvironment = None


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
