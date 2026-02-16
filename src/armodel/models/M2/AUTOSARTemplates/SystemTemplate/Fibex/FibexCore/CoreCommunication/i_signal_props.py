"""ISignalProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class ISignalProps(ARObject):
    """AUTOSAR ISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("handle_out_of_range", None, False, False, any (HandleOutOfRange)),  # handleOutOfRange
    ]

    def __init__(self) -> None:
        """Initialize ISignalProps."""
        super().__init__()
        self.handle_out_of_range: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ISignalProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalProps":
        """Create ISignalProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ISignalProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ISignalProps since parent returns ARObject
        return cast("ISignalProps", obj)


class ISignalPropsBuilder:
    """Builder for ISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalProps = ISignalProps()

    def build(self) -> ISignalProps:
        """Build and return ISignalProps object.

        Returns:
            ISignalProps instance
        """
        # TODO: Add validation
        return self._obj
