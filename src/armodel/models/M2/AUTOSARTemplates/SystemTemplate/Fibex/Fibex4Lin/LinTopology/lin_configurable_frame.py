"""LinConfigurableFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)


class LinConfigurableFrame(ARObject):
    """AUTOSAR LinConfigurableFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("frame", None, False, False, LinFrame),  # frame
        ("message_id", None, True, False, None),  # messageId
    ]

    def __init__(self) -> None:
        """Initialize LinConfigurableFrame."""
        super().__init__()
        self.frame: Optional[LinFrame] = None
        self.message_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinConfigurableFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinConfigurableFrame":
        """Create LinConfigurableFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinConfigurableFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinConfigurableFrame since parent returns ARObject
        return cast("LinConfigurableFrame", obj)


class LinConfigurableFrameBuilder:
    """Builder for LinConfigurableFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinConfigurableFrame = LinConfigurableFrame()

    def build(self) -> LinConfigurableFrame:
        """Build and return LinConfigurableFrame object.

        Returns:
            LinConfigurableFrame instance
        """
        # TODO: Add validation
        return self._obj
