"""LinConfigurableFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)


class LinConfigurableFrame(ARObject):
    """AUTOSAR LinConfigurableFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    frame_ref: Optional[ARRef]
    message_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize LinConfigurableFrame."""
        super().__init__()
        self.frame_ref: Optional[ARRef] = None
        self.message_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize LinConfigurableFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize frame_ref
        if self.frame_ref is not None:
            serialized = SerializationHelper.serialize_item(self.frame_ref, "LinFrame")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_id
        if self.message_id is not None:
            serialized = SerializationHelper.serialize_item(self.message_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinConfigurableFrame":
        """Deserialize XML element to LinConfigurableFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinConfigurableFrame object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse frame_ref
        child = SerializationHelper.find_child_element(element, "FRAME-REF")
        if child is not None:
            frame_ref_value = ARRef.deserialize(child)
            obj.frame_ref = frame_ref_value

        # Parse message_id
        child = SerializationHelper.find_child_element(element, "MESSAGE-ID")
        if child is not None:
            message_id_value = child.text
            obj.message_id = message_id_value

        return obj



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
