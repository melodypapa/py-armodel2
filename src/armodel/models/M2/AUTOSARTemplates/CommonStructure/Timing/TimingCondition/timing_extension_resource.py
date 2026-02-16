"""TimingExtensionResource AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TimingExtensionResource(Identifiable):
    """AUTOSAR TimingExtensionResource."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("timing_arguments", None, False, True, AutosarOperationArgumentInstance),  # timingArguments
        ("timing_modes", None, False, True, TimingModeInstance),  # timingModes
        ("timing_variables", None, False, True, any (AutosarVariable)),  # timingVariables
    ]

    def __init__(self) -> None:
        """Initialize TimingExtensionResource."""
        super().__init__()
        self.timing_arguments: list[AutosarOperationArgumentInstance] = []
        self.timing_modes: list[TimingModeInstance] = []
        self.timing_variables: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingExtensionResource to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingExtensionResource":
        """Create TimingExtensionResource from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingExtensionResource instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingExtensionResource since parent returns ARObject
        return cast("TimingExtensionResource", obj)


class TimingExtensionResourceBuilder:
    """Builder for TimingExtensionResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingExtensionResource = TimingExtensionResource()

    def build(self) -> TimingExtensionResource:
        """Build and return TimingExtensionResource object.

        Returns:
            TimingExtensionResource instance
        """
        # TODO: Add validation
        return self._obj
