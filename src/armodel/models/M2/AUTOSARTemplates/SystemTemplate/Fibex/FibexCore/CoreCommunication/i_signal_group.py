"""ISignalGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
    SystemSignalGroup,
)


class ISignalGroup(FibexElement):
    """AUTOSAR ISignalGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("com_based", None, False, False, DataTransformation),  # comBased
        ("i_signals", None, False, True, ISignal),  # iSignals
        ("system_signal_group", None, False, False, SystemSignalGroup),  # systemSignalGroup
        ("transformation_i_signals", None, False, True, any (TransformationISignal)),  # transformationISignals
    ]

    def __init__(self) -> None:
        """Initialize ISignalGroup."""
        super().__init__()
        self.com_based: Optional[DataTransformation] = None
        self.i_signals: list[ISignal] = []
        self.system_signal_group: Optional[SystemSignalGroup] = None
        self.transformation_i_signals: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ISignalGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalGroup":
        """Create ISignalGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ISignalGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ISignalGroup since parent returns ARObject
        return cast("ISignalGroup", obj)


class ISignalGroupBuilder:
    """Builder for ISignalGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalGroup = ISignalGroup()

    def build(self) -> ISignalGroup:
        """Build and return ISignalGroup object.

        Returns:
            ISignalGroup instance
        """
        # TODO: Add validation
        return self._obj
