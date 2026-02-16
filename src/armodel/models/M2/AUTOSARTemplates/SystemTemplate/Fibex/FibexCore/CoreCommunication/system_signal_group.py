"""SystemSignalGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SystemSignalGroup(ARElement):
    """AUTOSAR SystemSignalGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("system_signals", None, False, True, SystemSignal),  # systemSignals
        ("transforming", None, False, False, SystemSignal),  # transforming
    ]

    def __init__(self) -> None:
        """Initialize SystemSignalGroup."""
        super().__init__()
        self.system_signals: list[SystemSignal] = []
        self.transforming: Optional[SystemSignal] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SystemSignalGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignalGroup":
        """Create SystemSignalGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SystemSignalGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SystemSignalGroup since parent returns ARObject
        return cast("SystemSignalGroup", obj)


class SystemSignalGroupBuilder:
    """Builder for SystemSignalGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignalGroup = SystemSignalGroup()

    def build(self) -> SystemSignalGroup:
        """Build and return SystemSignalGroup object.

        Returns:
            SystemSignalGroup instance
        """
        # TODO: Add validation
        return self._obj
