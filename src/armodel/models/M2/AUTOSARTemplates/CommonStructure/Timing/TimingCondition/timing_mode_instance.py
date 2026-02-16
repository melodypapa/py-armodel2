"""TimingModeInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class TimingModeInstance(Identifiable):
    """AUTOSAR TimingModeInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mode_instance", None, False, False, any (ModeInSwcBsw)),  # modeInstance
    ]

    def __init__(self) -> None:
        """Initialize TimingModeInstance."""
        super().__init__()
        self.mode_instance: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingModeInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingModeInstance":
        """Create TimingModeInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingModeInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingModeInstance since parent returns ARObject
        return cast("TimingModeInstance", obj)


class TimingModeInstanceBuilder:
    """Builder for TimingModeInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingModeInstance = TimingModeInstance()

    def build(self) -> TimingModeInstance:
        """Build and return TimingModeInstance object.

        Returns:
            TimingModeInstance instance
        """
        # TODO: Add validation
        return self._obj
