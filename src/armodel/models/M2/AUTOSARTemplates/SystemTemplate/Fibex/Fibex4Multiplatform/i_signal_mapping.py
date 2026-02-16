"""ISignalMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)


class ISignalMapping(ARObject):
    """AUTOSAR ISignalMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("introduction", None, False, False, DocumentationBlock),  # introduction
        ("source_signal", None, False, False, ISignalTriggering),  # sourceSignal
        ("target_signal", None, False, False, ISignalTriggering),  # targetSignal
    ]

    def __init__(self) -> None:
        """Initialize ISignalMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.source_signal: Optional[ISignalTriggering] = None
        self.target_signal: Optional[ISignalTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ISignalMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalMapping":
        """Create ISignalMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ISignalMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ISignalMapping since parent returns ARObject
        return cast("ISignalMapping", obj)


class ISignalMappingBuilder:
    """Builder for ISignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalMapping = ISignalMapping()

    def build(self) -> ISignalMapping:
        """Build and return ISignalMapping object.

        Returns:
            ISignalMapping instance
        """
        # TODO: Add validation
        return self._obj
