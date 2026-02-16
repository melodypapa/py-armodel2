"""EndToEndTransformationISignalProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EndToEndTransformationISignalProps(ARObject):
    """AUTOSAR EndToEndTransformationISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_length", None, True, False, None),  # dataLength
        ("max_data_length", None, True, False, None),  # maxDataLength
        ("min_data_length", None, True, False, None),  # minDataLength
        ("source_id", None, True, False, None),  # sourceId
    ]

    def __init__(self) -> None:
        """Initialize EndToEndTransformationISignalProps."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.max_data_length: Optional[PositiveInteger] = None
        self.min_data_length: Optional[PositiveInteger] = None
        self.source_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EndToEndTransformationISignalProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndTransformationISignalProps":
        """Create EndToEndTransformationISignalProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EndToEndTransformationISignalProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EndToEndTransformationISignalProps since parent returns ARObject
        return cast("EndToEndTransformationISignalProps", obj)


class EndToEndTransformationISignalPropsBuilder:
    """Builder for EndToEndTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationISignalProps = EndToEndTransformationISignalProps()

    def build(self) -> EndToEndTransformationISignalProps:
        """Build and return EndToEndTransformationISignalProps object.

        Returns:
            EndToEndTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
